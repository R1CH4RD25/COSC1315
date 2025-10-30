# Lesson 12: While Loops

**Video Timestamp:** 1:20:40–1:41:44  
**Week:** Week 9  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this tutorial, I'm going to talk to you about if statements in Python if statements are extremely important in programming and they allow us to build programs that can make decisions based on some condition. So if some conditions are true we're going to do certain things, otherwise we're going to do other things. Here's an example. Over here I've got this text file with a bunch of rules for our program. If it's a hot day, perhaps we want to tell the user it's a hot day, so make sure to drink plenty of water. Otherwise, if it's cold, so here's another condition if this condition is true we're going to tell the user it's a cold day so where warm clothes. And otherwise if it's either hot or cold, we want to tell the user it's a lovely day. So let me show you how to write a program that simulates these rules. So, back to our program here, we start by defining a boolean variable is underline hot. We set this to true. Next, we add an if statement, so if, here we need to add a condition, in this case we're going to use our boolean variable. So, is underline hot. So if this values to true. Then we're going to do certain things. In this case, we want to tell the user hey it's a hot day, drink plenty of water. So, back to our program after our condition we add a colon, now, note that when I press enter pycharm automatically indents our cursor. Now any code that we write here will be executed if this condition is true, otherwise it will be ignored. Here is an example. Let's write a print statement, here I'm going to use double quotes because I want to use an apostrophe in our string. So, it's a hot day. Now let's press enter you can see the cursor is still indented, that means we can write more code that we executed if this condition is true, in this case let's say we don't want to write any extra code, so to terminate this block we need to press shift and tab, now the cursor is at the beginning of the line so lets write a print statement with a message like enjoy your day. Now when we run this program, because this condition is true, you're doing to say this message followed by this second message, take a look, so run, there you go, it's a hot day enjoy your day. But if I go over here and change this boolean value to false and run the program again, our first message disappears and we only see the second message, enjoy your day. So this is how if statements work. Now back here we can add another print statement let's say drink plenty of water. Now because this spirant statement is also indented it will be executed if this condition is true. So I'm going to revert is hot to true and run the program one more time. There you go, so it's a hot day, drink plenty of water, and enjoy your day. Alright now let's add a second rule here, if it's hot we're going to execute these two lines, otherwise if it's not hot we want to print a different message. So here we are moving an indentation and typing els colon. Now when we press enter once again our cursor indented so the code that we write here will be executed if this condition is not true. So here we can print it's a cold day, print, where warm clothes. Now let's run our program one more time. So we get the message about a hot day followed by enjoy your day. You don't see any message about a cold day. Now if we go back here on the top. And change this boolean value to false and run our program we see different set of messages. It's a cold day wear warm clothes and enjoy your day. But there's a problem with our program. If it's not hot it doesn't necessarily mean that it's cold, it means it's a lovely day. So the absence of heat doesn't mean its cold. Back to our conditions, here on line 4 we have this rule that says if it's a cold day, then print these messages otherwise if it's neither hot or cold say it's a lovely day. So, to implement this rule we need to go back and put py and define another variable. So let' say is underline cold we set this to true. Now here we need to add a second condition. So after our first if statement, we can use an el if statement to define a second condition. So here's how it works. So, el if which is short for els if or otherwise if, now here we add another condition, so, is cold So if t's cold you want to execute these few lines. So let's cut these from here, and move them under our second condition and finally if none of these conditions are true, you want to print a different message. It's a lovely day. So, right now, is hot is false, is cold is true, so when we run this program, python interpreter is going to execute the first if statement, in this case because our condition is false, these two lines will be ignored, then Python interpreter will look at line 7, it will evaluate this condition, in this case is cold is true so we're going to see these two messages on the terminal. Now, in this case, because one of these conditions was true, this els statement will be ignored, so we are not going to see this message, and finally as before, we are always going too see this message. So let's run our program, there you go. it's a cold day, where warm clothes and and enjoy your day. Now, back to the top, if we change is cold to false it's neither hot nor cold so it's going to be a lovely day. Let's run the program, and here you go, it's a lovely day enjoy your day. So these are the basics of using if statements. As you can see they are very useful in programming and with these we can build all kinds of rules into our programs. Okay here's an exercise or you. Imagine the price of a house is 1 million dollars. Now if the buyer has good credit, they will need to put down 10 percent of the price of this property otherwise they need to put down 20 percent write a program with these rules an display the down payment card for a buyer with good credit. You will see my solution next. Alright let's define a variable for the price of this house so price we set this to 1 million so 1 with 6 0s. Next we need a variable to tell if this buyer has good credit so has good credit, and we set this to true, now we need an if statement so if has good credit has true colon, here we need to calculate a down payment so the down\_payment should be equal to 0.1 x the price. That is 10 percent of the price of this property. Otherwise colon the down payment should be 0.2 times price. Now finally we remove the indentation and print here we can use a form of valid string, first we add a label, down payment colon and right after that we add a placeholder or a hole for our down payment variable. So curly braces down payment. Let's run this program, so down payment for a buyer with good credit is 100,000 dollars. Now let's improve this by adding a dollar sign before this number. So back to our formatted string, just before the curly brace I'm going to add a dollar sign let's



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Apply all comparison operators correctly**
- Use `==` to test equality between values
- Use `!=` to test inequality
- Use `>`, `<`, `>=`, `<=` for numerical and string comparisons
- Understand that comparison operators return boolean values

**Compare different data types**
- Compare numbers (integers and floats) using relational operators
- Compare strings alphabetically (lexicographically)
- Understand that uppercase letters come before lowercase in ASCII order

**Chain comparison operators**
- Write chained comparisons like `a < b < c`
- Understand that `a < b < c` is equivalent to `a < b and b < c`
- Use chaining to write more readable range checks

**Recognize common pitfalls**
- Remember that `==` tests equality while `=` is assignment
- Don't use `is` for value comparison; use `==` instead
- Be aware that string comparison is case-sensitive (`"Hello" != "hello"`)
- Understand that comparing incompatible types may cause errors or unexpected results

## Key Terms

- **Comparison Operator** — An operator that compares two values and returns `True` or `False`
- **Equality (`==`)** — Tests if two values are the same
- **Inequality (`!=`)** — Tests if two values are different
- **Relational Operator** — Operators that compare magnitudes: `>`, `<`, `>=`, `<=`
- **Lexicographic Comparison** — Comparing strings character by character based on character codes
- **Chained Comparison** — Multiple comparisons in a single expression (e.g., `x < y < z`)
- **Identity Operator (`is`)** — Checks if two variables refer to the same object in memory (different from `==`)
- **Loop Control** — Managing when a loop starts, continues, or terminates
- **Exit Condition** — The state that must be reached for a loop to stop executing
- **Loop Termination** — The act of ending a loop's execution when its condition becomes `False`


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Basic While Loop

**Description:** Create a while loop that prints numbers 1 through 5.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")
```

**Expected Output:**
```
1
2
3
4
5
Done
```

### Task 2: Print a Triangle Pattern

**Description:** Use a while loop to print asterisks in a triangle pattern.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
i = 1
while i <= 5:
    print("*" * i)
    i += 1
```

**Expected Output:**
```
*
**
***
****
*****
```

### Task 3: Guessing Game

**Description:** Build a guessing game where the user has 3 tries to guess the secret number.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed")
```

**Expected Output:**
```
Guess: 5
Guess: 8
Guess: 9
You won!
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
