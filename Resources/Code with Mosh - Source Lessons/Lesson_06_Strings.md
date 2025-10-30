# Lesson 06: Strings

**Video Timestamp:** 29:28–37:28  
**Week:** Week 5  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this tutorial, you're going to learn more about Python strings. So I've defined this course variable and set it to Python for beginners now earlier I told you you could use both single and double quotes to define a string, but there are times you have to use a specific form, otherwise you're going to run into issues. Here's an example. Imagine you wanted to change this string into Pythons course for Beginners. So we want to add an apostrophe, like this, Course for Beginners. You can immediately say this is going crazy, because our string starts here and then terminates here, all these characters that we have here after the second apostrophe Python interpreter doesn't know what they are. So to solve this problem we need to use double quotes to define our string so we can have a single quote in the middle of the string. So let's change this to double quotes, now you can see it adds another double quote to close it, you have to manually remove this, and also one more time at the beginning of the string, we need to add another double quote. Now you can see error is gone, so if you print course we see Python course for beginners. Beautiful. Now let's say we don't want this apostrophe here, so we have Python for Beginners, but we want to put Beginners in double quotes. Once again, if you add a double quote here Python interpreter gets confused because it assumes the second double quote indicates that end of the string, so it doesn't know what these characters are, so to solve this we need to change our double quotes to single quotes like this. And then we can add double quotes in the middle of the string. Now let's run this program, there you go. So we get Python for Beginners. So these are the cases for using single or double quotes. Now in all the examples I've shown you so far we only deal with short strings, but what if you wanted to define a string that is multiple lengths? For example, what if you wanted to define a string for the message that we send in an email. In that case we need to use triple quotes. So. We delete this. Now we add three quotes, so 1, 2, 3, there you go, So, we have three quotes to start our string and three to terminate it. Again these quotes can be single or double quotes. Okay? Now, with this we can define a string that spans multiple lines. For example, we can say Hi Jon here is our first email to you. Thank you, The Support Team. Like that. Now, let's run this program and here's the result. So, we get this beautiful multi line string. Now let's change this back to something simple so, we can look at other characteristics of strings and Python. So I'm going to use single quotes and set the course name to Python for Beginners. Now here we're going to use square brackets to get a character and a given index in this string. Let me show you. So to get the first character we use square brackets and type 0. So the index of the first character in the string is 0. In other words, this is how Python strings are indexed. 0, 1, 2, 3, 4, etc. So the index of the first character is 0, the second character is 1, and so on. So let me delete this and run this program we get p. We can also use a negative index here. And this is one of the features that we don't have in other programming languages as far as I know. So we have negative index we can get the characters started from the end. So if I pass negative 1 here, Assuming that 0 is the index of the first character negative 1 is the index of the last character. So when we run this program we should see s. Let's run it, there you go, we get s, if we pass negative 2, this will return the second character from the end. Let's run it one more time, now we get R because that is the second character from the end. Okay? So place close attention to this square brackets syntax because quite often it's the topic for online Python tests or university exams, so if you're preparing for a python test, make sure to watch this tutorial one more time and understand exactly how this square brackets syntax works, we can also use a similar syntax to extract a few characters instead of 1 character. For example, if we type 0, colon 3, Python interpreter will return all the characters starting with this index all the way to this second index, but it does not return the character at this index. In other words, back to these indexes so you have 0, 1, 2, 3, and so on. When you run this program. Python interpreter will return the characters starting from the index 0 all the way to index 3, but excludes the character and index 3, so when we run this Python program we're going to see pint (?). Let me show you, so we're going to delete this line, run this program, there you go. We get pint. Now here we also have default values for the start and end index. So if we don't supply the end index, Python will return all the characters to the end of the string. Let's take a look. So run this program, there you go, Python for Beginners. But if you change the start index to 1, this will exclude the first character so when we run this program, we see ython so p is removed. Okay? Now similarly we have a default value for the start index, so if we don't supply the start index but add an end index like 5. Python interpreter will assume 0 as the start index, so, let's run this program, there you go, we get pytho. Now what if we leave both the start and end index? Well, I told you? Now in this case 0 will be assumed as the start index, and the length of the string will assume as the end index. So with this syntax, you can basically copy or clone a string. In other words, if I define another variable here, let's call it another and set it to course square brackets with just a colon, now this expression will return all the characters in the course variable so variable will be copy of our first variable. Let's take a look, so, let's print another, and load our program there you go, we get Python for beginners. So once again the square bracket syntax is pretty important if you're preparing for online python tests, or college exams, make sure to watch this tutorial again. Now here's a little exercise for you. I'm going to delete all this code define a variable, called name, and set it to Jennifer. Now when we print name of 1: negative 1 what do you think we're going to see on the terminal? I want you to use your knowledge to tell what we're going to see on the terminal, we're now running this program. So pause the video, think about it for a few seconds, then come back and continue watching. So this expression will return the characters starting from index 1 which is the second character all the way to the first character from the end, but excluding the character at this index. In this case, the first character from the in is r, so r will be excluded, in other words we're going to see all the characters starting from e all the way to the second e. Let's take a look. So I'm going to run this program there you go. This is what we get,



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Create and manipulate string literals**
- Define strings using single quotes `'text'` or double quotes `"text"`
- Use triple quotes for multi-line strings
- Include special characters in strings using escape sequences

**Access individual characters with indexing**
- Use bracket notation `[]` to access characters by position (e.g., `name[0]`)
- Understand that indexing starts at `0` (first character is at index `0`)
- Use negative indices to count from the end (e.g., `name[-1]` is the last character)

**Extract substrings using slicing**
- Use slice notation `[start:end]` to extract portions of a string
- Understand that `end` is exclusive (not included in the result)
- Omit `start` to slice from the beginning (e.g., `[:5]`)
- Omit `end` to slice to the end (e.g., `[2:]`)

**Use string methods for manipulation**
- Convert strings to uppercase with `.upper()` and lowercase with `.lower()`
- Remove whitespace from ends with `.strip()`, `.lstrip()`, `.rstrip()`
- Find substrings using `.find()` and check existence with `in` operator
- Replace text using `.replace(old, new)`
- Split strings into lists using `.split()`

**Format strings for output**
- Use formatted string literals (f-strings) with `f"text {variable} more text"`
- Embed variables and expressions directly in strings using `{variable}`
- Understand the advantages of f-strings over older formatting methods

**Recognize common pitfalls**
- Remember that strings are **immutable**; methods return new strings, they don't modify the original
- Avoid off-by-one errors with indexing (first character is `[0]`, not `[1]`)
- Remember that string indices must be integers, not floats or strings
- Understand that accessing an invalid index causes an **IndexError**

## Key Terms

- **String** — A sequence of characters enclosed in quotes
- **String Literal** — A string value written directly in code (e.g., `"Hello"`)
- **Indexing** — Accessing individual characters in a string using `[position]` notation
- **Zero-Based Indexing** — The practice of counting positions starting from `0`
- **Negative Index** — A position counted from the end of a string (e.g., `-1` is the last character)
- **Slicing** — Extracting a substring using `[start:end]` notation
- **Substring** — A portion or slice of a larger string
- **String Method** — A function that belongs to string objects (e.g., `.upper()`, `.replace()`)
- **`.upper()` / `.lower()`** — Methods that return a copy of the string in uppercase/lowercase
- **`.strip()`** — Removes leading and trailing whitespace from a string
- **`.find(substring)`** — Returns the index of the first occurrence of a substring, or `-1` if not found
- **`.replace(old, new)`** — Returns a copy with all occurrences of `old` replaced by `new`
- **`.split()`** — Divides a string into a list of substrings based on a delimiter (default: whitespace)
- **`in` operator** — Checks if a substring exists within a string (returns `True` or `False`)
- **f-string (Formatted String Literal)** — A string prefixed with `f` that allows embedded expressions using `{}`
- **Escape Sequence** — A backslash followed by a character to represent special characters (e.g., `
` for newline)
- **Immutable** — Cannot be changed after creation; string methods return new strings rather than modifying the original
- **IndexError** — An exception raised when attempting to access an invalid string index


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: String Manipulation Basics

**Description:** Create a string variable, use string methods like .upper(), .lower(), and check if a substring exists.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course.find("Python"))
print("Python" in course)
```

**Expected Output:**
```
PYTHON FOR BEGINNERS
python for beginners
0
True
```

### Task 2: String Indexing and Slicing

**Description:** Access individual characters and extract substrings using indexing and slicing.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
course = "Python for Beginners"
print(course[0])
print(course[-1])
print(course[0:6])
print(course[:6])
```

**Expected Output:**
```
P
s
Python
Python
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
