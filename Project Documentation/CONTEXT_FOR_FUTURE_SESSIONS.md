# 🤖 Context for Future AI Sessions

**Last Updated:** October 20, 2025  
**Purpose:** Help AI assistants quickly understand project state and continue work seamlessly

---

## 🎯 Project Overview

**Course:** COSC 1315 - Introduction to Computer Science (Python)  
**Institution:** Cisco College (Dual Credit) + Woodson ISD  
**Instructor:** Professor Sullivan (also Tech Director)  
**Environment:** Google Colab notebooks on Chromebooks (1:1)  
**Budget:** $0 (everything must be free)

---

## 👨‍🎓 Critical Student Context

**You MUST understand this or you'll over-engineer everything:**

- **Interest in coding:** 0.2/10 (apathetic, placed not chosen)
- **Prior knowledge:** 1/10 (absolute beginners)
- **Primary interest:** Sports (use sports examples)
- **Help-seeking behavior:** Rare (build self-help resources)
- **Success metric:** COMPLETION, not passion
- **Goal:** Earn college credit (CCMR), not become programmers

**Design Principle:** Keep it simple, bland but functional, auto-grade everything.

**Read immediately:** `Course Planning/STUDENT_PROFILE_AND_CONSTRAINTS.md`

---

## 📚 Where to Find Everything

### **Start Here Documents** (READ FIRST!)
1. **README.md** - Master index of all documentation
2. **Course Planning/COURSE_OVERVIEW_AND_GOALS.md** - Why this course exists
3. **Course Planning/STUDENT_PROFILE_AND_CONSTRAINTS.md** - Who we're teaching
4. **Course Planning/IMPLEMENTATION_PLAN.md** - What to build and when

### **Current Work Templates**
- **Templates/COLAB_NOTEBOOK_STRUCTURE_WITH_GRADING.md** ⭐ - CURRENT lesson template (v3.0)
- **Templates/COLAB_HEADING_STRUCTURE.md** - Quick reference for headings
- **Templates/LESSON_OBJECTIVES_GUIDELINES.md** - How to create objectives
- **Templates/VIDEO_SOURCES.md** - All 36 lesson timestamps

### **Verification System** (Auto-Grading)
- **Verification System/VERIFICATION_SYSTEM_IMPLEMENTATION.md** - Complete guide
- **Verification System/COMPONENT_GRADING_SYSTEM_COMPLETE.md** - Grading details
- **Verification System/STUDENT_QUICK_START.md** - Student-facing guide

### **Historical Context**
- **Implementation History/** - What we built and why
- **Status Reports/** - Current status and urgent items
- **Deprecated/** - Old files (don't use these!)

---

## 🏗️ Current Project Structure

```
COSC1315/
├── Lessons/
│   ├── Lesson_01_Your_First_Python_Program.ipynb ✅ COMPLETE
│   ├── Lesson_02_How_Python_Code_Gets_Executed.ipynb ✅ COMPLETE
│   ├── Lesson_03_Variables.ipynb ✅ COMPLETE
│   ├── Lesson_04_Receiving_Input.ipynb ✅ COMPLETE
│   ├── Lesson_05_Type_Conversion.ipynb ✅ COMPLETE
│   └── Lesson_06-36... ⏳ TO DO
│
├── Lessons/Verifications/
│   ├── lesson_03_verification.py ✅ (with component grading)
│   └── [other lessons TBD]
│
├── Objectives/
│   └── Lesson_02_How_Python_Code_Gets_Executed_Objectives.html ✅
│
├── Projects/
│   └── Project_01_My_Pet_Info.ipynb ✅ COMPLETE
│
├── Quizzes/
│   ├── Assignment Quizzes - QTI - Canvas/
│   └── Vocabulary Quizzes - QTI - Canvas/
│
├── Resources/
│   └── Code with Mosh - Source Lessons/ (transcript extractions)
│
├── Sample Lessons/
│   ├── make_notebook.py (generates test notebooks)
│   └── Lesson_03_Test_Verification.ipynb (test notebook)
│
└── Project Documentation/ (YOU ARE HERE)
    ├── README.md ⭐ (START HERE)
    ├── Templates/ (current templates)
    ├── Course Planning/ (strategic docs)
    ├── Guides/ (how-to workflows)
    ├── Verification System/ (auto-grading docs)
    ├── Implementation History/ (completed work)
    ├── Status Reports/ (current status)
    └── Deprecated/ (old files - don't use)
```

---

## 🎓 Lesson Structure (Current Standard)

### **Google Colab Notebook Structure**

**Every lesson follows this pattern:**

```markdown
# Lesson XX: Topic Name

## 📚 Objectives
- Learning objective 1
- Learning objective 2
- Learning objective 3

## ⚙️ Setup
[Code cell with verification imports]

## 📺 Walk-Along (20 points)
### Walk-Along Task 1 (5 pts)
[Instructions]
[Code cell]
[Verification cell]

## 🎯 Try It Yourself (40 points)
### Try It Yourself Task 1 (10 pts)
[Instructions]
[Code cell]
[Verification cell]

## 🐞 Debug the Bug (40 points)
### Debug Exercise 1 (40 pts)
[Intentionally broken code]
[Code cell to fix]
[Verification cell]

## 📊 Calculate Your Grade
[Code cell: calculate_grade()]
```

### **Key Features**

1. **Collapsible Sections**
   - ONE H1 (#) for lesson title
   - SIX H2 (##) for major sections (collapsible in TOC)
   - Multiple H3 (###) for individual tasks

2. **Component-Based Grading**
   - Walk-Along: 20 points (4 components × 5 pts)
   - Try It Yourself: 40 points (variable components)
   - Debug: 40 points (variable components)
   - **Total: 100 points**

3. **Hidden Complexity**
   - Students see: `verify_walk_along_task_1()`
   - Students see: `calculate_grade()`
   - All logic is in: `Lessons/Verifications/lesson_XX_verification.py`

4. **Self-Help Resources**
   - "I'm Stuck" protocol in every notebook
   - Sports-themed examples
   - Instant feedback from verification

---

## 🔧 Verification System Details

### **How It Works**

1. **Student writes code** in a code cell
2. **Student runs verification** in next cell: `verify_task_name()`
3. **Verification uses AST analysis** to check code structure
4. **Instant feedback** (✅/❌) with specific guidance
5. **Component grading** tracks partial credit

### **Verification File Structure**

```python
# Lessons/Verifications/lesson_XX_verification.py

# Component tracking
_walk_along_results = {}
_try_it_yourself_results = {}
_debug_results = {}

def verify_walk_along_task_1():
    """Check if student completed task correctly."""
    # AST-based code analysis
    # Update _walk_along_results
    # Print feedback
    
def calculate_grade():
    """Calculate final grade with component breakdown."""
    # Sum all component scores
    # Display detailed breakdown
    # Show percentage and letter grade
```

### **Key Files**

- **lesson_03_verification.py** - REFERENCE implementation with component grading
- **Verification System/GENERIC_VERIFICATION_SYSTEM.md** - Template for new lessons
- **Verification System/COMPONENT_GRADING_SYSTEM_COMPLETE.md** - How grading works

---

## 🚀 Common Workflows

### **Creating a New Lesson**

1. **Extract Video Transcript**
   ```powershell
   python "Scripts/youtube_transcript_extractor.py" VIDEO_ID START_TIME END_TIME
   ```

2. **Create Lesson Notebook**
   - Use `Templates/COLAB_NOTEBOOK_STRUCTURE_WITH_GRADING.md`
   - Follow 6-section structure (Objectives, Setup, Walk-Along, Try It Yourself, Debug, Grade)
   - Use proper heading hierarchy (H1 → H2 → H3)

3. **Create Verification File**
   - Copy `Lessons/Verifications/lesson_03_verification.py` as template
   - Update verification functions for new tasks
   - Implement component grading

4. **Create Objectives HTML**
   - Use `Templates/LESSON_OBJECTIVES_GUIDELINES.md`
   - Canvas-ready HTML format
   - Save to `Objectives/`

5. **Create Quizzes**
   - Vocabulary Quiz (10 questions from Key Terms)
   - Assignment Quiz (10 questions from tasks)
   - QTI format for Canvas import

### **Testing a Lesson**

```powershell
# Generate test notebook
cd "Sample Lessons"
python make_notebook.py

# Upload to Google Colab
# Test all verification functions
# Test grade calculation
# Verify TOC collapsibility
```

### **Finding Video Timestamps**

Check: `Templates/VIDEO_SOURCES.md`

All 36 lessons have YouTube links with start/end times.

---

## 📋 Current Status (October 20, 2025)

### **✅ Completed**

- ✅ Lessons 01-05 created and complete
- ✅ Project 01 (My Pet Info) created
- ✅ Lesson 03 verification system with component grading
- ✅ Collapsible heading structure implemented
- ✅ Template system (v3.0) created
- ✅ Documentation fully organized (28 files → 3 in root)
- ✅ Verification system documented
- ✅ Student quick start guide created

### **⏳ In Progress**

- Creating remaining lessons (06-36)
- Creating verification files for each lesson
- Creating Canvas quizzes

### **🎯 Next Steps**

1. Continue creating lessons 06-36
2. Create verification files for each lesson
3. Create Canvas quizzes for each lesson
4. Test all lessons in Google Colab
5. Deploy to Canvas LMS

### **⚠️ Known Issues**

- Old template still exists in `Deprecated/` (marked as superseded)
- Some lessons may need sports examples added
- Quiz creation workflow not yet automated

---

## 🎨 Design Patterns We Use

### **✅ DO THIS**

- ✅ Use sports examples (batting average, yards per carry)
- ✅ Keep it simple (students are beginners)
- ✅ Auto-grade everything (Canvas quizzes, verification functions)
- ✅ Provide instant feedback (verification functions)
- ✅ Hide complexity (separate verification files)
- ✅ Use component grading (partial credit)
- ✅ Include "I'm Stuck" protocol
- ✅ Use collapsible sections (H2 headings)
- ✅ Follow 6-section structure

### **❌ DON'T DO THIS**

- ❌ Don't build badge systems (too complex)
- ❌ Don't create new video content (Mosh exists)
- ❌ Don't use external APIs (network restrictions)
- ❌ Don't expect passionate engagement (apathetic students)
- ❌ Don't over-engineer (Tech Director has limited time)
- ❌ Don't use old templates (check date/version)
- ❌ Don't make all-or-nothing grading (use components)
- ❌ Don't put 200+ lines of code in notebooks (hide it)

---

## 🔧 Tools & Technologies

### **Required Tools**

- **Google Colab** - Notebook environment (free, no installation)
- **Canvas LMS** - Course management and quizzes
- **Python 3.11** - Programming language
- **YouTube** - Video content (Code with Mosh)

### **Installed Python Packages**

```bash
youtube-transcript-api==1.2.3  # Extract video transcripts
markitdown[all]                # Convert DOCX to Markdown
# See Tools Available/PYTHON_TOOLS_REFERENCE.md for full list
```

### **VS Code Extensions** (for development)

- Python
- Jupyter
- Markdown Preview

---

## 🆘 Common Questions & Answers

### **Q: Where's the current lesson template?**
**A:** `Templates/COLAB_NOTEBOOK_STRUCTURE_WITH_GRADING.md` (Version 3.0)

### **Q: How do I create a verification file?**
**A:** Copy `Lessons/Verifications/lesson_03_verification.py` and modify. See `Verification System/GENERIC_VERIFICATION_SYSTEM.md`

### **Q: How many points is each section worth?**
**A:** Walk-Along: 20, Try It Yourself: 40, Debug: 40 (Total: 100)

### **Q: Do students see the grading code?**
**A:** No! It's hidden in separate verification files. Students only see `verify_task_name()` and `calculate_grade()`

### **Q: What if a student gets stuck?**
**A:** Every notebook has "I'm Stuck" protocol with 3 steps before asking for help

### **Q: Can I use the old template in Deprecated/ folder?**
**A:** NO! It's marked as SUPERSEDED. Use `Templates/COLAB_NOTEBOOK_STRUCTURE_WITH_GRADING.md` instead

### **Q: How do I make sections collapsible?**
**A:** Use H2 (##) for major sections. See `Templates/COLAB_HEADING_STRUCTURE.md`

### **Q: What's the YouTube video source?**
**A:** "Python Tutorial - Python Full Course for Beginners" by Programming with Mosh (6+ hours, free)

### **Q: Where are the learning objectives?**
**A:** Check `Templates/COURSE_SCHEDULE_AND_OBJECTIVES.md` for complete list by lesson

### **Q: Why sports examples?**
**A:** Students are rural Texas, low coding interest, HIGH sports interest. Sports = engagement.

---

## 🎯 Success Criteria

### **This Semester Success:**

- ✅ 80%+ completion rate
- ✅ 70%+ average quiz scores
- ✅ Students earn college credit
- ✅ Zero complaints to administration
- ✅ Professor maintains sanity

### **Student Success:**

- ✅ Can explain what a variable is
- ✅ Can identify syntax errors
- ✅ Can write "Hello, World!" from memory
- ✅ Can modify existing code
- ✅ Can decide if they want Programming I

### **NOT Expected (But Nice):**

- 🎁 1-2 students show genuine interest
- 🎁 1-2 students continue to Programming I
- 🎁 Student creates something independently

---

## 📞 Quick Command Reference

```powershell
# Extract YouTube transcript
python "Scripts/youtube_transcript_extractor.py" VIDEO_ID START END

# Generate test notebook
cd "Sample Lessons"
python make_notebook.py

# Check installed packages
python -m pip list

# Run verification tests
# (Upload to Google Colab and run cells)
```

---

## 🗺️ Navigation Shortcuts

| I Need To... | Go Here |
|--------------|---------|
| Understand project context | README.md |
| Create a new lesson | Templates/COLAB_NOTEBOOK_STRUCTURE_WITH_GRADING.md |
| Create verification file | Verification System/GENERIC_VERIFICATION_SYSTEM.md |
| Find video timestamps | Templates/VIDEO_SOURCES.md |
| See learning objectives | Templates/COURSE_SCHEDULE_AND_OBJECTIVES.md |
| Understand students | Course Planning/STUDENT_PROFILE_AND_CONSTRAINTS.md |
| Know what to build | Course Planning/IMPLEMENTATION_PLAN.md |
| See what's complete | Implementation History/ folder |
| Check current status | Status Reports/ folder |
| Reference old template | Deprecated/ (but DON'T USE IT!) |

---

## 🤖 Instructions for AI Assistants

### **When Starting a New Session:**

1. **Read this document first** (you're reading it now!)
2. **Read README.md** for complete overview
3. **Read Course Planning/STUDENT_PROFILE_AND_CONSTRAINTS.md** to understand students
4. **Ask user:** "What lesson are we working on?" or "What needs to be done?"

### **Key Principles to Remember:**

- **ALWAYS use current templates** (check Templates/ folder, check version/date)
- **NEVER suggest complex features** (remember: students are apathetic, budget is $0)
- **ALWAYS include sports examples** (their primary interest)
- **ALWAYS use component grading** (partial credit, not all-or-nothing)
- **ALWAYS hide complexity** (separate verification files)
- **ALWAYS check Deprecated/ folder** before using any file (old = bad!)

### **Before Creating Anything:**

- ✅ Check if similar work exists (Implementation History/)
- ✅ Verify you're using current template (check date/version)
- ✅ Confirm structure matches 6-section pattern
- ✅ Ensure heading hierarchy is correct (H1 → H2 → H3)
- ✅ Ask user if unsure about point distribution

### **Red Flags (Stop and Ask User):**

- 🚩 User mentions "badge system" or "gamification"
- 🚩 User wants to create new video content
- 🚩 User wants to use external APIs
- 🚩 User suggests all-or-nothing grading
- 🚩 You find yourself putting 200+ lines in a notebook cell
- 🚩 You're about to use a file from Deprecated/ folder

### **Trust But Verify:**

- Always check file dates/versions
- Always check if "SUPERSEDED" or "DEPRECATED" appears
- Always check README.md for current standards
- Always prioritize simplicity over features

---

## 📊 Project Health Indicators

### **🟢 Healthy Signs**

- Clear folder structure
- Recent documentation updates
- INDEX.md files in all folders
- Version numbers on templates
- Cross-references working

### **🟡 Warning Signs**

- Multiple versions of same file
- Conflicting information in docs
- Outdated references
- Missing INDEX.md files
- Broken cross-references

### **🔴 Critical Issues**

- Can't find current template
- Documentation contradicts itself
- Verification system broken
- Students can't access notebooks
- Grading not working

**As of October 20, 2025: Project is 🟢 HEALTHY**

---

## 📅 Maintenance Schedule

### **Weekly**

- Check Status Reports/ for urgent items
- Review any student issues
- Test new lessons in Colab

### **Monthly**

- Archive resolved status reports
- Review lesson completion rates
- Update Implementation History/

### **Quarterly**

- Review Deprecated/ folder (delete truly obsolete)
- Update templates if needed
- Assess student success metrics

---

## 🎉 Recent Major Updates

### **October 20, 2025**

- ✅ Component-based grading implemented
- ✅ Grading code hidden from students
- ✅ Collapsible heading structure added
- ✅ Template v3.0 created
- ✅ Documentation fully reorganized (28 files → 3 in root)
- ✅ Three new folders created (Verification System, Implementation History, Status Reports)
- ✅ Deprecated/ folder created and old template moved

See: `ORGANIZATION_COMPLETE_OCT_20_2025.md` for details

---

## 💡 Final Reminders

1. **Students are apathetic** - Design for completion, not passion
2. **Budget is $0** - Everything must be free
3. **Keep it simple** - You're Tech Director first, instructor second
4. **Sports examples** - Their primary interest
5. **Auto-grade everything** - No manual grading capacity
6. **Current template is v3.0** - In Templates/ folder, dated Oct 20, 2025
7. **Component grading** - Partial credit, not all-or-nothing
8. **Hide complexity** - Separate verification files
9. **Trust the documentation** - README.md is always current
10. **When in doubt, ask user** - Don't assume, verify

---

**Created:** October 20, 2025  
**Purpose:** Help AI assistants pick up project seamlessly  
**Status:** ✅ COMPLETE AND CURRENT

**To Future AI:** Read this document, read README.md, read student profile, then ask user what needs doing. You've got this! 🚀
