# Lesson 11: Weight Converter Program

**Video Timestamp:** 1:16:16–1:20:40  
**Week:** Week 8  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

make sure to watch his tutorial one more time. In this tutorial, we're going to look at a few useful functions for working with numbers let's start by defining a variable like x and set it to 2.9. Now to round this number we can use the built in round function, so we call the round function, give it x, and then print the result. Let's run this program so, we get 3, we have another useful built in function called abs which is short for absolute, and this is the absolute function we have in math, we give it a value and it always returns the positive representation of this value, even if the value is negative. Here's an example. Let's call the abs function and give it negative 2.9 When we run this program we're gong to see 2.9 on the terminal. So let's go ahead there you go. So absolute always returns a positive number. But technically in Python we have a handful of built in functions for performing mathematical operations, if you want to write a program that involves complex mathematical calculations, you need to import the math module. A module in Python is a separate file with some reusable code. We use these modules to organize our code into different files. As a metaphor think of a super market. When you go to a super market you see different sections for fruits and vegetables, cleaning products, junk food and so on. Each section in the super market is like a module in Python. So in Python we have this math module which contains a bunch of rustable functions for performing mathematical calculations. So, let me show you how to use this module. On the top we type import, math, all in lowercase with this we can import the math module. now math is an object like a string, so we can access it's functions or more accurately it's methods using the dot operator. So if you type math. look these are all the mathematical functions available in this module. For example you can call the seal method to get the sealing of a number. So if you pass 2.9 here and then print the result we should see 3. Let me delete all this other code here. Alright, let's run this program there you go. So we get 3. Another useful method is the floor method, so let's give that a try, floor of 2. 9. What do you think we're going to get? We get 2. Now there are so many functions built in this module and we don't really have time to go through all of them. But let me show you how we can learn about them on your own. Open up your browser and search for Python 3 math module. Make sure to add the version python 3. Because the math module in python 2 is slightly different from the math module in python 3. So python 3 math module, now here you can see the documentation of this kind of module let's go let's have a look, if you scroll down, we can see the list of all the functions and their explanation. So as an exercise I encourage you to have a quick look at this documentation. See what functions are there for you in case you need them.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Use logical operators to combine conditions**
- Use `and` to check if multiple conditions are all true
- Use `or` to check if at least one condition is true
- Use `not` to reverse a boolean value

**Build complex conditional expressions**
- Combine multiple comparisons using `and`, `or`, `not`
- Understand that `and` requires all conditions to be `True`
- Recognize that `or` requires only one condition to be `True`
- Use `not` to negate boolean expressions

**Understand short-circuit evaluation**
- Explain that Python stops evaluating `and` when it finds a `False` condition
- Understand that Python stops evaluating `or` when it finds a `True` condition
- Recognize how short-circuiting improves performance

**Apply operator precedence with logical operators**
- Know that `not` has highest precedence among logical operators
- Understand that `and` is evaluated before `or`
- Use parentheses to clarify complex logical expressions

**Recognize common pitfalls**
- Don't confuse `and`/`or` with `&`/`|` (bitwise operators)
- Remember that `0`, `""`, `None`, and empty collections are "falsy" values
- Use parentheses to avoid precedence errors in complex conditions
- Ensure all parts of a logical expression are valid boolean expressions

## Key Terms

- **Logical Operator** — An operator that combines or modifies boolean values
- **`and` operator** — Returns `True` only if both operands are `True`
- **`or` operator** — Returns `True` if at least one operand is `True`
- **`not` operator** — Reverses the boolean value of its operand
- **Boolean Logic** — The system of logic using `True` and `False` values
- **Short-Circuit Evaluation** — Stopping evaluation once the result is determined
- **Truth Table** — A table showing all possible combinations of boolean inputs and their results
- **Falsy Value** — A value that is considered `False` in a boolean context (e.g., `0`, `""`, `None`)
- **Truthy Value** — A value that is considered `True` in a boolean context (most non-zero, non-empty values)
- **Operand** — A value or variable that an operator acts upon in an expression


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Interactive Weight Converter

**Description:** Create a program that converts weight between pounds and kilograms based on user input.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
```

**Expected Output:**
```
Weight: 160
(L)bs or (K)g: L
You are 72.0 kilos
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
