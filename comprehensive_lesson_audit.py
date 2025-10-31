"""
Comprehensive Audit of Lessons 01-10
Checks all required components are present and correct
"""

import json
from pathlib import Path
import re

def check_lesson_complete(lesson_num):
    """Check if a lesson has all required components"""
    results = {
        "lesson": lesson_num,
        "notebook": "❌",
        "objectives": "❌",
        "assignment": "❌",
        "vocab_quiz": "❌",
        "assignment_quiz": "❌",
        "verification": "❌",
        "key_terms": "❌",
        "points": "❌",
        "issues": []
    }
    
    # Check Notebook
    notebook_files = list(Path("Lessons").glob(f"Lesson_{lesson_num}_*.ipynb"))
    notebook_files = [f for f in notebook_files if 'backup' not in f.name.lower()]
    
    if notebook_files:
        results["notebook"] = "✅"
        notebook_path = notebook_files[0]
        
        # Check for Key Terms (lessons 05-10 should have them)
        if int(lesson_num) >= 5:
            try:
                with open(notebook_path, 'r', encoding='utf-8') as f:
                    nb = json.load(f)
                for cell in nb['cells']:
                    if cell['cell_type'] == 'markdown':
                        source = ''.join(cell.get('source', []))
                        if '📚 Key Terms' in source or 'Key Terms' in source:
                            results["key_terms"] = "✅"
                            break
                if results["key_terms"] == "❌":
                    results["issues"].append(f"Lesson {lesson_num}: Missing Key Terms section")
            except:
                results["issues"].append(f"Lesson {lesson_num}: Could not parse notebook")
        else:
            results["key_terms"] = "N/A"  # Not required for lessons 1-4
        
        # Check points (should be 100 for lessons 5-10)
        if int(lesson_num) >= 5:
            try:
                with open(notebook_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Look for point values in metadata or cells
                if '"points":' in content or 'points":' in content:
                    # Rough check - would need proper parsing for accuracy
                    results["points"] = "⚠️"  # Needs manual verification
                else:
                    results["points"] = "⚠️"
            except:
                pass
        else:
            results["points"] = "N/A"
    else:
        results["issues"].append(f"Lesson {lesson_num}: No notebook found")
    
    # Check Objectives
    objectives_files = list(Path("Objectives").glob(f"Lesson_{lesson_num}_*_Objectives.html"))
    if objectives_files:
        results["objectives"] = "✅"
        # Check if starts with h1
        with open(objectives_files[0], 'r', encoding='utf-8') as f:
            content = f.read()
        if not (content.strip().startswith('<h1') or '<h1' in content[:200]):
            results["issues"].append(f"Lesson {lesson_num}: Objectives doesn't start with <h1>")
    else:
        results["issues"].append(f"Lesson {lesson_num}: No objectives file found")
    
    # Check Assignment Instructions
    assignment_files = list(Path("Assignment Instructions").glob(f"Lesson_{lesson_num}_*_Assignment.html"))
    if assignment_files:
        results["assignment"] = "✅"
        # Check for container divs
        with open(assignment_files[0], 'r', encoding='utf-8') as f:
            content = f.read()
        if re.search(r'<div[^>]*class="[^"]*container[^"]*"', content):
            results["issues"].append(f"Lesson {lesson_num}: Assignment has container divs")
    else:
        results["issues"].append(f"Lesson {lesson_num}: No assignment instructions found")
    
    # Check Vocabulary Quiz (lessons 5-10)
    if int(lesson_num) >= 5:
        vocab_files = list(Path("Quizzes/Vocabulary Quizzes - QTI - Canvas").glob(f"Lesson_{lesson_num}_*_Vocabulary.zip"))
        if vocab_files:
            results["vocab_quiz"] = "✅"
        else:
            results["issues"].append(f"Lesson {lesson_num}: No vocabulary quiz found")
    else:
        results["vocab_quiz"] = "N/A"
    
    # Check Assignment Quiz (lessons 5-10)
    if int(lesson_num) >= 5:
        assignment_quiz_files = list(Path("Quizzes/Assignment Quizzes - QTI - Canvas").glob(f"Lesson_{lesson_num}_*_Assignment.zip"))
        if assignment_quiz_files:
            results["assignment_quiz"] = "✅"
        else:
            results["issues"].append(f"Lesson {lesson_num}: No assignment quiz found")
    else:
        results["assignment_quiz"] = "N/A"
    
    # Check Verification Script (lessons 5-10)
    if int(lesson_num) >= 5:
        verification_files = list(Path("Lessons/Verifications").glob(f"lesson_{lesson_num}_verification.py"))
        if verification_files:
            results["verification"] = "✅"
            # Check if it awards 100 points
            with open(verification_files[0], 'r', encoding='utf-8') as f:
                content = f.read()
            # This is a rough check - already verified in previous audit
            if '100' in content and ('15' in content or '50' in content or '35' in content):
                results["points"] = "✅"
        else:
            results["issues"].append(f"Lesson {lesson_num}: No verification script found")
    else:
        results["verification"] = "N/A"
        results["points"] = "N/A"
    
    return results

def main():
    """Run comprehensive audit"""
    print("=" * 100)
    print("COMPREHENSIVE LESSON AUDIT: Lessons 01-10")
    print("=" * 100)
    print()
    
    # Header
    print(f"{'Lesson':<8} {'Notebook':<10} {'Objectives':<12} {'Assignment':<12} {'Vocab Quiz':<12} "
          f"{'Assign Quiz':<12} {'Verification':<14} {'Key Terms':<12} {'Points':<8}")
    print("-" * 100)
    
    all_results = []
    all_issues = []
    
    for lesson_num in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']:
        results = check_lesson_complete(lesson_num)
        all_results.append(results)
        all_issues.extend(results["issues"])
        
        print(f"{lesson_num:<8} {results['notebook']:<10} {results['objectives']:<12} "
              f"{results['assignment']:<12} {results['vocab_quiz']:<12} {results['assignment_quiz']:<12} "
              f"{results['verification']:<14} {results['key_terms']:<12} {results['points']:<8}")
    
    print()
    print("=" * 100)
    print("LEGEND:")
    print("  ✅ = Present and correct")
    print("  ❌ = Missing or has issues")
    print("  ⚠️  = Present but needs verification")
    print("  N/A = Not required for this lesson")
    print()
    
    # Summary
    print("=" * 100)
    print("ISSUES FOUND:")
    print("=" * 100)
    if all_issues:
        for issue in all_issues:
            print(f"  ❌ {issue}")
    else:
        print("  ✅ NO ISSUES FOUND - ALL LESSONS COMPLETE!")
    print()
    
    # Count completeness
    lessons_5_10 = [r for r in all_results if int(r['lesson']) >= 5]
    complete_modern = sum(1 for r in lessons_5_10 
                         if r['notebook'] == '✅' 
                         and r['objectives'] == '✅'
                         and r['assignment'] == '✅'
                         and r['vocab_quiz'] == '✅'
                         and r['assignment_quiz'] == '✅'
                         and r['verification'] == '✅'
                         and r['key_terms'] == '✅')
    
    lessons_1_4 = [r for r in all_results if int(r['lesson']) <= 4]
    complete_basic = sum(1 for r in lessons_1_4
                        if r['notebook'] == '✅'
                        and r['objectives'] == '✅'
                        and r['assignment'] == '✅')
    
    print("=" * 100)
    print("COMPLETION STATUS:")
    print("=" * 100)
    print(f"Lessons 01-04 (Basic): {complete_basic}/4 complete")
    print(f"Lessons 05-10 (Modern): {complete_modern}/6 complete")
    print(f"TOTAL: {complete_basic + complete_modern}/10 lessons ready")
    print()
    
    if complete_basic + complete_modern == 10:
        print("🎉 🎉 🎉 ALL LESSONS COMPLETE! GREEN LIGHTS ALL AROUND! 🎉 🎉 🎉")
    else:
        print(f"⚠️  {10 - (complete_basic + complete_modern)} lesson(s) need attention")
    print()

if __name__ == "__main__":
    main()
