# Lesson 13: For Loops

**Video Timestamp:** 1:41:44–1:47:44  
**Week:** Week 10  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

run this one more time, that is better. In this tutorial I'm going to talk to you about the logical operators within Python. We use these operators in situations where we have multiple conditions. Here is an example. Let' say we're building an application for processing loans. If an applicant has high income and good credit, then they're eligible for a loan. So in this example we have two conditions, one is having high income and the other is having good credit. So if both these conditions are true, then the applicant is eligible for a loan. So this is where we use the logical and operator. We use this operator to combine two conditions, and by the way this is not specific to python programming language, pretty much any programming language that supports if statements also supports the logical operators. So, back to our program, let's define two variables, has high income, we set this to true. And another one has good credit, we also set this to true, now our if statement if has high income has true, and has good credit is also true, then we're going to print eligible for null. So this is where we're using the and operator. So if both these conditions are true then this message will be printed. If one of them is false, we're not going to see this message. Let's try this out. So I'm going to run this program so we see it eligible for loan, but if we change either of these conditions to false, and run the program again look, the message disappears. So this is the logical and operator. We also have the logical or, and we want to use that in situations where we want to do certain things at least one of the conditions is true, for example let's change the rule for this program, such that if the applicant has high income, or good credit, then they're eligible for a loan, so if either or both these conditions are true then the candidate is eligible. Now back to our program we can implement this rule by using the logical or operator. So we simply replace and with or, now when we run this program we're going to see this message because at least one of our conditions is true, let's take a look. So the applicant is eligible for a loan for a loan because they have good credit. If you change this to false but set the other condition to true, we still see the same result, but if both these conditions are false then we're not going to see this message anymore. So this is the difference between these operators. With the logical and operator both conditions should be true, with the logical or operator at least one condition should be true we also have another logical operator called not and that basically inverses any boolean value we give it, if we give it, we give it a true boolean value it converts it to false. For example let's make up a new room, if applicant has good credit and doesn't have a criminal record then they're eligible for a loan. Let me show you how to implement this. So, we go back to our program, in this example we don't need a first variable for let's delete that. Let's set this variable to true we also define another variable like has criminal record. We set this to false. Now, we want to check to see if this applicant has good credit and not a criminal record. This is where we use the not operator. So, if they have good credit, and not criminal record. So, in this example, has criminal record is set to false, when we use the not operator this basically gets changed to true, so we have two conditions that are true. Here's ones and here's another one. So our applicant is eligible for a loan. And when we run this program we see this familiar message. However if an applicant has a criminal record, so let's change this to true, now when we run this program we can see our applicant is not eligible because when we apply then operator on this variable, we'll get false. So true changes to false. And we'll end up with two conditions, one that's true and the other is false. And that's why this message is not printed. So this is all about the logical operators in



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand loop concepts**
- Define a **loop** as a control structure that repeats code multiple times
- Explain that `while` loops continue executing as long as a condition is `True`
- Recognize that the condition is checked before each iteration

**Write while loops with correct syntax**
- Use the syntax `while condition:` to create a loop
- Indent the loop body to define which statements repeat
- Update loop variables to eventually make the condition `False`

**Control loop execution**
- Use a counter variable to track the number of iterations
- Update the counter within the loop to approach the exit condition
- Ensure loops eventually terminate by modifying the condition variable

**Build programs with while loops**
- Create programs that repeat actions until a condition is met
- Validate user input in a loop until correct data is provided
- Perform repeated calculations or operations

**Recognize common pitfalls**
- Avoid **infinite loops** where the condition never becomes `False`
- Always update variables that affect the loop condition
- Remember the colon `:` at the end of the `while` statement
- Ensure proper indentation of the loop body

## Key Terms

- **Loop** — A control structure that repeats a block of code
- **`while` loop** — A loop that continues executing as long as a condition is `True`
- **Iteration** — A single pass through the loop body
- **Loop Condition** — The boolean expression that determines whether the loop continues
- **Loop Variable** — A variable used to control loop execution, typically updated each iteration
- **Counter** — A variable that tracks the number of iterations
- **Infinite Loop** — A loop that never terminates because its condition never becomes `False`
- **Loop Body** — The indented code block that executes during each iteration
- **Iterate** — To repeat a process or loop through elements one by one
- **Loop Index** — A variable that tracks the current position in a sequence during iteration


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Iterate Over a String

**Description:** Use a for loop to print each character in a string on a new line.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
for item in "Python":
    print(item)
```

**Expected Output:**
```
P
y
t
h
o
n
```

### Task 2: Iterate Over a List

**Description:** Use a for loop to print each name in a list.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
for name in ["Mosh", "John", "Sarah"]:
    print(name)
```

**Expected Output:**
```
Mosh
John
Sarah
```

### Task 3: Using range() Function

**Description:** Use the range function to generate numbers from 0 to 9.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
for item in range(10):
    print(item)
```

**Expected Output:**
```
0
1
2
3
4
5
6
7
8
9
```

### Task 4: Calculate Shopping Cart Total

**Description:** Calculate the total cost of all items in a shopping cart using a for loop.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
```

**Expected Output:**
```
Total: 60
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
