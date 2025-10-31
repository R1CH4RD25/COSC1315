"""
Fix point values in notebooks to total exactly 100 points
Proportionally adjusts Walk-Along, Try It Yourself, and Debug sections
"""

import json
import re
import os
import shutil

def fix_notebook_points(filename, target_total=100):
    """
    Fix point values in a notebook to total target_total points
    """
    filepath = os.path.join('Lessons', filename)

    print(f'\nProcessing: {filename}')

    # Backup
    backup_path = filepath.replace('.ipynb', '_backup_points.ipynb')
    shutil.copy2(filepath, backup_path)
    print(f'  Backup created: {os.path.basename(backup_path)}')

    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Find all point values
    point_changes = []
    current_total = 0

    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            content = ''.join(cell['source'])

            # Find point patterns
            patterns = [
                (r'(\*\*\d+\s+points?\*\*)', r'\*\*(\d+)\s+points?\*\*'),  # **10 points**
                (r'(\d+\s+points?)', r'(\d+)\s+points?'),  # 10 points
            ]

            for full_pattern, digit_pattern in patterns:
                matches = re.finditer(digit_pattern, content, re.IGNORECASE)
                for match in matches:
                    old_points = int(match.group(1))
                    current_total += old_points
                    point_changes.append({
                        'cell_idx': i,
                        'old_points': old_points,
                        'match': match,
                        'content': content
                    })

    if current_total == 0:
        print('  No points found!')
        return

    print(f'  Current total: {current_total} points')

    # Calculate adjustment factor
    adjustment = target_total / current_total
    print(f'  Adjustment factor: {adjustment:.4f}')

    # Apply adjustments
    for change in point_changes:
        cell_idx = change['cell_idx']
        old_points = change['old_points']
        new_points = max(1, round(old_points * adjustment))  # Minimum 1 point

        # Update cell content
        content = ''.join(nb['cells'][cell_idx]['source'])

        # Replace the specific point value
        # Be careful to replace the right occurrence
        content = re.sub(
            rf'\b{old_points}\s+points?\b',
            f'{new_points} points',
            content,
            count=1,
            flags=re.IGNORECASE
        )

        nb['cells'][cell_idx]['source'] = content.split('\n')

        # Add newlines back if they were removed
        nb['cells'][cell_idx]['source'] = [line + '\n' for line in nb['cells'][cell_idx]['source'][:-1]] + [nb['cells'][cell_idx]['source'][-1]]

    # Calculate new total
    new_total = 0
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            content = ''.join(cell['source'])
            matches = re.findall(r'(\d+)\s+points?', content, re.IGNORECASE)
            new_total += sum(int(m) for m in matches)

    print(f'  New total: {new_total} points')

    # If not exactly 100, adjust the largest value
    if new_total != target_total:
        diff = target_total - new_total
        print(f'  Adjusting by {diff} to reach exactly {target_total}')

        # Find the cell with the most points and adjust it
        max_points = 0
        max_cell_idx = None

        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'markdown':
                content = ''.join(cell['source'])
                matches = re.findall(r'(\d+)\s+points?', content, re.IGNORECASE)
                if matches:
                    points = int(matches[0])
                    if points > max_points:
                        max_points = points
                        max_cell_idx = i

        if max_cell_idx is not None:
            content = ''.join(nb['cells'][max_cell_idx]['source'])
            new_value = max_points + diff
            content = re.sub(
                rf'\b{max_points}\s+points?\b',
                f'{new_value} points',
                content,
                count=1,
                flags=re.IGNORECASE
            )
            nb['cells'][max_cell_idx]['source'] = [line + '\n' for line in content.split('\n')[:-1]] + [content.split('\n')[-1]]

    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)

    print(f'  ✓ Saved with adjusted points')

# Fix each lesson
lessons = [
    'Lesson_05_Type_Conversion.ipynb',
    'Lesson_06_Strings.ipynb',
    'Lesson_07_Formatted_Strings.ipynb',
    'Lesson_08_Arithmetic_Operations.ipynb',
    'Lesson_09_If_Statements.ipynb',
    'Lesson_10_Logical_Operators.ipynb',
]

print('=' * 80)
print('FIXING NOTEBOOK POINT VALUES - ROUND 2')
print('Target: 100 points per notebook')
print('Includes Lessons 5-10')
print('=' * 80)

for lesson in lessons:
    fix_notebook_points(lesson)

print('\n' + '=' * 80)
print('DONE! All notebooks adjusted to 100 points')
print('Backups saved with _backup_points.ipynb suffix')
print('=' * 80)
