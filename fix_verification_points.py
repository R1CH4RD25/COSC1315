"""
Fix verification scripts to match notebook point distributions (15+50+35=100)
"""
import re
import shutil

def fix_lesson_08():
    """Fix Lesson 08: Currently 15+50+40=105, needs 15+50+35=100"""
    filepath = 'Lessons/Verifications/lesson_08_verification.py'

    # Backup
    shutil.copy2(filepath, filepath.replace('.py', '_backup.py'))

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix header comment
    content = re.sub(
        r'Grading Breakdown:.*?Total: \d+ points',
        'Grading Breakdown:\n- Walk-Along Tasks: 15 points (4 tasks: 4 + 3 + 4 + 4 points)\n- Try It Yourself: 50 points (17 + 17 + 16)\n- Debug Exercises: 35 points (12 + 12 + 11)\nTotal: 100 points',
        content,
        flags=re.DOTALL
    )

    # Fix calculate_grade max_points
    content = re.sub(
        r'max_points = 105',
        'max_points = 100',
        content
    )

    # Fix debug section display
    content = re.sub(
        r'Debug Challenges:\s+\{debug_total:>3\}/40 points',
        'Debug Challenges:     {debug_total:>3}/35 points',
        content
    )

    # Find and fix debug function max_points
    # Debug 1: Currently 15, should be 12
    content = re.sub(
        r'(def verify_debug_1\(\):.*?max_points = )15',
        r'\g<1>12',
        content,
        flags=re.DOTALL
    )

    # Debug 2: Currently 15, should be 12
    content = re.sub(
        r'(def verify_debug_2\(\):.*?max_points = )15',
        r'\g<1>12',
        content,
        flags=re.DOTALL
    )

    # Debug 3: Currently 10, should be 11
    content = re.sub(
        r'(def verify_debug_3\(\):.*?max_points = )10',
        r'\g<1>11',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print('✅ Fixed Lesson 08: 105 → 100 points (debug: 40→35)')

def fix_lesson_05():
    """Fix Lesson 05: Currently 20+40+40=100, needs 15+50+35=100"""
    filepath = 'Lessons/Verifications/lesson_05_verification.py'

    # Backup
    shutil.copy2(filepath, filepath.replace('.py', '_backup.py'))

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix walk-along points: 5,5,5,5 → 4,4,4,3
    # Task 1: 5 → 4
    content = re.sub(
        r'(def verify_walk_along_task_1\(\):.*?max_points = )5',
        r'\g<1>4',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Task 2: 5 → 4
    content = re.sub(
        r'(def verify_walk_along_task_2\(\):.*?max_points = )5',
        r'\g<1>4',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Task 3: 5 → 4
    content = re.sub(
        r'(def verify_walk_along_task_3\(\):.*?max_points = )5',
        r'\g<1>4',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Task 4: 5 → 3
    content = re.sub(
        r'(def verify_walk_along_task_4\(\):.*?max_points = )5',
        r'\g<1>3',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Fix try-it points: 15,15,10 → 17,17,16
    # Try It 1: 15 → 17
    content = re.sub(
        r'(def verify_try_it_yourself_1\(\):.*?max_points = )15',
        r'\g<1>17',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Try It 2: 15 → 17
    content = re.sub(
        r'(def verify_try_it_yourself_2\(\):.*?max_points = )15',
        r'\g<1>17',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Try It 3: 10 → 16
    content = re.sub(
        r'(def verify_try_it_yourself_3\(\):.*?max_points = )10',
        r'\g<1>16',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Fix debug points: 15,15,10 → 12,12,11
    # Debug 1: 15 → 12
    content = re.sub(
        r'(def verify_debug_1\(\):.*?max_points = )15',
        r'\g<1>12',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Debug 2: 15 → 12
    content = re.sub(
        r'(def verify_debug_2\(\):.*?max_points = )15',
        r'\g<1>12',
        content,
        flags=re.DOTALL,
        count=1
    )

    # Debug 3: 10 → 11
    content = re.sub(
        r'(def verify_debug_3\(\):.*?max_points = )10',
        r'\g<1>11',
        content,
        flags=re.DOTALL,
        count=1
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print('✅ Fixed Lesson 05: 20+40+40 → 15+50+35')

def fix_lesson_09():
    """Fix Lesson 09: Uses dictionary, needs 15+50+35"""
    filepath = 'Lessons/Verifications/lesson_09_verification.py'

    # Backup
    shutil.copy2(filepath, filepath.replace('.py', '_backup.py'))

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix walk-along assignments: Currently 5,5,5 → need 5,5,5 (15 total is correct!)
    # Actually walk-along might be correct, let me check try-it

    # Fix try-it assignments: Need to check current values and adjust to 17,17,16
    # Try It 1: Currently 15 → 17
    content = re.sub(
        r"points_earned\['try_it_1'\] = 15",
        "points_earned['try_it_1'] = 17",
        content
    )

    # Try It 2: Currently 20 → 17
    content = re.sub(
        r"points_earned\['try_it_2'\] = 20",
        "points_earned['try_it_2'] = 17",
        content
    )

    # Try It 3: Currently 15 → 16
    content = re.sub(
        r"points_earned\['try_it_3'\] = 15",
        "points_earned['try_it_3'] = 16",
        content
    )

    # Fix debug assignments: Need 12,12,11
    # Debug 1: Currently 10 → 12
    content = re.sub(
        r"points_earned\['debug_1'\] = 10",
        "points_earned['debug_1'] = 12",
        content
    )

    # Debug 2: Currently 15 → 12
    content = re.sub(
        r"points_earned\['debug_2'\] = 15",
        "points_earned['debug_2'] = 12",
        content
    )

    # Debug 3: Currently 10 → 11
    content = re.sub(
        r"points_earned\['debug_3'\] = 10",
        "points_earned['debug_3'] = 11",
        content
    )

    # Fix calculate_grade max_points if needed
    content = re.sub(
        r'max_points = \d+',
        'max_points = 100',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print('✅ Fixed Lesson 09: Adjusted point distribution to 15+50+35')

print('='*80)
print('FIXING VERIFICATION SCRIPTS TO MATCH NOTEBOOKS')
print('Target: 15 walk-along + 50 try-it + 35 debug = 100 points')
print('='*80)
print()

# Fix the lessons we can fix
fix_lesson_05()
fix_lesson_08()
fix_lesson_09()

print()
print('='*80)
print('REMAINING ISSUES:')
print('='*80)
print('❌ Lesson 06: Verification script structure unknown (0 points detected)')
print('❌ Lesson 07: Verification script structure unknown (0 points detected)')
print('❌ Lesson 10: Verification script structure unknown (0 points detected)')
print()
print('These lessons need manual inspection to understand their verification structure.')
print('='*80)
