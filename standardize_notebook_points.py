"""
Fix notebooks to have exactly 15+50+35=100 point distribution
"""
import json
import re
import shutil

def fix_notebook_to_standard(filename, walk_target=15, try_target=50, debug_target=35):
    """
    Adjust notebook to standard point distribution: 15 walk-along, 50 try-it, 35 debug = 100
    """
    filepath = f'Lessons/{filename}'
    print(f'\n{"="*80}')
    print(f'Processing: {filename}')
    print(f'Target: {walk_target} walk-along + {try_target} try-it + {debug_target} debug = {walk_target+try_target+debug_target}')
    
    # Backup
    backup_path = filepath.replace('.ipynb', '_backup_before_standard.ipynb')
    shutil.copy2(filepath, backup_path)
    print(f'Backup: {backup_path.split("/")[-1]}')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Find all tasks and their current points
    walk_tasks = []
    try_tasks = []
    debug_tasks = []
    
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            content = ''.join(cell['source'])
            
            if '### Walk-Along Task' in content:
                match = re.search(r'\((\d+)\s+points?\)', content)
                if match:
                    walk_tasks.append({'cell_idx': i, 'old_points': int(match.group(1))})
            elif '### Try It Yourself' in content and re.search(r'Try It Yourself \d+:', content):
                match = re.search(r'\((\d+)\s+points?\)', content)
                if match:
                    try_tasks.append({'cell_idx': i, 'old_points': int(match.group(1))})
            elif re.search(r'### Debug (Task|Challenge) \d+:', content):
                match = re.search(r'\((\d+)\s+points?\)', content)
                if match:
                    debug_tasks.append({'cell_idx': i, 'old_points': int(match.group(1))})
    
    print(f'\nFound:')
    print(f'  Walk-Along: {len(walk_tasks)} tasks ({sum(t["old_points"] for t in walk_tasks)} pts)')
    print(f'  Try It: {len(try_tasks)} tasks ({sum(t["old_points"] for t in try_tasks)} pts)')
    print(f'  Debug: {len(debug_tasks)} tasks ({sum(t["old_points"] for t in debug_tasks)} pts)')
    
    # Calculate new point distributions
    def distribute_points(target, num_tasks):
        """Distribute target points across tasks as evenly as possible"""
        if num_tasks == 0:
            return []
        base = target // num_tasks
        remainder = target % num_tasks
        return [base + (1 if i < remainder else 0) for i in range(num_tasks)]
    
    walk_new = distribute_points(walk_target, len(walk_tasks))
    try_new = distribute_points(try_target, len(try_tasks))
    debug_new = distribute_points(debug_target, len(debug_tasks))
    
    print(f'\nNew distribution:')
    print(f'  Walk-Along: {walk_new} = {sum(walk_new)} pts')
    print(f'  Try It: {try_new} = {sum(try_new)} pts')
    print(f'  Debug: {debug_new} = {sum(debug_new)} pts')
    
    # Apply changes
    for task, new_points in zip(walk_tasks, walk_new):
        cell_idx = task['cell_idx']
        old_points = task['old_points']
        content = ''.join(nb['cells'][cell_idx]['source'])
        content = re.sub(rf'\({old_points}\s+points?\)', f'({new_points} points)', content)
        nb['cells'][cell_idx]['source'] = content.split('\n')
        # Fix newlines
        nb['cells'][cell_idx]['source'] = [line + '\n' for line in nb['cells'][cell_idx]['source'][:-1]] + [nb['cells'][cell_idx]['source'][-1]]
    
    for task, new_points in zip(try_tasks, try_new):
        cell_idx = task['cell_idx']
        old_points = task['old_points']
        content = ''.join(nb['cells'][cell_idx]['source'])
        content = re.sub(rf'\({old_points}\s+points?\)', f'({new_points} points)', content)
        nb['cells'][cell_idx]['source'] = content.split('\n')
        nb['cells'][cell_idx]['source'] = [line + '\n' for line in nb['cells'][cell_idx]['source'][:-1]] + [nb['cells'][cell_idx]['source'][-1]]
    
    for task, new_points in zip(debug_tasks, debug_new):
        cell_idx = task['cell_idx']
        old_points = task['old_points']
        content = ''.join(nb['cells'][cell_idx]['source'])
        content = re.sub(rf'\({old_points}\s+points?\)', f'({new_points} points)', content)
        nb['cells'][cell_idx]['source'] = content.split('\n')
        nb['cells'][cell_idx]['source'] = [line + '\n' for line in nb['cells'][cell_idx]['source'][:-1]] + [nb['cells'][cell_idx]['source'][-1]]
    
    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)
    
    print(f'\n✅ FIXED: {filename} now has {sum(walk_new)+sum(try_new)+sum(debug_new)} points')

# Process all lessons 5-10
lessons = [
    'Lesson_05_Type_Conversion.ipynb',
    'Lesson_06_Strings.ipynb',
    'Lesson_07_Formatted_Strings.ipynb',
    'Lesson_08_Arithmetic_Operations.ipynb',
    'Lesson_09_If_Statements.ipynb',
    'Lesson_10_Logical_Operators.ipynb',
]

print('=' * 80)
print('STANDARDIZING NOTEBOOK POINT VALUES')
print('Target Distribution: 15 walk-along + 50 try-it + 35 debug = 100 points')
print('=' * 80)

for lesson in lessons:
    fix_notebook_to_standard(lesson)

print('\n' + '=' * 80)
print('✅ ALL NOTEBOOKS STANDARDIZED TO 100 POINTS')
print('=' * 80)
