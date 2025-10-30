# Verification Function Quick Reference

**Version:** 2.0  
**Date:** October 20, 2025

---

## Two Types of Verification

### 1. **Specific Verification** (Walk-Along Tasks)
**When to use:** Student follows Mosh exactly, we know the variable names and values

**Example:**
```python
# Task: Create variable 'price' = 10 and print it
verify_task_1()  # Checks exact name 'price' with value 10
```

---

### 2. **Generic Verification** (Try It Yourself)
**When to use:** Student creates their own code, we don't know variable names/values

**Example:**
```python
# Task: Create a variable with your favorite color and print it
verify_try_it_yourself()  # Checks pattern: variable created and used
```

---

## Available Functions

### Specific Verification Functions

#### `verify_task_1()`
- Checks: `price = 10`, printed using variable
- Use: Lesson 03, Task 1

#### `verify_task_2()`
- Checks: `price = 20` (updated), printed using variable
- Use: Lesson 03, Task 2

#### `verify_task_3()`
- Checks: `price`, `rating`, `name`, `is_published` with correct types
- Use: Lesson 03, Task 3

#### `verify_task_4()`
- Checks: `name`, `age`, `is_new` for patient system
- Use: Lesson 03, Task 4

---

### Generic Verification Functions

#### `verify_try_it_yourself()`
**Checks:**
- ✅ At least 1 variable created
- ✅ Has print() statement
- ✅ Print uses a variable (not a literal)

**Example Usage:**
```python
# Student creates ANY variable and prints it
favorite = 42
print(favorite)

# Verification:
verify_try_it_yourself()  # ✅ Pass
```

**Catches Mistakes:**
```python
# Student prints literal:
favorite = 42
print(42)  # ❌ Printing literal, not variable!

# Verification:
verify_try_it_yourself()  # ❌ Fail with helpful error
```

---

#### `verify_multiple_variables(count)`
**Checks:**
- ✅ At least `count` variables created
- ✅ Has print() statement
- ✅ Print uses variables (not literals)

**Example Usage:**
```python
# Task: Create 3 variables and print them
name = "Alice"
age = 25
city = "Austin"
print(name, age, city)

# Verification:
verify_multiple_variables(3)  # ✅ Pass
```

---

#### `verify_generic_variable_usage(min_variables, require_print, require_variable_in_print)`
**Most flexible - customize for any exercise**

**Parameters:**
- `min_variables` (int): Minimum variables to create (default: 1)
- `require_print` (bool): Must have print() (default: True)
- `require_variable_in_print` (bool): Print must use variable (default: True)

**Example Usage:**

```python
# Basic: 1 variable, must print it
verify_generic_variable_usage(min_variables=1)

# Advanced: 3 variables, must print them
verify_generic_variable_usage(min_variables=3)

# Relaxed: Variables okay, literals in print okay
verify_generic_variable_usage(
    min_variables=1,
    require_variable_in_print=False
)

# Just check variable creation (no print required)
verify_generic_variable_usage(
    min_variables=2,
    require_print=False
)
```

---

## Error Messages

### Error 1: No Variables Created
```
❌ No variables found. You need to create a variable!
   Example: my_variable = 10
```

**Fix:** Create a variable with assignment operator `=`

---

### Error 2: Not Enough Variables
```
❌ You created 1 variable(s), but need at least 3
   Variables found: name
```

**Fix:** Create more variables to meet the requirement

---

### Error 3: Printing Literal Instead of Variable
```
❌ You're printing a literal value, not a variable!
   You printed: [42]
   ⚠️  Remember: Create a variable FIRST, then print the variable
   ✅ Correct: my_variable = 10; print(my_variable)
```

**Fix:** Print the variable name, not the value directly

---

### Error 4: No Print Statement
```
❌ No print() statement found. You need to display your variable!
   Example: print(my_variable)
```

**Fix:** Add `print()` to display your variable

---

### Warning: Unused Variables
```
💡 Note: You created backup but didn't use them in print()
   That's okay for now, but remember: variables are meant to be used!

✅ Excellent! You're using variables correctly!
```

**Note:** This is just a warning, not an error. The verification still passes.

---

## When to Use Each Type

### Use Specific Verification When:
- ✅ Student following video tutorial
- ✅ Learning exact syntax/concepts
- ✅ Need to verify specific values
- ✅ "Walk-Along with Mosh" exercises

**Example:**
> "Watch Mosh create a variable called 'price' with value 10, then type the same code."

---

### Use Generic Verification When:
- ✅ "Try It Yourself" exercises
- ✅ Student creativity encouraged
- ✅ Testing understanding, not memorization
- ✅ Don't care about exact names/values

**Example:**
> "Create a variable to store your favorite movie and print it."

---

## Pattern Detection

### What Generic Verification Detects:

**Variable Creation:**
```python
x = 10              # ✅ Detected
name = "Alice"      # ✅ Detected
total = 5 + 3       # ✅ Detected
```

**Print Statements:**
```python
print(x)            # ✅ Detected
print(x, y)         # ✅ Detected
print(f"{x}")       # ✅ Detected
```

**Variable Usage in Print:**
```python
print(my_var)       # ✅ Using variable
print(my_var * 2)   # ✅ Using variable in expression
print(f"{x}")       # ✅ Using variable in f-string
```

**Literal in Print (BAD!):**
```python
print(10)           # ❌ Printing literal
print("hello")      # ❌ Printing literal
```

---

## Complete Examples

### Example 1: Basic Try It Yourself

**Markdown Instructions:**
```markdown
## Try It Yourself!

Create a variable to store your age and print it.

Use any variable name you want!
```

**Student Code:**
```python
my_age = 25
print(my_age)
```

**Verification:**
```python
verify_try_it_yourself()
```

**Output:**
```
✅ Excellent! You're using variables correctly!
   Variables created: my_age
   Variables used in print: my_age

🎉 Great job demonstrating your understanding of variables!
```

---

### Example 2: Multiple Variables

**Markdown Instructions:**
```markdown
## Challenge!

Create 3 variables:
1. Your name
2. Your favorite number
3. Your city

Then print all three!
```

**Student Code:**
```python
student_name = "Jordan"
lucky_number = 7
hometown = "Dallas"

print(student_name)
print(lucky_number)
print(hometown)
```

**Verification:**
```python
verify_multiple_variables(3)
```

**Output:**
```
✅ Excellent! You're using variables correctly!
   Variables created: student_name, lucky_number, hometown
   Variables used in print: student_name, lucky_number, hometown

🎉 Great job demonstrating your understanding of variables!
```

---

### Example 3: Common Mistake - Printing Literal

**Student Code (WRONG):**
```python
favorite_color = "blue"
print("blue")  # ❌ Printing the string, not the variable!
```

**Verification:**
```python
verify_try_it_yourself()
```

**Output:**
```
Issues found:

❌ You're printing a literal value, not a variable!
   You printed: ['blue']
   ⚠️  Remember: Create a variable FIRST, then print the variable
   ✅ Correct: my_variable = 10; print(my_variable)
```

---

### Example 4: Custom Requirements

**Markdown Instructions:**
```markdown
## Advanced Exercise!

Create 5 different variables with 5 different data types.

Just create them, no need to print yet!
```

**Student Code:**
```python
number = 42
decimal = 3.14
text = "Hello"
flag = True
nothing = None
```

**Verification:**
```python
verify_generic_variable_usage(
    min_variables=5,
    require_print=False  # Don't need to print
)
```

**Output:**
```
✅ Excellent! You're using variables correctly!
   Variables created: number, decimal, text, flag, nothing

🎉 Great job demonstrating your understanding of variables!
```

---

## Troubleshooting

### Issue: "Could not analyze your code"

**Causes:**
- Syntax error in code
- Empty code cell
- Code cell wasn't executed

**Solution:**
- Check for syntax errors (missing parentheses, quotes, etc.)
- Make sure you ran the code cell before verification cell
- Fix syntax and try again

---

### Issue: False positive (says I didn't use variable but I did)

**Possible Causes:**
- Used variable in complex way verification doesn't detect
- F-string or formatting issue

**Solution:**
- Try simpler print: `print(my_var)` instead of complex formatting
- Report to instructor if it's a legitimate use

---

### Issue: Verification passes but code doesn't work

**Explanation:**
- Verification checks patterns, not runtime behavior
- Code might have logic errors verification doesn't catch

**Solution:**
- Verification is for learning, not perfect debugging
- Test your code yourself to make sure it works as expected

---

## Best Practices

### For Students:

1. **Read the instructions carefully**
   - Know if it's a specific task or "try it yourself"
   - Understand what's being verified

2. **Use meaningful variable names**
   - `favorite_color` better than `x`
   - Helps you understand your own code

3. **Test before verifying**
   - Run your code first
   - Make sure it does what you want
   - Then verify

4. **Read error messages**
   - They tell you exactly what's wrong
   - Include examples of correct usage

---

### For Instructors:

1. **Be clear about requirements**
   - Tell students if it's specific or creative
   - Explain what verification will check

2. **Choose the right verification type**
   - Specific for walk-alongs
   - Generic for try-it-yourself

3. **Provide examples**
   - Show both correct and incorrect code
   - Explain what verification is looking for

4. **Adjust parameters as needed**
   - `min_variables` for complexity
   - `require_print` for display requirements
   - `require_variable_in_print` for strictness

---

## Summary

| Verification Type | Use Case | Variable Names | Values | Flexibility |
|-------------------|----------|----------------|--------|-------------|
| `verify_task_X()` | Walk-Along | ✅ Specific | ✅ Specific | ❌ Low |
| `verify_try_it_yourself()` | Try It Yourself | ❌ Any | ❌ Any | ✅ High |
| `verify_multiple_variables(n)` | Multiple Variables | ❌ Any | ❌ Any | ✅ High |
| `verify_generic_variable_usage()` | Custom | ❌ Any | ❌ Any | ✅✅ Very High |

---

**Quick Decision Tree:**

```
Do you know the exact variable names and values?
├─ YES → Use verify_task_X() (specific verification)
└─ NO  → Do you need multiple variables?
          ├─ YES → Use verify_multiple_variables(count)
          └─ NO  → Use verify_try_it_yourself()
```

---

**Maintained by:** Professor Richard Joseph Sullivan  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Institution:** Cisco College
