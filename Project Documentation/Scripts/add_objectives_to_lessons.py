"""
Script to add structured Learning Objectives sections to each Code with Mosh lesson file.
These objectives follow the HTML format used in the course and can be easily converted.
"""

import os
import re

# Define objectives for each lesson based on Code with Mosh content
lesson_objectives = {
    "01": {
        "title": "Your First Python Program",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Understand the fundamentals of Python programming**
- Explain that Python files use the `.py` extension by convention
- Describe the purpose of the `print()` function for displaying output
- Recognize that Python code produces results visible in a terminal or console window

**Write and execute a basic Python program**
- Create a new Python file (e.g., `app.py`) in their development environment
- Use the `print()` function to display text on the screen
- Include text inside quotation marks (single `'` or double `"`) as function arguments
- Successfully run a Python program and view its output

**Use the print() function correctly**
- Call `print()` with proper syntax: `print("text")`
- Place text inside quotation marks within the parentheses
- Choose between single quotes `'text'` or double quotes `"text"` appropriately
- Remember that both quote styles are valid for simple strings

**Display personalized output**
- Print their own name using `print("Your Name")`
- Customize the message inside the `print()` function
- Understand that the text inside quotes appears exactly as written in the output

**Navigate a development environment**
- Locate and use the Run menu or run button to execute code
- Understand keyboard shortcuts improve productivity (though specifics vary by environment)
- Resize or minimize the terminal/console window as needed while coding
- Recognize that output appears in the terminal window after running code

**Recognize common pitfalls**
- Remember that **missing closing quotes** cause syntax errors (e.g., `print("text` is incomplete)
- Remember that **missing closing parentheses** prevent code from running (e.g., `print("text"` needs `)`)
- Ensure quotation marks match at the beginning and end of text
- Understand that Python is **case-sensitive** (e.g., `Print` is different from `print`)
""",
        "key_terms": """
## Key Terms

- **Python** — A high-level programming language known for readability and versatility
- **`.py` extension** — The file extension used for Python program files (e.g., `app.py`)
- **`print()` function** — A built-in Python function that displays text or values to the console/terminal
- **Function** — A reusable block of code that performs a specific task; `print()` is an example
- **Argument** — The value passed inside parentheses to a function (e.g., `"Hello"` in `print("Hello")`)
- **String** — Text data enclosed in quotation marks (`"text"` or `'text'`)
- **Quotation marks** — Symbols (`"` or `'`) used to define the beginning and end of text strings
- **Terminal/Console** — A window that displays the output of a program
- **Execute/Run** — To carry out or perform the instructions in a program
- **Syntax** — The rules and structure for writing valid code in a programming language
- **Syntax Error** — A mistake in code structure that prevents the program from running
"""
    },
    
    "02": {
        "title": "How Python Code Gets Executed",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Understand how Python executes code**
- Explain that Python reads and executes code **line by line from top to bottom**
- Describe the role of the **Python interpreter** in translating code into instructions the computer can understand
- Recognize that each line is processed sequentially, in the exact order written

**Build multi-line output using print statements**
- Use multiple `print()` statements to create output across several lines
- Understand that each `print()` call produces a new line of output automatically
- Control the visual appearance of output by ordering `print()` statements correctly

**Create ASCII art and text-based drawings**
- Use text characters (like `o`, `-`, `|`) to draw simple shapes and images
- Combine multiple `print()` statements to build complete ASCII art designs
- Design letters, initials, or simple drawings using 10 or more lines of text output
- Apply spacing and alignment within strings to control visual layout

**Use string repetition with the multiplication operator**
- Multiply a string by a number to repeat it (e.g., `"*" * 10` produces `"**********"`)
- Recognize that `"text" * number` creates multiple copies of the text
- Understand that this is a Python-specific feature for string manipulation

**Understand expressions and evaluation**
- Define an **expression** as a piece of code that produces a value
- Recognize that `"*" * 10` is an expression that evaluates to a repeated string
- Explain that Python evaluates expressions before executing the containing statement

**Trace program execution flow**
- Follow the step-by-step execution of a Python program from first line to last
- Predict the output of a multi-line program by reading code top to bottom
- Understand that changing the order of `print()` statements changes the output order

**Recognize common pitfalls**
- Remember that **missing closing quotes** cause syntax errors
- Remember that **missing closing parentheses** prevent code from running
- Avoid mixing quote types incorrectly (e.g., `print("text')` with mismatched quotes)
- Use proper quote escaping or alternating quotes when strings contain quotes
""",
        "key_terms": """
## Key Terms

- **Python Interpreter** — The program that reads Python code line by line and translates it into instructions the computer can execute
- **Execute** — To run or carry out a program or command; Python executes code from top to bottom
- **Line by Line** — The sequential process where Python reads and runs each line of code in order
- **Sequential Execution** — The order in which statements are processed; code runs from first line to last
- **Multi-line Output** — Text output that spans multiple lines, created using multiple `print()` statements
- **ASCII Art** — Pictures or designs created using text characters arranged to form images
- **Expression** — A piece of code that produces a value when evaluated (e.g., `"*" * 10`)
- **String Multiplication** — Repeating a string multiple times using the `*` operator (e.g., `"hi" * 3` yields `"hihihi"`)
- **Operator** — A symbol that performs an operation on values; `*` is the multiplication operator
- **Program Flow** — The order and path in which a program's instructions are executed
"""
    },
    
    "03": {
        "title": "Variables",
        "objectives": """
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
""",
        "key_terms": """
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
"""
    },
    
    "04": {
        "title": "Receiving Input",
        "objectives": """
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
""",
        "key_terms": """
## Key Terms

- **`input()` function** — A built-in Python function that reads a line of text from the user
- **Prompt** — The message displayed to the user asking for input (e.g., `"Enter your name: "`)
- **Return Value** — The data that a function gives back after it executes; `input()` returns a string
- **Interactive Program** — A program that communicates with the user by requesting and responding to input
- **User Input** — Data provided by the person running the program in response to a prompt
- **String Input** — The default data type returned by `input()`; all input is text initially
"""
    },
    
    "05": {
        "title": "Type Conversion",
        "objectives": """
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
""",
        "key_terms": """
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
"""
    },
    
    "06": {
        "title": "Strings",
        "objectives": """
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
""",
        "key_terms": """
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
- **Escape Sequence** — A backslash followed by a character to represent special characters (e.g., `\\n` for newline)
- **Immutable** — Cannot be changed after creation; string methods return new strings rather than modifying the original
- **IndexError** — An exception raised when attempting to access an invalid string index
"""
    },
    
    "07": {
        "title": "Arithmetic Operations",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Perform basic arithmetic operations**
- Use the addition operator `+` to add numbers
- Use the subtraction operator `-` to subtract numbers
- Use the multiplication operator `*` to multiply numbers
- Use the division operator `/` to divide numbers (always returns a float)

**Use advanced arithmetic operators**
- Perform floor division using `//` to get an integer quotient
- Calculate remainders using the modulus operator `%`
- Raise numbers to powers using the exponentiation operator `**`

**Understand operator precedence**
- Recognize that exponentiation `**` has highest precedence
- Know that multiplication, division, floor division, and modulus are evaluated next
- Understand that addition and subtraction are evaluated last
- Use parentheses `()` to override default precedence

**Apply augmented assignment operators**
- Use `+=` to add and assign (e.g., `x += 5` is shorthand for `x = x + 5`)
- Use `-=`, `*=`, `/=`, `//=`, `%=`, `**=` for other operations
- Recognize that augmented operators provide a more concise syntax

**Build programs with calculations**
- Create programs that perform mathematical operations on user input
- Combine multiple operations in a single expression
- Store and display calculation results

**Recognize common pitfalls**
- Remember that `/` always returns a **float**, even for whole number results (e.g., `10 / 2` gives `5.0`)
- Use `//` for integer division if you need a whole number result
- Avoid division by zero, which causes a **ZeroDivisionError**
- Use parentheses to clarify complex expressions and control evaluation order
""",
        "key_terms": """
## Key Terms

- **Arithmetic Operator** — A symbol that performs a mathematical operation
- **Addition (`+`)** — Adds two numbers together
- **Subtraction (`-`)** — Subtracts one number from another
- **Multiplication (`*`)** — Multiplies two numbers
- **Division (`/`)** — Divides one number by another, always returning a float
- **Floor Division (`//`)** — Divides and rounds down to the nearest integer
- **Modulus (`%`)** — Returns the remainder after division
- **Exponentiation (`**`)** — Raises a number to a power (e.g., `2 ** 3` equals `8`)
- **Operator Precedence** — The order in which operations are performed in an expression
- **PEMDAS** — Mnemonic for order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
- **Augmented Assignment** — Operators like `+=`, `-=` that combine an operation with assignment
- **Expression** — A combination of values, variables, and operators that evaluates to a single value
- **ZeroDivisionError** — An exception raised when attempting to divide by zero
"""
    },
    
    "08": {
        "title": "Operator Precedence",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Understand the order of operations in Python**
- Explain that Python follows standard mathematical precedence rules
- Recognize that exponentiation `**` is evaluated first
- Know that multiplication, division, floor division, and modulus have equal precedence
- Understand that addition and subtraction are evaluated last

**Control evaluation order with parentheses**
- Use `()` to explicitly group operations and override default precedence
- Understand that expressions in parentheses are always evaluated first
- Nest parentheses to create complex expressions with clear evaluation order

**Predict expression results**
- Evaluate expressions mentally by applying precedence rules
- Understand that `2 + 3 * 4` equals `14`, not `20`
- Recognize that `(2 + 3) * 4` equals `20` due to parentheses

**Write clear and readable expressions**
- Use parentheses to make complex expressions easier to understand
- Avoid relying solely on precedence rules in complicated expressions
- Write code that is obvious in intent even if parentheses are technically redundant

**Recognize common pitfalls**
- Don't assume left-to-right evaluation; precedence rules apply
- Use parentheses when in doubt about evaluation order
- Avoid writing overly complex expressions in a single line
- Test expressions to verify they produce expected results
""",
        "key_terms": """
## Key Terms

- **Operator Precedence** — The rules determining the order in which operators are evaluated
- **Order of Operations** — The sequence in which mathematical operations are performed
- **Parentheses** — `()` used to group expressions and control evaluation order
- **Evaluation** — The process of computing the value of an expression
- **Grouping** — Using parentheses to explicitly define the order of operations
"""
    },
    
    "09": {
        "title": "Math Functions",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Use built-in mathematical functions**
- Use `round(number, digits)` to round floating-point numbers
- Use `abs(number)` to get the absolute value of a number
- Recognize these as built-in functions available without importing

**Import and use the math module**
- Import the `math` module using `import math`
- Access math functions using dot notation (e.g., `math.ceil()`)
- Understand that modules provide additional specialized functionality

**Apply common math module functions**
- Use `math.ceil()` to round up to the nearest integer
- Use `math.floor()` to round down to the nearest integer
- Use `math.sqrt()` to calculate square roots
- Use `math.pow()` for exponentiation (alternative to `**`)
- Access `math.pi` and `math.e` for mathematical constants

**Recognize common pitfalls**
- Remember to `import math` before using math module functions
- Understand that `round()` is built-in but `ceil()` and `floor()` require the math module
- Don't forget the `math.` prefix when calling module functions
- Know that `math.sqrt()` only accepts positive numbers (negative values cause errors)
""",
        "key_terms": """
## Key Terms

- **Built-in Function** — A function that is always available in Python without importing (e.g., `round()`, `abs()`)
- **`round(number, digits)`** — Rounds a number to a specified number of decimal places
- **`abs(number)`** — Returns the absolute value (distance from zero) of a number
- **Module** — A file containing Python code (functions, classes, variables) that can be imported and reused
- **`import`** — A statement that makes a module's contents available to your program
- **`math` module** — A standard library module providing mathematical functions and constants
- **`math.ceil(x)`** — Returns the smallest integer greater than or equal to `x`
- **`math.floor(x)`** — Returns the largest integer less than or equal to `x`
- **`math.sqrt(x)`** — Returns the square root of `x`
- **`math.pi`** — The mathematical constant π (approximately 3.14159)
- **Dot Notation** — Using a period `.` to access attributes or methods of an object or module
"""
    },
    
    "10": {
        "title": "If Statements",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Understand conditional execution**
- Explain that `if` statements allow programs to make decisions
- Describe how conditions determine which code blocks execute
- Recognize that code under an `if` runs only when the condition is `True`

**Write basic if statements**
- Use the syntax `if condition:` to create conditional statements
- Indent code blocks that should execute when the condition is true
- Understand that Python uses indentation to define code blocks

**Use comparison operators in conditions**
- Use `==` to check if two values are equal
- Use `!=` to check if two values are not equal
- Use `>`, `<`, `>=`, `<=` for numerical comparisons
- Understand that comparison operators return `True` or `False`

**Build programs with conditional logic**
- Create programs that respond differently based on user input
- Validate user input using `if` statements
- Display messages or perform actions only when conditions are met

**Recognize common pitfalls**
- Remember to use `==` for comparison, not `=` (which is assignment)
- Always include the colon `:` at the end of the `if` line
- Indent code blocks consistently (typically 4 spaces)
- Understand that forgetting indentation causes **IndentationError**
""",
        "key_terms": """
## Key Terms

- **Conditional Statement** — Code that executes only when a specified condition is true
- **`if` Statement** — A control structure that executes code conditionally based on a boolean expression
- **Condition** — A boolean expression that evaluates to `True` or `False`
- **Code Block** — A group of statements that are executed together, defined by indentation in Python
- **Indentation** — Whitespace at the beginning of a line that defines code block hierarchy
- **Comparison Operator** — An operator that compares values and returns a boolean result
- **`==` (Equal to)** — Checks if two values are the same
- **`!=` (Not equal to)** — Checks if two values are different
- **`>` (Greater than)** — Checks if the left value is larger than the right
- **`<` (Less than)** — Checks if the left value is smaller than the right
- **`>=` (Greater than or equal to)** — Checks if the left value is larger than or equal to the right
- **`<=` (Less than or equal to)** — Checks if the left value is smaller than or equal to the right
- **Boolean Expression** — An expression that evaluates to `True` or `False`
- **IndentationError** — An exception raised when indentation is incorrect or inconsistent
"""
    },
    
    "11": {
        "title": "Logical Operators",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Use logical operators to combine conditions**
- Use `and` to check if multiple conditions are all true
- Use `or` to check if at least one condition is true
- Use `not` to reverse a boolean value

**Build complex conditional expressions**
- Combine multiple comparisons using `and`, `or`, `not`
- Understand that `and` requires all conditions to be `True`
- Recognize that `or` requires only one condition to be `True`
- Use `not` to negate boolean expressions

**Understand short-circuit evaluation**
- Explain that Python stops evaluating `and` when it finds a `False` condition
- Understand that Python stops evaluating `or` when it finds a `True` condition
- Recognize how short-circuiting improves performance

**Apply operator precedence with logical operators**
- Know that `not` has highest precedence among logical operators
- Understand that `and` is evaluated before `or`
- Use parentheses to clarify complex logical expressions

**Recognize common pitfalls**
- Don't confuse `and`/`or` with `&`/`|` (bitwise operators)
- Remember that `0`, `""`, `None`, and empty collections are "falsy" values
- Use parentheses to avoid precedence errors in complex conditions
- Ensure all parts of a logical expression are valid boolean expressions
""",
        "key_terms": """
## Key Terms

- **Logical Operator** — An operator that combines or modifies boolean values
- **`and` operator** — Returns `True` only if both operands are `True`
- **`or` operator** — Returns `True` if at least one operand is `True`
- **`not` operator** — Reverses the boolean value of its operand
- **Boolean Logic** — The system of logic using `True` and `False` values
- **Short-Circuit Evaluation** — Stopping evaluation once the result is determined
- **Truth Table** — A table showing all possible combinations of boolean inputs and their results
- **Falsy Value** — A value that is considered `False` in a boolean context (e.g., `0`, `""`, `None`)
- **Truthy Value** — A value that is considered `True` in a boolean context (most non-zero, non-empty values)
"""
    },
    
    "12": {
        "title": "Comparison Operators",
        "objectives": """
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
""",
        "key_terms": """
## Key Terms

- **Comparison Operator** — An operator that compares two values and returns `True` or `False`
- **Equality (`==`)** — Tests if two values are the same
- **Inequality (`!=`)** — Tests if two values are different
- **Relational Operator** — Operators that compare magnitudes: `>`, `<`, `>=`, `<=`
- **Lexicographic Comparison** — Comparing strings character by character based on character codes
- **Chained Comparison** — Multiple comparisons in a single expression (e.g., `x < y < z`)
- **Identity Operator (`is`)** — Checks if two variables refer to the same object in memory (different from `==`)
"""
    },
    
    "13": {
        "title": "While Loops",
        "objectives": """
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
""",
        "key_terms": """
## Key Terms

- **Loop** — A control structure that repeats a block of code
- **`while` loop** — A loop that continues executing as long as a condition is `True`
- **Iteration** — A single pass through the loop body
- **Loop Condition** — The boolean expression that determines whether the loop continues
- **Loop Variable** — A variable used to control loop execution, typically updated each iteration
- **Counter** — A variable that tracks the number of iterations
- **Infinite Loop** — A loop that never terminates because its condition never becomes `False`
- **Loop Body** — The indented code block that executes during each iteration
"""
    },
    
    "14": {
        "title": "Lists",
        "objectives": """
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
""",
        "key_terms": """
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
"""
    },
    
    "15": {
        "title": "For Loops",
        "objectives": """
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
""",
        "key_terms": """
## Key Terms

- **`for` loop** — A loop that iterates over each item in a sequence
- **Iteration Variable** — The variable that takes on each item's value during iteration
- **Sequence** — An ordered collection like a list, string, or range
- **`range()` function** — Generates a sequence of numbers for iteration
- **Iterable** — Any object that can be looped over (lists, strings, tuples, ranges, etc.)
- **Nested Loop** — A loop inside another loop
- **Accumulator** — A variable that collects or sums values during iteration
"""
    },
    
    "16": {
        "title": "2D Lists",
        "objectives": """
## Learning Objectives

By the end of this lesson, students will be able to:

**Understand 2D list structure**
- Define a **2D list** as a list containing other lists (a list of lists)
- Recognize that 2D lists represent tabular data like matrices or grids
- Visualize 2D lists as rows and columns

**Create 2D lists**
- Create 2D lists using nested square brackets
- Initialize 2D lists with specific dimensions and values
- Understand that each inner list represents a row

**Access 2D list elements**
- Use double indexing `matrix[row][column]` to access specific elements
- Understand that the first index selects the row, the second selects the column
- Use negative indices to count from the end in either dimension

**Iterate over 2D lists**
- Use nested `for` loops to process all elements
- Use an outer loop for rows and an inner loop for columns
- Access both row and individual element values during iteration

**Recognize common pitfalls**
- Remember that `matrix[i][j]` accesses row `i`, column `j`
- Avoid index errors by staying within valid row and column bounds
- Understand that modifying one row doesn't affect other rows (unless they share references)
- Be cautious when creating 2D lists with repetition (e.g., `[[0] * 3] * 3` creates shared references)
""",
        "key_terms": """
## Key Terms

- **2D List (Two-Dimensional List)** — A list that contains other lists, forming a grid or matrix structure
- **Matrix** — A mathematical term for a 2D array of numbers; represented by 2D lists in Python
- **Row** — A horizontal sequence of elements in a 2D list (each inner list)
- **Column** — A vertical sequence of elements across multiple rows
- **Nested List** — A list inside another list
- **Double Indexing** — Using two indices to access elements in a 2D structure (e.g., `matrix[row][column]`)
- **Nested Loop** — A loop inside another loop, commonly used to traverse 2D lists
"""
    },
    
    "17": {
        "title": "Tuples",
        "objectives": """
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
""",
        "key_terms": """
## Key Terms

- **Tuple** — An ordered, immutable sequence of items enclosed in parentheses
- **Immutable** — Cannot be changed after creation
- **Hashable** — An object with a fixed hash value that can be used as a dictionary key; tuples are hashable
- **Tuple Unpacking** — Assigning tuple elements to multiple variables in one statement (e.g., `x, y = (1, 2)`)
- **Single-Item Tuple** — A tuple with one element, requiring a trailing comma: `(item,)`
- **TypeError** — An exception raised when attempting to modify an immutable object like a tuple
- **Parentheses** — `()` used to define tuples (sometimes optional)
"""
    },
    
    "18": {
        "title": "Unpacking",
        "objectives": """
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
""",
        "key_terms": """
## Key Terms

- **Unpacking** — Assigning elements of a sequence to multiple variables in one statement
- **Sequence** — An ordered collection like a list, tuple, or string
- **Tuple Unpacking** — Extracting tuple elements into separate variables
- **List Unpacking** — Extracting list elements into separate variables
- **Starred Expression (`*variable`)** — Captures multiple remaining items during unpacking
- **Swapping** — Exchanging the values of two variables; easily done with unpacking: `a, b = b, a`
- **ValueError** — An exception raised when the number of variables doesn't match the number of items in unpacking
"""
    },
}

# Base directory for lesson files
base_dir = r"G:\My Drive\Colab Notebooks\COSC1315\Resources\Code with Mosh - Source Lessons"

def add_objectives_to_lesson(lesson_num, lesson_data):
    """Add objectives section to a specific lesson file"""
    lesson_num_str = f"{lesson_num:02d}"
    
    if lesson_num_str not in lesson_objectives:
        print(f"⚠️  No objectives defined for Lesson {lesson_num_str} - skipping")
        return False
    
    # Find the lesson file
    files = os.listdir(base_dir)
    lesson_file = None
    for f in files:
        if f.startswith(f"Lesson_{lesson_num_str}_") and f.endswith(".md"):
            lesson_file = f
            break
    
    if not lesson_file:
        print(f"❌ Could not find file for Lesson {lesson_num_str}")
        return False
    
    filepath = os.path.join(base_dir, lesson_file)
    
    # Read the current file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract objectives and key terms
    obj_data = lesson_objectives[lesson_num_str]
    objectives_section = obj_data['objectives'].strip()
    key_terms_section = obj_data['key_terms'].strip()
    
    # Check if Key Terms already exists (better check than Learning Objectives)
    if "## Key Terms" in content:
        print(f"⏭️  Lesson {lesson_num_str} already has objectives - skipping")
        return True
    
    # Find where to insert (before Teaching Notes section)
    pattern = r'(---\s*\n\s*## Teaching Notes)'
    
    if re.search(pattern, content):
        # Insert objectives before Teaching Notes
        new_content = re.sub(
            pattern,
            f'\n---\n\n{objectives_section}\n\n{key_terms_section}\n\n---\n\n## Teaching Notes',
            content
        )
        
        # Write the updated content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Lesson {lesson_num_str}: {obj_data['objectives'].split('**')[1].split('**')[0]}")
        return True
    else:
        print(f"⚠️  Could not find insertion point in Lesson {lesson_num_str}")
        return False

# Process lessons that have objectives defined
print("Adding Learning Objectives to lesson files...\n")
print("="*80)

success_count = 0
for lesson_num in range(1, 19):  # Process ALL lessons 1-18
    if add_objectives_to_lesson(lesson_num, lesson_objectives):
        success_count += 1

print("="*80)
print(f"\n✅ Successfully updated {success_count} lesson files")
print(f"📂 Location: {base_dir}")
