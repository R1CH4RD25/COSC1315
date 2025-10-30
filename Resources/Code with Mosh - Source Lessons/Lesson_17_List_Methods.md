# Lesson 17: List Methods

**Video Timestamp:** 2:05:52–2:13:20  
**Week:** Week 12  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

again. In this tutorial, I'm going to talk to you guys about for loops in python. In the last tutorial, you learned about while loops you learned that we use while loops to execute a block of code multiple times. In python we have another kind of loop, that is a for loop, and we use that and we use that to iterate over items of a collection, such as a string. Because a string is a sequence of characters, so it looks like a collection so we can use a for loop to iterate over each character in a string and then do something with it. Here's an example. We type out for then we define a variable, this is what we call a loop variable. In each iteration, this variable will hold one item. So, let's call it item, in here we type out a string like Python, and then colon. So with this for loop we can iterate over a string and in each iteration this item variable will hold one character at a time in the first iteration it will be set to p then in the second iteration it will be set to y, and in the third iteration it will be set to t and so on. So here we are inside our for block, because of the indentation here, so whatever we type here will be executed in each iteration, for now we can simply print this item now let's run this program and see what happens. So you can see each character in this string is printed on a new line. Let's look at another example. In Python we can define lists using square brackets, so let me remove this string from here, and define a list using square brackets, a list is simply a list of items, a list of numbers, a list of customers, a list of emails, products, blog posts, whatever. So here we can define a list of names like Mosh, Jon, Sarah, and then go ahead and run our program so we can see in each iteration we get one name and print it on a new line. We can also loop over a list of numbers, for example, 1, 2, 3, 4, let's run it, again we see each number on a new line, but what if we want a list of numbers? We don't to explicitly type out a list with let's say 100 or 1000 numbers, we don't want to type, 5, 6 7 all the way to 100. That is when we use the range function. So, let me delete this, In Python we have a built in function called range, for creating range of numbers. So, we give it a number, let's say 10, let's run this program, now we can see here on the terminal we have 0 all the way to 9. So 10 is not included. So basically when we call the range function, this range creates an object, it's not a list, it's a special kind of object we can iterate over, in each iteration this object will spit out a new number. We can also work with a range of numbers here, let's say you want to start from 5, and go all the way to 10. So, let's run our program, now we have the numbers 5, 6, 7, and 9. Also, this range function can optionally take a step, so we can pass two asa step to this function, and when we run our program, we can see our first number is 5, now we go two steps forward to get 7, once again we go to two steps forward we get 9 and that is the end of our range. So this is the basics of using for loops in python. Now here's an exercise for you. I want you to write a program to calculate the total cost of all the items in a shopping cart. So let's say we have a list of prices like 10, 20, and 30, I want you to use a for loop, to calculate the total cost of all the items in our imaginary shopping cart, so calculate that, and then print it on the terminal. That's pretty easy. And you should do it in a couple minutes. So as you learned we use for loops to iterate over all the items in a collection, a collection can be a string, it can be a list, it can be a range object that is returned from the range function. Anything, any kind of object that has multiple items. So in this example we're going to use a for loop to iterate over the list of prices. So for item in prices, colon, and by the way this loop variable we don't have to call this item, can call this anything. For example, in this case we can rename it to price. So for price, in prices. Now in each iteration this price will hold one value. In the first iteration it's going to hold 10, then it's gooing to be 20, and then it's going to be 30. So we need to define another variable to calculate the total so we define that outside of our for loop, let's call it total and initially we set it to 0. Now in each iteration we get the current price and add it to the total so we write total equals total plus price or as you learned earlier we can use the augmented assignment operator to simplify this code. So, after our for loop. This total variable has a total of all the prices we can simply print it here, or we can use a formatted string, so a string prefix with f, the other label, like total, curly braces to dynamically include some value in our string, in this case our total variable. So let's go ahead and run this program, there you go, so the total cost of all the items in our imaginary shopping cart is 60.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Understand tuple characteristics**
- Define a **tuple** as an ordered, immutable sequence
- Explain that tuples are similar to lists but cannot be modified after creation
- Recognize that tuples use parentheses `()` instead of square brackets

**Create and initialize tuples**
- Create tuples using parentheses with comma-separated values: `(1, 2, 3)`
- Create single-item tuples with a trailing comma: `(value,)`
- Understand that parentheses are sometimes optional: `1, 2, 3` is also a tuple

**Access tuple elements**
- Use indexing to access items: `my_tuple[0]`
- Use negative indices to count from the end
- Slice tuples using `[start:end]` notation

**Understand immutability**
- Recognize that tuples **cannot be modified** after creation
- Understand that attempting to change a tuple element causes a **TypeError**
- Know that immutability makes tuples hashable and usable as dictionary keys

**Use tuples appropriately**
- Use tuples for fixed collections of related items (e.g., coordinates `(x, y)`)
- Return multiple values from functions using tuples
- Use tuple unpacking to assign multiple variables at once: `x, y = (10, 20)`

**Recognize common pitfalls**
- Remember the comma in single-item tuples: `(5,)` not `(5)`
- Don't try to modify tuples; create a new tuple instead
- Understand that a tuple containing mutable objects (like lists) can have those objects modified

## Key Terms

- **Tuple** — An ordered, immutable sequence of items enclosed in parentheses
- **Immutable** — Cannot be changed after creation
- **Hashable** — An object with a fixed hash value that can be used as a dictionary key; tuples are hashable
- **Tuple Unpacking** — Assigning tuple elements to multiple variables in one statement (e.g., `x, y = (1, 2)`)
- **Single-Item Tuple** — A tuple with one element, requiring a trailing comma: `(item,)`
- **TypeError** — An exception raised when attempting to modify an immutable object like a tuple
- **Parentheses** — `()` used to define tuples (sometimes optional)
- **List Modification** — Changing, adding, or removing elements from a list
- **In-Place Modification** — Changing a list directly without creating a new one
- **Method Chaining** — Calling multiple methods in sequence (limited for lists since many methods return `None`)


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Adding Items to Lists

**Description:** Use append() and insert() to add items to a list.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
```

**Expected Output:**
```
[5, 2, 1, 7, 4, 20]
[10, 5, 2, 1, 7, 4, 20]
```

### Task 2: Removing Items from Lists

**Description:** Use remove(), pop(), and clear() to remove items from a list.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
```

**Expected Output:**
```
[2, 1, 7, 4]
[2, 1, 7]
```

### Task 3: Finding Items in Lists

**Description:** Use index() and count() to find items in a list.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
numbers = [5, 2, 5, 7, 4]
print(numbers.index(5))
print(numbers.count(5))
print(50 in numbers)
```

**Expected Output:**
```
0
2
False
```

### Task 4: Sorting Lists

**Description:** Use sort() and reverse() to reorder lists.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
numbers = [5, 2, 1, 7, 4]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
```

**Expected Output:**
```
[1, 2, 4, 5, 7]
[7, 5, 4, 2, 1]
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
