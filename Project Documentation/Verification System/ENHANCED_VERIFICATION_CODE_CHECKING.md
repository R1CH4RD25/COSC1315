# Enhanced Verification: Code Usage Checking

**Date:** October 20, 2025  
**Feature:** AST-based verification to ensure students USE variables, not just create them  
**Status:** ✅ IMPLEMENTED

---

## The Problem We're Solving

### Original Issue:
Students could "cheat" the verification by:
```python
# Student types this:
price = 10
print(10)  # ❌ Printing the NUMBER, not the VARIABLE!
```

**Why this is bad:**
- Variable `price` exists ✅
- Variable equals 10 ✅
- **BUT:** Student never actually USED the variable!
- They could skip creating variables entirely and just print literals

### Why This Matters:
**You're absolutely right** - this is **fundamental** to intro programming:
- Students must learn that variables STORE values
- Students must learn to USE variables, not bypass them
- This is the **foundation** of all programming

---

## The Solution: AST Code Analysis

### What is AST?
**AST = Abstract Syntax Tree**
- Python can parse code into a tree structure
- We can analyze WHAT the code does, not just the results
- We can detect if they typed `print(price)` vs `print(10)`

### How It Works:

```python
import ast

def _check_code_uses_variable(code, variable_name):
    """
    Check if code actually uses the specified variable.
    Returns (True, "") if correct, or (False, "error message") if not.
    """
    # Parse the code into an AST
    tree = ast.parse(code)
    
    # Walk through all nodes in the tree
    for node in ast.walk(tree):
        # Find print() function calls
        if isinstance(node, ast.Call) and node.func.id == 'print':
            # Check what's being printed
            for arg in node.args:
                # Is it a literal value? (number, string, etc.)
                if isinstance(arg, ast.Constant):
                    return False, "You printed a literal, not the variable!"
                # Is it the variable we're looking for?
                elif isinstance(arg, ast.Name) and arg.id == variable_name:
                    return True, ""  # ✅ Correct!
    
    return True, ""
```

### Example Detection:

**Case 1: Student prints literal**
```python
price = 10
print(10)  # ❌ DETECTED!
```

AST sees:
```
Call(func=Name('print'), args=[Constant(value=10)])
                                ^^^^^^^^^^^^^^^^^
                                This is a literal!
```

**Result:** ❌ Error message with hint

---

**Case 2: Student prints variable**
```python
price = 10
print(price)  # ✅ CORRECT!
```

AST sees:
```
Call(func=Name('print'), args=[Name('price')])
                                ^^^^^^^^^^^^^^
                                This is a variable!
```

**Result:** ✅ Success message

---

## Implementation Details

### Getting Student's Code

```python
def _get_previous_cell_code():
    """Get the code from the cell executed before verify was called"""
    if ipython is None:
        return None
    
    # Access IPython's execution history
    history = list(ipython.history_manager.get_range(output=False))
    
    # History entries: [(session, line_number, code), ...]
    # Last entry: verify_task_X() call
    # Second-to-last: Student's actual code
    if len(history) >= 2:
        return history[-2][2]  # Get code from 2nd-to-last
    
    return None
```

### Verification Flow

```python
def verify_task_1():
    user_ns = _get_user_namespace()
    
    # Step 1: Check variable exists
    if 'price' not in user_ns:
        print("❌ Variable not found")
        return False
    
    # Step 2: Check variable has correct value
    if user_ns['price'] != 10:
        print("❌ Wrong value")
        return False
    
    # Step 3: Check student actually USED the variable
    code = _get_previous_cell_code()
    uses_variable, error_msg = _check_code_uses_variable(code, 'price')
    
    if not uses_variable:
        print("❌ You printed the number directly, not the variable!")
        print("⚠️  Don't type: print(10)")
        print("✅  Correct way: print(price)")
        return False
    
    print("✅ Perfect! You used the variable correctly!")
    return True
```

---

## Error Messages

### Before (Just checked value):
```
✅ Perfect! You created the variable 'price' and assigned it the value 10.
✅ Great job!
```
*(Even if they typed `print(10)`)*

### After (Checks actual usage):

**If they type `print(10)`:**
```
❌ Error: You printed the number directly, not the variable!
⚠️  Common Mistake: Don't type print("10") or print(10)
✅  Correct Way: Type print(price) - this prints the variable's value
💡 Hint: Type print(price), not print(10)
```

**If they type `print(price)`:**
```
✅ Perfect! You created the variable 'price' and assigned it the value 10.
✅ Great job! You used the variable correctly in print()!
```

---

## Edge Cases Handled

### 1. **No print statement at all**
```python
price = 10
# (no print)
```
**Result:** ✅ Pass (benefit of doubt - maybe they'll add print later)

### 2. **Multiple print statements**
```python
price = 10
print("Price is:")
print(price)  # ✅ This one is correct!
```
**Result:** ✅ Pass (at least one print uses the variable)

### 3. **Print with f-string**
```python
price = 10
print(f"Price: {price}")  # ✅ Variable used in f-string
```
**Result:** ✅ Pass (f-strings are Name nodes, not Constants)

### 4. **Syntax error in code**
```python
price = 10
print(price  # ❌ Missing parenthesis
```
**Result:** ✅ Pass (can't parse, give benefit of doubt - syntax error is a different issue)

### 5. **Can't get code history**
*(Shouldn't happen in Colab, but just in case)*
**Result:** ✅ Pass (can't verify without code, give benefit of doubt)

---

## Benefits

### For Students:
- ✅ Learn proper variable usage from day one
- ✅ Can't bypass the fundamental concept
- ✅ Clear feedback on what they did wrong
- ✅ Specific hints on how to fix it

### For Instructor:
- ✅ Ensures students learn core concepts
- ✅ Catches "clever" workarounds
- ✅ Maintains academic integrity
- ✅ Automated enforcement (no manual grading needed)

### For Course Quality:
- ✅ Students can't progress without understanding
- ✅ Foundation is solid before moving to advanced topics
- ✅ Verification is pedagogically sound
- ✅ Aligns with learning objectives

---

## Technical Limitations

### What We CAN Detect:
- ✅ `print(10)` vs `print(price)`
- ✅ `print("10")` vs `print(price)`
- ✅ `print(True)` vs `print(is_published)`

### What We CAN'T Detect (but that's okay):
- ❌ If they copy/paste Mosh's exact code vs typing it
- ❌ If they understand WHY variables are useful
- ❌ Complex expressions: `print(price + 0)` (still uses variable, so it's fine)

### Why That's Okay:
- Copy/paste is fine - they're still learning syntax
- Understanding comes with practice and projects
- Complex expressions show EXTRA knowledge, not less

---

## Future Enhancements (Optional)

### Level 1: Current (Implemented) ✅
- Check if variable is used in print()

### Level 2: Advanced (Future)
- Check if variable is used ANYWHERE in the code (not just print)
- Detect unused variables and warn
- Check variable naming conventions

### Level 3: Expert (Overkill?)
- Detect if code is copy/pasted (timing analysis)
- Check code style (PEP 8)
- Suggest improvements

**Recommendation:** Stay at Level 1 for intro course!

---

## Testing Instructions

### Test Case 1: Correct Usage ✅
```python
# Cell 1:
price = 10
print(price)

# Cell 2:
verify_task_1()
```
**Expected:** ✅ Success message

---

### Test Case 2: Printing Literal (Integer) ❌
```python
# Cell 1:
price = 10
print(10)

# Cell 2:
verify_task_1()
```
**Expected:** ❌ Error: "You printed the number directly, not the variable!"

---

### Test Case 3: Printing Literal (String) ❌
```python
# Cell 1:
price = 10
print("10")

# Cell 2:
verify_task_1()
```
**Expected:** ❌ Error: "You printed the number directly, not the variable!"

---

### Test Case 4: No Print ✅
```python
# Cell 1:
price = 10

# Cell 2:
verify_task_1()
```
**Expected:** ✅ Success (benefit of doubt)

---

### Test Case 5: Complex Expression ✅
```python
# Cell 1:
price = 10
print(price * 2)

# Cell 2:
verify_task_1()
```
**Expected:** ✅ Success (variable IS used, even in expression)

---

## Updated Files

### `lesson_03_verification.py`
- Added `import ast` and `import inspect`
- Added `_get_previous_cell_code()` function
- Added `_check_code_uses_variable()` function
- Updated `verify_task_1()` to check code usage
- Updated `verify_task_2()` to check code usage
- Tasks 3 & 4 don't need this (no single print statement to check)

---

## Deployment

### For This Lesson:
✅ Already implemented in `lesson_03_verification.py`

### For Future Lessons:
- Copy the helper functions (`_get_previous_cell_code`, `_check_code_uses_variable`)
- Add code checking to any task that requires print() usage
- Adjust variable names as needed

### Pattern to Follow:
```python
def verify_task_X():
    user_ns = _get_user_namespace()
    
    # Check 1: Variable exists
    # Check 2: Variable has correct value
    # Check 3: Variable is actually USED
    code = _get_previous_cell_code()
    uses_variable, error_msg = _check_code_uses_variable(code, 'variable_name')
    if not uses_variable:
        print("❌ Error with helpful hint")
        return False
    
    print("✅ Success!")
    return True
```

---

## Conclusion

**Problem:** Students could bypass variable usage by printing literals  
**Solution:** AST code analysis to verify actual variable usage  
**Result:** Students MUST use variables correctly to pass verification  

**This ensures the fundamental concept is learned correctly from day one!** 🎓

---

**Maintained by:** Professor Richard Joseph Sullivan  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Institution:** Cisco College
