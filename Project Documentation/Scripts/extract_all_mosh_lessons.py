"""
Comprehensive script to extract all Code with Mosh lessons
and create individual lesson files matching COSC 1315 schedule
"""
import os
import re

# Map lessons to course schedule
lesson_mapping = {
    "01": {"title": "Your First Python Program", "timestamp": "6:08–8:08", "week": 1},
    "02": {"title": "How Python Code Gets Executed", "timestamp": "8:08–11:20", "week": 2},
    "03": {"title": "Variables", "timestamp": "12:56–18:16", "week": 3},
    "04": {"title": "Receiving Input", "timestamp": "18:16–22:08", "week": 3},
    "05": {"title": "Type Conversion", "timestamp": "22:40–29:28", "week": 4},
    "06": {"title": "Strings", "timestamp": "29:28–37:28", "week": 5},
    "07": {"title": "Formatted Strings & String Methods", "timestamp": "37:28–48:32", "week": 5},
    "08": {"title": "Arithmetic Operations, Operator Precedence & Math Functions", "timestamp": "48:32–58:16", "week": 6},
    "09": {"title": "If Statements", "timestamp": "58:16–1:06:24", "week": 7},
    "10": {"title": "Logical Operators & Comparison Operators", "timestamp": "1:06:24–1:16:16", "week": 7},
    "11": {"title": "Weight Converter Program", "timestamp": "1:16:16–1:20:40", "week": 8},
    "12": {"title": "While Loops", "timestamp": "1:20:40–1:41:44", "week": 9},
    "13": {"title": "For Loops", "timestamp": "1:41:44–1:47:44", "week": 10},
    "14": {"title": "Nested Loops", "timestamp": "1:47:44–1:55:44", "week": 10},
    "15": {"title": "Lists", "timestamp": "1:55:44–2:01:44", "week": 11},
    "16": {"title": "2D Lists", "timestamp": "2:01:44–2:05:04", "week": 11},
    "17": {"title": "List Methods", "timestamp": "2:05:52–2:13:20", "week": 12},
    "18": {"title": "Tuples", "timestamp": "2:13:20–2:15:28", "week": 13},
}

# Read the original markdown file
source_file = r"G:\My Drive\Colab Notebooks\COSC1315\Project Documentation\Markdown\CodeWithMosh_Lessons.md"
base_dir = r"G:\My Drive\Colab Notebooks\COSC1315\Resources\Code with Mosh - Source Lessons"

print("Reading source file...")
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split content by lesson headers (lines starting with # followed by lesson title)
lessons_text = content.split('\n\n# ')[1:]  # Skip intro text

print(f"Found {len(lessons_text)} lessons in source file\n")

# Process each lesson
for idx, lesson_text in enumerate(lessons_text[:18], 1):  # Only first 18 lessons
    lesson_num = f"{idx:02d}"
    
    if lesson_num not in lesson_mapping:
        continue
    
    # Extract lesson title and content
    parts = lesson_text.split('\n\n', 1)
    header = parts[0]
    lesson_content = parts[1] if len(parts) > 1 else ""
    
    # Get mapped lesson info
    lesson_info = lesson_mapping[lesson_num]
    
    # Create filename
    safe_title = lesson_info['title'].replace(':', '').replace('&', 'and').replace('/', '-')
    safe_title = re.sub(r'[^\w\s-]', '', safe_title).strip().replace(' ', '_')
    filename = f"Lesson_{lesson_num}_{safe_title}.md"
    filepath = os.path.join(base_dir, filename)
    
    # Create lesson file content
    file_content = f"""# Lesson {lesson_num}: {lesson_info['title']}

**Video Timestamp:** {lesson_info['timestamp']}  
**Week:** Week {lesson_info['week']}  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

{lesson_content.strip()}

---

## Teaching Notes

### Key Concepts
- [To be added by instructor]

### Learning Objectives
- [To be added by instructor]

### Common Student Mistakes
- [To be added by instructor]

### Practice Exercises
- [To be added by instructor]

---

*This transcript is sourced from Code with Mosh's "Python for Beginners" video tutorial.*  
*Video link: https://www.youtube.com/watch?v=_uQrJ0TkZlc*
"""
    
    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)
    
    print(f"✅ Lesson {lesson_num}: {lesson_info['title']}")

print(f"\n{'='*80}")
print(f"📁 All {len(lesson_mapping)} lesson files created successfully!")
print(f"📂 Location: {base_dir}")
print(f"{'='*80}")
