# Lesson 04: Receiving Input

**Video Timestamp:** 18:16–22:08  
**Week:** Week 3  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

So, you have learned how to print messages on the terminal window. In this tutorial, I'm going to show you how to receive input from the user. So we're going to write a small program that asks the user's name and then we'll print a greeting message customized for that user. So instead of print we're going to use input. Now both these input and print are functions that are built into Python. As a metaphor think of the remote control of the TV. On this remote control we have a bunch of buttons, these are the functions built into your tv, you can turn it on, turn it off, change the volume and so on. In Python we also have functions for common tasks such as printing messages, receiving input, and so on. So we're going to use the input function, now whenever we have these parenthesis, we're going to say we're calling or executing that function, it's like pressing a button on a remote control. So we're going to call the input function and in between parenthesis we want to add a string to print something on the terminal, what is your name? With a question mark followed by a space. You will see why in a second. So this input function will print this message on the terminal, and then it will wait for the user to enter a value. Whatever the user enters this input function will return. So now we can get that value and store it in the memory using a variable. So we get the result and put it in a variable called name. Okay? Now on the second line we want to print a message like Hi John or Hi Mosh or whatever, so, print, quotations Hi with a space, now after the quotation we want to dynamically print what we have in the name variable. So we had a plus sign and then name. So here we have Hi which is a string, we're concatenating or combining the string with another string, that is what we have in the name variable. So here's another example of an expression. Remember what is an expression? It's a piece of code that uses a value. So this expression concatenates or combines 2 strings. Let's run this program and see what happens. So run okay, here is a question, what is your name? Mosh, now note that earlier we added a space after the question mark, we did this, so here in the terminal window the cursor is separated from the question mark, otherwise it would be so close. So let's type whatever here, plus enter, now we get this message, Hi, Mosh. Now here's a little exercise for you. I want you to extend this program and ask two questions. First all the person's name and then their favorite color. And then print a message like Mosh likes blue. So pause the video, do this exercise and then come back and continue watching. Alright, so here's the first question right after that, all the input functions one more time, this time we're going to ask a different question. What is your favorite color? Now, we get the new value and store it in the variable called color, or you could call it favorite underline. color. Either works. And finally we're going to change what we pass to the print function, so first we print the name then we concatenate this with a string, here we're going to type likes, we also put one space before and after likes, and once again we concatenate this. With the favorite color. So, favorite color, now let's run this program, so what is your name Mosh enter, favorite color, blue, enter, we get this message, Mosh likes blue.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Use the input() function to receive user data**
- Call `input()` to prompt the user for information
- Display a custom prompt message using `input("prompt text")`
- Store the value returned by `input()` in a variable

**Create interactive programs**
- Build programs that ask questions and wait for user responses
- Use meaningful prompt messages that clearly communicate what input is expected
- Combine multiple `input()` statements to gather several pieces of information

**Understand input() return values**
- Recognize that `input()` always returns a **string** data type
- Understand that even numeric input (like `"20"`) is received as text
- Anticipate the need for type conversion when performing calculations with input

**Build simple applications**
- Create a program that asks for a user's name and displays a greeting
- Build a survey or questionnaire using multiple `input()` calls
- Store and display multiple pieces of user information

**Recognize common pitfalls**
- Remember that `input()` **returns a string**, not a number
- Understand that mathematical operations on input require **type conversion**
- Avoid empty prompts; always provide clear instructions to the user
- Remember to store the return value of `input()` in a variable to use it later

## Key Terms

- **`input()` function** — A built-in Python function that reads a line of text from the user
- **Prompt** — The message displayed to the user asking for input (e.g., `"Enter your name: "`)
- **Return Value** — The data that a function gives back after it executes; `input()` returns a string
- **Interactive Program** — A program that communicates with the user by requesting and responding to input
- **User Input** — Data provided by the person running the program in response to a prompt
- **String Input** — The default data type returned by `input()`; all input is text initially
- **User Interaction** — The process of a program communicating with and receiving data from the user
- **Console Input** — Data entered by the user through the terminal or console window
- **Variable Assignment** — Storing the result of `input()` in a variable for later use
- **Blocking Operation** — A function call that waits for user action before continuing (like `input()`)


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Ask for User's Name

**Description:** Use the input() function to ask the user for their name, store it in a variable, and print a greeting.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
name = input("What is your name? ")
print("Hi " + name)
```

**Expected Output:**
```
What is your name? Mosh
Hi Mosh
```

### Task 2: Name and Favorite Color

**Description:** Ask for the user's name and favorite color, then print a message like 'Mosh likes blue'.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
name = input("What is your name? ")
color = input("What is your favorite color? ")
print(name + " likes " + color)
```

**Expected Output:**
```
What is your name? Mosh
What is your favorite color? blue
Mosh likes blue
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
