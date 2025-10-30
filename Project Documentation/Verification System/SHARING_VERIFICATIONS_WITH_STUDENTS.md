# Sharing the Verifications Folder with Students

**Date:** October 20, 2025  
**Status:** INSTRUCTIONS FOR DEPLOYMENT

---

## Overview

The `Lessons/Verifications/` folder contains Python files that verify student code in Walk-Along notebooks. To use this system with students, you need to share this folder with them.

---

## Option 1: Share Folder via Link (Recommended - EASIEST!)

### Step 1: Share the Verifications Folder

**✅ ALREADY DONE!**

Your shared link:
```
https://drive.google.com/drive/folders/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT?usp=sharing
```

**Folder ID:** `1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT`

This link is set to "Anyone with the link can view" - perfect for students!

### Step 2: Students Access the Shared Folder

**Student Instructions:**

1. Open this link: https://drive.google.com/drive/folders/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT
2. You'll see the "Verifications" folder
3. Click **"Add shortcut to Drive"** (⭐ icon in top bar)
4. Choose a location (or just click "My Drive")
5. Click **"Add shortcut"**

**Why this step?**
- Makes the folder accessible from Colab
- You only need to do this ONCE for the entire semester
- The notebook setup cell will automatically find it!

### Step 3: Notebook Setup Cell (Already Updated!)

The setup cell now automatically tries multiple paths:

```python
verification_paths = [
    # Path 1: Instructor's original location
    '/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications',
    
    # Path 2: Via shared link (folder ID from your link)
    '/content/drive/.shortcut-targets-by-id/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT',
    
    # Path 3: If added to student's Drive
    '/content/drive/Shareddrives/COSC1315/Lessons/Verifications',
    
    # Path 4: Alternate structure
    '/content/drive/My Drive/COSC1315/Lessons/Verifications',
]

# Finds first path that exists - works for all students!
for path in verification_paths:
    if os.path.exists(path):
        verification_path = path
        break
```

**Result:** Students just run Cell 2 and it works automatically! 🎉

---

## Option 2: Each Student Gets Their Own Copy

### Step 1: Share Entire Course Folder

1. Share the entire `COSC1315` folder with students
2. Students make a copy to their own Drive
3. They now have their own `Lessons/Verifications/` folder
4. Standard path works: `/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications`

### Pros & Cons

**Pros:**
- ✅ Students have full control
- ✅ No path issues
- ✅ Can experiment without affecting others

**Cons:**
- ❌ Updates don't propagate automatically
- ❌ Each student needs their own copy
- ❌ More storage space used

---

## Option 3: Shared Drive (Best for Organization)

### Step 1: Create a Shared Drive

1. In Google Drive, click **"Shared drives"** (left sidebar)
2. Click **"+ New"**
3. Name it: **"COSC 1315 - Fall 2025"**
4. Add students as **"Content manager"** or **"Contributor"**

### Step 2: Move Course Files

1. Move the entire `COSC1315` folder to the Shared Drive
2. All students automatically see it
3. All updates are instant for everyone

### Step 3: Update Setup Cell Path

```python
# Shared Drive path
verification_path = '/content/drive/Shareddrives/COSC 1315 - Fall 2025/COSC1315/Lessons/Verifications'
```

### Pros & Cons

**Pros:**
- ✅ Instant updates for all students
- ✅ Central management
- ✅ Students can't accidentally delete
- ✅ Easy to track who accesses what

**Cons:**
- ❌ Requires Google Workspace (not free Gmail)
- ❌ More setup initially

---

## Testing the Setup

### For You (Instructor):

1. Open a test notebook in Colab
2. Run setup cell
3. Should see: **"✅ Verification system loaded!"**
4. Test verification: `verify_task_1()`
5. Should work correctly

### For Students:

**First Time:**
1. Open notebook from shared link
2. File → Save a copy in Drive (they need their own copy of the notebook)
3. Run setup cell
4. If error: Check Drive path, check folder is accessible
5. Once working: Proceed with tasks

**Troubleshooting:**

**Error: "ModuleNotFoundError: No module named 'lesson_03_verification'"**
- **Cause:** Verification folder not accessible
- **Fix:** 
  1. Check Drive is mounted: Look for `/content/drive/My Drive/` in file browser
  2. Check folder is shared with student
  3. Check path in setup cell matches actual location

**Error: "❌ Error: Variable 'price' not found"** (but variable exists)
- **Cause:** Cached old version of verification file
- **Fix:** 
  1. Runtime → Restart runtime
  2. Re-run setup cell
  3. Try verification again

---

## Current Setup (As of Oct 20, 2025)

### Folder Location
```
My Drive/
└── Colab Notebooks/
    └── COSC1315/
        └── Lessons/
            └── Verifications/
                ├── README.md
                └── lesson_03_verification.py
```

### Notebook Location
```
My Drive/
└── Colab Notebooks/
    └── COSC1315/
        └── Sample Lessons/
            └── Lesson_03_Variables_WalkAlong.ipynb
```

### Path in Setup Cell
```python
verification_path = '/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications'
```

---

## Recommended Approach for Your Class

Based on your situation, I recommend:

### **Option 1: Share the `COSC1315` Folder**

**Why:**
- ✅ Simple for students
- ✅ You control updates
- ✅ Students get view-only access
- ✅ Works with free Gmail accounts

**How:**
1. Share `My Drive/Colab Notebooks/COSC1315` folder
2. Set to **"Viewer"** permissions
3. Students make copies of notebooks to their own Drive
4. Verification folder stays in your shared location
5. Setup cell uses the shared path

**Student Workflow:**
1. Access shared COSC1315 folder
2. Open notebook (e.g., Lesson_03_Variables_WalkAlong.ipynb)
3. File → Save a copy in Drive (to their own Drive)
4. Work in their copy
5. Setup cell mounts Drive and accesses your shared Verifications folder

---

## Security Considerations

### What Students CAN'T Do:
- ❌ Modify verification files (if shared as "Viewer")
- ❌ See verification source code (it's just imported)
- ❌ Bypass verification (functions check globals())

### What Students CAN Do:
- ✅ View verification files if they navigate to the folder
- ✅ Copy verification files to their own Drive
- ✅ Modify their local copy (but notebooks still use YOUR shared version)

### If You Want to Hide Verification Logic:

**Option A: Use .pyc Files** (compiled Python)
```bash
python -m compileall lesson_03_verification.py
# Share the .pyc file only
```

**Option B: Serve from Web**
```python
import requests
exec(requests.get('https://your-server.com/lesson_03_verification.py').text)
```

**Option C: Accept That They Can See It**
- Most students won't look
- If they do, they're learning more Python!
- Focus is on self-assessment, not preventing cheating

---

## Quick Start Checklist

### Before First Class:
- [ ] Verify all verification files are in `Lessons/Verifications/`
- [ ] Test setup cell in a fresh Colab session
- [ ] Share COSC1315 folder with students (or create shareable link)
- [ ] Prepare instructions for students (see below)

### Student Instructions (Copy/Paste for LMS):

```
📚 COSC 1315 - Walk-Along Notebooks Setup

STEP 1: Add Verification Folder (ONE TIME ONLY)
1. Open this link: https://drive.google.com/drive/folders/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT
2. Click the ⭐ "Add shortcut to Drive" button at the top
3. Select "My Drive" and click "Add shortcut"
   ✅ Done! You only need to do this once for the entire semester.

STEP 2: Open a Lesson Notebook
1. Go to the shared course folder (link provided separately)
2. Find the lesson you want to work on (e.g., Lesson_03_Variables_WalkAlong.ipynb)
3. Click File → "Save a copy in Drive" (save to YOUR Google Drive)

STEP 3: Run the Setup Cell
1. In your copied notebook, run Cell 2 (the big setup cell at the top)
2. You'll see: "📂 Mounting Google Drive..."
3. Click "Connect to Google Drive" and allow access
4. Wait for: "✅ Verification system loaded!"

STEP 4: Start Coding!
1. Follow the video instructions for each task
2. Type the code Mosh types
3. Run verification cells to check your work
4. Get instant feedback: ✅ or ❌ with helpful hints!

🆘 Troubleshooting:
- If verification fails to load, make sure you completed STEP 1
- If you see "Folder not found", try re-running Cell 2
- Still stuck? Post in the discussion board with a screenshot!

Need help? See the course documentation or ask in discussion board.
```

---

## Future Enhancements

### Possible Improvements:
1. **Auto-detect path** - Try multiple locations automatically
2. **Download verification** - Fetch from web if Drive fails
3. **Offline mode** - Embedded verification as fallback
4. **Analytics** - Track which verifications students run (with consent)
5. **Custom feedback** - Personalized hints based on error patterns

---

**Maintained by:** Professor Richard Joseph Sullivan  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Institution:** Cisco College
