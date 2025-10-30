"""
Script to remove duplicate Learning Objectives and Key Terms sections from lesson files.
Keeps only the LAST occurrence (which should be right before Teaching Notes).
"""

import os
import re

BASE_DIR = r"G:\My Drive\Colab Notebooks\COSC1315\Resources\Code with Mosh - Source Lessons"

def clean_lesson_file(filepath):
    """Remove all but the last Learning Objectives and Key Terms sections"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the Teaching Notes section
    teaching_notes_pattern = r'---\s*\n\s*## Teaching Notes'
    
    if not re.search(teaching_notes_pattern, content):
        print(f"⚠️  No Teaching Notes found in {os.path.basename(filepath)}")
        return False
    
    # Split at Teaching Notes
    parts = re.split(teaching_notes_pattern, content)
    
    if len(parts) != 2:
        print(f"⚠️  Unexpected structure in {os.path.basename(filepath)}")
        return False
    
    before_teaching = parts[0]
    teaching_and_after = parts[1]
    
    # Find the original transcript section (should be first)
    transcript_pattern = r'(## Original Video Transcript\s*\n\n.*?)(\n\n---\s*\n\n## Learning Objectives)'
    
    match = re.search(transcript_pattern, before_teaching, re.DOTALL)
    
    if match:
        # Keep just the transcript part
        cleaned_content = before_teaching[:match.end(1)] + '\n\n---\n\n## Teaching Notes' + teaching_and_after
    else:
        # If pattern doesn't match, try to find transcript end another way
        # Keep everything up to first "---" after transcript
        transcript_end = re.search(r'(## Original Video Transcript\s*\n\n.*?\n\n)---', before_teaching, re.DOTALL)
        if transcript_end:
            cleaned_content = before_teaching[:transcript_end.end()] + '\n\n## Teaching Notes' + teaching_and_after
        else:
            print(f"❌ Could not find transcript section in {os.path.basename(filepath)}")
            return False
    
    # Write cleaned content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    return True

# Process all lesson files
print("="*80)
print("CLEANING DUPLICATE OBJECTIVES FROM LESSON FILES")
print("="*80)
print()

files = sorted([f for f in os.listdir(BASE_DIR) if f.startswith("Lesson_") and f.endswith(".md")])

success = 0
failed = 0

for filename in files:
    filepath = os.path.join(BASE_DIR, filename)
    if clean_lesson_file(filepath):
        print(f"✅ Cleaned: {filename}")
        success += 1
    else:
        print(f"❌ Failed: {filename}")
        failed += 1

print()
print("="*80)
print(f"✅ Successfully cleaned: {success} files")
print(f"❌ Failed: {failed} files")
print("="*80)
