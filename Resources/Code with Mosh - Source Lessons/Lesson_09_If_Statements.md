# Lesson 09: If Statements

**Video Timestamp:** 58:16–1:06:24  
**Week:** Week 7  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

So, you have learned that in Python programming language you have 2 types of numbers, integers which are whole numbers like 10, they don't have a decimal point, and floating point numbers or floats. Which are numbers with a decimal point. Now in this tutorial you're going to look at the arithmetic operations supported in python language these are the same arithmetic operations that we have in math, we can add numbers, multiply them and so on. So let's look at a few examples, we can print, 10 plus 3, so this is the addition operator, we also have subtraction, we have multiplication, we have two kinds of division, here's one with a forward slash, let's run this program and see what we get. we get a floating point number. But we also have another division operator for getting an integer. So if we add another slash here and run this program we get an integer. We have another operator called modulis (?) which is a percent sign. And this returns the remainder of the division. So when we run this program we should get 1, there you go. And one last operator we have here is exponent which is the power. So, that is indicated with 2 asterisks and this will return 10 to the power of 3. So let's run this program we get 1000 so these are the arithmetic operators in python programming language. Now for all these operators that you learned we have an augmented assignment operator. That is very useful, let me show you. So let's say we have a variable called x we set it to 10, now we want to increment this by 3, we'll have to write code like this. X we set this to x plus 3. So Python interpreter will add 10 to 3, the result is 13, and then it gets stored into x again. So when we print x we should see 13, there you go. So this is how you can increment a number, right? Now augmented assignment operator is a way to write the same code but in a shorter form. This is how it works. We type x plus equals 3. What we have on line 3 is exactly like what we have on line 2. So this is what we call the augmented assignment operator we have augmented or enhanced the assignment operator. Now in this particular case we are incremented a number using the augmented assignment operator, but we can also subtract or multiply a number by a given value for example, let's delete what we have on line 2, we can type subtract equals 3. So here we subtracted 3 from x. When we run this program we should see 7, there you go.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Use built-in mathematical functions**
- Use `round(number, digits)` to round floating-point numbers
- Use `abs(number)` to get the absolute value of a number
- Recognize these as built-in functions available without importing

**Import and use the math module**
- Import the `math` module using `import math`
- Access math functions using dot notation (e.g., `math.ceil()`)
- Understand that modules provide additional specialized functionality

**Apply common math module functions**
- Use `math.ceil()` to round up to the nearest integer
- Use `math.floor()` to round down to the nearest integer
- Use `math.sqrt()` to calculate square roots
- Use `math.pow()` for exponentiation (alternative to `**`)
- Access `math.pi` and `math.e` for mathematical constants

**Recognize common pitfalls**
- Remember to `import math` before using math module functions
- Understand that `round()` is built-in but `ceil()` and `floor()` require the math module
- Don't forget the `math.` prefix when calling module functions
- Know that `math.sqrt()` only accepts positive numbers (negative values cause errors)

## Key Terms

- **Built-in Function** — A function that is always available in Python without importing (e.g., `round()`, `abs()`)
- **`round(number, digits)`** — Rounds a number to a specified number of decimal places
- **`abs(number)`** — Returns the absolute value (distance from zero) of a number
- **Module** — A file containing Python code (functions, classes, variables) that can be imported and reused
- **`import`** — A statement that makes a module's contents available to your program
- **`math` module** — A standard library module providing mathematical functions and constants
- **`math.ceil(x)`** — Returns the smallest integer greater than or equal to `x`
- **`math.floor(x)`** — Returns the largest integer less than or equal to `x`
- **`math.sqrt(x)`** — Returns the square root of `x`
- **`math.pi`** — The mathematical constant π (approximately 3.14159)
- **Dot Notation** — Using a period `.` to access attributes or methods of an object or module


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Simple If Statement

**Description:** Create a program that checks if it's a hot day and prints a message.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")
```

**Expected Output:**
```
It's a hot day
Drink plenty of water
Enjoy your day
```

### Task 2: If-Elif-Else Statement

**Description:** Create a program with multiple conditions for hot, cold, or lovely day.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")
```

**Expected Output:**
```
It's a lovely day
Enjoy your day
```

### Task 3: Down Payment Calculator

**Description:** Calculate down payment based on credit status (10% for good credit, 20% otherwise).

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
```

**Expected Output:**
```
Down payment: $100000.0
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
