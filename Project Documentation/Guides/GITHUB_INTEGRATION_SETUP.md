# GitHub Integration Setup Guide

**Date:** October 30, 2025  
**Purpose:** Push COSC1315 course to GitHub and integrate with Google Colab

---

## 📋 Step-by-Step Setup

### **Step 1: Install Git (if not already installed)**

**Download Git for Windows:**
- URL: https://git-scm.com/download/win
- Install with default settings
- Restart VS Code after installation

**Verify installation:**
```powershell
git --version
```

---

### **Step 2: Create GitHub Repository**

**Option A: Via GitHub Website (Easier)**
1. Go to https://github.com
2. Log in (or create account)
3. Click **"New repository"** (green button)
4. Repository settings:
   - **Name:** `COSC1315-Python-Course`
   - **Description:** "Introduction to Computer Science - Python (Dual Credit)"
   - **Visibility:** Choose one:
     - **Public:** ✅ Free, students can view
     - **Private:** ⚠️ Need GitHub Pro or Education account
   - **Initialize:** Leave unchecked (we'll push existing code)
5. Click **"Create repository"**

**Option B: Via GitHub CLI**
```powershell
# Install GitHub CLI first: winget install GitHub.cli
gh repo create COSC1315-Python-Course --public --description "Python course for dual credit students"
```

---

### **Step 3: Initialize Local Repository**

**In VS Code Terminal (PowerShell):**

```powershell
# Navigate to your course folder
cd "g:\My Drive\Colab Notebooks\COSC1315"

# Initialize git repository
git init

# Configure your identity (first time only)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Create .gitignore file
New-Item -ItemType File -Name ".gitignore" -Force
```

**Add to .gitignore:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
.ipynb_checkpoints/

# VS Code
.vscode/

# System files
.DS_Store
Thumbs.db
desktop.ini

# Large files
*.mp4
*.zip
*.tar.gz

# Temporary files
*~
*.swp
*.bak
```

---

### **Step 4: Push to GitHub**

```powershell
# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit: COSC1315 Python course with Lessons 1-5"

# Add remote repository (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/COSC1315-Python-Course.git

# Push to GitHub
git push -u origin main
```

**If you get an error about 'master' vs 'main':**
```powershell
git branch -M main
git push -u origin main
```

---

### **Step 5: Future Updates (Your Regular Workflow)**

**After making changes locally:**

```powershell
# Check what changed
git status

# Stage changes
git add .

# Commit with descriptive message
git commit -m "Added Lesson 6: Strings"

# Push to GitHub
git push
```

---

## 🔗 Accessing from Google Colab

### **Method 1: Direct Colab Links (Recommended for Students)**

**URL Pattern:**
```
https://colab.research.google.com/github/USERNAME/COSC1315-Python-Course/blob/main/Lessons/LESSON_NAME.ipynb
```

**Examples:**
- Lesson 1: `https://colab.research.google.com/github/USERNAME/COSC1315-Python-Course/blob/main/Lessons/Lesson_01_Your_First_Python_Program.ipynb`
- Lesson 5: `https://colab.research.google.com/github/USERNAME/COSC1315-Python-Course/blob/main/Lessons/Lesson_05_Type_Conversion.ipynb`

**✅ Benefits:**
- Students click link → opens in Colab automatically
- No downloading required
- Always gets latest version from GitHub
- Works on Chromebooks

### **Method 2: Clone Entire Repo in Colab**

**Students can run this in a Colab notebook:**
```python
# Clone the repository
!git clone https://github.com/USERNAME/COSC1315-Python-Course.git

# Navigate to folder
%cd COSC1315-Python-Course/Lessons
```

### **Method 3: Mount Drive + Pull Updates**

**If students have personal copies:**
```python
from google.colab import drive
drive.mount('/content/drive')

%cd /content/drive/MyDrive/COSC1315

# Pull latest changes
!git pull
```

---

## 📚 Canvas Integration

### **In Canvas Assignments:**

**Option A: Embed Direct Link**
```html
<h2>📓 Lesson 05: Type Conversion</h2>
<p>Click the button below to open the lesson in Google Colab:</p>
<p>
  <a href="https://colab.research.google.com/github/USERNAME/COSC1315-Python-Course/blob/main/Lessons/Lesson_05_Type_Conversion.ipynb" 
     class="btn btn-primary" 
     target="_blank">
    Open Lesson 5 in Colab
  </a>
</p>
```

**Option B: Create Module with Links**
1. Canvas → Modules
2. Add External URL
3. Paste Colab GitHub URL
4. Students click → opens in new tab

---

## 🔧 Verification Files Setup

### **Challenge: Verification Files Need to be Accessible**

**Current setup:**
```python
# In notebooks, we import from:
sys.path.append('/content/drive/MyDrive/Colab Notebooks/COSC1315/Lessons/Verifications')
from lesson_05_verification import *
```

**Problem:** This requires students to have files in their Drive

### **Solution Options:**

**Option 1: Include Verification in Notebook (Simplest)**
- Embed verification code directly in notebook cells
- ❌ Makes notebooks longer
- ✅ Self-contained, no imports needed

**Option 2: GitHub Raw Files**
```python
# Download verification from GitHub
!wget https://raw.githubusercontent.com/USERNAME/COSC1315-Python-Course/main/Lessons/Verifications/lesson_05_verification.py

# Import it
from lesson_05_verification import *
```

**Option 3: Students Clone Repo Once**
```python
# First time only:
!git clone https://github.com/USERNAME/COSC1315-Python-Course.git
%cd COSC1315-Python-Course

# Then they can run notebooks with local verification files
```

**Option 4: PyPI Package (Advanced)**
- Create Python package with all verifications
- Students: `!pip install cosc1315-verifications`
- ✅ Most professional
- ⚠️ Requires package maintenance

**Recommended for Your Setup: Option 2 (GitHub Raw Files)**

---

## 📂 Recommended Repository Structure

```
COSC1315-Python-Course/
├── README.md (Course overview)
├── .gitignore
├── Lessons/
│   ├── Lesson_01_Your_First_Python_Program.ipynb
│   ├── Lesson_02_How_Python_Code_Gets_Executed.ipynb
│   ├── Lesson_03_Variables.ipynb
│   ├── Lesson_04_Receiving_Input.ipynb
│   ├── Lesson_05_Type_Conversion.ipynb
│   └── Verifications/
│       ├── lesson_01_verification.py
│       ├── lesson_03_verification.py
│       └── lesson_05_verification.py
├── Projects/
│   └── Project_01_My_Pet_Info.ipynb
├── Resources/
│   └── Video_Links.md
└── Documentation/
    └── Setup_Instructions.md
```

---

## 🎓 Student Workflow

### **Week 1: Initial Setup**
1. Instructor shares Colab link in Canvas
2. Student clicks link
3. Notebook opens in Colab (read-only)
4. Student: **File → Save a copy in Drive**
5. Student works in their copy

### **Week 5: Lesson 5**
1. Instructor pushes Lesson 5 to GitHub
2. Instructor updates Canvas link
3. Student clicks new link
4. Student saves copy and completes work

### **No Git Knowledge Required for Students!**
- They just click links
- Work in Colab
- Submit via Canvas

---

## 🔄 Your Development Workflow

### **Creating New Lesson:**
1. **Local:** Create `Lesson_06_Strings.ipynb` in VS Code
2. **Local:** Create `lesson_06_verification.py`
3. **Test:** Upload to Colab, verify it works
4. **Commit:** `git add . && git commit -m "Added Lesson 6"`
5. **Push:** `git push`
6. **Canvas:** Update assignment with new Colab link

### **Updating Existing Lesson:**
1. **Local:** Edit `Lesson_05_Type_Conversion.ipynb`
2. **Test:** Verify changes work
3. **Commit:** `git commit -am "Fixed typo in Lesson 5"`
4. **Push:** `git push`
5. **Students:** Next time they click link, they get updated version

---

## ⚠️ Important Considerations

### **GitHub File Size Limits:**
- Individual files: 100 MB max
- Repository: 1 GB recommended max
- Your notebooks are ~16 KB each ✅ No problem

### **Google Drive Sync:**
- Git repos in Google Drive can be slow
- **Better:** Keep local copy outside Drive, sync to Drive separately
- **Workflow:** 
  ```
  C:\Dev\COSC1315\  (git repo, fast)
  G:\My Drive\...   (backup copy, no git)
  ```

### **Student Privacy:**
- Public repo = anyone can see lesson content ✅ This is fine
- Students' work stays in their own Colab/Drive ✅ Private
- Verification code is visible ⚠️ Students could cheat by reading it
  - **Solution:** Obfuscate critical verification logic
  - **Reality:** Most won't bother, apathetic students remember? 😉

---

## 🚀 Quick Start Commands

**First Time Setup:**
```powershell
cd "g:\My Drive\Colab Notebooks\COSC1315"
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/COSC1315-Python-Course.git
git push -u origin main
```

**Daily Updates:**
```powershell
git add .
git commit -m "Description of changes"
git push
```

**Check Status:**
```powershell
git status           # What changed?
git log --oneline    # Commit history
git diff             # See exact changes
```

---

## 📖 Example Canvas Assignment

**Title:** Lesson 05: Type Conversion

**Description:**
```
In this lesson, you'll learn how to convert between data types in Python.

📺 Video: Watch Code with Mosh (22:40-29:28)
📓 Notebook: Click below to open in Google Colab

[Open Lesson 5 in Colab]
https://colab.research.google.com/github/USERNAME/COSC1315-Python-Course/blob/main/Lessons/Lesson_05_Type_Conversion.ipynb

Instructions:
1. Click the link above
2. File → Save a copy in Drive
3. Complete all tasks
4. Run calculate_grade() to see your score
5. Submit screenshot of your grade in Canvas

Due: [Date] 11:59 PM (48-hour grace period)
```

---

## ✅ Benefits of This Workflow

**For You:**
- ✅ Version control (never lose work)
- ✅ Easy rollback if something breaks
- ✅ Professional development workflow
- ✅ Backup outside Google Drive
- ✅ Collaborate with other instructors

**For Students:**
- ✅ One-click access (no downloads)
- ✅ Always latest version
- ✅ Works on Chromebooks
- ✅ No Git knowledge required
- ✅ Free (public repos)

**For IT/Admin:**
- ✅ No server setup needed
- ✅ Zero cost
- ✅ No network restrictions
- ✅ Standards-based (GitHub education)

---

## 🎯 Next Steps

1. **Install Git** (if not already)
2. **Create GitHub account** (if needed)
3. **Create repository** (COSC1315-Python-Course)
4. **Push existing code** (follow commands above)
5. **Test Colab link** (verify Lesson 5 opens)
6. **Update Canvas** (add Colab links to assignments)
7. **Document for students** (setup instructions)

---

**Need help with any of these steps?** Let me know which part you'd like to tackle first!

**Ready to initialize git?** I can run the commands for you once git is installed.

---

**Created:** October 30, 2025  
**Status:** Ready to implement  
**Estimated Time:** 30 minutes for full setup
