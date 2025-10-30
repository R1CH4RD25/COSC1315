# Google Colab Heading Structure - Quick Reference

**Purpose:** Ensure all notebooks use proper heading hierarchy for collapsible sections  
**Date:** October 20, 2025  
**Version:** 3.0

---

## 📑 Why Heading Structure Matters

Google Colab automatically creates a **Table of Contents** from Markdown headings. Proper heading hierarchy enables:

✅ **Collapsible sections** - Students can hide completed work  
✅ **Easy navigation** - Jump to any section instantly  
✅ **Reduced clutter** - Focus on one task at a time  
✅ **Better organization** - Clear visual structure  
✅ **Progress tracking** - See outline of all tasks

---

## 🏗️ Required Heading Structure

### Complete Hierarchy:

```markdown
# Lesson XX: Topic Name                    ← H1 (only one per notebook)
  └─ Main title, always visible

## 📚 Objectives and Learning Goals        ← H2 (collapsible section)
  └─ Can be hidden after reading

## ⚙️ Run This First - Setup                ← H2 (collapsible section)
  └─ Run once, then hide

## 📺 Walk-Along Tasks                      ← H2 (collapsible section)
  ├─ ### Walk-Along Task 1: [Name]         ← H3 (sub-item)
  ├─ ### Walk-Along Task 2: [Name]         ← H3 (sub-item)
  └─ ### Walk-Along Task 3: [Name]         ← H3 (sub-item)

## 🎯 Try It Yourself                       ← H2 (collapsible section)
  ├─ ### Try It Yourself 1: [Name]         ← H3 (sub-item)
  └─ ### Try It Yourself 2: [Name]         ← H3 (sub-item)

## 🐞 Debug the Bug                         ← H2 (collapsible section)
  ├─ ### Debug Task 1: [Name]              ← H3 (sub-item)
  └─ ### Debug Task 2: [Name]              ← H3 (sub-item)

## 📊 What's My Grade?                      ← H2 (collapsible section)
  └─ Final grading section
```

---

## 📋 Cell-by-Cell Implementation

### Section 1: Title and Objectives

```markdown
Cell 1 (Markdown):
# Lesson XX: Topic Name

**Video Source:** [Link]
**Time Range:** HH:MM - HH:MM

---

Cell 2 (Markdown):
## 📚 Objectives and Learning Goals

By the end of this lesson, you will be able to:
- [Objective 1]
- [Objective 2]
- [Objective 3]

---
```

### Section 2: Setup

```markdown
Cell 3 (Markdown):
## ⚙️ Run This First - Setup

**Instructions:**
1. Click play ▶️ on the cell below
2. Authorize Google Drive access
3. Wait for "✅ Setup complete!"

You only need to run this ONCE per session.

---

Cell 4 (Code):
# Setup code here
from google.colab import drive
drive.mount('/content/drive')
# ... imports ...
print("✅ Setup complete!")
```

### Section 3: Walk-Along

```markdown
Cell 5 (Markdown):
---

## 📺 Walk-Along Tasks

**Instructions:** Follow Mosh's video. Run verification after each task.

**Total Points:** 20 points

---

Cell 6 (Markdown):
### Walk-Along Task 1: [Description] ([X] points)

[Task instructions here]

Cell 7 (Code):
# Student code

Cell 8 (Code):
verify_task_1()
```

### Section 4: Try It Yourself

```markdown
Cell N (Markdown):
---

## 🎯 Try It Yourself

**Instructions:** Create your own code. No examples provided!

**Total Points:** 40 points

---

Cell N+1 (Markdown):
### Try It Yourself 1: [Description] ([X] points)

Requirements:
1. [Requirement]
2. [Requirement]

Cell N+2 (Code):
# Student code

Cell N+3 (Code):
verify_try_it_yourself_1()
```

### Section 5: Debug

```markdown
Cell M (Markdown):
---

## 🐞 Debug the Bug

**Instructions:** Find and fix the bugs in the code below.

**Total Points:** 40 points

---

Cell M+1 (Markdown):
### Debug Task 1: [Description] ([X] points)

**Goal:** [What code should do]

Cell M+2 (Code):
# Broken code here

Cell M+3 (Code):
verify_debug_1()
```

### Section 6: Grading

```markdown
Cell Z-1 (Markdown):
---

## 📊 What's My Grade?

**Total Points:** 100

Run the cell below to see your grade.

After checking, you can:
- ✅ Submit if happy
- 🔄 Go back and fix tasks
- 💾 Run again to see updated score

---

Cell Z (Code):
calculate_grade()
```

---

## 🎯 Heading Level Rules

### DO:
- ✅ Use ONE `#` (H1) for lesson title only
- ✅ Use `##` (H2) for all major sections
- ✅ Use `###` (H3) for individual tasks within sections
- ✅ Add emojis to section headers for visual recognition
- ✅ Include point values in task headers
- ✅ Use `---` horizontal rules between major sections

### DON'T:
- ❌ Use multiple H1 headings
- ❌ Skip heading levels (H2 → H4)
- ❌ Put task numbers in H2 headers
- ❌ Forget horizontal rules between sections
- ❌ Use H2 for individual tasks (makes TOC too cluttered)

---

## 📖 Table of Contents Preview

When properly structured, students see:

```
📖 Table of Contents
  ▼ Lesson 03: Variables                    ← Always visible
    ▶ 📚 Objectives and Learning Goals      ← Can collapse
    ▶ ⚙️ Run This First - Setup              ← Can collapse
    ▼ 📺 Walk-Along Tasks                    ← Expanded
        Walk-Along Task 1: Create Variable
        Walk-Along Task 2: Update Variable
        Walk-Along Task 3: Data Types
    ▶ 🎯 Try It Yourself                     ← Can collapse
    ▶ 🐞 Debug the Bug                       ← Can collapse
    ▶ 📊 What's My Grade?                    ← Can collapse
```

**Click ▶ to expand** | **Click ▼ to collapse**

---

## 🎓 Benefits for Students

### Scenario 1: First Time Opening Notebook
- See full outline in TOC
- Understand lesson structure
- Know how many tasks to complete

### Scenario 2: Working Through Lesson
- Collapse completed sections
- Focus only on current task
- Less scrolling required

### Scenario 3: Returning to Lesson
- Quickly jump to incomplete tasks
- Review specific sections
- Check final grade

### Scenario 4: Debugging Issues
- Navigate directly to problem task
- See related tasks in same section
- Keep other sections collapsed

---

## ✅ Quick Checklist

When creating a new notebook, verify:

- [ ] ONE H1 heading (`#`) for lesson title
- [ ] SIX H2 headings (`##`) for major sections:
  - [ ] Objectives and Learning Goals
  - [ ] Run This First - Setup
  - [ ] Walk-Along Tasks
  - [ ] Try It Yourself
  - [ ] Debug the Bug
  - [ ] What's My Grade?
- [ ] H3 headings (`###`) for individual tasks
- [ ] Emojis in section headers (📚 ⚙️ 📺 🎯 🐞 📊)
- [ ] Point values in task headers
- [ ] Horizontal rules (`---`) between sections
- [ ] Proper nesting (H2 → H3, not H2 → H4)

---

## 📁 Example Files

**See Working Example:**  
`Sample Lessons/Lesson_03_Test_Verification.ipynb`

**Complete Template:**  
`Templates/COLAB_NOTEBOOK_STRUCTURE_WITH_GRADING.md`

---

## 🔧 Troubleshooting

### Problem: Sections Not Collapsible
**Cause:** Using wrong heading level  
**Fix:** Ensure major sections use `##` (H2)

### Problem: TOC Too Cluttered
**Cause:** Using H2 for individual tasks  
**Fix:** Use `###` (H3) for tasks, `##` (H2) for sections only

### Problem: Can't Find Section in TOC
**Cause:** Forgot heading markup  
**Fix:** Ensure all section headers start with `##`

### Problem: Wrong Nesting
**Cause:** Skipped heading levels  
**Fix:** Follow hierarchy: H1 → H2 → H3 (don't skip)

---

**Last Updated:** October 20, 2025  
**Status:** ✅ CURRENT STANDARD  
**Applies To:** All COSC 1315 lesson notebooks
