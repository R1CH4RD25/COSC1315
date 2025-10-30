# Google Colab Notebook Structure Template (WITH VERIFICATION & GRADING)

**Version:** 3.0 (October 2025)  
**Status:** ✅ CURRENT - Component-Based Grading System  
**Purpose:** Standard structure for all COSC 1315 Lesson notebooks with automated verification and grading

---

## 📋 Overview

Each lesson notebook follows this structure:
1. **Setup Cell** - Mount Drive & Import Verifications
2. **Walk-Along Tasks** - Follow Mosh (with verification)
3. **Try It Yourself** - Independent practice (with verification)
4. **Debug the Bug** - Fix broken code (with verification)
5. **What's My Grade?** - Component-based grading

**Key Principle:** Students see MINIMAL code. All complex logic is hidden in verification files.

---

## 📑 Collapsible Heading Structure (Table of Contents)

**IMPORTANT:** Use proper heading hierarchy to enable Google Colab's collapsible sections!

Google Colab automatically creates a **Table of Contents** from Markdown headings (click the chevron ▶️ on the left sidebar). Students can collapse sections to reduce clutter and focus on one task at a time.

### Required Section Headings:

```markdown
# Lesson XX: Topic Name
    ↓ (Main title - always visible)

## 📚 Objectives and Learning Goals
    ↓ (Collapsible section - can be hidden after reading)
    
## ⚙️ Run This First - Setup
    ↓ (Collapsible section - run once, then hide)
    
## 📺 Walk-Along Tasks
    ↓ (Collapsible section - contains all walk-along tasks)
    ### Walk-Along Task 1: [Description]
    ### Walk-Along Task 2: [Description]
    ### Walk-Along Task 3: [Description]
    
## 🎯 Try It Yourself
    ↓ (Collapsible section - independent practice)
    ### Try It Yourself 1: [Description]
    ### Try It Yourself 2: [Description]
    
## 🐞 Debug the Bug
    ↓ (Collapsible section - debugging exercises)
    ### Debug Task 1: [Description]
    ### Debug Task 2: [Description]
    
## 📊 What's My Grade?
    ↓ (Collapsible section - final grading)
```

### Heading Levels Explained:

- **`#` (H1)** - Lesson title only (ONE per notebook)
- **`##` (H2)** - Major sections (collapsible in TOC)
- **`###` (H3)** - Individual tasks within sections (sub-items in TOC)
- **`####` (H4)** - Sub-details if needed (rarely used)

### Benefits for Students:

✅ **Reduce Visual Clutter** - Collapse completed sections  
✅ **Focus on Current Task** - See only what you're working on  
✅ **Easy Navigation** - Jump to any section via TOC  
✅ **Track Progress** - See outline of all tasks  
✅ **Less Overwhelming** - One section at a time

### Example TOC Structure:

When students click the chevron ▶️ they see:
```
📖 Table of Contents
  ▼ Lesson 03: Variables
    ▶ 📚 Objectives and Learning Goals
    ▶ ⚙️ Run This First - Setup
    ▼ 📺 Walk-Along Tasks
        Walk-Along Task 1: Create a Variable
        Walk-Along Task 2: Update a Variable
        Walk-Along Task 3: Data Types
    ▶ 🎯 Try It Yourself
    ▶ 🐞 Debug the Bug
    ▶ 📊 What's My Grade?
```

Students can click ▶ to expand or ▼ to collapse any section!

### Complete Notebook Outline with Cell Count:

```
Lesson XX: Topic Name
│
├─── Cell 1 (Markdown): # Lesson Title
├─── Cell 2 (Markdown): ## 📚 Objectives and Learning Goals
│
├─── Cell 3 (Markdown): ## ⚙️ Run This First - Setup
├─── Cell 4 (Code):     Setup code (Drive mount + imports)
│
├─── Cell 5 (Markdown): ## 📺 Walk-Along Tasks (Section Header)
├─── Cell 6 (Markdown): ### Walk-Along Task 1
├─── Cell 7 (Code):     Student code for Task 1
├─── Cell 8 (Code):     verify_task_1()
├─── Cell 9 (Markdown): ### Walk-Along Task 2
├─── Cell 10 (Code):    Student code for Task 2
├─── Cell 11 (Code):    verify_task_2()
│    ... (repeat for each walk-along task)
│
├─── Cell N (Markdown): ## 🎯 Try It Yourself (Section Header)
├─── Cell N+1 (Markdown): ### Try It Yourself 1
├─── Cell N+2 (Code):   Student code for TIY 1
├─── Cell N+3 (Code):   verify_try_it_yourself_1()
│    ... (repeat for each TIY task)
│
├─── Cell M (Markdown): ## 🐞 Debug the Bug (Section Header)
├─── Cell M+1 (Markdown): ### Debug Task 1
├─── Cell M+2 (Code):   Broken code for debugging
├─── Cell M+3 (Code):   verify_debug_1()
│    ... (repeat for each debug task)
│
├─── Cell Z-1 (Markdown): ## 📊 What's My Grade? (Section Header)
└─── Cell Z (Code):     calculate_grade()
```

**Total Cells:** Typically 30-50 cells depending on number of tasks

**Collapsible Sections:** 6 major sections that students can hide/show

---

## 🏗️ Standard Notebook Structure

### Cell 1: Title and Objectives (Markdown)
```markdown
# Lesson XX: Topic Name

**Video Source:** [Code with Mosh - Python Tutorial](link)  
**Time Range:** HH:MM - HH:MM

---

## 📚 Objectives and Learning Goals

By the end of this lesson, you will be able to:

- [Objective 1]
- [Objective 2]
- [Objective 3]

**Key Concepts:** [List 3-5 key terms students will learn]

---
```

### Cell 2: Setup Section Header (Markdown)
```markdown
## ⚙️ Run This First - Setup

**Instructions:**
1. Click the play button ▶️ on the cell below
2. When prompted, authorize Google Drive access
3. Wait for "✅ Setup complete!" message

**You only need to run this ONCE per session.**

After setup is complete, you can collapse this section using the Table of Contents (click ▶️ on the left sidebar).

---
```

### Cell 3: Setup Code (Code) - **STUDENTS SEE THIS**
```python
# Setup: Mount Google Drive and import verification functions
from google.colab import drive
drive.mount('/content/drive')

import sys
import importlib

# Add verification folder to path
verif_path = '/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications'
if verif_path not in sys.path:
    sys.path.insert(0, verif_path)

# Import and reload verification module
import lesson_XX_verification
importlib.reload(lesson_XX_verification)

# Import the functions we'll use
from lesson_XX_verification import *

print("✅ Setup complete! Ready to start the lesson.")
```

**What Students See:** Simple Drive mount + import statement  
**What's Hidden:** All verification logic is in `lesson_XX_verification.py`

---

## 📺 Walk-Along Section (20 points)

### Cell N: Walk-Along Section Header (Markdown)
```markdown
---

## 📺 Walk-Along Tasks

**Instructions:** Follow along with Mosh's video. After each task, run the verification cell to check your work.

**Total Points:** 20 points (divided among all walk-along tasks)

---
```

### Pattern for Each Walk-Along Task

**Cell N+1: Task Instructions (Markdown)**
```markdown
### Walk-Along Task 1: [Action Description] ([X] points)

**Video:** [Link with timestamp]

### What to Do:

Watch Mosh's video at timestamp [MM:SS]. Mosh will show you [what he does].

**Your job:** Watch him code, then pause and type the same code yourself.

⚠️ **Remember:** Type what you see in the video - don't skip ahead!

---
```

**Cell N+1: Student Code (Code)**
```python
# Type your code below:
# [Brief description of what to code]

```

**Cell N+2: Verification (Code) - SIMPLE!**
```python
# Run this to check your work
verify_task_1()
```

### Walk-Along Grading Components
- **Total Points:** 20 points (divided among all walk-along tasks)
- **Components per task:** 4-5 components × points each
  - Variable exists
  - Correct value
  - Used print() function
  - Printed variable (not literal)
  - Additional task-specific requirements

**Repeat for Task 2, Task 3, Task 4, etc.**

---

## 🎯 Try It Yourself Section (40 points)

### Cell N: Try It Yourself Section Header (Markdown)
```markdown
---

## 🎯 Try It Yourself

**Instructions:** Now it's YOUR turn! Create your own code based on the requirements. No example code provided - you need to think through the solution yourself!

**Total Points:** 40 points (divided among all try-it-yourself tasks)

---
```

### Pattern for Each Try It Yourself

**Cell N+1: Task Instructions (Markdown)**
```markdown
### Try It Yourself [#]: [Task Name] ([X] points)

Now it's your turn to create your own [concept]!

### Requirements:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

### Example Output:
```
[Example output - NOT the code!]
```
*(Your output may be different)*

---
```

**Cell N+1: Student Code (Code)**
```python
# Type your code below:
# [Brief hint without giving away the answer]

```

**Cell N+2: Verification (Code) - SIMPLE!**
```python
# Run this to check your work
verify_try_it_yourself_1()
```

### Try It Yourself Grading Components
- **Total Points:** 40 points (divided among all try-it-yourself tasks)
- **Components per task:** 4-5 components with weighted points
  - Created variable(s): 10 points
  - Used print() function: 10 points
  - Printed variable (not literal): 15 points
  - No literals in print: 5 points
  - Additional task-specific requirements

**Repeat for TIY 2, TIY 3, etc.**

---

## 🐞 Debug the Bug Section (40 points)

### Cell N: Debug Section Header (Markdown)
```markdown
---

## 🐞 Debug the Bug

**Instructions:** Each task below has broken code. Your job is to find the bug and fix it!

**Total Points:** 40 points (divided among all debugging tasks)

**Tips:**
- Read error messages carefully
- Check for typos, missing quotes, wrong indentation
- Test your fix by running the verification cell

---
```

### Pattern for Each Debug Task

**Cell N+1: Task Instructions (Markdown)**
```markdown
### Debug Task [#]: [Bug Name] ([X] points)

**Goal:** [What the code should do]

The code below has a bug. Your job is to find it and fix it!

### What's Wrong?
[Optional hint about the type of error]

---
```

**Cell N+1: Broken Code (Code)**
```python
# FIX THIS CODE:
# There's a bug below - can you find and fix it?

[broken code provided]
```

**Cell N+2: Verification (Code) - SIMPLE!**
```python
# Run this to check your fix
verify_debug_1()
```

### Debug Grading Components
- **Total Points:** 40 points (divided among all debugging tasks)
- **Components per task:** 4-5 components checking:
  - Bug identified
  - Bug fixed correctly
  - Code runs without errors
  - Output is correct
  - Code follows best practices

**Repeat for Debug 2, Debug 3, etc.**

---

## 📊 Grading Section

### Cell N: Grade Section Header (Markdown)
```markdown
---

## 📊 What's My Grade?

Run the cell below to see your grade for this lesson.

**Total Points: 100**
- Walk-Along Tasks: 20 points (component grading)
- Try It Yourself: 40 points (component grading)
- Debug the Bug: 40 points (component grading)

**Your grade shows:**
- ✅ Which components you completed correctly
- ❌ Which components need work
- 📊 Your total score and letter grade

After checking your grade, you can:
- ✅ Submit if you're happy with your score
- 🔄 Go back and fix tasks to improve your grade
- 💾 Run this cell again to see your updated score

---
```

### Cell N+1: Grade Calculator (Code) - SUPER SIMPLE!
```python
# Calculate your grade
calculate_grade()
```

**What Students See:** ONE LINE  
**What's Hidden:** 200+ lines of component-based grading logic in `lesson_XX_verification.py`

---

## 🎓 Completion Section

### Final Cell: Completion Message (Markdown)
```markdown
---

## 🎉 Lesson Complete!

### What You Learned:

**Walk-Along (Follow & Practice):**
- ✅ [Skill 1]
- ✅ [Skill 2]
- ✅ [Skill 3]

**Try It Yourself (Independent Application):**
- ✅ [Skill 1]
- ✅ [Skill 2]
- ✅ [Skill 3]

**Debug the Bug (Problem Solving):**
- ✅ [Skill 1]
- ✅ [Skill 2]

---

## 🚀 Next Steps:

1. ✅ Check your grade above
2. 🔄 If needed, go back and improve your work
3. 💾 Save this notebook (File → Save)
4. 📤 Submit when ready

---

**Questions?** Ask your instructor for help!
```

---

## 📁 Required Verification File Structure

For EACH lesson, create: `lesson_XX_verification.py` in `Lessons/Verifications/`

### Verification File Must Include:

```python
"""
Lesson XX: [Topic] - Verification Functions
COSC 1315 - Introduction to Computer Programming
"""

import ast
import inspect

# Get IPython instance
try:
    from IPython import get_ipython
    ipython = get_ipython()
except:
    ipython = None

def _get_user_namespace():
    """Get user's namespace (where their variables live)"""
    if ipython is not None:
        return ipython.user_ns
    else:
        return globals()

def _get_previous_cell_code():
    """Get code from cell executed before verify was called"""
    if ipython is None:
        return None
    history = list(ipython.history_manager.get_range(output=False))
    if len(history) >= 2:
        return history[-2][2]
    return None

def _check_code_uses_variable(code, variable_name):
    """Check if code uses specified variable (not literal)"""
    # AST checking logic here
    pass

def _analyze_code_structure(code):
    """Analyze code for patterns (generic verification)"""
    # AST analysis logic here
    pass

# ============ WALK-ALONG VERIFICATIONS ============
def verify_task_1():
    """Verify Walk-Along Task 1 - Specific checking"""
    # Check exact variable names/values
    # Provide detailed feedback
    # Return True/False
    pass

def verify_task_2():
    """Verify Walk-Along Task 2"""
    pass

# ============ TRY IT YOURSELF VERIFICATIONS ============
def verify_try_it_yourself_1():
    """Verify TIY 1 - Generic checking"""
    # Check patterns, not exact names
    # Accept any variable name/value
    # Verify correct usage
    pass

# ============ DEBUG VERIFICATIONS ============
def verify_debug_1():
    """Verify Debug Task 1"""
    # Check if bug is fixed
    # Verify output is correct
    pass

# ============ GRADING SYSTEM ============
def calculate_grade():
    """
    Component-based grading system.
    Returns detailed grade report.
    """
    print("="*60)
    print("📊 GRADE REPORT - Lesson XX: [Topic]")
    print("="*60)
    print()
    
    total_points = 0
    max_points = 100
    
    # Walk-Along Section (20 points)
    print("📺 WALK-ALONG (20 points possible)")
    print("-" * 60)
    # Component grading for each walk-along
    # Award points per component (5 pts each typically)
    
    # Try It Yourself Section (40 points)
    print("🎯 TRY IT YOURSELF (40 points possible)")
    print("-" * 60)
    # Component grading (10+10+15+5 pattern)
    
    # Debug Section (40 points)
    print("🐛 DEBUG THE BUG (40 points possible)")
    print("-" * 60)
    # Component grading for debugging tasks
    
    # Final grade calculation
    print("="*60)
    print(f"📈 TOTAL SCORE: {total_points}/{max_points} points")
    percentage = (total_points / max_points) * 100
    print(f"📊 PERCENTAGE: {percentage:.1f}%")
    
    # Letter grade
    if percentage >= 90:
        letter = "A 🌟"
    elif percentage >= 80:
        letter = "B 😊"
    # ... etc
    
    print(f"📝 LETTER GRADE: {letter}")
    print("="*60)
    
    # Feedback based on score
    # Guide students on what to improve
    
    return total_points, max_points

# Module metadata
__version__ = "1.0.0"
__author__ = "Professor Richard Joseph Sullivan"
__course__ = "COSC 1315"
```

---

## 🎯 Point Distribution Guidelines

### Standard Distribution (Total: 100 points)

| Section | Points | Rationale |
|---------|--------|-----------|
| **Walk-Along** | 20 pts | Following instructions - foundational skill |
| **Try It Yourself** | 40 pts | Independent application - core learning |
| **Debug the Bug** | 40 pts | Problem solving - highest cognitive skill |

### Component Subdivision Examples

**Walk-Along (20 pts ÷ 4 tasks = 5 pts each):**
- Variable created: 1-2 pts
- Correct value: 1-2 pts
- Used print(): 1 pt
- Used variable in print: 1-2 pts

**Try It Yourself (40 pts ÷ 2-3 tasks):**
- Created variable: 10 pts
- Used print(): 10 pts
- Variable in print (not literal): 15 pts
- No literals/correct usage: 5 pts

**Debug (40 pts ÷ 3-4 tasks):**
- Bug identified: 3 pts
- Bug fixed correctly: 3 pts
- Code runs: 2 pts
- Output correct: 2 pts

---

## 💡 Key Pedagogical Principles

### ✅ DO:
- Keep student-facing code SIMPLE (1 line function calls)
- Hide complex logic in verification files
- Provide granular component feedback
- Allow multiple attempts (revise and recheck)
- Show exactly what to fix
- Give partial credit for partial completion

### ❌ DON'T:
- Show step-by-step code (prevents copy/paste)
- Give away answers in Try It Yourself examples
- Show "common mistakes" with solutions
- Display overwhelming amounts of code to students
- Use pass/fail only (need component breakdown)

### 🎓 Student Experience:
1. Watch video
2. Type code (no copy/paste opportunity)
3. Run simple verification (`verify_task_1()`)
4. Get instant feedback
5. Fix if needed
6. Check grade (`calculate_grade()`)
7. See exactly which components need work
8. Revise and recheck until satisfied

---

## 📝 Example Complete Structure

See: `Sample Lessons/Lesson_03_Test_Verification.ipynb`

This test notebook demonstrates:
- ✅ Clean, minimal student-facing code
- ✅ Hidden verification logic
- ✅ Component-based grading
- ✅ One-line grade calculator
- ✅ Detailed feedback without overwhelming code

---

## 🔄 Migration from Old Format

If updating existing notebooks:

1. **Add Setup Cell** with Drive mount + verification imports
2. **Convert Walk-Alongs:**
   - Remove step-by-step instructions
   - Add video timestamp reference
   - Add verification cell after each task
3. **Convert Try It Yourself:**
   - Remove example code
   - Show example OUTPUT only
   - Remove "common mistakes" section
   - Add verification cell
4. **Add Debug Section** (if not present)
5. **Add Grading Section:**
   - Markdown explaining point distribution
   - Single-line `calculate_grade()` call
6. **Create Verification File:**
   - Implement all verify functions
   - Implement `calculate_grade()` with components
7. **Test thoroughly** with various student scenarios

---

## 📚 Related Documentation

- **Component Grading Details:** `COMPONENT_GRADING_SYSTEM_COMPLETE.md`
- **Verification System:** `GENERIC_VERIFICATION_SYSTEM.md`
- **Quick Reference:** `VERIFICATION_QUICK_REFERENCE.md`
- **Testing Guide:** `TESTING_GUIDE_LESSON_03.md`
- **Lesson Objectives:** `LESSON_OBJECTIVES_GUIDELINES.md`

---

**Last Updated:** October 20, 2025  
**Version:** 3.0  
**Status:** ✅ CURRENT STANDARD for all new lessons
