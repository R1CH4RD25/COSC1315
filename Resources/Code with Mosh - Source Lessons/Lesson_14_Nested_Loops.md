# Lesson 14: Nested Loops

**Video Timestamp:** 1:47:44–1:55:44  
**Week:** Week 10  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

python. In this tutorial I'm going to talk to you guys about comparison operators in Python. We use comparison operators in situations where we want to compare a variable with a value, for example, if temperature is greater than 30, then we want to print it's a hot day. Otherwise, if it's less then 10, it's a cold day, otherwise it it's neither hot nor cold. And by the way I'm taking about celsius, not farenheit. So, to build these rules into our program, we need to use comparison operators. Back to app.py, I define this temperature value, let's write an if statement, if temperature now we want to check to see if this is greater than 30, so we use the greater than operator. If this is greater than 30, we want to print it's a hot day otherwise, let's just print it's not a hot day. Now, when we run this program, we're going to see this second message because 30 is not greater than 30. So our first condition a value is to false. let's verify that. So run, it's not a hot day. Now if you change the temperature to 35 and run this again, we're going to see a different message, it's a hot day, so this is where we use comparison operators. Now what we have here as you know is an expression because it's a piece of code that produces a value. So more accurately this is a boolean expression. So this is the greater than operator, we also have greater than or equal to, we have less then, less then or equal to, here's the equality operator, so if the temperature equals to 30, then you can say it's a hot day. Note that this is different from the assignment operator that has only one equals sign. You can see that if we use only one equal sign here we immediately get this red underline because this is simply an assignment statement. We're changing the value of the temperature. you are setting the value of something else. So we don't have a boolean expression, you are not producing a boolean value. Okay? So, our equality operator has two equal signs and finally we have not equal which is an exclamation followed by an equal sign. Now here's an exercise for you. You have probably seen that when you fill out a form online, sometimes the input fields have validation messages, for example, let's say we have an input field for the user to enter their name. Now if the name is less then 3 characters wrong we want to display a validation error, like name must be at least three characters, otherwise, if the name is more then 50 characters long then we want to display a different validation error like name can be a maximum of 50 characters. Otherwise if the name is between 3 and 50 characters then we just want to tell the user that name looks good. So go ahead, and write a plan to implement these rules. Alright let's define a variable called name and set it to let's say j. So we're assuming this is what the user types into an input field. Now, we want to get the number of characters in this string. So we use the len function, right? Len of name. When we print this we get 1, right you have seen this before. Now here we want to use an if statement so if len of name is less then 3, then we want to print name must be at least 3 characters now here we need a second condition to check the upper limit. So el if len of name is greater than 50, then we want to print a different message, name, must be a maximum of 50 characters. Okay? And otherwise if else none of these conditions are true that means the name looks good. So, print, name looks good. Let's run our program. So in this case we get this message because our name is too short. Now if you go back here and type something really really long. And then we run our program we're going to see a different message name must be a maximum of 50 characters and finally if we type a proper name here like John Smith and run our program we get name looks good.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Create and initialize lists**
- Create lists using square brackets `[]` with comma-separated values
- Create empty lists using `[]` or `list()`
- Store multiple items of any data type in a single list

**Access list elements**
- Use indexing with `[]` to access individual items (e.g., `names[0]`)
- Use negative indices to access items from the end (e.g., `names[-1]`)
- Understand that list indexing starts at `0`

**Modify list contents**
- Change individual items using assignment (e.g., `names[0] = "New Value"`)
- Add items with `.append(item)` to add to the end
- Insert items at specific positions with `.insert(index, item)`
- Remove items with `.remove(item)`, `.pop()`, or `.pop(index)`

**Use list operations**
- Find the length of a list using `len(list)`
- Check if an item exists using the `in` operator
- Concatenate lists using `+`
- Repeat lists using `*`

**Slice lists to extract portions**
- Use slice notation `[start:end]` to extract sublists
- Omit `start` or `end` to slice from beginning or to end
- Use negative indices in slices

**Recognize common pitfalls**
- Avoid accessing invalid indices which cause **IndexError**
- Remember that lists are **mutable**; changes affect all references to the same list
- Don't confuse `.append(item)` with `.insert(index, item)`
- Understand that `.remove(item)` removes the first occurrence only

## Key Terms

- **List** — An ordered, mutable collection of items enclosed in square brackets
- **Element/Item** — A single value stored in a list
- **Index** — The numerical position of an item in a list (starting from `0`)
- **Mutable** — Can be changed after creation; lists are mutable
- **`.append(item)`** — Adds an item to the end of a list
- **`.insert(index, item)`** — Inserts an item at a specific position
- **`.remove(item)`** — Removes the first occurrence of an item
- **`.pop()`** — Removes and returns the last item, or the item at a specified index
- **`.pop(index)`** — Removes and returns the item at the given index
- **`len(list)`** — Returns the number of items in a list
- **`in` operator** — Checks if an item exists in a list
- **List Slicing** — Extracting a portion of a list using `[start:end]` notation
- **IndexError** — An exception raised when accessing an invalid list index


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Generate Coordinates

**Description:** Use nested loops to generate a list of (x, y) coordinates.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
```

**Expected Output:**
```
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
```

### Task 2: Draw F Shape

**Description:** Use nested loops to draw an F shape with X's based on a list of numbers.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
```

**Expected Output:**
```
xxxxx
xx
xxxxx
xx
xx
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
