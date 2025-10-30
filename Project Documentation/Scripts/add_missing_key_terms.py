"""
Add additional key terms to lessons that have fewer than 10 terms.
These additions include review terms and related concepts.
"""

import os
import re

BASE_DIR = r"G:\My Drive\Colab Notebooks\COSC1315\Resources\Code with Mosh - Source Lessons"

# Additional terms to add to each lesson (only for those with < 10 terms)
ADDITIONAL_TERMS = {
    "04": [
        "- **User Interaction** — The process of a program communicating with and receiving data from the user",
        "- **Console Input** — Data entered by the user through the terminal or console window",
        "- **Variable Assignment** — Storing the result of `input()` in a variable for later use",
        "- **Blocking Operation** — A function call that waits for user action before continuing (like `input()`)",
    ],
    
    "05": [
        "- **Type Mismatch** — An error that occurs when performing operations on incompatible data types",
    ],
    
    "08": [
        "- **Binary Operator** — An operator that works with two operands (e.g., `+`, `-`, `*`, `/`)",
        "- **Unary Operator** — An operator that works with one operand (e.g., `-x` for negation)",
        "- **Integer Division** — Division that produces a whole number result (using `//` operator)",
        "- **Floating-Point Division** — Division that produces a decimal result (using `/` operator)",
        "- **Remainder** — The value left over after division; obtained using the modulus operator `%`",
    ],
    
    "11": [
        "- **Operand** — A value or variable that an operator acts upon in an expression",
    ],
    
    "12": [
        "- **Loop Control** — Managing when a loop starts, continues, or terminates",
        "- **Exit Condition** — The state that must be reached for a loop to stop executing",
        "- **Loop Termination** — The act of ending a loop's execution when its condition becomes `False`",
    ],
    
    "13": [
        "- **Iterate** — To repeat a process or loop through elements one by one",
        "- **Loop Index** — A variable that tracks the current position in a sequence during iteration",
    ],
    
    "15": [
        "- **Ordered Collection** — A data structure where elements maintain their position and can be accessed by index",
        "- **Collection** — A general term for data structures that store multiple values",
        "- **Array** — A similar concept to a list in other programming languages; Python uses lists instead",
    ],
    
    "16": [
        "- **Multidimensional Array** — A general term for arrays with more than one dimension",
        "- **Grid** — A visual representation of data arranged in rows and columns, like a 2D list",
        "- **Element Access** — Retrieving a specific value from a data structure using its position",
    ],
    
    "17": [
        "- **List Modification** — Changing, adding, or removing elements from a list",
        "- **In-Place Modification** — Changing a list directly without creating a new one",
        "- **Method Chaining** — Calling multiple methods in sequence (limited for lists since many methods return `None`)",
    ],
    
    "18": [
        "- **Packing** — Creating a tuple by grouping multiple values together",
        "- **Sequence Type** — A category of data types that store ordered collections (lists, tuples, strings)",
        "- **Ordered Sequence** — A collection where elements have a defined order and position",
    ],
}

def add_terms_to_lesson(lesson_num):
    """Add additional key terms to a specific lesson file"""
    lesson_key = f"{lesson_num:02d}"
    
    if lesson_key not in ADDITIONAL_TERMS:
        return False, "No additional terms defined"
    
    # Find the file
    files = os.listdir(BASE_DIR)
    lesson_file = None
    for f in files:
        if f.startswith(f"Lesson_{lesson_key}_") and f.endswith(".md"):
            lesson_file = f
            break
    
    if not lesson_file:
        return False, "File not found"
    
    filepath = os.path.join(BASE_DIR, lesson_file)
    
    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Key Terms section and add terms before the closing ---
    pattern = r'(## Key Terms\s*\n\n(?:.*?\n)*?)(\n---\s*\n\s*## Teaching Notes)'
    
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return False, "Key Terms section not found"
    
    key_terms_section = match.group(1)
    additional_terms_text = "\n".join(ADDITIONAL_TERMS[lesson_key])
    
    # Insert additional terms at the end of the Key Terms section
    new_key_terms = key_terms_section.rstrip() + "\n" + additional_terms_text + "\n"
    
    new_content = content[:match.start()] + new_key_terms + match.group(2) + content[match.end():]
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f"Added {len(ADDITIONAL_TERMS[lesson_key])} terms"

# Process lessons needing more terms
print("="*80)
print("ADDING ADDITIONAL KEY TERMS TO LESSONS WITH FEWER THAN 10")
print("="*80)
print()

lessons_to_update = [4, 5, 8, 11, 12, 13, 15, 16, 17, 18]

success = 0
failed = 0

for lesson_num in lessons_to_update:
    result, message = add_terms_to_lesson(lesson_num)
    if result:
        print(f"✅ Lesson {lesson_num:02d}: {message}")
        success += 1
    else:
        print(f"❌ Lesson {lesson_num:02d}: {message}")
        failed += 1

print()
print("="*80)
print(f"✅ Successfully updated: {success} lessons")
if failed > 0:
    print(f"❌ Failed: {failed} lessons")
print("="*80)
