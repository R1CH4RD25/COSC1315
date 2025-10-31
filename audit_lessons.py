"""
Comprehensive audit of all lesson components
Using Lessons 6 & 7 as gold standard
"""

import os
import json
import re
import glob

print('=' * 80)
print('COMPREHENSIVE LESSON AUDIT')
print('Using Lessons 6 & 7 as Gold Standard')
print('=' * 80)

def audit_lesson(lesson_num):
    print(f'\n{"=" * 80}')
    print(f'LESSON {lesson_num:02d}')
    print('=' * 80)
    
    lesson_prefix = f'Lesson_{lesson_num:02d}_'
    issues = []
    
    # 1. Check Objectives HTML
    obj_files = [f for f in os.listdir('Objectives') if f.startswith(lesson_prefix) and f.endswith('.html')]
    if obj_files:
        obj_file = os.path.join('Objectives', obj_files[0])
        with open(obj_file, 'r', encoding='utf-8') as f:
            obj_content = f.read()
        
        has_container_div = '<div class="container">' in obj_content or '<div id="container">' in obj_content
        body_split = obj_content.split('<body>')
        starts_with_h1 = len(body_split) > 1 and body_split[1].strip().startswith('<h1')
        
        print(f'\nOBJECTIVES HTML: {obj_files[0]}')
        print(f'  Container div: {"FAIL" if has_container_div else "PASS"}')
        print(f'  Starts with <h1>: {"PASS" if starts_with_h1 else "FAIL"}')
        
        if has_container_div:
            issues.append('Objectives has container div')
        if not starts_with_h1:
            issues.append('Objectives does not start with <h1>')
    else:
        print(f'\nOBJECTIVES HTML: NOT FOUND')
        issues.append('No objectives file')
    
    # 2. Check Notebook
    nb_files = [f for f in os.listdir('Lessons') if f.startswith(lesson_prefix) and f.endswith('.ipynb') and 'backup' not in f.lower()]
    
    if len(nb_files) > 1:
        print(f'\nNOTEBOOK: MULTIPLE FILES ({len(nb_files)})')
        for nf in nb_files:
            print(f'  - {nf}')
        issues.append(f'Multiple notebook files: {nb_files}')
        nb_file = os.path.join('Lessons', nb_files[0])
    elif nb_files:
        nb_file = os.path.join('Lessons', nb_files[0])
        print(f'\nNOTEBOOK: {nb_files[0]}')
    else:
        print(f'\nNOTEBOOK: NOT FOUND')
        issues.append('No notebook file')
        nb_file = None
    
    if nb_file and os.path.exists(nb_file):
        with open(nb_file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        cell_count = len(nb.get('cells', []))
        print(f'  Total cells: {cell_count}')
        
        if cell_count == 0:
            print(f'  Status: EMPTY NOTEBOOK')
            issues.append('Empty notebook')
        else:
            # Check for setup cell
            has_setup = False
            has_verification_import = False
            for cell in nb['cells']:
                if cell['cell_type'] == 'code':
                    content = ''.join(cell.get('source', []))
                    if 'urllib.request' in content and 'verification' in content:
                        has_setup = True
                    if 'from lesson_' in content and 'verification' in content:
                        has_verification_import = True
            
            print(f'  Setup cell: {"PASS" if has_setup else "FAIL"}')
            print(f'  Verification import: {"PASS" if has_verification_import else "FAIL"}')
            
            if not has_setup:
                issues.append('No setup cell with verification download')
            if not has_verification_import:
                issues.append('No verification function imports')
            
            # Extract point structure
            nb_content = json.dumps(nb)
            
            # Multiple regex patterns to catch different formats
            walk_patterns = [
                r'Walk-Along.*?(\d+)\s*point',
                r'Walk Along.*?(\d+)\s*point',
                r'WalkAlong.*?(\d+)\s*point',
            ]
            try_patterns = [
                r'Try It Yourself.*?(\d+)\s*point',
                r'Try it yourself.*?(\d+)\s*point',
            ]
            debug_patterns = [
                r'Debug.*?(\d+)\s*point',
            ]
            
            walk_along_matches = []
            for pattern in walk_patterns:
                walk_along_matches.extend(re.findall(pattern, nb_content, re.IGNORECASE))
            
            try_it_matches = []
            for pattern in try_patterns:
                try_it_matches.extend(re.findall(pattern, nb_content, re.IGNORECASE))
            
            debug_matches = []
            for pattern in debug_patterns:
                debug_matches.extend(re.findall(pattern, nb_content, re.IGNORECASE))
            
            walk_along_total = sum(int(p) for p in walk_along_matches) if walk_along_matches else 0
            try_it_total = sum(int(p) for p in try_it_matches) if try_it_matches else 0
            debug_total = sum(int(p) for p in debug_matches) if debug_matches else 0
            total = walk_along_total + try_it_total + debug_total
            
            print(f'  Walk-Along: {walk_along_total} pts ({len(walk_along_matches)} tasks)')
            print(f'  Try It Yourself: {try_it_total} pts ({len(try_it_matches)} tasks)')
            print(f'  Debug Challenges: {debug_total} pts ({len(debug_matches)} tasks)')
            print(f'  TOTAL: {total} points', end='')
            
            if total == 100:
                print(' - PASS')
            elif total == 0:
                print(' - FAIL (no points found)')
                issues.append('No point values in notebook')
            else:
                print(f' - FAIL (should be 100)')
                issues.append(f'Notebook has {total} points instead of 100')
    
    # 3. Check Verification Script
    ver_files = [f for f in os.listdir('Lessons/Verifications') if f.startswith(f'lesson_{lesson_num:02d}_')]
    if ver_files:
        ver_file = os.path.join('Lessons/Verifications', ver_files[0])
        with open(ver_file, 'r', encoding='utf-8') as f:
            ver_content = f.read()
        
        func_count = ver_content.count('def verify_')
        has_calculate_grade = 'def calculate_grade' in ver_content
        
        print(f'\nVERIFICATION: {ver_files[0]}')
        print(f'  Verification functions: {func_count}')
        print(f'  Has calculate_grade(): {"PASS" if has_calculate_grade else "FAIL"}')
        
        if not has_calculate_grade:
            issues.append('No calculate_grade() function')
    else:
        print(f'\nVERIFICATION: NOT FOUND')
        issues.append('No verification script')
    
    # 4. Check Quizzes
    vocab_files = glob.glob(f'Quizzes/Vocabulary Quizzes - QTI - Canvas/Lesson_{lesson_num:02d}_*.zip')
    assign_files = glob.glob(f'Quizzes/Assignment Quizzes - QTI - Canvas/Lesson_{lesson_num:02d}_*.zip')
    
    print(f'\nQUIZZES:')
    print(f'  Vocabulary: {"PASS" if vocab_files else "FAIL"}')
    print(f'  Assignment: {"PASS" if assign_files else "FAIL"}')
    
    if not vocab_files:
        issues.append('No vocabulary quiz')
    if not assign_files:
        issues.append('No assignment quiz')
    
    # 5. Check Assignment Instructions HTML
    assign_html_files = [f for f in os.listdir('Assignment Instructions') if f.startswith(lesson_prefix) and f.endswith('.html')]
    if assign_html_files:
        assign_file = os.path.join('Assignment Instructions', assign_html_files[0])
        with open(assign_file, 'r', encoding='utf-8') as f:
            assign_content = f.read()
        
        has_container_div = '<div class="container">' in assign_content or '<div id="container">' in assign_content
        
        print(f'\nASSIGNMENT INSTRUCTIONS: {assign_html_files[0]}')
        print(f'  Container div: {"FAIL" if has_container_div else "PASS"}')
        
        if has_container_div:
            issues.append('Assignment instructions has container div')
    else:
        print(f'\nASSIGNMENT INSTRUCTIONS: NOT FOUND')
        issues.append('No assignment instructions')
    
    # Summary
    print(f'\n{"=" * 40}')
    if issues:
        print(f'ISSUES FOUND ({len(issues)}):')
        for issue in issues:
            print(f'  - {issue}')
    else:
        print('STATUS: ALL CHECKS PASSED')
    
    return issues

# Audit all lessons 1-10
all_issues = {}
for i in range(1, 11):
    issues = audit_lesson(i)
    if issues:
        all_issues[i] = issues

print(f'\n{"=" * 80}')
print('AUDIT SUMMARY')
print('=' * 80)

lessons_with_issues = len(all_issues)
lessons_passing = 10 - lessons_with_issues

print(f'\nLessons passing all checks: {lessons_passing}/10')
print(f'Lessons with issues: {lessons_with_issues}/10')

if all_issues:
    print(f'\nLESSONS NEEDING FIXES:')
    for lesson_num, issues in sorted(all_issues.items()):
        print(f'\n  Lesson {lesson_num:02d} ({len(issues)} issues):')
        for issue in issues:
            print(f'    - {issue}')

print(f'\n{"=" * 80}')
