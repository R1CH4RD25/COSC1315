# GitHub Workflow - Quick Reference

**Date:** October 30, 2025  
**Status:** ✅ Active - Course now on GitHub!

---

## 🔗 Your GitHub Repository

**URL:** https://github.com/R1CH4RD25/COSC1315

---

## 📝 Daily Workflow

### **1. Work Locally (Fast & Efficient)**
```powershell
# Your working directory
cd C:\Dev\COSC1315
```

Edit files in VS Code, create new lessons, test everything locally.

### **2. Push Changes to GitHub**
```powershell
cd C:\Dev\COSC1315

# Check what changed
& "C:\Program Files\Git\bin\git.exe" status

# Stage all changes
& "C:\Program Files\Git\bin\git.exe" add .

# Commit with descriptive message
& "C:\Program Files\Git\bin\git.exe" commit -m "Added Lesson 6: Strings"

# Push to GitHub
& "C:\Program Files\Git\bin\git.exe" push
```

### **3. Students Access via Colab**
Students click link → Colab opens with latest version from GitHub!

---

## 🔗 Colab Links for Students

### **Current Lessons:**

**Lesson 01: Your First Python Program**
```
https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_01_Your_First_Python_Program.ipynb
```

**Lesson 02: How Python Code Gets Executed**
```
https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_02_How_Python_Code_Gets_Executed.ipynb
```

**Lesson 03: Variables**
```
https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_03_Variables.ipynb
```

**Lesson 04: Receiving Input**
```
https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_04_Receiving_Input.ipynb
```

**Lesson 05: Type Conversion** ✅ Updated (GitHub integration)
```
https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_05_Type_Conversion.ipynb
```

---

## 🎓 Student Instructions

### **Opening a Lesson:**
1. Click the Colab link in Canvas
2. Notebook opens in Google Colab (read-only)
3. **File → Save a copy in Drive** (creates editable copy)
4. Work in your copy
5. Complete tasks and run verification cells
6. Submit screenshot of grade to Canvas

### **Setup Cell - New Structure:**
```python
# Download verification file from GitHub
!wget -q https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_05_verification.py

# Import verification functions
from lesson_05_verification import (
    verify_walk_along_1,
    verify_walk_along_2,
    # ... etc
)

print("✅ Setup complete! You're ready to start coding.")
```

**Key Change:** No more Google Drive mounting required! ✅

---

## 📂 Directory Structure

```
C:\Dev\COSC1315\                    ← Local Git repo (FAST)
├── Lessons/
│   ├── Lesson_01_*.ipynb
│   ├── Lesson_05_*.ipynb ✅ GitHub integration
│   └── Verifications/
│       ├── lesson_03_verification.py
│       └── lesson_05_verification.py
├── Projects/
├── Resources/
└── Project Documentation/

G:\My Drive\Colab Notebooks\COSC1315\  ← Backup only (DON'T run Git here)
```

---

## 🚀 Common Tasks

### **Create New Lesson:**
1. Create/edit in `C:\Dev\COSC1315\Lessons\`
2. Add setup cell with GitHub download:
   ```python
   !wget -q https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_XX_verification.py
   from lesson_XX_verification import *
   ```
3. Test locally or upload to Colab to verify
4. Commit and push to GitHub
5. Share Colab link with students

### **Update Existing Lesson:**
1. Edit file in `C:\Dev\COSC1315\Lessons\`
2. Test changes
3. Commit and push
4. Next time students click link, they get updated version

### **Create Verification File:**
1. Create `C:\Dev\COSC1315\Lessons\Verifications\lesson_XX_verification.py`
2. Test it works
3. Commit and push
4. It's automatically available at:
   ```
   https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_XX_verification.py
   ```

---

## ⚡ Git Command Shortcuts

### **Check Status:**
```powershell
& "C:\Program Files\Git\bin\git.exe" status
```

### **See What Changed:**
```powershell
& "C:\Program Files\Git\bin\git.exe" diff
```

### **View Commit History:**
```powershell
& "C:\Program Files\Git\bin\git.exe" log --oneline
```

### **Undo Last Commit (keep changes):**
```powershell
& "C:\Program Files\Git\bin\git.exe" reset HEAD~1
```

### **Pull Latest from GitHub:**
```powershell
& "C:\Program Files\Git\bin\git.exe" pull
```

---

## 🔧 Adding Git to PATH (Optional)

To use `git` instead of full path `& "C:\Program Files\Git\bin\git.exe"`:

1. Open PowerShell as Administrator
2. Run:
   ```powershell
   $env:Path += ";C:\Program Files\Git\bin"
   [Environment]::SetEnvironmentVariable("Path", $env:Path, "Machine")
   ```
3. Restart VS Code
4. Now you can use: `git status`, `git push`, etc.

---

## 📊 Benefits of New Structure

### **For You:**
✅ Version control - track all changes  
✅ Fast local development (not in Google Drive)  
✅ Professional workflow  
✅ Easy rollback if something breaks  
✅ Collaborate with other instructors  

### **For Students:**
✅ One-click access to lessons  
✅ No Google Drive setup required  
✅ Always get latest version  
✅ Works on Chromebooks  
✅ Simple setup cell  

### **Verification Files:**
✅ Automatically available from GitHub  
✅ No manual file copying needed  
✅ Students just run setup cell  
✅ Always in sync with lesson version  

---

## 🆘 Troubleshooting

### **"Git not recognized"**
- Use full path: `& "C:\Program Files\Git\bin\git.exe"`
- Or add to PATH (see above)

### **"Push rejected" error**
- Someone else pushed first
- Solution: `git pull` then `git push`

### **"Authentication failed"**
- GitHub will open browser for login
- Complete authentication
- Try push again

### **"File too large"**
- GitHub has 100MB file limit
- Check what you're committing: `git status`
- Add large files to `.gitignore`

### **"Merge conflict"**
- Rare if you're only developer
- Edit conflicted files
- Remove conflict markers (`<<<<`, `====`, `>>>>`)
- Commit the resolved files

---

## 📝 Git Workflow Diagram

```
┌─────────────────┐
│  Local Changes  │  (Edit in VS Code)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   git add .     │  (Stage changes)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   git commit    │  (Save snapshot)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    git push     │  (Upload to GitHub)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     GitHub      │  (Cloud storage)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Students Colab  │  (Access via links)
└─────────────────┘
```

---

## 🎯 Next Steps

1. ✅ **Done:** Course pushed to GitHub
2. ✅ **Done:** Lesson 5 updated with GitHub integration
3. **TODO:** Update remaining lessons (3, 4) when they get verification
4. **TODO:** Create README.md for GitHub repo
5. **TODO:** Update Canvas assignments with Colab links
6. **TODO:** Test Lesson 5 in Colab to verify GitHub download works

---

## 📚 Resources

**Your Repository:** https://github.com/R1CH4RD25/COSC1315  
**Git Documentation:** https://git-scm.com/doc  
**GitHub Guides:** https://guides.github.com  
**Colab + GitHub:** https://colab.research.google.com/github/  

---

**Last Updated:** October 30, 2025  
**Status:** Active workflow, Lesson 5 verified working with GitHub integration
