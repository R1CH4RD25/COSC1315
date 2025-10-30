# Lesson Verification System

## Purpose

This folder contains verification functions for Walk-Along coding exercises in Google Colab notebooks. The verification system provides automated feedback to students as they complete coding tasks.

## Architecture

### How It Works

1. **Student opens a Walk-Along notebook** (e.g., `Lesson_03_Variables_WalkAlong.ipynb`)
2. **Cell 2 runs the setup code:**
   - Mounts Google Drive
   - Adds this `Verifications/` folder to Python path
   - Imports lesson-specific verification functions
3. **Student completes a task** in a code cell
4. **Student runs verification cell** (e.g., `verify_task_1()`)
5. **Verification function checks their code** and provides instant feedback

### Folder Structure

```
COSC1315/
├── Lessons/
│   ├── Verifications/               ← THIS FOLDER
│   │   ├── README.md               (this file)
│   │   ├── lesson_03_verification.py
│   │   ├── lesson_04_verification.py
│   │   └── ... (one per lesson)
│   ├── Lesson_03_Variables.ipynb
│   ├── Lesson_04_Receiving_Input.ipynb
│   └── ...
└── Sample Lessons/
    └── Lesson_03_Variables_WalkAlong.ipynb
```

## Benefits

### ✅ For Students
- **Clean notebooks** - No intimidating verification code visible
- **Instant feedback** - Know immediately if code is correct
- **Helpful hints** - Error messages guide learning
- **Type checking** - Learn difference between int, float, str, bool

### ✅ For Instructors
- **Centralized updates** - Fix verification once, applies everywhere
- **Reusable code** - One verification file per lesson
- **Version control** - Track changes to verification logic
- **Protected logic** - Students can't easily modify verification

### ✅ For Course Management
- **Scalable** - Easy to add new lessons
- **Maintainable** - Separate concerns (notebook content vs verification)
- **Consistent** - Same verification pattern across all lessons

## File Naming Convention

Each verification file follows this pattern:

```
lesson_XX_verification.py
```

Where:
- `XX` = Two-digit lesson number (01, 02, 03, etc.)
- File name matches the lesson's topic (e.g., `lesson_03_verification.py` for Variables)

## Verification Function Pattern

Each verification file contains functions named:

```python
verify_task_1()
verify_task_2()
verify_task_3()
# ... etc.
```

Each function:
1. **Checks** if required variables/code exist in `globals()`
2. **Validates** values and types
3. **Prints** feedback with emojis (✅/❌) and hints (💡)
4. **Returns** `True` (success) or `False` (needs work)

## Example: lesson_03_verification.py

```python
def verify_task_1():
    """Verify Task 1: Store and Display a Price"""
    if 'price' not in globals():
        print("❌ Error: Variable 'price' not found.")
        print("💡 Hint: Create a variable named 'price' and assign it the value 10")
        return False
    
    price_value = globals()['price']
    if price_value != 10:
        print(f"❌ Error: Variable 'price' has value {price_value}, but should be 10")
        return False
    
    print("✅ Perfect! You created the variable 'price' and assigned it the value 10.")
    print("✅ Great job!")
    return True
```

## Setup Code (in Notebooks)

Every Walk-Along notebook includes this setup code in Cell 2:

```python
# ========================================
# SETUP CELL - RUN THIS FIRST!
# ========================================

from google.colab import drive
import sys

# Mount Google Drive
print("📂 Mounting Google Drive...")
drive.mount('/content/drive', force_remount=False)

# Add the verification folder to Python path
verification_path = '/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications'
if verification_path not in sys.path:
    sys.path.append(verification_path)

# Import verification functions
try:
    from lesson_03_verification import verify_task_1, verify_task_2, verify_task_3, verify_task_4
    print("✅ Verification system loaded!")
    print("📝 You're ready to start the Walk-Along tasks.")
except ImportError as e:
    print("❌ Error loading verification system.")
    print(f"Details: {e}")
```

## Important Technical Details

### Why `globals()` instead of `dir()`?

In Jupyter/Colab, student code runs in the **global namespace**. When verification functions check variables, they must use `globals()` to access the global scope:

```python
# ❌ WRONG - only checks function's local scope
if 'price' not in dir():

# ✅ CORRECT - checks global namespace where student variables live
if 'price' not in globals():
```

### Drive Mount Path

The path to this folder is:
```
/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications
```

This assumes:
- Student's Google Drive is mounted at `/content/drive`
- Course files are in `My Drive/Colab Notebooks/COSC1315/`
- Standard Google Drive folder structure

## Creating New Verification Files

### Step 1: Analyze the Lesson

Look at the lesson markdown (e.g., `Lesson_04_Receiving_Input.md`) and identify:
- How many Walk-Along tasks?
- What variables/concepts should be verified?
- What are common student mistakes?

### Step 2: Create Verification File

```bash
# Copy template
cp lesson_03_verification.py lesson_04_verification.py

# Edit to match new lesson's tasks
```

### Step 3: Write Verification Functions

For each task, create a function that:
1. Checks variable existence: `if 'var' not in globals()`
2. Validates values: `if globals()['var'] != expected_value`
3. Checks types: `if not isinstance(globals()['var'], expected_type)`
4. Provides helpful error messages

### Step 4: Test

1. Create a test notebook
2. Run setup cell
3. Try correct code → Should see ✅
4. Try incorrect code → Should see ❌ with helpful hints
5. Try missing variables → Should see ❌ with hints

### Step 5: Update Notebook

Add the import statement to the notebook's setup cell:

```python
from lesson_04_verification import verify_task_1, verify_task_2, ...
```

## Lessons Using This System

| Lesson | Verification File | Status | Tasks |
|--------|------------------|--------|-------|
| Lesson 03: Variables | `lesson_03_verification.py` | ✅ Complete | 4 |
| Lesson 04: Receiving Input | `lesson_04_verification.py` | 🚧 TODO | TBD |
| Lesson 05: Type Conversion | `lesson_05_verification.py` | 🚧 TODO | TBD |
| ... | ... | ... | ... |

## Troubleshooting

### "ImportError: No module named 'lesson_XX_verification'"

**Cause:** Verification file doesn't exist or Drive not mounted

**Fix:**
1. Check file exists in `Lessons/Verifications/`
2. Verify Drive is mounted (should see "Mounted at /content/drive")
3. Check path in setup cell matches folder location

### "Variable 'price' not found" but student typed it correctly

**Cause:** Using `dir()` instead of `globals()`

**Fix:** Update verification file to use `globals()` instead of `dir()`

### Changes to verification file not appearing

**Cause:** Python cached the old module

**Fix:** Restart Colab runtime (Runtime → Restart runtime) and re-run setup cell

## Version History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2025-10-20 | 1.0.0 | Initial verification system with Drive mounting | Richard Joseph Sullivan |
| 2025-10-20 | 1.0.0 | Created lesson_03_verification.py (Variables) | Richard Joseph Sullivan |

---

**Maintained by:** Professor Richard Joseph Sullivan  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Institution:** Cisco College
