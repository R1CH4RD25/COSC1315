"""
Fix Lessons 6, 7, 10 verification scripts
These use hardcoded points in calculate_grade() function
"""
import re
import shutil

def fix_lesson_06():
    """Fix Lesson 06: Currently 15+45+40=100, needs 15+50+35=100"""
    filepath = 'Lessons/Verifications/lesson_06_verification.py'

    # Backup
    shutil.copy2(filepath, filepath.replace('.py', '_backup.py'))

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Try It Yourself section comment: 45 → 50
    content = re.sub(
        r'# Try It Yourself \(45 points total\)',
        '# Try It Yourself (50 points total)',
        content
    )

    content = re.sub(
        r'print\("🎯 Try It Yourself \(45 points\):"\)',
        'print("🎯 Try It Yourself (50 points):")',
        content
    )

    content = re.sub(
        r'print\(f"   Subtotal: \{try_it_points\}/45 points',
        'print(f"   Subtotal: {try_it_points}/50 points',
        content
    )

    # Fix Try It point values: 15,15,15 → 17,17,16
    content = re.sub(
        r'(if verify_try_it_yourself_1\(\):\s+try_it_points \+= )15',
        r'\g<1>17',
        content
    )

    content = re.sub(
        r'(if verify_try_it_yourself_2\(\):\s+try_it_points \+= )15',
        r'\g<1>17',
        content
    )

    content = re.sub(
        r'(if verify_try_it_yourself_3\(\):\s+try_it_points \+= )15',
        r'\g<1>16',
        content
    )

    # Fix Debug section comment: 40 → 35
    content = re.sub(
        r'# Debug Tasks \(40 points total\)',
        '# Debug Tasks (35 points total)',
        content
    )

    content = re.sub(
        r'print\("🐞 Debug Tasks \(40 points\):"\)',
        'print("🐞 Debug Tasks (35 points):")',
        content
    )

    content = re.sub(
        r'print\(f"   Subtotal: \{debug_points\}/40 points',
        'print(f"   Subtotal: {debug_points}/35 points',
        content
    )

    # Fix Debug point values: 15,10,15 → 12,11,12
    content = re.sub(
        r'(if verify_debug_1\(\):\s+debug_points \+= )15',
        r'\g<1>12',
        content
    )

    content = re.sub(
        r'(if verify_debug_2\(\):\s+debug_points \+= )10',
        r'\g<1>11',
        content
    )

    content = re.sub(
        r'(if verify_debug_3\(\):\s+debug_points \+= )15',
        r'\g<1>12',
        content
    )

    # Update function docstrings
    content = re.sub(
        r'def verify_try_it_yourself_1\(\):\s+"""Verify Try It Yourself 1.*?\(15 points\)',
        'def verify_try_it_yourself_1():\n    """Verify Try It Yourself 1: Team Name Formatter (17 points)',
        content
    )

    content = re.sub(
        r'def verify_try_it_yourself_2\(\):\s+"""Verify Try It Yourself 2.*?\(15 points\)',
        'def verify_try_it_yourself_2():\n    """Verify Try It Yourself 2: Player Stats Display (17 points)',
        content
    )

    content = re.sub(
        r'def verify_try_it_yourself_3\(\):\s+"""Verify Try It Yourself 3.*?\(15 points\)',
        'def verify_try_it_yourself_3():\n    """Verify Try It Yourself 3: Score Analysis (16 points)',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print('✅ Fixed Lesson 06: 15+45+40 → 15+50+35')

def fix_lesson_07():
    """Fix Lesson 07: Needs verification"""
    filepath = 'Lessons/Verifications/lesson_07_verification.py'

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print('❌ Lesson 07 verification file not found or unreadable')
        return

    # Backup
    shutil.copy2(filepath, filepath.replace('.py', '_backup.py'))

    # Check current structure
    if 'Try It Yourself (45 points' in content:
        # Similar structure to Lesson 06
        # Fix Try It: 45 → 50
        content = re.sub(
            r'# Try It Yourself \(45 points total\)',
            '# Try It Yourself (50 points total)',
            content
        )

        content = re.sub(
            r'print\("🎯 Try It Yourself \(45 points\):"\)',
            'print("🎯 Try It Yourself (50 points):")',
            content
        )

        content = re.sub(
            r'print\(f"   Subtotal: \{try_it_points\}/45 points',
            'print(f"   Subtotal: {try_it_points}/50 points',
            content
        )

        # Adjust point values
        # Assuming 15+15+15, change to 17+17+16
        lines = content.split('\n')
        new_lines = []
        try_it_count = 0

        for line in lines:
            if 'if verify_try_it_yourself_' in line and 'try_it_points += 15' in line:
                try_it_count += 1
                if try_it_count <= 2:
                    line = re.sub(r'(\+= )15', r'\g<1>17', line)
                else:
                    line = re.sub(r'(\+= )15', r'\g<1>16', line)
            new_lines.append(line)

        content = '\n'.join(new_lines)

        # Fix Debug: 40 → 35
        content = re.sub(
            r'# Debug Tasks \(40 points total\)',
            '# Debug Tasks (35 points total)',
            content
        )

        content = re.sub(
            r'print\("🐞 Debug Tasks \(40 points\):"\)',
            'print("🐞 Debug Tasks (35 points):")',
            content
        )

        content = re.sub(
            r'print\(f"   Subtotal: \{debug_points\}/40 points',
            'print(f"   Subtotal: {debug_points}/35 points',
            content
        )

        # Adjust debug points
        lines = content.split('\n')
        new_lines = []
        debug_count = 0

        for line in lines:
            if 'if verify_debug_' in line and 'debug_points +=' in line:
                debug_count += 1
                if debug_count == 1:
                    # First debug: keep as is or adjust based on current value
                    line = re.sub(r'(\+= )15', r'\g<1>12', line)
                    line = re.sub(r'(\+= )10', r'\g<1>12', line)
                elif debug_count == 2:
                    line = re.sub(r'(\+= )15', r'\g<1>12', line)
                    line = re.sub(r'(\+= )10', r'\g<1>11', line)
                elif debug_count == 3:
                    line = re.sub(r'(\+= )15', r'\g<1>11', line)
                    line = re.sub(r'(\+= )10', r'\g<1>11', line)
            new_lines.append(line)

        content = '\n'.join(new_lines)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print('✅ Fixed Lesson 07: Adjusted to 15+50+35')
    else:
        print('⚠️  Lesson 07 has different structure, needs manual review')

def fix_lesson_10():
    """Fix Lesson 10: Similar to Lesson 09, uses dictionary"""
    filepath = 'Lessons/Verifications/lesson_10_verification.py'

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        print('❌ Lesson 10 verification file not found')
        return

    # Backup
    shutil.copy2(filepath, filepath.replace('.py', '_backup.py'))

    # Check if it uses dictionary pattern
    if '_walk_along_points' in content or 'points_earned' in content:
        # Dictionary pattern - fix point assignments
        # This needs inspection of actual values
        print('ℹ️  Lesson 10 uses dictionary pattern, checking current values...')

        # Read current assignment patterns
        walk_patterns = re.findall(r"_walk_along_points\['[^']+'\] = (\d+)", content)
        try_patterns = re.findall(r"_try_it_yourself_points\['[^']+'\] = (\d+)", content)
        debug_patterns = re.findall(r"_debug_points\['[^']+'\] = (\d+)", content)

        print(f'   Current Walk-Along: {walk_patterns} = {sum(int(p) for p in walk_patterns)}')
        print(f'   Current Try It: {try_patterns} = {sum(int(p) for p in try_patterns)}')
        print(f'   Current Debug: {debug_patterns} = {sum(int(p) for p in debug_patterns)}')

        # We need manual adjustment based on actual structure
        print('⚠️  Lesson 10 needs manual point adjustment in code')
    else:
        print('❌ Lesson 10 structure unknown, needs manual review')

print('='*80)
print('FIXING REMAINING VERIFICATION SCRIPTS (Lessons 6, 7, 10)')
print('='*80)
print()

fix_lesson_06()
fix_lesson_07()
fix_lesson_10()

print()
print('='*80)
print('DONE! Run audit_grading_validation.py to verify fixes.')
print('='*80)
