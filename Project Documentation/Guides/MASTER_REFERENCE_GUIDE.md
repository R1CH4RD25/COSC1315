# COSC 1315 Course Development - Master Reference Guide

**Course:** COSC 1315.35 - Programming (Python)  
**Institution:** Cisco College  
**Platform:** Canvas LMS + Google Colab  
**Last Updated:** October 20, 2025

---

## 📁 Quick Navigation

### **Essential Documents**
- **[Teaching Instructions](../TEACHING_INSTRUCTIONS.md)** - Course context, roles, and responsibilities
- **[Lesson Objectives Guidelines](../LESSON_OBJECTIVES_GUIDELINES.md)** - Complete spec for creating lesson objectives
- **[Lesson Template](../Markdown/Colab_Lesson_Template_PromptOnly.md)** - Jupyter notebook structure template
- **[Code with Mosh Lessons](../Markdown/CodeWithMosh_Lessons.md)** - Full video transcript breakdown with timestamps

### **Tools & Resources**
- **[Python Tools Reference](../Tools Available/PYTHON_TOOLS_REFERENCE.md)** ⭐ - Quick reference for all available tools
- **[YouTube Transcript Tools Guide](YOUTUBE_TRANSCRIPT_TOOLS_GUIDE.md)** - Detailed guide for video transcript extraction

### **Scripts**
- **[YouTube Transcript Extractor](../Scripts/youtube_transcript_extractor.py)** - Extract transcripts by time range

---

## 🎯 Purpose of This Guide

This is your **central hub** for course development. Use this document to:
- **Orient yourself** when returning to the project
- **Find the right tool** for the task at hand
- **Understand the workflow** from start to finish
- **Avoid reinventing** solutions already created

---

## 🏗️ Project Structure

```
COSC1315/
├── Lessons/                    # Jupyter notebooks (.ipynb)
│   ├── Lesson_01_Your_First_Python_Program.ipynb
│   ├── Lesson_02_How_Python_Code_Gets_Executed.ipynb
│   ├── Lesson_03_Variables.ipynb
│   └── ...
│
├── Objectives/                 # HTML objectives for Canvas
│   ├── Lesson_02_How_Python_Code_Gets_Executed_Objectives.html
│   └── ...
│
├── Projects/                   # Student project notebooks
│   ├── Project_01_My_Pet_Info.ipynb
│   └── ...
│
├── Quizzes/                    # Quiz materials
│   ├── Assignment Quizzes - QTI - Canvas/
│   └── Vocabulary Quizzes - QTI - Canvas/
│
├── Assessments/               # Assessment materials
│
├── Resources/                 # Course resources
│
├── Syllabus/                  # Course syllabus documents
│
└── Project Documentation/     # ⭐ Course development materials
    ├── TEACHING_INSTRUCTIONS.md
    ├── LESSON_OBJECTIVES_GUIDELINES.md
    │
    ├── Guides/                # How-to guides for future you
    │   ├── MASTER_REFERENCE_GUIDE.md (this file)
    │   └── YOUTUBE_TRANSCRIPT_TOOLS_GUIDE.md
    │
    ├── Tools Available/       # Tool references and documentation
    │   └── PYTHON_TOOLS_REFERENCE.md
    │
    ├── Scripts/               # Python automation scripts
    │   └── youtube_transcript_extractor.py
    │
    └── Markdown/              # Converted DOCX templates
        ├── Colab_Lesson_Template_PromptOnly.md
        └── CodeWithMosh_Lessons.md
```

---

## 🔄 Complete Workflow: Creating a New Lesson

### **Phase 1: Gather Source Material**

**1. Identify the lesson from CodeWithMosh breakdown**
```markdown
Reference: Project Documentation/Markdown/CodeWithMosh_Lessons.md

Example - Lesson 06: Strings
- Timestamp: 29:28 – 37:28
- Topics covered: len(), upper(), lower(), find(), replace(), in operator
```

**2. Extract video transcript (optional but helpful)**
```bash
cd "Project Documentation/Scripts"
python youtube_transcript_extractor.py _uQrJ0TkZlc 29:28 37:28 -o temp_lesson_06.txt
```

**Benefits:**
- Get exact terminology Mosh uses
- Identify all technical terms mentioned
- Find specific code examples
- Verify concepts covered

---

### **Phase 2: Create Lesson Objectives**

**1. Reference the guidelines**
```markdown
Read: Project Documentation/LESSON_OBJECTIVES_GUIDELINES.md
```

**2. Create HTML objectives file**
```markdown
Location: Objectives/Lesson_XX_Topic_Name_Objectives.html
Format: Three sections (Learning Objectives, Assignment, Key Terms)
Key Requirement: Exactly 10 vocabulary terms
```

**3. Structure:**
```html
<h1>Lesson XX — Topic Name</h1>

<h2>Learning Objectives</h2>
<!-- 4-7 major categories with specific objectives -->

<h2>Assignment Instructions</h2>
<!-- Progressive exercises -->

<h2>Key Terms</h2>
<!-- Exactly 10 terms with definitions -->
```

**Example:**
```
See: Objectives/Lesson_02_How_Python_Code_Gets_Executed_Objectives.html
```

---

### **Phase 3: Build Jupyter Notebook**

**1. Reference the template**
```markdown
Read: Project Documentation/Markdown/Colab_Lesson_Template_PromptOnly.md
```

**2. Create notebook structure:**

```markdown
# Lesson XX — TITLE (TIME RANGE)

## 🎥 Watch
Clip: HH:MM–HH:MM
Focus: One-line description

## 🎯 Goal (Learning Objectives)
- Objective 1
- Objective 2
- Objective 3

## 🧭 What You Will Learn
- Key concept 1
- Key concept 2
- Key concept 3

## 🧠 Key Terms (10)
1. Term - Definition
2. Term - Definition
...

## 💻 How to run in Colab
- Instructions for students

## 🚶 Walk-Along Tasks
### 🥕 Task 1 — Description
Prompt: Clear instruction
Code: # Type your code below:
Expected Output: Example

## 📌 Try It Yourself
### 🧠 TIY 1 — Title
Prompt: Similar to walk-along but independent
Code: # Type your code below:
Example Output: Example

## 🐞 Debug the Bug
### 🔧 Bug 1 — Title
Goal: What students must achieve
# Broken starter code
```

**3. Save location:**
```
Lessons/Lesson_XX_Topic_Name.ipynb
```

---

### **Phase 4: Quality Check**

**Verify:**
- ✅ Video timestamp matches CodeWithMosh breakdown
- ✅ All code examples work in Google Colab
- ✅ Objectives align with actual lesson content
- ✅ Exactly 10 vocabulary terms
- ✅ Progressive difficulty in exercises
- ✅ Proper naming convention used
- ✅ Files in correct folders

---

## 🛠️ Common Tasks & How-To

### **Task: Extract Transcript for Specific Lesson**

```bash
# Navigate to scripts folder
cd "Project Documentation/Scripts"

# Extract lesson transcript
python youtube_transcript_extractor.py _uQrJ0TkZlc START END

# Example - Lesson 03 (Variables: 12:56–18:16)
python youtube_transcript_extractor.py _uQrJ0TkZlc 12:56 18:16 -o lesson_03_transcript.txt
```

---

### **Task: Convert DOCX Template to Markdown**

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert('path/to/template.docx')

with open('output.md', 'w', encoding='utf-8') as f:
    f.write(result.text_content)
```

---

### **Task: Find Technical Terms in Transcript**

```python
import re

# Read transcript
with open('lesson_transcript.txt') as f:
    text = f.read()

# Common Python terms
python_terms = ['print', 'input', 'int', 'float', 'str', 'variable', 
                'function', 'parameter', 'argument', 'return', 'type']

# Find occurrences
found_terms = []
for term in python_terms:
    if re.search(rf'\b{term}\b', text, re.IGNORECASE):
        found_terms.append(term)

print(f"Found {len(found_terms)} technical terms:")
for term in found_terms:
    print(f"  - {term}")
```

---

### **Task: Create Quick Vocabulary Draft**

```python
from youtube_transcript_api import YouTubeTranscriptApi

# Extract lesson content
video_id = "_uQrJ0TkZlc"
start = 12*60 + 56  # 12:56 in seconds
end = 18*60 + 16    # 18:16 in seconds

transcript = YouTubeTranscriptApi.get_transcript(video_id)
lesson_text = ' '.join([
    entry['text'] for entry in transcript
    if start <= entry['start'] <= end
])

# Identify capitalized terms (often technical terms)
import re
terms = re.findall(r'\b[A-Z][a-z]+\b', lesson_text)
unique_terms = list(set(terms))

print(f"Potential vocabulary words: {unique_terms[:10]}")
```

---

## 📚 Key Reference Documents

### **[TEACHING_INSTRUCTIONS.md](../TEACHING_INSTRUCTIONS.md)**

**When to use:** Starting any new lesson or project

**Contains:**
- Course context (Cisco College, Canvas LMS)
- Video source (Code with Mosh)
- Your role vs. AI assistant role
- Content creation guidelines
- Teaching approach principles

**Key takeaways:**
- Base content on Mosh's videos
- Format for Google Colab
- Write as a top professor
- Progressive difficulty
- Hands-on, practical examples

---

### **[LESSON_OBJECTIVES_GUIDELINES.md](../LESSON_OBJECTIVES_GUIDELINES.md)**

**When to use:** Creating any lesson objectives HTML file

**Contains:**
- File organization structure
- Naming conventions
- Three-section format (Objectives, Assignment, Key Terms)
- HTML formatting examples
- Quality checklist

**Critical requirement:**
- **Exactly 10 vocabulary terms per lesson**
- Terms must be Python-specific or programming concepts
- Include clear, student-friendly definitions

---

### **[Colab_Lesson_Template_PromptOnly.md](../Markdown/Colab_Lesson_Template_PromptOnly.md)**

**When to use:** Creating any Jupyter notebook lesson

**Contains:**
- Complete notebook structure
- Section headers with emojis
- Task types (Walk-Along, Try It Yourself, Debug the Bug)
- Code cell format
- Output examples

**Sections:**
- 🎥 Watch (video timestamp)
- 🎯 Goal (objectives)
- 🧭 What You Will Learn
- 🧠 Key Terms (10)
- 💻 How to run in Colab
- 🚶 Walk-Along Tasks (3+)
- 📌 Try It Yourself (5+)
- 🐞 Debug the Bug (5+)

---

### **[CodeWithMosh_Lessons.md](../Markdown/CodeWithMosh_Lessons.md)**

**When to use:** Finding which topics are covered in which video segments

**Contains:**
- Complete breakdown of Code with Mosh video
- Exact timestamps for each lesson
- Full transcripts of Mosh's teaching
- Topics covered in each segment

**How to use:**
1. Find lesson by topic name
2. Note timestamp range
3. Read transcript for key concepts
4. Use transcript to align your objectives

**Example:**
```markdown
# Variables 12:56 – 18:16
[Full transcript of Mosh teaching variables...]

Key concepts:
- Defining variables
- Data types (int, float, string, boolean)
- Assignment operator
- Updating variables
```

---

## 🔧 Tools at Your Disposal

### **Quick Reference**

**See:** [Python Tools Reference](../Tools Available/PYTHON_TOOLS_REFERENCE.md)

**Installed packages:**
- ✅ MarkItDown (with all dependencies)
- ✅ YouTube Transcript API
- ✅ Mammoth (DOCX conversion)
- ✅ OpenPyXL (Excel processing)
- ✅ PDFMiner-Six (PDF extraction)
- ✅ Python-PPTX (PowerPoint processing)
- ✅ Pandas (data manipulation)

**Custom scripts:**
- ✅ YouTube Transcript Extractor

**What each does:**
| Tool | Purpose | Example Use |
|------|---------|-------------|
| MarkItDown | Convert documents to Markdown | DOCX templates → readable MD |
| YouTube Transcript API | Extract video transcripts | Get Mosh's exact words by timestamp |
| youtube_transcript_extractor.py | Easy transcript extraction | One command to get lesson transcript |

---

## 💡 Best Practices

### **When Creating Lessons:**

**DO:**
- ✅ Watch the Code with Mosh video segment first
- ✅ Extract transcript to verify concepts
- ✅ Test all code in Google Colab before publishing
- ✅ Use progressive difficulty (easy → medium → hard)
- ✅ Include exactly 10 vocabulary terms
- ✅ Add timestamps for student reference
- ✅ Follow naming conventions precisely

**DON'T:**
- ❌ Copy transcript verbatim (add your expertise!)
- ❌ Skip testing in Colab (different from local Python)
- ❌ Use more or fewer than 10 vocab terms
- ❌ Forget to organize files in proper folders
- ❌ Mix up lesson numbers or naming

---

### **File Naming Checklist:**

```
✅ Objectives: Lesson_XX_Topic_Name_Objectives.html
✅ Lessons:    Lesson_XX_Topic_Name.ipynb
✅ Projects:   Project_XX_Project_Name.ipynb

Example:
✅ Lesson_02_How_Python_Code_Gets_Executed_Objectives.html
✅ Lesson_02_How_Python_Code_Gets_Executed.ipynb
```

---

## 🚀 Workflow Shortcuts

### **Creating Lesson in 7 Steps:**

```bash
# 1. Find lesson in CodeWithMosh_Lessons.md
#    Note: Title, timestamp, key concepts

# 2. Extract transcript (optional)
cd "Project Documentation/Scripts"
python youtube_transcript_extractor.py _uQrJ0TkZlc START END -o temp.txt

# 3. Create objectives HTML
#    Location: Objectives/Lesson_XX_Topic_Name_Objectives.html
#    Template: LESSON_OBJECTIVES_GUIDELINES.md

# 4. Identify 10 vocabulary terms
#    From: Transcript + Mosh video + your expertise

# 5. Create Jupyter notebook
#    Location: Lessons/Lesson_XX_Topic_Name.ipynb
#    Template: Colab_Lesson_Template_PromptOnly.md

# 6. Test in Google Colab
#    Upload to Colab, run all cells, verify output

# 7. Quality check
#    - Timestamps correct?
#    - 10 vocab terms?
#    - Code works?
#    - Files named correctly?
#    - In right folders?
```

---

## 📞 Getting Help (For Future You)

### **"I forgot how to extract transcripts"**
→ See: [YouTube Transcript Tools Guide](YOUTUBE_TRANSCRIPT_TOOLS_GUIDE.md)  
→ Quick ref: [Python Tools Reference](../Tools Available/PYTHON_TOOLS_REFERENCE.md)

### **"I need to create objectives"**
→ See: [Lesson Objectives Guidelines](../LESSON_OBJECTIVES_GUIDELINES.md)  
→ Example: `Objectives/Lesson_02_How_Python_Code_Gets_Executed_Objectives.html`

### **"I need the lesson notebook template"**
→ See: [Lesson Template](../Markdown/Colab_Lesson_Template_PromptOnly.md)  
→ Example: `Lessons/Lesson_02_How_Python_Code_Gets_Executed.ipynb`

### **"What topics does Mosh cover at timestamp X?"**
→ See: [CodeWithMosh Lessons](../Markdown/CodeWithMosh_Lessons.md)  
→ Ctrl+F to search for timestamp

### **"What Python tools do I have available?"**
→ See: [Python Tools Reference](../Tools Available/PYTHON_TOOLS_REFERENCE.md)

### **"I forgot the course context"**
→ See: [Teaching Instructions](../TEACHING_INSTRUCTIONS.md)

---

## 🎓 Course-Specific Information

### **Video Source**
- **Title:** Code with Mosh - Python Programming Course for Beginners
- **Full URL:** https://www.youtube.com/watch?v=_uQrJ0TkZlc&vl=en
- **Video ID:** `_uQrJ0TkZlc`
- **Duration:** ~4 hours 58 minutes (4:58:32)
- **Language:** English (with auto-generated captions)

### **Lesson Breakdown Available**
All lessons with timestamps are documented in:
```
Project Documentation/Markdown/CodeWithMosh_Lessons.md
```

### **Critical Requirements**
- ✅ All materials must work in **Google Colab**
- ✅ HTML objectives formatted for **Canvas LMS**
- ✅ Exactly **10 vocabulary terms** per lesson
- ✅ Progressive difficulty in exercises
- ✅ Professional, college-level content

---

## 📝 Quick Commands Reference

```bash
# Navigate to project
cd "G:\My Drive\Colab Notebooks\COSC1315"

# Extract transcript
cd "Project Documentation\Scripts"
python youtube_transcript_extractor.py _uQrJ0TkZlc 6:08 8:08

# Convert DOCX to Markdown (one-liner)
python -c "from markitdown import MarkItDown; md=MarkItDown(); r=md.convert('file.docx'); open('out.md','w',encoding='utf-8').write(r.text_content)"

# Install YouTube Transcript API (if needed)
pip install youtube-transcript-api

# Check installed packages
pip list | grep -E "(markitdown|youtube)"
```

---

## 🔄 Version History

| Date | Update | By |
|------|--------|-----|
| 2025-10-20 | Created master reference guide | Sullivan |
| 2025-10-20 | Added YouTube transcript tools | Sullivan |
| 2025-10-20 | Organized project documentation structure | Sullivan |

---

## 📌 Reminders for Future You

- **ffmpeg warning is harmless** - ignore it when using MarkItDown
- **Always test in Colab** - local Python ≠ Colab environment
- **Cache transcripts** - avoid repeated API calls
- **Use consistent naming** - future you will thank past you
- **Quality > Quantity** - better to have fewer excellent lessons
- **Students learn by doing** - prioritize hands-on exercises
- **Align with video** - students will watch Code with Mosh too

---

**Remember:** You're not just creating lessons, you're building a comprehensive learning experience for your students. Take pride in the quality! 🌟

---

**Last Updated:** October 20, 2025  
**Maintained By:** Professor Sullivan  
**Next Review:** As needed when adding new tools or workflows
