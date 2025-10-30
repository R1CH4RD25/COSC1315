# Lesson 02: How Python Code Gets Executed

**Video Timestamp:** 8:08–11:20  
**Week:** Week 2  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this Python tutorial, we're gong to take this program to the next level and make it more interesting. So I'm going to show you how to draw a dog hair. Now as part of this tutorial you will learn how Python code gets executed and you will also learn about a few programming terms. So press enter, and on line 2 write another print statement, so print, open and close parenthesis, add a quotation, now here you want to draw a dog. So, add an o, that is the head of our dog, followed by 4 hyphens. So this is the body. alright, now one more time another print statement with quotations, now we need to draw the legs. So add a space. Follow it by 4 vertical bars. So, like this, so here's a little imaginary dot. Now let's run this program and see what we get. So on the top right corner you should see this play button, click that, there you go, so we have our name and right below that we have our imaginary dog. Now what you need to understand here, is that our python code gets executed line by line from the top. So earlier I told you about Python interpreter that is the program that knows how to translate or interpret our Python code into instructions that a computer can understand. So when we run this program by clicking this program here, python interpreter starts executing or running our program line by line from the top. So first it executes line 1, then, moves onto line 2, and so on. So this is how python programs get executed. Now let me show you something cool. Let's add another print statement, with quotations now in between the quotations, add a star or an asterisk, like this. Now after the quotation and before the parenthesis, add a space, once again, add an asterisk, space, 10. What is going on here? Well, anywhere we have quotations like here or here we're defining a string, a string is a programming term which means a series of characters so here we have a string, we also have a string on line 3, as well as line 2 and line 1. Now here, we're multiplying the string by number 10. So this is the multiplication operator, just like the multiplication operator we have in math. So with this piece of code we can draw 10 asterisks on the terminal, let me show you. So let's run this program one more time, there you go. So we have 10 asterisks. Now what we have here, this piece of code here, is called an expression. An expression is a piece of code that produces a value. So when Python interpreter tries to execute line 4, first it will evaluate the code that we put in between parenthesis, so we could evaluate our expressions Our expression will produce 10 asterisks and then those asterisks will be printed on the terminal. Now as an exercise you can use these print statements to draw another shape, you can draw a heart, a ball, whatever you like.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand how Python executes code**
- Explain that Python reads and executes code **line by line from top to bottom**
- Describe the role of the **Python interpreter** in translating code into instructions the computer can understand
- Recognize that each line is processed sequentially, in the exact order written

**Build multi-line output using print statements**
- Use multiple `print()` statements to create output across several lines
- Understand that each `print()` call produces a new line of output automatically
- Control the visual appearance of output by ordering `print()` statements correctly

**Create ASCII art and text-based drawings**
- Use text characters (like `o`, `-`, `|`) to draw simple shapes and images
- Combine multiple `print()` statements to build complete ASCII art designs
- Design letters, initials, or simple drawings using 10 or more lines of text output
- Apply spacing and alignment within strings to control visual layout

**Use string repetition with the multiplication operator**
- Multiply a string by a number to repeat it (e.g., `"*" * 10` produces `"**********"`)
- Recognize that `"text" * number` creates multiple copies of the text
- Understand that this is a Python-specific feature for string manipulation

**Understand expressions and evaluation**
- Define an **expression** as a piece of code that produces a value
- Recognize that `"*" * 10` is an expression that evaluates to a repeated string
- Explain that Python evaluates expressions before executing the containing statement

**Trace program execution flow**
- Follow the step-by-step execution of a Python program from first line to last
- Predict the output of a multi-line program by reading code top to bottom
- Understand that changing the order of `print()` statements changes the output order

**Recognize common pitfalls**
- Remember that **missing closing quotes** cause syntax errors
- Remember that **missing closing parentheses** prevent code from running
- Avoid mixing quote types incorrectly (e.g., `print("text')` with mismatched quotes)
- Use proper quote escaping or alternating quotes when strings contain quotes

## Key Terms

- **Python Interpreter** — The program that reads Python code line by line and translates it into instructions the computer can execute
- **Execute** — To run or carry out a program or command; Python executes code from top to bottom
- **Line by Line** — The sequential process where Python reads and runs each line of code in order
- **Sequential Execution** — The order in which statements are processed; code runs from first line to last
- **Multi-line Output** — Text output that spans multiple lines, created using multiple `print()` statements
- **ASCII Art** — Pictures or designs created using text characters arranged to form images
- **Expression** — A piece of code that produces a value when evaluated (e.g., `"*" * 10`)
- **String Multiplication** — Repeating a string multiple times using the `*` operator (e.g., `"hi" * 3` yields `"hihihi"`)
- **Operator** — A symbol that performs an operation on values; `*` is the multiplication operator
- **Program Flow** — The order and path in which a program's instructions are executed


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Draw ASCII Art with Your Initial

**Description:** Use multiple print() statements with string repetition to draw a letter or shape using text characters.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
print("*" * 10)
print("*")
print("*")
print("*")
print("*" * 10)
```

**Expected Output:**
```
**********
*
*
*
**********
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
