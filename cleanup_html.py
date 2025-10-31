"""
HTML Cleanup Script
Fixes two issues:
1. Objectives files that don't start with <h1>
2. Assignment Instructions with container divs
"""

import re
from pathlib import Path

def fix_objectives_h1(file_path):
    """Ensure objectives file starts with <h1>"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already starts with <h1> after <body>
    if re.search(r'<body[^>]*>\s*<h1', content):
        return False, "Already starts with <h1>"
    
    # Find the first heading after <body>
    match = re.search(r'(<body[^>]*>)(.*?)(<h[1-6])', content, re.DOTALL)
    if not match:
        return False, "No heading found"
    
    body_open = match.group(1)
    before_heading = match.group(2)
    heading_tag = match.group(3)
    
    # If it's not h1, we need to change it
    if heading_tag != '<h1':
        # Find the full heading
        heading_match = re.search(r'(<h[2-6][^>]*>.*?</h[2-6]>)', content[match.start(3):], re.DOTALL)
        if heading_match:
            old_heading = heading_match.group(1)
            new_heading = re.sub(r'<h[2-6]', '<h1', old_heading)
            new_heading = re.sub(r'</h[2-6]>', '</h1>', new_heading)
            
            content = content.replace(old_heading, new_heading, 1)
            
            # Save backup
            backup = file_path.with_suffix('.html.backup')
            with open(backup, 'w', encoding='utf-8') as f:
                f.write(open(file_path).read())
            
            # Save fixed version
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, f"Changed {heading_tag} to <h1>"
    
    return False, "Already uses <h1>"

def remove_container_divs(file_path):
    """Remove container divs from assignment instructions"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count container divs
    container_count = len(re.findall(r'<div[^>]*class="[^"]*container[^"]*"', content, re.I))
    
    if container_count == 0:
        return False, "No container divs found"
    
    # Save backup
    backup = file_path.with_suffix('.html.backup')
    with open(backup, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Remove container divs and their closing tags
    # This is tricky - we need to match the div and find its closing tag
    
    # Pattern to find container divs
    pattern = r'<div[^>]*class="[^"]*container[^"]*"[^>]*>'
    
    # Remove opening container divs
    new_content = re.sub(pattern, '', content, flags=re.I)
    
    # Count removed opening tags
    removed = container_count
    
    # Remove matching number of </div> tags (remove last N)
    div_closes = list(re.finditer(r'</div>', new_content))
    if len(div_closes) >= removed:
        # Remove the last N closing divs (likely the container ones)
        for i in range(removed):
            pos = div_closes[-(i+1)].start()
            new_content = new_content[:pos] + new_content[pos+6:]
    
    # Save fixed version
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f"Removed {removed} container div(s)"

def main():
    """Run HTML cleanup"""
    print("=" * 80)
    print("HTML CLEANUP")
    print("=" * 80)
    print()
    
    # Fix Objectives
    print("FIXING OBJECTIVES FILES:")
    print("-" * 80)
    objectives_dir = Path("Objectives")
    fixed_objectives = 0
    
    for file in sorted(objectives_dir.glob("Lesson_*_Objectives.html")):
        fixed, msg = fix_objectives_h1(file)
        status = "✅" if fixed else "⏭️ "
        print(f"{status} {file.name}: {msg}")
        if fixed:
            fixed_objectives += 1
    
    print()
    
    # Fix Assignment Instructions
    print("FIXING ASSIGNMENT INSTRUCTIONS:")
    print("-" * 80)
    assignments_dir = Path("Assignment Instructions")
    fixed_assignments = 0
    
    for file in sorted(assignments_dir.glob("Lesson_*_Assignment.html")):
        fixed, msg = remove_container_divs(file)
        status = "✅" if fixed else "⏭️ "
        print(f"{status} {file.name}: {msg}")
        if fixed:
            fixed_assignments += 1
    
    print()
    print("=" * 80)
    print(f"SUMMARY: Fixed {fixed_objectives} objectives, {fixed_assignments} assignments")
    print("=" * 80)

if __name__ == "__main__":
    main()
