# Lesson 07: Formatted Strings & String Methods

**Video Timestamp:** 37:28–48:32  
**Week:** Week 5  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

I hope you guessed it right. In this tutorial, we're going to look at formatted strings in Python programming language. Formatted strings are particularly useful in situations where you dynamically generate some text with your variables. Let me show you. Let's say we have two variables first name and last name. So first we set this to John, and last we set this to Smith. Now it's better to call these variables first name and last name, because they're more descriptive. But here I'm using shorter names because I want you to see the entire code on display screen. So let's say with these two variables, we want to generate some text like this. Jon, in square brackets Smith is a coder. Let's say we want to print this on the terminal. How do we do this? Well, we define another variable like message, now here we add the first name, now we need to concatenate this, with a string that contains a space and a square bracket next we need to add a last name, then we need to add a string that contains the closing square brackets followed by is a coder okay? So, then, if you print message and run this program to see John Smith is a coder, right? Now, while this approach perfectly works, it's not ideal because as our text gets more complicated it becomes harder to visualize the output. So someone else reading this code, they have to visualize all the string concatenations in their head. This is where we use formatted strings, they make it easier for us to visualize the output. So, I'm going to define another variable, let's say msg short for message, and set this to a formatted string. A formatted string is one that is prefixed with an f. So f, quotes. Now in between the quotes, first we want to add the value of the first name variable, so, we add curly braces and here we type first. Next we add a space, we add our square brackets, in between the square brackets, we want to display the last name so once again we add curly braces, and type last, and finally here we type is a coder. So this is what we call the formatted string. With these curly braces, we're defining place holders or holes in our string, and when we run our program these holes will be filled with the value of our variables. So here we have two place holders or two holes in our string. One is for the value of our first name variable and the other is for the value of the last name variable. But compare this formatted string with string concatenation. With this formatted string we can easily visualize what the output looks like, right? Now let's print this other terminal to make sure we get the same exact output. So, let's print message there you go. So Jon Smith is a coder. So to define formatted strings, prefix your strings with an F and then use curly braces to dynamically insert values into your strings.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Perform basic arithmetic operations**
- Use the addition operator `+` to add numbers
- Use the subtraction operator `-` to subtract numbers
- Use the multiplication operator `*` to multiply numbers
- Use the division operator `/` to divide numbers (always returns a float)

**Use advanced arithmetic operators**
- Perform floor division using `//` to get an integer quotient
- Calculate remainders using the modulus operator `%`
- Raise numbers to powers using the exponentiation operator `**`

**Understand operator precedence**
- Recognize that exponentiation `**` has highest precedence
- Know that multiplication, division, floor division, and modulus are evaluated next
- Understand that addition and subtraction are evaluated last
- Use parentheses `()` to override default precedence

**Apply augmented assignment operators**
- Use `+=` to add and assign (e.g., `x += 5` is shorthand for `x = x + 5`)
- Use `-=`, `*=`, `/=`, `//=`, `%=`, `**=` for other operations
- Recognize that augmented operators provide a more concise syntax

**Build programs with calculations**
- Create programs that perform mathematical operations on user input
- Combine multiple operations in a single expression
- Store and display calculation results

**Recognize common pitfalls**
- Remember that `/` always returns a **float**, even for whole number results (e.g., `10 / 2` gives `5.0`)
- Use `//` for integer division if you need a whole number result
- Avoid division by zero, which causes a **ZeroDivisionError**
- Use parentheses to clarify complex expressions and control evaluation order

## Key Terms

- **Arithmetic Operator** — A symbol that performs a mathematical operation
- **Addition (`+`)** — Adds two numbers together
- **Subtraction (`-`)** — Subtracts one number from another
- **Multiplication (`*`)** — Multiplies two numbers
- **Division (`/`)** — Divides one number by another, always returning a float
- **Floor Division (`//`)** — Divides and rounds down to the nearest integer
- **Modulus (`%`)** — Returns the remainder after division
- **Exponentiation (`**`)** — Raises a number to a power (e.g., `2 ** 3` equals `8`)
- **Operator Precedence** — The order in which operations are performed in an expression
- **PEMDAS** — Mnemonic for order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
- **Augmented Assignment** — Operators like `+=`, `-=` that combine an operation with assignment
- **Expression** — A combination of values, variables, and operators that evaluates to a single value
- **ZeroDivisionError** — An exception raised when attempting to divide by zero


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: String Concatenation

**Description:** Create a message by concatenating strings with variables containing first name and last name.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder"
print(message)
```

**Expected Output:**
```
John [Smith] is a coder
```

### Task 2: Formatted Strings

**Description:** Use an f-string to create the same message more elegantly with placeholders.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
first = "John"
last = "Smith"
msg = f"{first} [{last}] is a coder"
print(msg)
```

**Expected Output:**
```
John [Smith] is a coder
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
