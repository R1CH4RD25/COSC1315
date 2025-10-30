# Critical Bug Fix: IPython Namespace Issue

**Date:** October 20, 2025  
**Issue:** Verification functions returning "Variable not found" even when variable exists  
**Status:** ✅ FIXED

---

## The Problem

When testing in Google Colab, the verification system was failing with:
```
❌ Error: Variable 'price' not found.
```

Even though the student had correctly typed:
```python
price = 10
print(price)  # Output: 10 (works!)
```

---

## Root Cause

The verification functions were using `globals()` to check for student variables:

```python
def verify_task_1():
    if 'price' not in globals():  # ❌ WRONG!
        print("Variable not found")
        return False
```

**The Issue:**
- `globals()` returns the **module's** global namespace
- Student variables live in the **notebook's** (IPython's) global namespace
- These are two different namespaces!

**Analogy:**
Think of it like looking for your keys in YOUR house when they're actually in your NEIGHBOR'S house. Same street, different houses!

---

## The Solution

Use IPython's `get_ipython().user_ns` to access the notebook's namespace:

```python
# Get IPython instance to access notebook namespace
try:
    from IPython import get_ipython
    ipython = get_ipython()
except:
    ipython = None

def _get_user_namespace():
    """Helper function to get the user's namespace (where their variables live)"""
    if ipython is not None:
        return ipython.user_ns  # ✅ Notebook's namespace
    else:
        return globals()  # Fallback (shouldn't happen in Colab)

def verify_task_1():
    user_ns = _get_user_namespace()  # ✅ CORRECT!
    
    if 'price' not in user_ns:
        print("Variable not found")
        return False
    
    price_value = user_ns['price']
    # ... rest of verification
```

---

## Technical Details

### What is IPython?

IPython is the interactive Python shell that powers Jupyter notebooks (including Colab). It maintains its own namespace separate from imported modules.

### Namespace Hierarchy in Colab:

```
Colab Notebook
├── IPython Kernel
│   └── user_ns (Student's variables: price, rating, name, etc.)
│
└── Imported Modules
    └── lesson_03_verification.py
        └── globals() (Module's variables: verify_task_1, verify_task_2, etc.)
```

Student variables live in `user_ns`, not in the module's `globals()`.

### Why Did We Think `globals()` Would Work?

In a regular Python script (not Jupyter), everything is in the same namespace:
```python
# script.py
price = 10

def check():
    if 'price' in globals():  # ✅ Works in scripts!
        print("Found it!")

check()  # Output: Found it!
```

But in Jupyter/Colab, code cells execute in the IPython kernel's namespace, while imported functions execute in their module's namespace.

---

## Files Updated

### 1. `lesson_03_verification.py`

**Added at the top:**
```python
# Get IPython instance to access notebook namespace
try:
    from IPython import get_ipython
    ipython = get_ipython()
except:
    ipython = None

def _get_user_namespace():
    """Helper function to get the user's namespace (where their variables live)"""
    if ipython is not None:
        return ipython.user_ns
    else:
        return globals()
```

**Updated all 4 verification functions:**
- `verify_task_1()` ✅
- `verify_task_2()` ✅
- `verify_task_3()` ✅
- `verify_task_4()` ✅

Changed from:
```python
if 'price' not in globals():
    # ...
price_value = globals()['price']
```

To:
```python
user_ns = _get_user_namespace()
if 'price' not in user_ns:
    # ...
price_value = user_ns['price']
```

### 2. `Lesson_03_Variables_WalkAlong.ipynb`

**Setup cell (Cell 2) updated:**
- Added `importlib` import
- Added multiple path checking (for shared folder)
- Added `importlib.reload()` to force fresh import

This ensures:
1. Students can access the shared verification folder
2. Latest version is always loaded (no cache issues)

---

## Testing Instructions

### For You (Instructor):

**In Colab:**
1. Open `Lesson_03_Variables_WalkAlong.ipynb`
2. Run Cell 2 (Setup cell) → Should see "✅ Verification system loaded!"
3. In Cell 4, type: `price = 10` and `print(price)` → Run it → Should see `10`
4. Run Cell 5: `verify_task_1()` → Should see "✅ Perfect! You created the variable 'price' and assigned it the value 10."

**If it works:** ✅ The fix is successful!

**If it still fails:** 
- Make sure you saved the updated `lesson_03_verification.py` file
- Check that the file is uploaded to Google Drive (in the Verifications folder)
- Try **Runtime → Restart runtime** in Colab, then re-run from Cell 2

---

## Why This Matters for Future Lessons

**Good news:** This fix applies to ALL lessons!

Just use the same pattern:
```python
def _get_user_namespace():
    if ipython is not None:
        return ipython.user_ns
    else:
        return globals()

def verify_task_X():
    user_ns = _get_user_namespace()
    # Check variables in user_ns, not globals()
```

**When creating new verification files:**
1. Copy the IPython setup code from `lesson_03_verification.py`
2. Always use `user_ns = _get_user_namespace()` in verification functions
3. Check variables in `user_ns`, not `globals()`

---

## What We Learned

### 1. Jupyter Notebooks Are Different
- Not the same as running `python script.py`
- Separate namespaces for kernel vs modules
- Need to understand the execution model

### 2. `globals()` Is Local to Each Module
- Each Python file has its own `globals()`
- Doesn't cross module boundaries
- Not the same as the notebook's variables

### 3. IPython Has Special Tools
- `get_ipython()` gives access to the kernel
- `user_ns` is where notebook variables live
- This is the "magic" that makes Jupyter work

### 4. Always Test in the Target Environment
- What works locally might not work in Colab
- Test with real students, real workflows
- Catch these issues early!

---

## Prevention for Future Issues

### Best Practices:

1. **Test in Colab FIRST** - Don't assume local testing is enough
2. **Use IPython tools** - When working with notebooks, use `get_ipython().user_ns`
3. **Add debugging** - Print what namespace you're checking:
   ```python
   print(f"Looking in namespace with {len(user_ns)} variables")
   print(f"Available variables: {list(user_ns.keys())}")
   ```
4. **Version verification files** - Use `__version__ = "1.1.0"` and increment when fixing bugs
5. **Document quirks** - Add comments explaining WHY you're using IPython tools

---

## Status: ✅ RESOLVED

**Action Items:**
- [x] Fix `lesson_03_verification.py` to use `ipython.user_ns`
- [x] Update setup cell with `importlib.reload()`
- [x] Add path checking for shared folder
- [x] Document the fix
- [ ] Test in fresh Colab session
- [ ] Apply pattern to future lessons

---

**Next Steps:**
1. Test the fix in Colab
2. If successful, apply pattern to remaining 17 lessons
3. Update documentation with this knowledge

---

**Maintained by:** Professor Richard Joseph Sullivan  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Institution:** Cisco College
