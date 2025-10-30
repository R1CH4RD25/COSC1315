# Testing Guide: Generic Verification in Lesson 03

**Date:** October 20, 2025  
**Notebook:** Lesson_03_Variables_WalkAlong.ipynb  
**New Features:** Try It Yourself + Bonus Challenge with generic verification

---

## What Was Added

### New Cells in Notebook:

**Cell 16:** Try It Yourself Instructions (Markdown)
- Single variable challenge
- Create favorite number variable and print it

**Cell 17:** Student Code Cell (Python)
- Students type their own code here

**Cell 18:** Verification Cell (Python)
- `verify_try_it_yourself()` - Generic verification

**Cell 19:** Bonus Challenge Instructions (Markdown)
- Three variable challenge
- Create name, age, hobby and print all

**Cell 20:** Student Code Cell (Python)
- Students type their bonus code here

**Cell 21:** Bonus Verification Cell (Python)
- `verify_multiple_variables(3)` - Checks for 3 variables

**Cell 22:** Completion Message (Markdown)
- Congratulations and next steps

---

## Testing Checklist

### Setup (Do Once):
- [ ] Open notebook in Google Colab
- [ ] Run Cell 2 (Setup cell)
- [ ] Verify you see: "✅ Verification system loaded!"
- [ ] Verify new imports include `verify_try_it_yourself` and `verify_multiple_variables`

---

## Test Case 1: Try It Yourself - Correct Usage ✅

**Goal:** Verify it accepts ANY variable name and value when used correctly

### Test 1A: Simple Variable
**In Cell 17, type:**
```python
favorite_number = 7
print(favorite_number)
```

**Run Cell 17, then Cell 18**

**Expected Output:**
```
🔍 Checking your 'Try It Yourself' code...

✅ Excellent! You're using variables correctly!
   Variables created: favorite_number
   Variables used in print: favorite_number

🎉 Great job demonstrating your understanding of variables!
```

---

### Test 1B: Different Variable Name
**In Cell 17, type:**
```python
lucky = 13
print(lucky)
```

**Run Cell 17, then Cell 18**

**Expected Output:**
```
🔍 Checking your 'Try It Yourself' code...

✅ Excellent! You're using variables correctly!
   Variables created: lucky
   Variables used in print: lucky

🎉 Great job demonstrating your understanding of variables!
```

---

### Test 1C: Different Value and Name
**In Cell 17, type:**
```python
best_digit = 42
print(best_digit)
```

**Expected:** ✅ Should pass with success message

---

## Test Case 2: Try It Yourself - Printing Literal ❌

**Goal:** Verify it catches students printing the value directly

### Test 2A: Printing Number Instead of Variable
**In Cell 17, type:**
```python
my_number = 100
print(100)  # ❌ Printing literal!
```

**Run Cell 17, then Cell 18**

**Expected Output:**
```
🔍 Checking your 'Try It Yourself' code...

Issues found:

❌ You're printing a literal value, not a variable!
   You printed: [100]
   ⚠️  Remember: Create a variable FIRST, then print the variable
   ✅ Correct: my_variable = 10; print(my_variable)
```

---

### Test 2B: Printing String Literal
**In Cell 17, type:**
```python
favorite = 7
print("7")  # ❌ Printing string literal!
```

**Expected:** ❌ Should show error about printing literal

---

## Test Case 3: Try It Yourself - No Variable Created ❌

**Goal:** Verify it catches missing variable creation

### Test 3A: Just Print, No Variable
**In Cell 17, type:**
```python
print(42)  # No variable created!
```

**Run Cell 17, then Cell 18**

**Expected Output:**
```
🔍 Checking your 'Try It Yourself' code...

Issues found:

❌ No variables found. You need to create a variable!
   Example: my_variable = 10
❌ You're printing a literal value, not a variable!
   You printed: [42]
   ⚠️  Remember: Create a variable FIRST, then print the variable
   ✅ Correct: my_variable = 10; print(my_variable)
```

---

## Test Case 4: Bonus Challenge - Correct Usage ✅

**Goal:** Verify it accepts 3+ variables correctly

### Test 4A: Three Variables
**In Cell 20, type:**
```python
name = "Alex"
age = 20
hobby = "coding"

print(name)
print(age)
print(hobby)
```

**Run Cell 20, then Cell 21**

**Expected Output:**
```
🔍 Checking that you created 3 variables...

✅ Excellent! You're using variables correctly!
   Variables created: name, age, hobby
   Variables used in print: name, age, hobby

🎉 Great job demonstrating your understanding of variables!
```

---

### Test 4B: More Than Three Variables (Should Pass)
**In Cell 20, type:**
```python
first_name = "Jordan"
last_name = "Smith"
age = 25
city = "Austin"

print(first_name)
print(last_name)
print(age)
print(city)
```

**Expected:** ✅ Should pass (has more than minimum 3)

---

## Test Case 5: Bonus Challenge - Not Enough Variables ❌

**Goal:** Verify it catches when fewer than 3 variables created

### Test 5A: Only Two Variables
**In Cell 20, type:**
```python
name = "Sam"
age = 22

print(name)
print(age)
```

**Run Cell 20, then Cell 21**

**Expected Output:**
```
🔍 Checking that you created 3 variables...

Issues found:

❌ You created 2 variable(s), but need at least 3
   Variables found: name, age
```

---

### Test 5B: One Variable
**In Cell 20, type:**
```python
name = "Pat"
print(name)
```

**Expected:** ❌ Should show error about needing 3 variables

---

## Test Case 6: Bonus Challenge - Printing Literals ❌

**Goal:** Verify it catches literal printing even with 3 variables

### Test 6A: Three Variables But Printing Literals
**In Cell 20, type:**
```python
name = "Taylor"
age = 21
city = "Houston"

print("Taylor")  # ❌ Printing literals!
print(21)
print("Houston")
```

**Run Cell 20, then Cell 21**

**Expected Output:**
```
🔍 Checking that you created 3 variables...

Issues found:

❌ You're printing a literal value, not a variable!
   You printed: ['Taylor', 21, 'Houston']
   ⚠️  Remember: Create a variable FIRST, then print the variable
   ✅ Correct: my_variable = 10; print(my_variable)
```

---

## Test Case 7: Edge Cases

### Test 7A: Variable Created But Not Used (Warning)
**In Cell 17, type:**
```python
favorite = 10
backup = 20
print(favorite)  # Only using one
```

**Expected:** 
- ✅ Should pass (has variable usage)
- 💡 Should show warning about unused 'backup'

---

### Test 7B: Multiple Print Statements (All Variables)
**In Cell 17, type:**
```python
number = 5
print("My favorite number is:")
print(number)
```

**Expected:** ✅ Should pass (variable is used in one of the prints)

---

### Test 7C: Variable in Expression
**In Cell 17, type:**
```python
base = 10
print(base * 2)
```

**Expected:** ✅ Should pass (variable used in expression)

---

### Test 7D: F-String with Variable
**In Cell 17, type:**
```python
favorite = 7
print(f"My favorite number is {favorite}")
```

**Expected:** ✅ Should pass (variable used in f-string)

---

## Common Issues and Solutions

### Issue 1: "Could not analyze your code"
**Cause:** Syntax error in student code

**Test:**
```python
favorite = 10
print(favorite  # Missing )
```

**Expected:** Warning message about invalid Python

---

### Issue 2: Import Error
**Cause:** Setup cell not run or verification file missing

**Solution:**
- Re-run Cell 2 (setup cell)
- Check that verification folder is accessible
- Verify imports include new functions

---

### Issue 3: Old Version of Verification
**Cause:** Module not reloaded

**Solution:**
- Restart Colab runtime
- Re-run Cell 2
- Should see `importlib.reload()` working

---

## Success Criteria

### All Tests Should:
- [ ] Specific verification (Tasks 1-4) still works as before
- [ ] Generic verification accepts ANY variable name
- [ ] Generic verification accepts ANY value
- [ ] Error messages are clear and helpful
- [ ] Success messages show which variables were created/used
- [ ] Catches printing literals vs variables
- [ ] Catches missing variables
- [ ] Counts variables correctly
- [ ] Gives helpful hints on failures

---

## What to Look For

### Good Signs ✅:
- Students can be creative with variable names
- Clear feedback on what they did right/wrong
- Helpful error messages with examples
- Success messages list their actual variable names

### Red Flags ❌:
- False positives (passes when it shouldn't)
- False negatives (fails when it shouldn't)
- Confusing error messages
- Crashes or Python errors

---

## Report Issues

If you find problems, note:
1. **What you typed** in the code cell
2. **What verification said** (actual output)
3. **What you expected** (should pass/fail?)
4. **Cell numbers** where issue occurred

---

## Next Steps After Testing

### If All Tests Pass:
1. ✅ System is working correctly!
2. Consider testing with actual students
3. Gather feedback on error message clarity
4. Apply pattern to other lessons

### If Tests Fail:
1. Note which specific test case failed
2. Check if it's the verification logic or test case
3. Review the AST analysis in `_analyze_code_structure()`
4. Adjust as needed

---

## Quick Test Summary

**Run these 5 tests for quick validation:**

1. **Correct Usage:**
   ```python
   lucky = 7
   print(lucky)
   ```
   → Should PASS ✅

2. **Printing Literal:**
   ```python
   lucky = 7
   print(7)
   ```
   → Should FAIL ❌

3. **No Variable:**
   ```python
   print(42)
   ```
   → Should FAIL ❌

4. **Bonus (3 vars):**
   ```python
   a = 1
   b = 2
   c = 3
   print(a, b, c)
   ```
   → Should PASS ✅

5. **Bonus (2 vars):**
   ```python
   a = 1
   b = 2
   print(a, b)
   ```
   → Should FAIL ❌ (need 3)

---

**Ready to test!** Open the notebook in Colab and work through these test cases. 🧪

---

**Maintained by:** Professor Richard Joseph Sullivan  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Institution:** Cisco College
