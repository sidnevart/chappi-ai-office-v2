create extension if not exists vector;
create extension if not exists pgcrypto;
create extension if not exists pg_trgm;

create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create table if not exists public.memory_documents (
  id uuid primary key default gen_random_uuid(),
  source_path text not null unique,
  source_type text not null check (source_type in ('memory','daily_note','research','plan','decision','profile','tools','other')),
  title text not null,
  project text,
  topic text,
  tags text[] not null default '{}',
  content_hash text not null,
  sensitivity text not null default 'normal' check (sensitivity in ('normal','internal','restricted')),
  status text not null default 'active' check (status in ('active','archived','deleted')),
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  last_indexed_at timestamptz
);

create table if not exists public.memory_chunks (
  id uuid primary key default gen_random_uuid(),
  document_id uuid not null references public.memory_documents(id) on delete cascade,
  chunk_index integer not null,
  chunk_text text not null,
  token_count integer,
  embedding_model text not null default 'nomic-embed-text',
  embedding vector(768) not null,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  unique (document_id, chunk_index)
);

create table if not exists public.memory_facts (
  id uuid primary key default gen_random_uuid(),
  fact_text text not null,
  source_document_id uuid references public.memory_documents(id) on delete set null,
  confidence numeric(4,3) check (confidence >= 0 and confidence <= 1),
  status text not null default 'candidate' check (status in ('candidate','accepted','rejected')),
  promoted_to_memory_md boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  metadata jsonb not null default '{}'::jsonb
);

create table if not exists public.ingestion_runs (
  id uuid primary key default gen_random_uuid(),
  source text not null,
  status text not null check (status in ('started','completed','failed')),
  documents_processed integer not null default 0,
  chunks_written integer not null default 0,
  error_text text,
  metadata jsonb not null default '{}'::jsonb,
  started_at timestamptz not null default now(),
  finished_at timestamptz
);

create index if not exists memory_documents_source_type_idx on public.memory_documents(source_type);
create index if not exists memory_documents_project_idx on public.memory_documents(project);
create index if not exists memory_documents_topic_idx on public.memory_documents(topic);
create index if not exists memory_documents_tags_idx on public.memory_documents using gin(tags);
create index if not exists memory_documents_metadata_idx on public.memory_documents using gin(metadata);
create index if not exists memory_chunks_document_idx on public.memory_chunks(document_id, chunk_index);
create index if not exists memory_chunks_metadata_idx on public.memory_chunks using gin(metadata);
create index if not exists memory_facts_status_idx on public.memory_facts(status);

create index if not exists memory_chunks_embedding_cosine_idx
  on public.memory_chunks
  using ivfflat (embedding vector_cosine_ops)
  with (lists = 100);

create index if not exists memory_chunks_text_trgm_idx
  on public.memory_chunks
  using gin (chunk_text gin_trgm_ops);

create trigger memory_documents_set_updated_at
before update on public.memory_documents
for each row execute function public.set_updated_at();

create trigger memory_facts_set_updated_at
before update on public.memory_facts
for each row execute function public.set_updated_at();

create or replace function public.match_memory_chunks(
  query_embedding vector(768),
  match_count integer default 8,
  filter_source_types text[] default null,
  filter_project text default null,
  filter_topic text default null
)
returns table (
  chunk_id uuid,
  document_id uuid,
  source_path text,
  source_type text,
  title text,
  topic text,
  chunk_index integer,
  chunk_text text,
  similarity double precision,
  metadata jsonb
)
language sql
stable
as $$
  select
    c.id as chunk_id,
    d.id as document_id,
    d.source_path,
    d.source_type,
    d.title,
    d.topic,
    c.chunk_index,
    c.chunk_text,
    1 - (c.embedding <=> query_embedding) as similarity,
    coalesce(c.metadata, '{}'::jsonb) || jsonb_build_object('document_metadata', d.metadata) as metadata
  from public.memory_chunks c
  join public.memory_documents d on d.id = c.document_id
  where d.status = 'active'
    and (filter_source_types is null or d.source_type = any(filter_source_types))
    and (filter_project is null or d.project = filter_project)
    and (filter_topic is null or d.topic = filter_topic)
  order by c.embedding <=> query_embedding
  limit greatest(match_count, 1);
$$;
