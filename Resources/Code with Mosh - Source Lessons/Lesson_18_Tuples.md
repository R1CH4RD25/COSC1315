# Lesson 18: Tuples

**Video Timestamp:** 2:13:20–2:15:28  
**Week:** Week 13  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this tutorial I'm going to talk to you guys about nested loops in python. Using a nested loop basically means adding one loop inside of another loop, and with this technique we can do some amazing things for example we can easily generate a list of coordinates. So, a acquired (?) as you know is a combination of x and y value. Let's say 0 and 0. Now let's say you wan to generate a list of coordinates like this. So we have 0 and 0, then we'll have 0 and 1, then 0 and 2, next we're going to change x, so we're going to use 1 for x, and once again we're going to use these 3 values for the y coordinates so 1 and 0 then 1 and 1 and 1 and 2, you got the point. We can easily generate these coordinates using nested loops. Let me show you. So, we start with one loop, let's say for x in range 4. With this loop, we can generate value for the x coordinate. Let's print this on the terminal, Okay, so, we get the values, 0 to 3. Now for each x, like 0, we should generate a few y values. So that is where we use a nested loop. So inside of this loop we're going to add another loop, so instead of just printing x first we want to add another loop, for y in range let's say 3, now we can print x and y together so, print, here, we use a formatted string. to display coordinates like this. So we add parenthesis inside of this parenthesis first we need to add x so curly braces x then a comma followed by another set of curly braces, and y, let's run this program and see what we get. There you go. So, we have these coordinates 0 and 0, 0 and 1, 0 and 2, then you have 1 and 0 1 and 1 1 and 2 and so on. So let me explain exactly how this program gets executed. So in the first iteration, of our outer loop, x is 0. Now we are on line 2, here we have a new loop which we call an inner loop. In this inner loop, in the first iteration y is going to be 0, so we print 0 and 0 on the terminal. Now the control goes back to line 2 or our inner loop. In this second iteration y will be set to 1, but we are still in the first iteration of our outer loop. So x is still 0, but now y is incremented to 1. So that is why we see 0 and 1 on the terminal. Once again, the control goes back to line 2, we are in the third iteration of our inner loop, so this will continue until our inner loop completes. That is when y reaches 2 because this range function generates number 0 to 3 but not including 3. So we'll have 0 1 and 2. After this inner loop completes, then the control goes back to line 1, and at this point we're going to be in the second iteration of our outer loop. So x will be 1, then the control will be moved to line 2, or our inner loop, at this point, this range function is going to generate the numbers 0 to 3 one more time. So this inner loop will be executed 3 times. And then we'll go back to our outer loop. So this is how nested loops get executed. Okay, here's an exercise for you, but this one is a little bit more challenging then the exercises you have done so far. So I really don't expect you to do it, but if you do it, wow, I will be so proud of you, so see what I've done here? Using nested loops, I've written some code to draw this f shape, can you see that? So I let me give you a hint, first of all we have this list, called numbers, in this list we have these values, 5, 2, 5, 2, 5, 2. These values determine the number of x's we have in each line. So, for example, the first item in this list, this tells us that we should have 5 x's on the first line. There you go, so 1, 2, 3, 4, 5, on the second line we're going to have 2 x's, on the third line we're going to have 5 x's like this. So I've written code to convert a simple list of numbers into a shape like this. Now here's a tip for you. Using your for loop you need to iterate over this list. In each iteration you get one number, this determines the number of x's to be displayed on that particular line. So if you want to cheat, you can get this number and multiply by a string that contains x, so if you multiply x by 5, we'll get 5 x's, that's not what I want you to do. I want you to use an inner loop here to generate a string that contains 5 x's. So imagine in Python we cannot multiply a string by a number so to solve this problem we need a nested loop. So go ahead and spend five minutes on this exercise. And by the way, do your best to solve this. It is a little bit challenging, but it's not extremely difficult. It just requires a little bit of focus. You'll see my solution next. Alright so first we need to iterate over all the items in this list. So for item in numbers, or, you could rename this variable to x\_count. That is the number of x's on each line. Okay? Now I told you that if you want to cheat you can write code like this. Print x times x underline count. If you run this program we get the same output. So this is the beauty of Python, with Python we can write expressions like this, we can multiply a string by a number to repeat it. A lot of other programming languages don't support this feature. But for this exercise, I wanted you to imagine that we don't have this feature in Python so you will have to use an inner loop to solve this problem. Here's how it works. In the first iteration, x count is going to be 5. So we need to generate 5 x's. How can we do that? Well, let's say we define a variable called output and initially set it to an empty string. Now we need to add 5 x's to this string. So, we can use another loop for count in range, of x underline count. So we're using the range function to generate a sequence of numbers from 0 up to x count. So in our first iteration x count is going to be 5, so range of 5 would generate the numbers 1, 2, 3, 4. So this inner loop will be executed 5 times. That is exactly what this count represents. So now in each iteration we simply need to append an x to our output variable. So we set output, plus, equals x, and then after this inner loop we simply print the output. With his we'll print 5 x's on the first row. Then we go to the second iteration of our outer loop. At this point x count is going to be 2, now on line 3, we're going to reset our output variable to an empty string. So we start over. Then we go to our inner loop, this loop will be executed 2 times, so we'll append to x's to the output variable and then print it, as simple as that. So see, it wasn't really that difficult, but it was slightly more difficult then the previous exercises. So let's run this program, there you go. Now if you're adventurous, I want you to modify the values that we have in our numbers list,



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand unpacking concepts**
- Define **unpacking** as assigning sequence elements to multiple variables simultaneously
- Recognize that unpacking works with lists, tuples, and other sequences
- Understand that the number of variables must match the number of items

**Unpack sequences into variables**
- Unpack tuples: `x, y = (10, 20)`
- Unpack lists: `first, second, third = [1, 2, 3]`
- Unpack strings: `a, b, c = "abc"`

**Use unpacking in practical scenarios**
- Swap variable values: `a, b = b, a`
- Return and unpack multiple values from functions
- Extract specific elements from sequences

**Apply the asterisk operator for variable-length unpacking**
- Use `*rest` to capture remaining items: `first, *rest = [1, 2, 3, 4]`
- Place `*` before any variable name to collect multiple items
- Understand that starred variables always collect into a list

**Recognize common pitfalls**
- Ensure the number of variables matches the number of items (unless using `*`)
- Attempting to unpack with a mismatched count causes a **ValueError**
- Remember that `*rest` creates a list, even if only one item is captured
- Understand that only one starred variable is allowed per unpacking

## Key Terms

- **Unpacking** — Assigning elements of a sequence to multiple variables in one statement
- **Sequence** — An ordered collection like a list, tuple, or string
- **Tuple Unpacking** — Extracting tuple elements into separate variables
- **List Unpacking** — Extracting list elements into separate variables
- **Starred Expression (`*variable`)** — Captures multiple remaining items during unpacking
- **Swapping** — Exchanging the values of two variables; easily done with unpacking: `a, b = b, a`
- **ValueError** — An exception raised when the number of variables doesn't match the number of items in unpacking
- **Packing** — Creating a tuple by grouping multiple values together
- **Sequence Type** — A category of data types that store ordered collections (lists, tuples, strings)
- **Ordered Sequence** — A collection where elements have a defined order and position


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Create and Access Tuples

**Description:** Create a tuple and access its elements using indexing.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
numbers = (1, 2, 3)
print(numbers[0])
print(numbers[-1])
```

**Expected Output:**
```
1
3
```

### Task 2: Demonstrate Tuple Immutability

**Description:** Show that tuples cannot be modified after creation.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
numbers = (1, 2, 3)
print(numbers)
# Attempting to modify will cause an error:
# numbers[0] = 10  # This would raise a TypeError
```

**Expected Output:**
```
(1, 2, 3)
```

### Task 3: Tuple Unpacking

**Description:** Unpack tuple elements into separate variables.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
coordinates = (1, 2, 3)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")
```

**Expected Output:**
```
x=1, y=2, z=3
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
