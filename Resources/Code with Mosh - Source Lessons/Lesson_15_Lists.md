# Lesson 15: Lists

**Video Timestamp:** 1:55:44–2:01:44  
**Week:** Week 11  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

Here's another good exercise that combines many of the materials you have learned so far, so earlier you built a program to convert someone's weight from pounds to kilograms. Now we want to extend this program and allow the user to enter their weight in either kilograms or pounds and then we will convert it to the other unit. Here's how our program is going to work. So I enter my weight in pounds so 100 and 60 now it's telling me if it's in pounds or kilograms. So here I'm adding l to lbs or k for kilograms. And by the way, this program is not case sensitive so when I enter a capital l or lowercase l it takes it as pounds. Now it tells me ur set it to kilos. Let's run this program one more time, this time I'm going to enter my weight in kilo's, so send it to is the weight and the unit is kilograms so k, and it says you are 160 pounds. So go ahead and spend a few minutes on this exercise, you will see my solution next. Alright first let's ask the user their weight. So we use the input function, weight colon we get the return value and store it in the variable called weight. Now the second question, so one more time we use the input function el for pounds. Or k for kilograms. So, let's get that too and store it in a variable called unit now we need an if statement. So if unit equals l then we need to convert this weight into kilograms. However, with this implementation we are only allowing the user to enter a capitol l, if they enter a lowercase l this code is not going to work. So this is where we use the upper method of string objects so this unit is a string because as I told you before, the input function always returns a string. So, we can use the dot operator to access all it's methods or functions, here we call the upper method, this will convert whatever the user enters to upper case and then we'll convert it to a capital l. Now, if this condition is true, then we need to get the weight and multiply it by 0,.45 However, as you know this weight is a string object, and we cannot multiply a string by a floating point number, we talked about this earlier in this course. So first we need to convert this weight to a numerical value. So right here, when we call the input function, we can get the return value and pass it to the int function. So, we call the int function and give it the return value of the input function. Now, the in function will return an integer so we can store it in this weight variable. So here's the converted weight, let's store it in a variable called converted, then we print here we can use a formatted string, so we prefix this string with f ur we add curly braces to dynamically insert the value of converted variable. And finally we add kilo. Otherwise, if the unit is kilograms. We need to divide the weight by 0.45. q So, weight divided by 0.45 and just to refresh your memory, this division operator returns a floating point number but if we use double slashes we'll get an integer. In this case, we want to get a floating point number, finally let's print a formatted string, ur curly braces, converted pounds. Okay? Now let's run this program and see what happens. So weight is 160 and lbs in and that equals to 72 kilos, perfect, if we run it one more time, and enter 72 kilos we get 160 pounds.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand for loop concepts**
- Explain that `for` loops iterate over sequences (lists, strings, ranges)
- Describe how a loop variable takes on each item's value in turn
- Recognize that `for` loops are ideal when the number of iterations is known

**Write for loops with correct syntax**
- Use the syntax `for variable in sequence:` to create a loop
- Indent the loop body to define which statements repeat
- Choose meaningful names for loop variables

**Iterate over different sequences**
- Loop through lists with `for item in list:`
- Loop through strings character by character
- Generate number sequences with `range()`

**Use the range() function**
- Create sequences with `range(stop)` (from 0 to stop-1)
- Specify start and stop with `range(start, stop)`
- Use `range(start, stop, step)` for custom increments
- Understand that `range()` does not include the stop value

**Build programs with for loops**
- Process all items in a collection
- Perform repeated actions a specific number of times
- Accumulate values (sums, counts) while iterating

**Recognize common pitfalls**
- Remember the colon `:` at the end of the `for` statement
- Ensure proper indentation of the loop body
- Understand that `range(5)` generates numbers 0-4, not 1-5
- Don't modify a list while iterating over it (can cause unexpected behavior)

## Key Terms

- **`for` loop** — A loop that iterates over each item in a sequence
- **Iteration Variable** — The variable that takes on each item's value during iteration
- **Sequence** — An ordered collection like a list, string, or range
- **`range()` function** — Generates a sequence of numbers for iteration
- **Iterable** — Any object that can be looped over (lists, strings, tuples, ranges, etc.)
- **Nested Loop** — A loop inside another loop
- **Accumulator** — A variable that collects or sums values during iteration
- **Ordered Collection** — A data structure where elements maintain their position and can be accessed by index
- **Collection** — A general term for data structures that store multiple values
- **Array** — A similar concept to a list in other programming languages; Python uses lists instead


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Create and Access Lists

**Description:** Create a list of names and access individual elements using indexing.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])
```

**Expected Output:**
```
John
Mosh
Mary
Sarah
```

### Task 2: Modify List Elements

**Description:** Change a list element and print the updated list.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
names[0] = "Jon"
print(names)
```

**Expected Output:**
```
['Jon', 'Bob', 'Mosh', 'Sarah', 'Mary']
```

### Task 3: List Slicing

**Description:** Extract portions of a list using slice notation.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[2:4])
print(names[:3])
print(names[2:])
```

**Expected Output:**
```
['Mosh', 'Sarah']
['John', 'Bob', 'Mosh']
['Mosh', 'Sarah', 'Mary']
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
