#!/usr/bin/env python3
"""
Eval Runner — comprehensive skill testing
Parses eval YAML and tests skills against criteria
"""

import yaml
import os
import glob
from pathlib import Path
from datetime import datetime

class EvalRunner:
    def __init__(self, skills_dir='/opt/openclaw-stack/workspace/skills'):
        self.skills_dir = Path(skills_dir)
        self.results = []
        self.total_tests = 0
        self.total_passed = 0
        self.total_failed = 0
        self.total_skipped = 0
    
    def load_eval(self, eval_path):
        """Load eval YAML file"""
        with open(eval_path, 'r') as f:
            return yaml.safe_load(f)
    
    def load_skill(self, skill_name):
        """Load skill markdown"""
        skill_path = self.skills_dir / skill_name / 'SKILL.md'
        if not skill_path.exists():
            return None
        with open(skill_path, 'r') as f:
            return f.read()
    
    def run_test(self, test_case, skill_content):
        """Run a single test case against skill content"""
        test_id = test_case.get('id', 'unknown')
        name = test_case.get('name', 'Unnamed test')
        expected = test_case.get('expected', [])
        
        if not skill_content:
            return {'id': test_id, 'name': name, 'status': 'SKIPPED', 'reason': 'Skill not found'}
        
        passed = 0
        failed = 0
        details = []
        
        for check in expected:
            if isinstance(check, str):
                check = {'contains': check}
            
            check_type = list(check.keys())[0]
            check_value = check[check_type]
            
            if check_type == 'contains':
                check_str = str(check_value)
                if check_str.lower() in skill_content.lower():
                    passed += 1
                    details.append(f"✅ '{check_str}' found")
                else:
                    failed += 1
                    details.append(f"❌ '{check_str}' NOT found")
            
            elif check_type == 'not_contains':
                check_str = str(check_value)
                if check_str.lower() not in skill_content.lower():
                    passed += 1
                    details.append(f"✅ '{check_str}' correctly absent")
                else:
                    failed += 1
                    details.append(f"❌ '{check_str}' should NOT be present")
            
            elif check_type == 'file_exists':
                # Check if file pattern exists
                pattern = check_value.replace('*', '.*')
                found = False
                for line in skill_content.split('\n'):
                    if check_value in line:
                        found = True
                        break
                if found:
                    passed += 1
                    details.append(f"✅ File pattern '{check_value}' referenced")
                else:
                    failed += 1
                    details.append(f"❌ File pattern '{check_value}' NOT referenced")
        
        status = 'PASSED' if failed == 0 else 'FAILED'
        
        return {
            'id': test_id,
            'name': name,
            'status': status,
            'passed': passed,
            'failed': failed,
            'total': passed + failed,
            'details': details
        }
    
    def run_skill_evals(self, skill_name, eval_path):
        """Run all evals for a skill"""
        eval_data = self.load_eval(eval_path)
        skill_content = self.load_skill(skill_name)
        
        if not eval_data:
            return None
        
        cases = eval_data.get('cases', [])
        results = []
        
        for case in cases:
            result = self.run_test(case, skill_content)
            results.append(result)
            
            self.total_tests += 1
            if result['status'] == 'PASSED':
                self.total_passed += 1
            elif result['status'] == 'FAILED':
                self.total_failed += 1
            else:
                self.total_skipped += 1
        
        passed_count = sum(1 for r in results if r['status'] == 'PASSED')
        score = (passed_count / len(results) * 100) if results else 0
        
        return {
            'skill': skill_name,
            'total_tests': len(results),
            'passed': passed_count,
            'failed': len(results) - passed_count,
            'score': score,
            'results': results
        }
    
    def run_all(self):
        """Run all evals for all skills"""
        print("=" * 70)
        print("EVAL RUNNER — Comprehensive Skill Testing")
        print("=" * 70)
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("")
        
        # Find all eval files
        eval_files = glob.glob(str(self.skills_dir / '*/evals/requirements.yaml'))
        
        print(f"Found {len(eval_files)} skills with evals")
        print("")
        
        for eval_path in sorted(eval_files):
            skill_name = Path(eval_path).parent.parent.name
            result = self.run_skill_evals(skill_name, eval_path)
            
            if result:
                self.results.append(result)
                
                # Print result
                status_icon = "✅" if result['score'] == 100 else "⚠️" if result['score'] >= 80 else "❌"
                print(f"{status_icon} {skill_name}")
                print(f"   Tests: {result['total_tests']} | Passed: {result['passed']} | Failed: {result['failed']} | Score: {result['score']:.1f}%")
                
                # Print failures
                for test in result['results']:
                    if test['status'] == 'FAILED':
                        print(f"   ❌ {test['id']}: {test['name']}")
                        for detail in test['details']:
                            if detail.startswith('❌'):
                                print(f"      {detail}")
                print("")
        
        # Summary
        print("=" * 70)
        print("SUMMARY")
        print("=" * 70)
        print(f"Total Skills: {len(self.results)}")
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.total_passed} ({self.total_passed/self.total_tests*100:.1f}%)")
        print(f"Failed: {self.total_failed} ({self.total_failed/self.total_tests*100:.1f}%)")
        print(f"Skipped: {self.total_skipped}")
        
        # Generate HTML report
        self.generate_html_report()
        
        return self.results
    
    def generate_html_report(self):
        """Generate HTML report"""
        report_path = '/mnt/files/research-state/reports/html/eval-results.html'
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        
        html = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Eval Results — {datetime.now().strftime('%Y-%m-%d')}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 40px; }}
        h1 {{ color: #1a237e; border-bottom: 3px solid #667eea; padding-bottom: 10px; }}
        .summary {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 30px; border-radius: 10px; margin: 20px 0; }}
        .summary h2 {{ margin: 0 0 10px 0; }}
        .metric {{ display: inline-block; margin: 10px 20px 10px 0; }}
        .metric-value {{ font-size: 32px; font-weight: bold; }}
        .metric-label {{ font-size: 14px; opacity: 0.9; }}
        .skill {{ border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin: 10px 0; }}
        .skill-pass {{ border-left: 5px solid #4caf50; }}
        .skill-fail {{ border-left: 5px solid #f44336; }}
        .skill-warn {{ border-left: 5px solid #ff9800; }}
        .test-pass {{ color: #4caf50; }}
        .test-fail {{ color: #f44336; }}
        .footer {{ margin-top: 40px; padding-top: 20px; border-top: 2px solid #eee; color: #999; font-size: 13px; }}
    </style>
</head>
<body>
    <h1>📊 Eval Results — {datetime.now().strftime('%Y-%m-%d')}</h1>
    
    <div class="summary">
        <h2>Summary</h2>
        <div class="metric">
            <div class="metric-value">{len(self.results)}</div>
            <div class="metric-label">Skills</div>
        </div>
        <div class="metric">
            <div class="metric-value">{self.total_tests}</div>
            <div class="metric-label">Tests</div>
        </div>
        <div class="metric">
            <div class="metric-value">{self.total_passed}</div>
            <div class="metric-label">Passed</div>
        </div>
        <div class="metric">
            <div class="metric-value">{self.total_failed}</div>
            <div class="metric-label">Failed</div>
        </div>
        <div class="metric">
            <div class="metric-value">{self.total_passed/self.total_tests*100:.1f}%</div>
            <div class="metric-label">Pass Rate</div>
        </div>
    </div>
"""
        
        for result in self.results:
            css_class = 'skill-pass' if result['score'] == 100 else 'skill-warn' if result['score'] >= 80 else 'skill-fail'
            html += f"""
    <div class="skill {css_class}">
        <h3>{result['skill']}</h3>
        <p>Tests: {result['total_tests']} | Passed: {result['passed']} | Failed: {result['failed']} | Score: {result['score']:.1f}%</p>
"""
            for test in result['results']:
                if test['status'] == 'FAILED':
                    html += f"""
        <div class="test-fail">❌ {test['id']}: {test['name']}</div>
"""
            html += "    </div>\n"
        
        html += """
    <div class="footer">
        <p>🤖 Generated by OpenClaw Eval Runner</p>
    </div>
</body>
</html>
"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"\n✅ HTML report: {report_path}")

if __name__ == '__main__':
    runner = EvalRunner()
    runner.run_all()
