# Lesson 08: Arithmetic Operations, Operator Precedence & Math Functions

**Video Timestamp:** 48:32–58:16  
**Week:** Week 6  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this Python tutorial, I'm going to show you some really cool things you can do with Python strings. So let's start by defining a variable, course and we set that to Python for beginners. Now to calculate the number of characters in this string, you can use a built in function called len. So len we give it this course variable, and then, we can print the result. Let's run this program, so as you can see we have 20 characters in this string, this is particularly useful when you receive input from the user. For example you have noticed that when you fill out a form online, each input field often has a limit. For example, you might have 50 characters for your name, so using this len function we can enforce a limit on the number of characters in an input field. If the user types in more characters than we allow, we can display an error, now, this, len function is another function built into Python, it's a general purpose function, so it's not limited to counting the number of characters in a string, in the future when we look at lists, I want to show you that we can use this function to count the number of items in a list. So it's a general purpose function. Now we also have functions specifically for strings for example we have functions for converting all these characters to upper case or lower case. To access these functions we use the dot operator. let me show you. So first we type course, then dot look these are all the functions that are specific to strings. Now in more accurate terms, you refer to these function as methods, this is a term in object oriented programming that we want to look at in the future, but for now, what I want you to take away, is that when a function belongs to something else, or is specific to some kind of object, we refer to that function as a method. For example, here we have this function, upper, for converting the string into upper case, now more accurately because this function is specific to a string, we refer to this as a method. In contrast len and print are general purpose functions, they don't belong to strings or numbers or other kinds of objects. So this is the difference between functions and methods. Now let's take look at this upper method. So, let's print the results and we run our program, there you go, you get all these characters displayed in uppercase. Now note this method does not change or modify our original string, in fact it creates a new string and returns it. So, if we print our course variable right after we call the upper method, we can see that our course variable still has it's original form, so let's run this program one more time, there you go. Look, here is our original course variable, it's not modified. Now similar to the upper method we have another method for converting a string into lower case. So let me show you. Print, course.lower. Now, let's run the program, so on the second line you can see, all characters are in lower case. Now there are times that you want to find a character or a sequence of characters in a string. In those situations you can use the find method. So let me delete these few lines. Call course. find here we pass a character, let's say p, and this will return the index of the first occurrence of that character, let me show you. So let's print the result we get 0, because the index of the first capital p in the string is 0. As another example, if we pass a lower case o here, let's see what we get, we get 4 because the index of this o here is 4. Now note that the find method is case sensitive, so it's sensitive to lower case and and upper case characters. As an example if you pass an upper case here and run this program, we get negative 1 because we don't have an upper case o anywhere in this string, okay? We can also pass a sequence of characters, for example, we can pass beginners with a capital B let's run this program, we get 11 because beginners starts with index 11, now we also have method for replacing a character or a sequence of characters and that is called replace. So let's change find to replace let's say we want to replace beginners with absolute beginners, so we add a comma to pass a second value to this function, or more accurately this method. We add a string, here I'm going to pass absolute beginners. Okay, now let's run this program, so, we get python for absolute beginners. Again, this method like the find method is case sensitive so if you pass beginners all in lowercase, this method is not going to find this exact word in our string, so it's not going to place it with absolute beginners. Let's take a look. So I'm going to run the program One more time, look, we still get python for beginners. We can also replace a single character, for example we can replace capital p with let's say capital j. Now when we run this program we get jython for beginners. So these are the find and replace methods and one last things I want to show you in this tutorial. There are times that you want to check the existence of a character or sequence of characters in your string. In those situations you use the in operator, so let's say you want to know if this string contains the word python. We can write an expression like this. String python space in space course. So we're checking to see if python is in course variable. And this is an expression that produces a boolean value, and I get true or false, so we refer to this expression as a boolean expression, now if we print this on the terminal, we should get true, and by the way I'm going to delete the second line, we don't need it anymore, so run the program we get true, but if I change this capitol p to a lower case p and run the program we get false because we don't have is exact sequence of characters in our strings. Now note that the difference between the in operator and the find method is that our find method returns the index of character or sequence of characters but the in operator produces a boolean value. Do we have this or not? So that's the difference. Now let's recap all the cool things you learned to do with strings in this tutorial. We can use the len function to count the number of characters in a string, this is the general purpose function built into python, we also have specific functions for strings which we refer to as methods, these include upper for converting a string into uppercase you also have lower and title methods, you learn about the find method which returns the index of a character or sequence of characters, we have the replace method for replacing characters and words in a string and finally you learned about the in operator. So some characters in a string.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand the order of operations in Python**
- Explain that Python follows standard mathematical precedence rules
- Recognize that exponentiation `**` is evaluated first
- Know that multiplication, division, floor division, and modulus have equal precedence
- Understand that addition and subtraction are evaluated last

**Control evaluation order with parentheses**
- Use `()` to explicitly group operations and override default precedence
- Understand that expressions in parentheses are always evaluated first
- Nest parentheses to create complex expressions with clear evaluation order

**Predict expression results**
- Evaluate expressions mentally by applying precedence rules
- Understand that `2 + 3 * 4` equals `14`, not `20`
- Recognize that `(2 + 3) * 4` equals `20` due to parentheses

**Write clear and readable expressions**
- Use parentheses to make complex expressions easier to understand
- Avoid relying solely on precedence rules in complicated expressions
- Write code that is obvious in intent even if parentheses are technically redundant

**Recognize common pitfalls**
- Don't assume left-to-right evaluation; precedence rules apply
- Use parentheses when in doubt about evaluation order
- Avoid writing overly complex expressions in a single line
- Test expressions to verify they produce expected results

## Key Terms

- **Operator Precedence** — The rules determining the order in which operators are evaluated
- **Order of Operations** — The sequence in which mathematical operations are performed
- **Parentheses** — `()` used to group expressions and control evaluation order
- **Evaluation** — The process of computing the value of an expression
- **Grouping** — Using parentheses to explicitly define the order of operations
- **Binary Operator** — An operator that works with two operands (e.g., `+`, `-`, `*`, `/`)
- **Unary Operator** — An operator that works with one operand (e.g., `-x` for negation)
- **Integer Division** — Division that produces a whole number result (using `//` operator)
- **Floating-Point Division** — Division that produces a decimal result (using `/` operator)
- **Remainder** — The value left over after division; obtained using the modulus operator `%`


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Basic Arithmetic Operations

**Description:** Demonstrate addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
```

**Expected Output:**
```
13
7
30
3.3333333333333335
3
1
1000
```

### Task 2: Augmented Assignment Operators

**Description:** Use augmented assignment operators to increment and decrement variables.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
x = 10
x += 3
print(x)
x -= 3
print(x)
```

**Expected Output:**
```
13
10
```

### Task 3: Operator Precedence

**Description:** Demonstrate operator precedence with exponentiation, multiplication, and addition.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
x = 10 + 3 * 2 ** 2
print(x)
```

**Expected Output:**
```
22
```

### Task 4: Using Math Functions

**Description:** Import the math module and use ceil, floor, and other math functions.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
import math

print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.9))
print(math.floor(2.9))
```

**Expected Output:**
```
3
2.9
3
2
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
