# Lesson 10: Logical Operators & Comparison Operators

**Video Timestamp:** 1:06:24–1:16:16  
**Week:** Week 7  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

Now let me ask you a question, I'm going to clear all this code here to define x and set it to 10 plus 3 times 2. What do you think is the result of this expression? this is a very basic math question that unfortunately a lot of people fail to answer. The answer is 16. Because in math we have this concept called operator precedence which means the order of operations. So the multiplication operator has a higher precendence which means it's applied first which means 3 x 2 is executed first, the result is 6 and then its added to 10, that's why x showed up as 16 after we run this code, let's verify that. So, print x run the program, x is 16. So this is what we call operator precedence, it's just a basic math concept. It's not about python programming language. So all the other programming languages behave the same way, so here's the order, first we have the exponentiation which is the power, like 2 to the power of 3, then we have multiplication or division and finally we have addition or subtraction. This is the order of operations. Let me show you another example. Here I'm going to add the exponentiation operator, so, 2 to the power of 2. Once again, what do you think is the result of this expression? Pause the video and think about it for a few seconds. The answer is 22. Because the exponentiation operator takes precedence, so first 2 to the power of 2 is executed, the result is 4, then 4 is multiplied by 3, that is 12, and finally 12 is added to 10. So x should be 22. So let's run this program and verify this. So I'm going to delete these lines here. Run the program, there you go. X is 22. Now let me bring back these rules here. We can also use parenthesis to change the order of operations so if we have parenthesis we always takes priority. In this case we can add parenthesis around 10 + 3, so this piece of 3 will be executed first, the result is 13, then the exponentiation operator will be executed, so 2 to the power of 2 is 4, and finally 4 is multiplied by 13. Now here is a little exercise for you. I'm going to set x to parenthesis 2 + 3 x 10 minus 3. What is the result of this? Pause the video and think about it for a few seconds. So you learned that parenthesis always overrides the order, so this piece of code is executed first. The result of these 5. Then, between the multiplication and subtraction, you know that multiplication takes precedence. So next, 5 will be multiplied by 10, the result is 50 and finally we have subtraction. So 50 minus 3 will be 47. Let's verify this, print x, run the program there you go, I hope you guessed it right. So this is all bout operator precedence, it's a very important topic and I see it quite often in Python tests. So if you're preparing for a Python test



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand conditional execution**
- Explain that `if` statements allow programs to make decisions
- Describe how conditions determine which code blocks execute
- Recognize that code under an `if` runs only when the condition is `True`

**Write basic if statements**
- Use the syntax `if condition:` to create conditional statements
- Indent code blocks that should execute when the condition is true
- Understand that Python uses indentation to define code blocks

**Use comparison operators in conditions**
- Use `==` to check if two values are equal
- Use `!=` to check if two values are not equal
- Use `>`, `<`, `>=`, `<=` for numerical comparisons
- Understand that comparison operators return `True` or `False`

**Build programs with conditional logic**
- Create programs that respond differently based on user input
- Validate user input using `if` statements
- Display messages or perform actions only when conditions are met

**Recognize common pitfalls**
- Remember to use `==` for comparison, not `=` (which is assignment)
- Always include the colon `:` at the end of the `if` line
- Indent code blocks consistently (typically 4 spaces)
- Understand that forgetting indentation causes **IndentationError**

## Key Terms

- **Conditional Statement** — Code that executes only when a specified condition is true
- **`if` Statement** — A control structure that executes code conditionally based on a boolean expression
- **Condition** — A boolean expression that evaluates to `True` or `False`
- **Code Block** — A group of statements that are executed together, defined by indentation in Python
- **Indentation** — Whitespace at the beginning of a line that defines code block hierarchy
- **Comparison Operator** — An operator that compares values and returns a boolean result
- **`==` (Equal to)** — Checks if two values are the same
- **`!=` (Not equal to)** — Checks if two values are different
- **`>` (Greater than)** — Checks if the left value is larger than the right
- **`<` (Less than)** — Checks if the left value is smaller than the right
- **`>=` (Greater than or equal to)** — Checks if the left value is larger than or equal to the right
- **`<=` (Less than or equal to)** — Checks if the left value is smaller than or equal to the right
- **Boolean Expression** — An expression that evaluates to `True` or `False`
- **IndentationError** — An exception raised when indentation is incorrect or inconsistent


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Logical AND Operator

**Description:** Check if an applicant has both high income AND good credit for loan eligibility.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
```

**Expected Output:**
```
Eligible for loan
```

### Task 2: Logical OR Operator

**Description:** Check if an applicant has high income OR good credit for loan eligibility.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")
```

**Expected Output:**
```
Eligible for loan
```

### Task 3: Logical NOT Operator

**Description:** Check if applicant has good credit AND does NOT have a criminal record.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
```

**Expected Output:**
```
Eligible for loan
```

### Task 4: Comparison Operators

**Description:** Use comparison operators to check temperature and display appropriate messages.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
```

**Expected Output:**
```
It's a hot day
```

### Task 5: Name Validation

**Description:** Validate user name length is between 3 and 50 characters.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
name = "John Smith"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")
```

**Expected Output:**
```
Name looks good
```

---

## Teaching Notes

### Key Concepts
- [To be added by instructor]

### Learning Objectives
- [To be added by instructor]

### Common Student Mistakes
- [To be added by instructor]

### Practice Exercises
- [To be added by instructor]

---

*This transcript is sourced from Code with Mosh's "Python for Beginners" video tutorial.*  
*Video link: https://www.youtube.com/watch?v=_uQrJ0TkZlc*
