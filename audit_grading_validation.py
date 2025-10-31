"""
Audit verification scripts to ensure they match notebook point values
"""
import re
import json

def analyze_verification_script(lesson_num):
    """Analyze a verification script to extract actual point awards"""
    filepath = f'Lessons/Verifications/lesson_{lesson_num:02d}_verification.py'

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return None

    # Find all verify functions and their max_points
    walk_along_points = []
    try_it_points = []
    debug_points = []

    # Extract Walk-Along tasks
    for match in re.finditer(r'def verify_walk_along_(\d+)\(\):(.*?)(?=def |$)', content, re.DOTALL):
        task_num = match.group(1)
        func_body = match.group(2)
        max_pts_match = re.search(r'max_points\s*=\s*(\d+)', func_body)
        if max_pts_match:
            walk_along_points.append(int(max_pts_match.group(1)))

    # Extract Try It Yourself tasks (both verify_try_it_N and verify_try_it_yourself_N)
    for match in re.finditer(r'def verify_try_it(?:_yourself)?_(\d+)\(\):(.*?)(?=def |$)', content, re.DOTALL):
        task_num = match.group(1)
        func_body = match.group(2)
        max_pts_match = re.search(r'max_points\s*=\s*(\d+)', func_body)
        if max_pts_match:
            try_it_points.append(int(max_pts_match.group(1)))

    # Extract Debug tasks
    for match in re.finditer(r'def verify_debug_(\d+)\(\):(.*?)(?=def |$)', content, re.DOTALL):
        task_num = match.group(1)
        func_body = match.group(2)
        max_pts_match = re.search(r'max_points\s*=\s*(\d+)', func_body)
        if max_pts_match:
            debug_points.append(int(max_pts_match.group(1)))

    # Find declared total in calculate_grade
    calc_grade_match = re.search(r'def calculate_grade\(\):(.*?)(?=\ndef |$)', content, re.DOTALL)
    declared_total = None
    if calc_grade_match:
        max_pts_match = re.search(r'max_points\s*=\s*(\d+)', calc_grade_match.group(1))
        if max_pts_match:
            declared_total = int(max_pts_match.group(1))

    walk_total = sum(walk_along_points)
    try_total = sum(try_it_points)
    debug_total = sum(debug_points)
    actual_total = walk_total + try_total + debug_total

    return {
        'lesson': lesson_num,
        'walk_along': {'points': walk_along_points, 'total': walk_total},
        'try_it': {'points': try_it_points, 'total': try_total},
        'debug': {'points': debug_points, 'total': debug_total},
        'actual_total': actual_total,
        'declared_total': declared_total
    }

def analyze_notebook_points(lesson_num):
    """Analyze notebook to extract point values from task headers"""
    import glob
    files = glob.glob(f'Lessons/Lesson_{lesson_num:02d}_*.ipynb')
    if not files:
        return None

    # Get main file (not backup)
    main_file = [f for f in files if 'backup' not in f]
    if not main_file:
        return None

    with open(main_file[0], 'r', encoding='utf-8') as f:
        nb = json.load(f)

    walk_along_points = []
    try_it_points = []
    debug_points = []

    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            content = ''.join(cell['source'])

            # Check for task headers with points
            if re.search(r'###\s+Walk-Along Task\s+\d+:', content):
                match = re.search(r'\((\d+)\s+points?\)', content)
                if match:
                    walk_along_points.append(int(match.group(1)))

            elif re.search(r'###\s+Try It Yourself\s+\d+:', content):
                match = re.search(r'\((\d+)\s+points?\)', content)
                if match:
                    try_it_points.append(int(match.group(1)))

            elif re.search(r'###\s+Debug (Task|Challenge)\s+\d+:', content):
                match = re.search(r'\((\d+)\s+points?\)', content)
                if match:
                    debug_points.append(int(match.group(1)))

    walk_total = sum(walk_along_points)
    try_total = sum(try_it_points)
    debug_total = sum(debug_points)

    return {
        'lesson': lesson_num,
        'walk_along': {'points': walk_along_points, 'total': walk_total},
        'try_it': {'points': try_it_points, 'total': try_total},
        'debug': {'points': debug_points, 'total': debug_total},
        'notebook_total': walk_total + try_total + debug_total
    }

print('='*80)
print('COMPREHENSIVE GRADING VALIDATION AUDIT')
print('Comparing Notebook Point Values vs Verification Script Awards')
print('='*80)

for lesson_num in range(5, 11):
    print(f'\\n{"="*80}')
    print(f'LESSON {lesson_num:02d}')
    print(f'{"="*80}')

    # Get notebook points
    nb_data = analyze_notebook_points(lesson_num)
    if not nb_data:
        print('❌ Notebook not found or empty')
        continue

    # Get verification points
    ver_data = analyze_verification_script(lesson_num)
    if not ver_data:
        print('❌ Verification script not found')
        continue

    # Display comparison
    print(f'\\nNOTEBOOK (what students see):')
    print(f'  Walk-Along: {nb_data["walk_along"]["points"]} = {nb_data["walk_along"]["total"]} pts')
    print(f'  Try It:     {nb_data["try_it"]["points"]} = {nb_data["try_it"]["total"]} pts')
    print(f'  Debug:      {nb_data["debug"]["points"]} = {nb_data["debug"]["total"]} pts')
    print(f'  TOTAL:      {nb_data["notebook_total"]} points')

    print(f'\\nVERIFICATION SCRIPT (what system awards):')
    print(f'  Walk-Along: {ver_data["walk_along"]["points"]} = {ver_data["walk_along"]["total"]} pts')
    print(f'  Try It:     {ver_data["try_it"]["points"]} = {ver_data["try_it"]["total"]} pts')
    print(f'  Debug:      {ver_data["debug"]["points"]} = {ver_data["debug"]["total"]} pts')
    print(f'  TOTAL:      {ver_data["actual_total"]} points')
    print(f'  Declared:   {ver_data["declared_total"]} points (in calculate_grade)')

    # Check for mismatches
    print(f'\\nVALIDATION:')
    issues = []

    if nb_data['notebook_total'] != 100:
        issues.append(f'❌ Notebook shows {nb_data["notebook_total"]} points (should be 100)')
    else:
        print('  ✅ Notebook shows exactly 100 points')

    if ver_data['actual_total'] != 100:
        issues.append(f'❌ Verification awards {ver_data["actual_total"]} points (should be 100)')
    else:
        print('  ✅ Verification awards exactly 100 points')

    if ver_data['declared_total'] and ver_data['declared_total'] != ver_data['actual_total']:
        issues.append(f'❌ calculate_grade declares {ver_data["declared_total"]} but functions award {ver_data["actual_total"]}')
    elif ver_data['declared_total'] == ver_data['actual_total']:
        print(f'  ✅ calculate_grade declaration matches function awards')

    if nb_data['notebook_total'] != ver_data['actual_total']:
        issues.append(f'❌ MISMATCH: Notebook shows {nb_data["notebook_total"]} but verification awards {ver_data["actual_total"]}')
    else:
        print('  ✅ Notebook and verification match!')

    if issues:
        print()
        for issue in issues:
            print(f'  {issue}')

    # Section-by-section comparison
    walk_match = nb_data['walk_along']['total'] == ver_data['walk_along']['total']
    try_match = nb_data['try_it']['total'] == ver_data['try_it']['total']
    debug_match = nb_data['debug']['total'] == ver_data['debug']['total']

    if not (walk_match and try_match and debug_match):
        print(f'\\n  SECTION MISMATCHES:')
        if not walk_match:
            print(f'    ❌ Walk-Along: Notebook={nb_data["walk_along"]["total"]}, Verification={ver_data["walk_along"]["total"]}')
        if not try_match:
            print(f'    ❌ Try It: Notebook={nb_data["try_it"]["total"]}, Verification={ver_data["try_it"]["total"]}')
        if not debug_match:
            print(f'    ❌ Debug: Notebook={nb_data["debug"]["total"]}, Verification={ver_data["debug"]["total"]}')

print(f'\\n{"="*80}')
print('AUDIT COMPLETE')
print('='*80)
