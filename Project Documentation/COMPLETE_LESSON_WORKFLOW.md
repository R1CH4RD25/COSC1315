# Complete Lesson Creation Workflow

**Purpose:** Step-by-step process for creating complete lesson packages for COSC 1315
**Created:** October 30, 2025
**Updated:** October 31, 2025 - Added QTI 1.2 format requirements
**Status:** Established and validated through Lesson 10

---

## ⚠️ CRITICAL REQUIREMENTS

### Quiz Format
**ALL quizzes MUST use full QTI 1.2 format** (`<questestinterop>` structure).
- ❌ Simple `<quiz>` format does NOT auto-create quizzes in Canvas
- ✅ Use `convert_quizzes_to_qti.py` script to convert simple format to QTI 1.2
- ✅ Reference Lessons 05-10 quizzes for proper format examples

### Point Values
- Each quiz MUST total **100 points**
- 10 questions × 10 points each = 100 points
- Set `<fieldentry>10</fieldentry>` for `points_possible` in each question

---

## 📋 Workflow Overview

For each lesson, create **FOUR components** in this order:

1. **Learning Objectives (HTML)** → Canvas assignment page (no container divs!)
2. **Lesson Notebook (Colab)** → Google Colab with GitHub integration
3. **Vocabulary Quiz (QTI 1.2 XML)** → Canvas quiz import (use conversion script)
4. **Assignment Quiz (QTI 1.2 XML)** → Canvas quiz import (use conversion script)

---## 🎯 STEP 1: Create Learning Objectives (HTML)

### Purpose
Canvas assignment page that students see before opening the Colab notebook. Provides clear expectations and vocabulary.

### File Location
```
Objectives/Lesson_XX_Topic_Name_Objectives.html
```

### Required Structure

#### **Section 1: Learning Objectives**
Format:
```html
<h2>Learning Objectives</h2>
<p>By the end of this lesson, students will be able to:</p>

<p><strong>Objective Category Name</strong></p>
<ul>
    <li><p>Specific measurable outcome with examples</p></li>
    <li><p>Another specific outcome</p></li>
</ul>
```

**Requirements:**
- **5-7 objective categories** (bold headers)
- **12-16 specific measurable outcomes** (bullet points)
- Use `<code>` tags for Python code: `<code>input()</code>`
- Include concrete examples in bullet points
- Last category always: **"Recognize common pitfalls"**

#### **Section 2: Assignment Instructions**
Format:
```html
<hr />
<h2>Assignment Instructions</h2>
<p>For this activity, you will:</p>
<ul>
    <li><p>Open a new notebook in Google Colab and give it a title that reflects <strong>Lesson XX &mdash; Topic Name</strong>.</p></li>
    <li>
        <p>Write a program that:</p>
        <ul>
            <li><p>Specific coding task with code example</p></li>
            <li><p>Another requirement</p></li>
        </ul>
    </li>
    <li><p>Run all cells top-to-bottom to ensure there are no errors.</p></li>
    <li><p>Save and submit your completed notebook through <strong>Google Classroom</strong>.</p></li>
</ul>
```

**Requirements:**
- Nested bullet structure (main tasks → sub-tasks)
- Concrete code examples where relevant
- Clear step-by-step instructions
- Final step always: "Run all cells... submit through Google Classroom"

#### **Section 3: Key Terms (Vocabulary)**
Format:
```html
<hr />
<h2>Key Terms</h2>
<ul>
    <li><p><strong>Term Name</strong> &mdash; Clear, concise definition with example if needed.</p></li>
</ul>
```

**Requirements:**
- **EXACTLY 10 terms** (no more, no fewer)
- Each term: `<strong>Term</strong> &mdash; Definition`
- Definitions must be testable (for vocabulary quiz)
- Include function names, concepts, and technical terms
- Use `<code>` tags for code elements in definitions

### HTML Formatting Standards
- Use `&mdash;` for em-dashes (not `-` or `--`)
- Use `&rsquo;` for apostrophes in contractions
- Use `<code>` for all code elements
- Use `<strong>` for bold terms
- Proper nesting: `<li><p>...</p></li>`
- Use `&nbsp;` for blank lines

### Example Reference
See `Objectives/Lesson_02_How_Python_Code_Gets_Executed_Objectives.html` or the Lesson 04 example provided in this document.

---

## 📓 STEP 2: Create Lesson Notebook (Google Colab)

### Purpose
Interactive coding lesson where students watch video, code along, and get auto-graded feedback.

### File Location
```
Lessons/Lesson_XX_Topic_Name.ipynb
```

### Required Structure

#### **Cell 1: Title**
```markdown
# Lesson XX — Topic Name (MM:SS–MM:SS)
```

#### **Cell 2: Watch Section**
```markdown
## 🎥 Watch
**Clip:** MM:SS–MM:SS
**Video:** [Code with Mosh - Python for Beginners](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=XXXXs)

**Focus:** Brief description of what Mosh teaches in this segment.
```

#### **Cell 3: Learning Objectives**
```markdown
## 📚 Objectives and Learning Goals

By the end of this lesson, you will be able to:
- Objective 1 from HTML file
- Objective 2 from HTML file
- [etc.]

### Key Concepts:
- Key concept 1 (simplified from objectives)
- Key concept 2
- [4-6 bullet points total]
```

#### **Cell 4: Setup Cell** (Python)
**CRITICAL:** This cell downloads verification file from GitHub

```python
import urllib.request
import os

url = 'https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_XX_verification.py'
filename = 'lesson_XX_verification.py'

print('Downloading verification file...')
urllib.request.urlretrieve(url, filename)

# Verify download
if os.path.exists(filename):
    print(f'✅ Downloaded {filename} successfully!')
    print(f'File size: {os.path.getsize(filename)} bytes')

# Show current directory and files (for debugging)
print(f'Current directory: {os.getcwd()}')
print(f'Files in directory: {os.listdir()}')

# Add current directory to Python path
import sys
if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())

# Import verification functions
from lesson_XX_verification import (
    verify_walk_along_1,
    verify_walk_along_2,
    # [all verification functions]
    calculate_grade
)

print('✅ Setup complete! You\'re ready to start coding.')
```

**Requirements:**
- Always use `urllib.request` (not wget)
- Include file size verification
- Print current directory for debugging
- Import all verification functions
- Success message at end

#### **Cell 5: Walk-Along Tasks Section**
```markdown
## 📺 Walk-Along Tasks

**Instructions:** Follow along with the Code with Mosh video. Type the code yourself in each cell below.

**Total Points:** XX points (X points per task)

---
```

#### **Cells 6+: Individual Walk-Along Tasks**
Pattern for each task:
```markdown
### Walk-Along Task N: Task Name (X points)

**Goal:** Brief description of what to accomplish

**Instructions:**
1. Step 1
2. Step 2
3. Step 3

**Run This Cell** to complete the task, then run the verification cell below.
```

Followed by:
```python
# Student code cell (empty or starter code)
```

Then:
```python
# Verification cell
verify_walk_along_N()
```

**Requirements:**
- 3-4 walk-along tasks matching Mosh video examples
- Each task: markdown description → code cell → verification cell
- Clear numbered instructions
- 5 points per task typically

#### **Try It Yourself Section**
Similar structure but tasks require independent thinking:
- More challenging than walk-along
- Apply concepts from video to new scenarios
- Sports-themed examples where possible
- 10-15 points per task

#### **Debug the Bug Section**
Tasks with intentional errors:
- Code provided with subtle bugs
- Student must find and fix
- Tests debugging skills
- 10-15 points per task

#### **Grade Calculation Cell**
```python
calculate_grade()
```

#### **Help Section**
```markdown
## 🆘 I'm Stuck! What Do I Do?

1. **Read the error message** - Python errors tell you what's wrong
2. **Check the instructions** - Did you follow all the steps?
3. **Compare to the example** - How is your code different from the walk-along?
4. **Ask for help** - Use the class Discord/Canvas discussion
```

### Code Style Requirements
- Use sports examples where appropriate (touchdowns, yards, basketball)
- Clear variable names (no `x`, `y` - use `touchdowns`, `points`)
- Comments explaining tricky parts
- Consistent indentation
- Follow PEP 8 style guide

---

## 🔍 STEP 3: Create Verification System (Python)

### Purpose
Auto-grading functions that check student code and provide instant feedback.

### File Location
```
Lessons/Verifications/lesson_XX_verification.py
```

### Requirements
- One verification function per task
- `calculate_grade()` function that summarizes all scores
- Check variable existence, types, and values
- Check code structure (uses input(), uses print(), etc.)
- Provide helpful hints when tasks fail
- Show point breakdown clearly

### Example Function Structure
```python
def verify_walk_along_1():
    """
    Verify Walk-Along Task 1: Task Name (5 points)
    Components:
    - Component 1 (2 pts)
    - Component 2 (1 pt)
    - Component 3 (2 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 5
    feedback = []

    # Check component 1
    if 'variable_name' in user_ns:
        points += 2
        feedback.append("✅ Variable exists (+2 pts)")
    else:
        feedback.append("❌ Variable not found (0 pts)")
        feedback.append("💡 Hint: Create a variable named 'variable_name'")

    # [More checks...]

    # Display results
    print(f"\n{'='*50}")
    print(f"Walk-Along Task 1: Task Name")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\n🎯 Score: {points}/{max_points} points")
    print(f"{'='*50}\n")

    return points, max_points
```

### Repository Upload
- Push to GitHub: `Lessons/Verifications/lesson_XX_verification.py`
- File must be publicly accessible
- URL pattern: `https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_XX_verification.py`

---

## 📝 STEP 4: Create Vocabulary Quiz (QTI XML)

### Purpose
10-question Canvas quiz testing key terminology and concepts.

### File Location
```
Quizzes/Vocabulary Quizzes - QTI - Canvas/Lesson_XX_Topic_Name_Vocabulary.xml
```

### Requirements

#### ⚠️ CRITICAL: Use Full QTI 1.2 Format
**MUST use the complete QTI 1.2 format with `<questestinterop>` structure.**
Simple `<quiz>` format does NOT auto-create quizzes in Canvas!

See `convert_quizzes_to_qti.py` script or reference Lesson 05/06 quizzes for proper format.

#### Quiz Format
- **MUST total 100 points** when imported to Canvas
- **10 questions = 10 points each** (set `points_possible` to 10 in each `<item>`)
- **MUST use full QTI 1.2 structure** (see Required Structure below)

#### Required XML Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2
                 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="lesson_XX_vocabulary_quiz" title="Lesson XX: Topic Name - Vocabulary Quiz">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>3</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>cc_weighting</fieldlabel>
        <fieldentry>not_weighted</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_timelimit</fieldlabel>
        <fieldentry>600</fieldentry>  <!-- 10 minutes -->
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
      <!-- Questions go here -->
    </section>
  </assessment>
</questestinterop>
```

#### Question Content
- **10 questions total** (exactly 10, no more, no fewer)
- **1 point per question**
- **Multiple choice format**
- **Questions derived from Key Terms section** of objectives HTML

#### Question Types
1. **Definition Questions** (4-5 questions)
   - "What does the `input()` function do?"
   - Direct testing of vocabulary definitions

2. **Conceptual Questions** (3-4 questions)
   - "Why does input() always return a string?"
   - Testing understanding of concepts

3. **Application Questions** (2-3 questions)
   - "When should you use int() instead of float()?"
   - Testing when/how to use terms

#### Answer Choices
- 4 options per question (a, b, c, d)
- One clearly correct answer
- Distractors should be plausible but wrong
- Avoid "all of the above" or "none of the above"

#### HTML Encoding
- Use `&lt;code&gt;` for code in questions: `&lt;code&gt;input()&lt;/code&gt;`
- Escape special characters properly
- Use `&lt;pre&gt;` for code blocks

### Example Question Structure
```xml
<item ident="q1" title="Question 1">
    <itemmetadata>
        <qtimetadata>
            <qtimetadatafield>
                <fieldlabel>question_type</fieldlabel>
                <fieldentry>multiple_choice_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
                <fieldlabel>points_possible</fieldlabel>
                <fieldentry>10</fieldentry>  <!-- 10 points per question = 100 total -->
            </qtimetadatafield>
        </qtimetadata>
    </itemmetadata>
    <presentation>
        <material>
            <mattext texttype="text/html">&lt;p&gt;Question text here&lt;/p&gt;</mattext>
        </material>
        <response_lid ident="response1" rcardinality="Single">
            <render_choice>
                <response_label ident="a">
                    <material>
                        <mattext texttype="text/plain">Answer choice A</mattext>
                    </material>
                </response_label>
                <response_label ident="b">
                    <material>
                        <mattext texttype="text/plain">Answer choice B</mattext>
                    </material>
                </response_label>
                <response_label ident="c">
                    <material>
                        <mattext texttype="text/plain">Answer choice C</mattext>
                    </material>
                </response_label>
                <response_label ident="d">
                    <material>
                        <mattext texttype="text/plain">Answer choice D</mattext>
                    </material>
                </response_label>
            </render_choice>
        </response_lid>
    </presentation>
    <resprocessing>
        <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
        </outcomes>
        <respcondition continue="No">
            <conditionvar>
                <varequal respident="response1">a</varequal>  <!-- Correct answer -->
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
        </respcondition>
    </resprocessing>
</item>
```

#### How to Create Quizzes
**Option 1: Use the Conversion Script (Recommended)**
1. Create quiz in simple format with `<quiz>`, `<question>`, `<answer fraction="100">` tags
2. Run: `python convert_quizzes_to_qti.py` (modify script with your lesson details)
3. Script converts to full QTI 1.2 format automatically

**Option 2: Manual Creation**
- Copy structure from `Lessons/Vocabulary Quizzes - QTI - Canvas/Lesson_05_Type_Conversion_Vocabulary.zip`
- Extract, modify questions, repackage as ZIP

#### Required Package Structure
Must create a ZIP file containing:
- `imsmanifest.xml` (Canvas package metadata)
- `quiz.xml` (QTI 1.2 formatted quiz)

Use `convert_quizzes_to_qti.py` to generate both files automatically.

---

## 🎯 STEP 5: Create Assignment Quiz (QTI XML)

### Purpose
10-question Canvas quiz testing practical application and problem-solving.

### File Location
```
Quizzes/Assignment Quizzes - QTI - Canvas/Lesson_XX_Topic_Name_Assignment.xml
```

### Requirements

#### ⚠️ CRITICAL: Use Full QTI 1.2 Format
**MUST use the complete QTI 1.2 format with `<questestinterop>` structure.**
Simple `<quiz>` format does NOT auto-create quizzes in Canvas!

See `convert_quizzes_to_qti.py` script or reference Lesson 05/06 quizzes for proper format.

#### Quiz Format
- **MUST total 100 points** when imported to Canvas
- **10 questions = 10 points each** (set `points_possible` to 10 in each `<item>`)
- **MUST use full QTI 1.2 structure** (same as vocabulary quiz)

#### Required XML Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2
                 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="lesson_XX_assignment_quiz" title="Lesson XX: Topic Name - Assignment Quiz">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>3</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>cc_weighting</fieldlabel>
        <fieldentry>not_weighted</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_timelimit</fieldlabel>
        <fieldentry>900</fieldentry>  <!-- 15 minutes -->
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
      <!-- Questions go here -->
    </section>
  </assessment>
</questestinterop>
```
    <qtimetadatafield>
        <fieldlabel>qmd_timelimit</fieldlabel>
        <fieldentry>900</fieldentry>  <!-- 15 minutes -->
    </qtimetadatafield>
</qtimetadata>
```

#### Question Content
- **10 questions total**
- **1 point per question**
- **Multiple choice format**
- **Questions derived from lesson tasks** (walk-along, try it yourself, debug)

#### Question Types
1. **Code Output Prediction** (2-3 questions)
   ```
   What will this code output?
   ```python
   name = input("Name: ")
   print(type(name))
   ```
   Answer: <class 'str'>
   ```

2. **Debug Scenarios** (3-4 questions)
   ```
   This code produces a TypeError. How do you fix it?
   ```python
   age = input("Age: ")
   years_left = 100 - age
   ```
   Answer: Convert age with int(): years_left = 100 - int(age)
   ```

3. **Application Problems** (2-3 questions)
   ```
   You're converting weight from pounds to kg (multiply by 0.45).
   What type conversion should you use?
   Answer: float() - because weight can have decimals
   ```

4. **Real-World Scenarios** (1-2 questions)
   ```
   You're building a touchdown calculator. User enters touchdowns,
   multiply by 6. What's the complete correct code?
   Answer: [show complete working code]
   ```

#### Sports-Themed Examples
- Touchdowns → points calculator
- Yards → meters converter
- Basketball score tracker
- Football statistics

#### Code Formatting
Use `&lt;pre&gt;` for code blocks:
```xml
<mattext texttype="text/html">&lt;p&gt;What will this code output?&lt;/p&gt;
&lt;pre&gt;birth_year = input("Year: ")
print(type(birth_year))&lt;/pre&gt;</mattext>
```

---

## 🚀 STEP 6: Deploy to GitHub and Canvas

### GitHub Deployment

1. **Copy files to Git repository** (C:\Dev\COSC1315):
   ```powershell
   Copy-Item "g:\My Drive\Colab Notebooks\COSC1315\Lessons\Lesson_XX_*.ipynb" "C:\Dev\COSC1315\Lessons\"
   Copy-Item "g:\My Drive\Colab Notebooks\COSC1315\Quizzes\**\Lesson_XX_*.xml" "C:\Dev\COSC1315\Quizzes\"
   ```

2. **Add and commit**:
   ```powershell
   cd C:\Dev\COSC1315
   & "C:\Program Files\Git\bin\git.exe" add Lessons/Lesson_XX_*.ipynb
   & "C:\Program Files\Git\bin\git.exe" add Quizzes/
   & "C:\Program Files\Git\bin\git.exe" commit -m "Add complete Lesson XX: Topic Name (notebook + quizzes)"
   ```

3. **Push to GitHub**:
   ```powershell
   & "C:\Program Files\Git\bin\git.exe" push
   ```

4. **Verify URLs**:
   - Colab: `https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_XX_Topic_Name.ipynb`
   - Verification: `https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_XX_verification.py`

### Canvas Deployment

1. **Create Assignment**:
   - Assignments → + Assignment
   - Name: "Lesson XX: Topic Name"
   - Points: 100
   - Submission type: URL submission
   - Description: Paste entire HTML from objectives file

2. **Import Vocabulary Quiz**:
   - Quizzes → Options → Import Quiz
   - Upload: `Lesson_XX_Topic_Name_Vocabulary.xml`
   - Set: Available from [date], Due [date], 10 points
   - Publish

3. **Import Assignment Quiz**:
   - Quizzes → Options → Import Quiz
   - Upload: `Lesson_XX_Topic_Name_Assignment.xml`
   - Set: Available from [date], Due [date], 10 points
   - Publish

4. **Update Assignment with Colab Link**:
   - Edit assignment description
   - Add at top:
     ```html
     <p><strong>Click here to open the lesson:</strong>
     <a href="https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_XX_Topic_Name.ipynb">
     Open Lesson XX in Google Colab</a></p>
     ```

---

## ✅ Quality Checklist

Before considering a lesson complete, verify:

### Objectives HTML
- [ ] Exactly 10 key terms
- [ ] 5-7 objective categories
- [ ] 12-16 specific measurable outcomes
- [ ] Proper HTML formatting (entities, nesting, tags)
- [ ] Assignment instructions are clear and sequential
- [ ] Last objective category: "Recognize common pitfalls"

### Lesson Notebook
- [ ] Setup cell uses urllib.request (not wget)
- [ ] All verification functions imported correctly
- [ ] 3-4 walk-along tasks (matching Mosh video)
- [ ] 3-4 try it yourself tasks
- [ ] 3 debug tasks
- [ ] Sports-themed examples where appropriate
- [ ] Clear instructions for each task
- [ ] calculate_grade() cell at end
- [ ] Help section included

### Verification System
- [ ] One function per task
- [ ] Clear point breakdown
- [ ] Helpful hints for failures
- [ ] calculate_grade() summarizes all scores
- [ ] Pushed to GitHub
- [ ] Publicly accessible via raw URL
- [ ] File size > 20KB (comprehensive checking)

### Vocabulary Quiz
- [ ] Exactly 10 questions
- [ ] All questions test key terms from objectives
- [ ] 4 answer choices per question
- [ ] 1 point per question (10 points total)
- [ ] 10 minute time limit
- [ ] 3 attempts allowed
- [ ] Proper HTML encoding for code

### Assignment Quiz
- [ ] Exactly 10 questions
- [ ] Questions test practical application
- [ ] Mix of output prediction, debugging, application
- [ ] Sports-themed examples included
- [ ] 1 point per question (10 points total)
- [ ] 15 minute time limit
- [ ] 3 attempts allowed
- [ ] Code blocks properly formatted

### GitHub Integration
- [ ] All files pushed to GitHub
- [ ] Colab link works (opens notebook)
- [ ] Setup cell downloads verification file successfully
- [ ] File size prints correctly (>20KB)
- [ ] Import functions works without errors

### Canvas Setup
- [ ] Assignment created with objectives HTML
- [ ] Colab link added to assignment
- [ ] Vocabulary quiz imported and published
- [ ] Assignment quiz imported and published
- [ ] Due dates set appropriately
- [ ] Points configured correctly (100 for assignment, 10 each quiz)

---

## 📊 Complete Lesson Package Deliverables

When finished, you should have:

| Component | File Location | Deployed To | Points |
|-----------|---------------|-------------|--------|
| Objectives HTML | `Objectives/Lesson_XX_Topic_Name_Objectives.html` | Canvas Assignment Description | N/A |
| Lesson Notebook | `Lessons/Lesson_XX_Topic_Name.ipynb` | GitHub → Colab | 100 |
| Verification System | `Lessons/Verifications/lesson_XX_verification.py` | GitHub (raw URL) | N/A |
| Vocabulary Quiz | `Quizzes/Vocabulary Quizzes - QTI - Canvas/` | Canvas Quiz | 10 |
| Assignment Quiz | `Quizzes/Assignment Quizzes - QTI - Canvas/` | Canvas Quiz | 10 |

**Total Points per Lesson:** 120 points (100 notebook + 10 vocab + 10 assignment)

---

## 🎓 Student Workflow (Their Experience)

1. **Open Canvas** → See assignment with objectives and key terms
2. **Click Colab link** → Opens lesson notebook from GitHub
3. **File → Save a copy in Drive** → Creates editable copy
4. **Run setup cell** → Downloads verification file (auto-grades tasks)
5. **Watch Mosh video** → Learn concepts
6. **Complete walk-along tasks** → Type code, run verification
7. **Complete try it yourself** → Apply concepts independently
8. **Complete debug tasks** → Find and fix errors
9. **Run calculate_grade()** → See total score
10. **Take vocabulary quiz** → Test terminology (10 pts, 3 attempts)
11. **Take assignment quiz** → Test application (10 pts, 3 attempts)
12. **Submit Colab link to Canvas** → Professor sees grade from calculate_grade()

---

## 🔧 Tools Required

- **VS Code** - File editing
- **Git** - Version control (`C:\Program Files\Git\bin\git.exe`)
- **GitHub** - Repository hosting (public: https://github.com/R1CH4RD25/COSC1315)
- **Google Drive** - Backup and file sync
- **Canvas LMS** - Course delivery
- **Python** - Testing verification scripts locally
- **Browser** - Testing Colab links and GitHub URLs

---

## 📚 Reference Documents

- **LESSON_OBJECTIVES_GUIDELINES.md** - Detailed HTML formatting rules
- **TEACHING_INSTRUCTIONS.md** - Lesson template and structure
- **GITHUB_INTEGRATION_SETUP.md** - GitHub workflow guide
- **Quizzes/README.md** - QTI quiz standards and Canvas import
- **Lesson 5** - Complete example of all four components

---

## 💡 Tips for Efficiency

1. **Start with objectives** - They define everything else
2. **Use Lesson 5 as template** - Copy structure, replace content
3. **Create verification system early** - Test as you build notebook
4. **Generate quiz questions while building** - Fresh in your mind
5. **Test in Colab before committing** - Catch URL errors early
6. **Commit frequently** - Small commits are easier to debug
7. **Use sports themes** - Engages rural Texas students
8. **Keep it simple** - Students have low motivation (0.2/10)

---

**Status:** Established workflow based on Lesson 5 success
**Last Updated:** October 30, 2025
**Repository:** https://github.com/R1CH4RD25/COSC1315
