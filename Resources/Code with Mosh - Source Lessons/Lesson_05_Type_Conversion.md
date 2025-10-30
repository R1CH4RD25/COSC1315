# Lesson 05: Type Conversion

**Video Timestamp:** 22:40–29:28  
**Week:** Week 4  
**Course:** COSC 1315 - Introduction to Computer Programming  
**Source:** Code with Mosh - Python for Beginners

---

## Original Video Transcript

In this Python tutorial, we're going to write a program that will ask the year that we were born in, and then it will calculate our age and print it on the terminal. So, let's start with our input function, input let's print birth here, followed by a colon, and a space. Now let's get the return value and store it in a variable, called birth\_year. So as I told you before, we use an underscore to separate multiple words Next, we need to calculate the age, so we define another variable called age, and here we do some basic math, currently we are in 2019, so let's write an expression like this. 2019 - birth year. Now finally let's print age on the terminal. Let's run our program and see what happens. So, my birth year is 1982, enter, oops, we got an error, what is going on here? So whenever you see this message, that means there is something wrong with your program. With the information here, we can find exactly where the error occurred. So, next to the file you can see the file that generated this error, in this case that is app.py. So currently our program only has a single file, but real complex programs often have hundreds or even thousands of files. So in this file, on line 2, this is where we got this error, and right below that we can see the piece of code that generated this error. So that is where we're calculating the age, and right below that you can see the type of error. In this case, we have a type error, and here's the message. Unsupported operand types for subtraction. Int and str. So int is short for integer and that represents a whole number and str is short for string, so here we're subtracting a string from an integer, and Python doesn't know what to do with it. Let me explain. So I'm going to close the terminal window. So after the first line we executed we have this birth year variable set to a string, so whatever we type in the terminal is always treated as a string, even if you type the number, in other words, when we run this program, this birth year variable will be set to a string, with four characters. 1982. This string is different from the actual number 1982. One is an integer and the other is a string. Right? So, back to line 2, where this error occurred. At run time, which means when we run our program this expression on the right side of the assignment operator is going to look like this. 2019 - string 1982. Python doesn't know how to interpret or how to evaluate this expression. To fix this problem we need to convert this 1982 into an integer and then we'll be able to subtract it from 2019 and that is easy. So far you have learned about two built in functions one is print the other is input. We have a few other functions for converting values into different types. So we have int for converting a string into an integer, we also have float for converting a string into a float, or a number with a decimal point. And we also have bool for converting a string into a boolean value. So to fix this problem, we need to go back on line 2, and pass this birth year variable to the int function like this. int parenthesis, like this so we pass this string to the int function, int will convert it into an itneger and then Python interpreter will be able to evaluate this expression. Now let's run this program one more time, so birth year is 1982 enter so I am 37 years old. In Python we have a useful function for getting the type of variables, for example, let's print the type of birth year, so right after line 1, let's print, now here we're going to call another built in function, called type, and now let's pass birth year, okay, now similarly after line 3, let's also print the type of age, so print type of age. Okay? So let's run our program, so birth year one more time, 1982, okay, here's the result so the type of birth year as you can see is a class of str or strings, we look at classes in the future so for now don't worry about them, and also below them you cans ee the type of the age variable is int or integer. So here's what you need to take away. Whenever you use the input function, you always get a string, so if you're expecting a numerical value you should always convert that string into an integer or a float. So here's a little exercise for you. I want you to write a program ask the user their weight and then convert it to kilograms and print it on a terminal. So pause the video, do the exercise and when you're ready come back to watch it. Alright so let's use our input function and ask for the weight in pounds here we get the weight in lbs or pounds now we need to convert this into kilograms, it's very easy so we defined another variable weight\_kg we set this to weight\_lbs times 0.45. And finally let's print weight underline kg. Let's run this Python program and see what happens. So my weight is 160, alright once again we got an error, can't multiply sequence by non int of type float. So as I told you before, this input function returns a string, so we cannot multiply a string by a float. Python doesn't know what to do with it. So in this case, we should convert this number by an integer or float and then multiply by 0.45. So let's call the int function. And pass weight underline lbs. And run our program one more time, 160 okay, so I am 72 kg's.



---

## Learning Objectives

By the end of this lesson, students will be able to:

**Convert between data types using built-in functions**
- Use `int()` to convert strings to integers (e.g., `int("20")` yields `20`)
- Use `float()` to convert strings to floating-point numbers (e.g., `float("19.95")`)
- Use `str()` to convert numbers to strings for concatenation or display
- Use `bool()` to convert values to boolean `True` or `False`

**Perform calculations with user input**
- Convert input strings to numbers before performing arithmetic operations
- Add, subtract, multiply, or divide numeric values obtained from the user
- Store calculation results in variables for later use

**Understand type conversion necessity**
- Explain why `input()` returns strings that must be converted for math
- Recognize that `"20" + "10"` concatenates strings (`"2010"`) rather than adding numbers
- Understand that `int("20") + int("10")` correctly evaluates to `30`

**Handle different numeric types**
- Distinguish between integers (whole numbers) and floats (decimal numbers)
- Choose `int()` for whole number conversions and `float()` for decimals
- Understand that `int()` truncates decimal portions (e.g., `int(3.9)` gives `3`)

**Build interactive calculators**
- Create programs that perform arithmetic on user-provided numbers
- Combine `input()` with type conversion functions for numerical calculations
- Display results using `print()` with properly formatted output

**Recognize common pitfalls**
- Avoid trying to perform math directly on strings without conversion
- Remember that `int("3.5")` causes an error; use `float()` first then `int()` if needed
- Understand that invalid conversions (e.g., `int("hello")`) cause **ValueError** exceptions
- Don't forget to convert input strings before using them in calculations

## Key Terms

- **Type Conversion** — Changing data from one type to another (e.g., string to integer)
- **`int()` function** — Converts a value to an integer; truncates decimals without rounding
- **`float()` function** — Converts a value to a floating-point number (decimal)
- **`str()` function** — Converts a value to a string representation
- **`bool()` function** — Converts a value to a boolean (`True` or `False`)
- **Casting** — Another term for type conversion; "casting a string to an integer"
- **ValueError** — An exception raised when a conversion fails (e.g., `int("abc")`)
- **Concatenation** — Joining strings together; `"2" + "3"` produces `"23"`
- **Arithmetic Operations** — Mathematical calculations like addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`)
- **Type Mismatch** — An error that occurs when performing operations on incompatible data types


---

## Walk-Along Coding Tasks

*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*

### Task 1: Calculate Age from Birth Year

**Description:** Ask for birth year, convert it to an integer, calculate age, and display it.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
birth_year = input("Birth year: ")
age = 2024 - int(birth_year)
print("Age: " + str(age))
```

**Expected Output:**
```
Birth year: 2000
Age: 24
```

### Task 2: Simple Weight Converter

**Description:** Ask for weight in pounds, convert to kilograms (divide by 2.205), and display the result.

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**
```python
weight_lbs = input("Weight (lbs): ")
weight_kg = float(weight_lbs) / 2.205
print("Weight (kg): " + str(weight_kg))
```

**Expected Output:**
```
Weight (lbs): 165
Weight (kg): 74.82993197278912
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
