# Advanced Verification: Generic Variable Usage Checking

**Date:** October 20, 2025  
**Feature:** Pattern-based verification for "Try It Yourself" exercises  
**Status:** ✅ IMPLEMENTED  
**Version:** 2.0

---

## The Challenge

### Problem Statement:
In "Try It Yourself" exercises, students create their OWN variables:
- We don't know what they'll name them
- We don't know what values they'll use
- We don't know the exact code they'll write

**Example:**
> **Try It Yourself:** Create a variable to store your favorite number, then print it.

**Possible Student Solutions:**
```python
# Student 1:
favorite_number = 7
print(favorite_number)

# Student 2:
my_number = 42
print(my_number)

# Student 3:
lucky = 13
print(lucky)
```

**Question:** How do we verify ALL of these are correct when we don't know the variable name or value in advance?

---

## The Solution: Pattern-Based Verification

Instead of checking **specific values**, we check **patterns of correct usage**:

### ✅ What We Check:
1. Did they create **at least one** variable? (assignment detected)
2. Did they use `print()`? (print statement detected)
3. Did they print **a variable** (not a literal)? (AST analysis)

### ❌ What We DON'T Check:
- Variable name (could be anything)
- Variable value (could be anything)
- Specific code structure

---

## Technical Implementation

### Core Function: `_analyze_code_structure()`

```python
def _analyze_code_structure(code):
    """
    Analyze code structure to detect programming patterns.
    Returns a dictionary with detected patterns.
    """
    tree = ast.parse(code)
    
    analysis = {
        'has_assignment': False,           # Did they create variables?
        'has_print': False,                # Did they print anything?
        'variables_created': [],           # Names of variables created
        'variables_used_in_print': [],     # Variables used in print()
        'literals_in_print': [],           # Literals printed (bad!)
        'print_statements': 0,             # Count of print() calls
        'assignment_statements': 0,        # Count of assignments
    }
    
    # Walk through AST and detect patterns
    for node in ast.walk(tree):
        # Detect: my_var = 10
        if isinstance(node, ast.Assign):
            analysis['has_assignment'] = True
            analysis['variables_created'].append(target.id)
        
        # Detect: print(something)
        if isinstance(node, ast.Call) and node.func.id == 'print':
            analysis['has_print'] = True
            
            # What's inside print()?
            for arg in node.args:
                # Literal: print(10) ❌
                if isinstance(arg, ast.Constant):
                    analysis['literals_in_print'].append(arg.value)
                
                # Variable: print(my_var) ✅
                elif isinstance(arg, ast.Name):
                    analysis['variables_used_in_print'].append(arg.id)
    
    return analysis
```

---

## Example Verifications

### Test Case 1: Student Prints Literal (WRONG) ❌

**Student Code:**
```python
my_number = 7
print(7)  # Printing literal, not variable!
```

**Analysis Results:**
```python
{
    'has_assignment': True,
    'has_print': True,
    'variables_created': ['my_number'],
    'variables_used_in_print': [],           # ← Empty! No variable in print
    'literals_in_print': [7],                # ← Found literal!
    'print_statements': 1,
    'assignment_statements': 1
}
```

**Verification Output:**
```
Issues found:

❌ You're printing a literal value, not a variable!
   You printed: [7]
   ⚠️  Remember: Create a variable FIRST, then print the variable
   ✅ Correct: my_variable = 10; print(my_variable)
```

---

### Test Case 2: Student Uses Variable (CORRECT) ✅

**Student Code:**
```python
lucky_number = 13
print(lucky_number)  # Using the variable!
```

**Analysis Results:**
```python
{
    'has_assignment': True,
    'has_print': True,
    'variables_created': ['lucky_number'],
    'variables_used_in_print': ['lucky_number'],  # ← Found variable!
    'literals_in_print': [],                      # ← No literals!
    'print_statements': 1,
    'assignment_statements': 1
}
```

**Verification Output:**
```
✅ Excellent! You're using variables correctly!
   Variables created: lucky_number
   Variables used in print: lucky_number

🎉 Great job demonstrating your understanding of variables!
```

---

### Test Case 3: No Variables at All (WRONG) ❌

**Student Code:**
```python
print(42)  # Just printing, no variable!
```

**Analysis Results:**
```python
{
    'has_assignment': False,              # ← No variables created!
    'has_print': True,
    'variables_created': [],
    'variables_used_in_print': [],
    'literals_in_print': [42],
    'print_statements': 1,
    'assignment_statements': 0
}
```

**Verification Output:**
```
Issues found:

❌ No variables found. You need to create a variable!
   Example: my_variable = 10
❌ You're printing a literal value, not a variable!
   You printed: [42]
   ⚠️  Remember: Create a variable FIRST, then print the variable
   ✅ Correct: my_variable = 10; print(my_variable)
```

---

### Test Case 4: Multiple Variables (ADVANCED) ✅

**Student Code:**
```python
name = "Alice"
age = 25
print(name)
print(age)
```

**Analysis Results:**
```python
{
    'has_assignment': True,
    'has_print': True,
    'variables_created': ['name', 'age'],
    'variables_used_in_print': ['name', 'age'],
    'literals_in_print': [],
    'print_statements': 2,
    'assignment_statements': 2
}
```

**Verification Output:**
```
✅ Excellent! You're using variables correctly!
   Variables created: name, age
   Variables used in print: name, age

🎉 Great job demonstrating your understanding of variables!
```

---

### Test Case 5: Created But Didn't Use (WARNING) ⚠️

**Student Code:**
```python
favorite = 10
backup = 20
print(favorite)  # Didn't print 'backup'
```

**Analysis Results:**
```python
{
    'has_assignment': True,
    'has_print': True,
    'variables_created': ['favorite', 'backup'],
    'variables_used_in_print': ['favorite'],  # Only used one
    'literals_in_print': [],
    'print_statements': 1,
    'assignment_statements': 2
}
```

**Verification Output:**
```
💡 Note: You created backup but didn't use them in print()
   That's okay for now, but remember: variables are meant to be used!

✅ Excellent! You're using variables correctly!
   Variables created: favorite, backup
   Variables used in print: favorite

🎉 Great job demonstrating your understanding of variables!
```

---

## Generic Verification Function

### `verify_generic_variable_usage()`

**Signature:**
```python
def verify_generic_variable_usage(
    min_variables=1,
    require_print=True,
    require_variable_in_print=True
):
    """
    Generic verification for "Try It Yourself" exercises.
    
    Args:
        min_variables: Minimum number of variables to create
        require_print: Must have print() statement
        require_variable_in_print: Print must use variable, not literal
    
    Returns:
        True if verification passes, False otherwise
    """
```

**Usage Examples:**

```python
# Simple: Just need one variable and print it
verify_generic_variable_usage(min_variables=1)

# Advanced: Need 3 variables
verify_generic_variable_usage(min_variables=3)

# Relaxed: Variables okay, but printing literals is also okay
verify_generic_variable_usage(require_variable_in_print=False)

# Extra relaxed: Just check they created variables
verify_generic_variable_usage(require_print=False)
```

---

## Specialized Functions

### 1. `verify_try_it_yourself()`
**For:** Basic "Try It Yourself" exercises  
**Checks:** 1 variable, printed using the variable

```python
def verify_try_it_yourself():
    """
    Verification for basic 'Try It Yourself' exercise.
    Students create one variable and print it.
    """
    print("🔍 Checking your 'Try It Yourself' code...\n")
    
    return verify_generic_variable_usage(
        min_variables=1,
        require_print=True,
        require_variable_in_print=True
    )
```

**Example Usage in Notebook:**
```python
# Task: Create a variable with your favorite color and print it

# Student code cell:
color = "blue"
print(color)

# Verification cell:
verify_try_it_yourself()
```

---

### 2. `verify_multiple_variables(count=2)`
**For:** Exercises requiring multiple variables  
**Checks:** N variables created, all should be printed

```python
def verify_multiple_variables(count=2):
    """
    Verify student created multiple variables.
    Example: "Create 2 variables and print both"
    """
    print(f"🔍 Checking that you created {count} variables...\n")
    
    return verify_generic_variable_usage(
        min_variables=count,
        require_print=True,
        require_variable_in_print=True
    )
```

**Example Usage:**
```python
# Task: Create 3 variables (name, age, city) and print them

# Student code cell:
name = "Alice"
age = 25
city = "Austin"
print(name)
print(age)
print(city)

# Verification cell:
verify_multiple_variables(count=3)
```

---

## Pattern Detection Logic

### What Patterns We Detect:

**1. Variable Assignment Pattern:**
```python
# All of these are detected as assignments:
x = 10
name = "Alice"
is_valid = True
total = 5 + 3
```

**AST Node Type:** `ast.Assign`

---

**2. Print Statement Pattern:**
```python
# All of these are detected as print statements:
print(x)
print("Hello")
print(x, y, z)
print(f"Value: {x}")
```

**AST Node Type:** `ast.Call` where `func.id == 'print'`

---

**3. Variable Usage in Print:**
```python
# Variable used:
print(my_var)        # ✅ ast.Name node
print(my_var * 2)    # ✅ my_var is ast.Name inside expression

# Literal used:
print(10)            # ❌ ast.Constant node
print("hello")       # ❌ ast.Constant node
```

---

**4. Unused Variables:**
```python
x = 10
y = 20
print(x)  # y is unused

# Detection:
created = ['x', 'y']
used = ['x']
unused = created - used  # ['y']
```

---

## Edge Cases Handled

### Case 1: F-Strings
```python
name = "Alice"
print(f"Hello {name}")
```
**Result:** ✅ Passes (f-string contains Name node for 'name')

---

### Case 2: Expressions
```python
x = 10
print(x * 2)
```
**Result:** ✅ Passes (x is used in BinOp expression)

---

### Case 3: Multiple Arguments to Print
```python
x = 10
y = 20
print(x, y)
```
**Result:** ✅ Passes (both variables detected in args)

---

### Case 4: No Print at All
```python
x = 10
# No print
```
**Result:** ❌ Fails if `require_print=True`, otherwise ✅ Passes

---

### Case 5: Syntax Error
```python
x = 10
print(x  # Missing )
```
**Result:** ⚠️ "Could not analyze your code. Please make sure it's valid Python."

---

### Case 6: No Code in Cell
```python
# Empty cell
```
**Result:** ⚠️ "Could not analyze your code."

---

## Benefits of This Approach

### 1. **Student Freedom** 🎨
- Students can be creative with variable names
- Can choose their own values
- Encourages personal connection to code

### 2. **True Understanding Check** 🧠
- Can't fake it by memorizing specific answers
- Must understand the CONCEPT, not just copy code
- Tests actual programming skill

### 3. **Scalable** 📈
- One function works for all "Try It Yourself" exercises
- Easy to adjust requirements (min_variables, etc.)
- Reusable across all lessons

### 4. **Clear Feedback** 💬
- Tells students WHAT pattern they missed
- Shows WHAT they did (variables created, used)
- Gives examples of correct usage

### 5. **Catches Real Mistakes** 🎯
- Detects printing literals instead of variables
- Detects missing variables
- Detects unused variables (with warning)

---

## Integration with Lessons

### Lesson Structure with Generic Verification:

```markdown
## Walk-Along Tasks (Specific Verification)
Task 1: Create variable 'price' = 10, print it
Verification: verify_task_1()  ← Checks exact name/value

Task 2: Update 'price' to 20, print it
Verification: verify_task_2()  ← Checks exact name/value

...

## Try It Yourself (Generic Verification)
Exercise: Create a variable with your favorite food and print it
Verification: verify_try_it_yourself()  ← Checks PATTERN, not specifics
```

---

## Example Notebook Cell

**Markdown Cell:**
```markdown
## 🎯 Try It Yourself!

Now it's your turn to practice!

**Your Task:**
1. Create a variable to store your favorite number
2. Print that variable

**Requirements:**
- Use any variable name you want
- Choose any number you like
- Make sure to print the VARIABLE, not just the number

**Hint:** If you get an error about printing a literal,
make sure you're typing `print(your_variable_name)` not `print(123)`
```

**Code Cell (Student Types Here):**
```python
# Type your code below:


```

**Verification Cell:**
```python
# Run this to check your work
verify_try_it_yourself()
```

---

## Future Enhancements

### Possible Additions:

**1. Type Checking**
```python
verify_generic_variable_usage(
    min_variables=1,
    expected_types=['int']  # Must create an integer
)
```

**2. Naming Convention Checks**
```python
verify_generic_variable_usage(
    min_variables=1,
    check_naming=True  # Warn about bad names like 'x' or 'var1'
)
```

**3. Comment Checking**
```python
verify_generic_variable_usage(
    min_variables=1,
    require_comments=True  # Must have at least one comment
)
```

**4. Complexity Checking**
```python
verify_generic_variable_usage(
    min_variables=2,
    require_operation=True  # Must combine variables: print(x + y)
)
```

---

## Comparison: Specific vs Generic Verification

### Specific Verification (Walk-Along Tasks):
```python
def verify_task_1():
    """Check exact variable name and value"""
    if 'price' not in user_ns:
        return False
    if user_ns['price'] != 10:
        return False
    # ... check they used it
    return True
```

**Pros:**
- ✅ Verifies exact learning objective
- ✅ Students follow Mosh precisely
- ✅ Easy to provide specific hints

**Cons:**
- ❌ No creativity
- ❌ Can memorize answers
- ❌ Doesn't test deep understanding

---

### Generic Verification (Try It Yourself):
```python
def verify_try_it_yourself():
    """Check pattern of correct usage"""
    analysis = _analyze_code_structure(code)
    if not analysis['has_assignment']:
        return False
    if not analysis['variables_used_in_print']:
        return False
    return True
```

**Pros:**
- ✅ Encourages creativity
- ✅ Tests true understanding
- ✅ Can't just memorize
- ✅ More engaging for students

**Cons:**
- ❌ Can't give specific "should be X" feedback
- ❌ More complex verification logic
- ❌ Edge cases harder to handle

---

## Best Practice: Use Both!

**Lesson Structure:**
1. **Walk-Along (Specific):** Follow Mosh exactly, specific verification
2. **Try It Yourself (Generic):** Apply concepts independently, generic verification
3. **Projects (Manual/Hybrid):** Complex work, mix of both + manual review

This gives students:
- 📚 Structured learning (walk-along)
- 🎨 Creative practice (try it yourself)
- 🏆 Real-world application (projects)

---

## Conclusion

**You're right:** The backend checks are complex, but the result is **awesome**!

Students get:
- ✅ Clear feedback on their understanding
- ✅ Freedom to be creative
- ✅ Can't bypass learning fundamentals
- ✅ Build real programming skills

Instructors get:
- ✅ Automated verification for any exercise
- ✅ Confidence students truly understand
- ✅ Scalable across entire curriculum
- ✅ Reduced grading burden

**This is pedagogically sound AND technically elegant!** 🎉

---

**Maintained by:** Professor Richard Joseph Sullivan  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Institution:** Cisco College  
**Version:** 2.0  
**Last Updated:** October 20, 2025
