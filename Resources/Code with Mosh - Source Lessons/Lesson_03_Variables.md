# Lesson 03: Variables

**Video Timestamp:** 12:56–18:16  
**Week:** Week 3  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this Python tutorial, you're going to learn about variables, which are one of the most fundamental concepts in programming, they're not specific to Python, they exist in pretty much every programming language out there. We use variables to temporarily store data in a computer's memory. Here's an example, let's type price = 10, when Python interpreter executes this code, it will allocate some memory, then it will store the number 10 in that memory, and finally it will attach this price label in that memory location. As a metahor imagine we have a box. In that box, we have number 10 and price is the label that we put on the box. Now we can use this label anywhere in our program to access the value that we have in that box. This is a very simplified explanation. So now, let's print price on the terminal. Print, now this time we're not going to add quotations, because if we put quotations here, we will see the text price on the terminal. Now the value of the price variable. So, put it in quotations, and type price, now, let's run this program one more time, there you go. So we see 10, on the terminal. So this is how we define variables, we start with an identifier which is the name of our variable, then, an equal sign and finally a value. Now more accurately, when this number 10 is about to be stored in the memory, first it will get converted to this binary for presentation. So this number 10, is in the decimal system which has all the digits from 0 to 9. Computers don't understand all these digits, they only understand 0s and 1s. So when we store the number 10 in the computer's memory first it will get converted to it's binary representation which will be a bunch of 0's and 1's, like 001, 001, whatever I don't know. Then it will get stored in the computer's memory. So, let's take this program to the next level. On the second line we can update the value of this price variable, so we can reset it to a new value like 20, now when we run our program, we should see 20, because as I told you before Python interpreter executes our code line by line from the top. So first we set the price to 10, then we reset it to 20, and finally we print it on the terminal, let's run the terminal, there you go, so, we see 20 here, okay? Now these numbers that we have here are whole numbers without a decimal point. In programming, we refer to these numbers as integers. But integer is a number without a decimal point. We can also use numbers with a decimal point for example on line 2, we can define another variable called rating and set it to number 4.9. Now in programming, we refer to this kind of number as a floating point number of float for short. So we have integers and floats. We can also define a variable and set it to a string, for example, name equals Mosh, we also have another kind of value which is called boolean, which can be true or false. They are line yes and no in English. Here is an example, I'm going to define a variable, is underline published so we use an underscore to separate multiple words in our variables name. We set this to true, or false. These are boolean values. now note that Python is a case sensitive language, which means it's sensitive to lower case and upper case letters. So when defining variables we should always use lowercase letters, but here false and true are special keywords in the language, so if we spell it with a lowercase f, Python doesn't understand it. You can see we have a red underline here, which indicates an error. Make sure to spell this with a capital F, or if you want to set this to true, make sure the T is capital, so in this program, you're storing simple values in our computer's memory. Simple values can be numbers, which can be integers or floats or they can be strings or booleans. But in Python we can also store complex values like lists and values. And that's what I'm going to show you in the future. So before going any further, I want you to do a little exercise. Imagine we're going to write a program for a hospital. So we check on a patient named John Smith. He's 20 years old and is a new patient. I want you to define 3 variables here, for his name, his age, and another variable for if this is a new or an existing patient. So pause the video and spend one minute on this exercise. When you're done, come back, continue and see my solution. Alright, so here we need three variables, the first one is the patient's name, we set that to John Smith. We can also call this full name, these are both valid names for our variables. The second variable is for the age of our patient. So age is 20, and finally we need a variable to tell if this is a new or existing patient. That's where we can use a boolean value. So, we define a variable, is new and we set it to true.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand the purpose and concept of variables**
- Define a **variable** as a container or box that stores a value in memory
- Explain that variables allow programs to remember and reuse data
- Recognize that variables have names (identifiers) and hold specific values

**Declare and assign values to variables**
- Create variables using the assignment operator `=` (e.g., `price = 10`)
- Use meaningful, descriptive variable names that indicate their purpose
- Assign different data types to variables (integers, floats, strings, booleans)

**Follow Python naming conventions**
- Start variable names with a **letter** or **underscore** (`_`)
- Use only letters, digits, and underscores in variable names
- Avoid using Python **keywords** (like `print`, `if`, `for`) as variable names
- Write variable names in **lowercase** with underscores between words (`first_name`)

**Use variables in expressions and output**
- Reference variables by name to retrieve their stored values
- Include variables in `print()` statements to display their values
- Perform calculations using variables (e.g., `total = price * quantity`)

**Reassign and update variable values**
- Change a variable's value by assigning it a new value
- Understand that assignment replaces the old value with the new one
- Use the current value of a variable to calculate a new value for the same variable

**Work with different data types**
- Store **integers** (whole numbers) in variables (e.g., `age = 20`)
- Store **floats** (decimal numbers) in variables (e.g., `price = 19.95`)
- Store **strings** (text) in variables (e.g., `name = "John"`)
- Store **booleans** (`True` or `False`) in variables (e.g., `is_online = True`)

**Recognize common pitfalls**
- Avoid starting variable names with **digits** (e.g., `1st_name` is invalid)
- Don't include **spaces** in variable names (use `first_name`, not `first name`)
- Remember that Python is **case-sensitive** (`Price` and `price` are different variables)
- Understand that using **descriptive names** makes code more readable than cryptic abbreviations

## Key Terms

- **Variable** — A named container that stores a value in computer memory
- **Assignment** — The act of giving a value to a variable using the `=` operator
- **Assignment Operator (`=`)** — The symbol used to assign a value to a variable (e.g., `x = 5`)
- **Identifier** — The name given to a variable, function, class, or other program element
- **Data Type** — The category of data a variable holds (e.g., integer, float, string, boolean)
- **Integer (int)** — A whole number without a decimal point (e.g., `10`, `-5`, `0`)
- **Float** — A number with a decimal point (e.g., `19.95`, `3.14`)
- **String (str)** — Text data enclosed in quotes (e.g., `"Hello"`, `'Python'`)
- **Boolean (bool)** — A data type that can only be `True` or `False`
- **Keyword** — A reserved word in Python that has special meaning and cannot be used as a variable name (e.g., `print`, `if`, `for`)
- **Naming Convention** — Standard rules for naming variables, typically using lowercase with underscores (`snake_case`)
- **Reassignment** — Changing the value of an existing variable by assigning it a new value
- **Case-Sensitive** — Distinguishing between uppercase and lowercase letters; `name` and `Name` are different variables


---

## Walk-Along Coding Tasks

*Follow along with Mosh in the video. Watch him code, pause the video, and type the code yourself.*

---

### Task 1: Store and Display a Price

**What Mosh Does:**
Mosh creates a variable to store a price and then displays it.

**Your Steps:**
1. Create a variable named `price`
2. Assign it the value `10`
3. Print the variable to see its value

**When You Run Your Code:**
```
10
```

---

### Task 2: Update a Variable Value

**What Mosh Does:**
Mosh shows that you can change the value of a variable after creating it.

**Your Steps:**
1. Create a variable `price` with value `10`
2. Change `price` to `20`
3. Print the updated value

**When You Run Your Code:**
```
20
```

---

### Task 3: Work with Different Data Types

**What Mosh Does:**
Mosh demonstrates the four main data types in Python by creating variables of each type.

**Your Steps:**
1. Create `price` as an integer with value `10`
2. Create `rating` as a float (decimal) with value `4.9`
3. Create `name` as a string with value `'Mosh'`
4. Create `is_published` as a boolean with value `True`
5. Print all four variables

**When You Run Your Code:**
```
10
4.9
Mosh
True
```

*Tip: Strings use quotes, booleans are True/False (capitalized), floats have decimals*

---

### Task 4: Patient Information System

**What Mosh Does:**
Mosh creates a simple system to store patient information using three variables.

**Your Steps:**
1. Create a variable `name` with value `'John Smith'`
2. Create a variable `age` with value `20`
3. Create a variable `is_new` with value `True` (indicating a new patient)
4. Print all three variables

**When You Run Your Code:**
```
John Smith
20
True
```

*Challenge: Try creating variables for yourself with your own name and age!*

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
