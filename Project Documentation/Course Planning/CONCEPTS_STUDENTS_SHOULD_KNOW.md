# 🎓 COSC 1315 - What Students Should Know Upon Completion

**Course:** COSC 1315.35 - Introduction to Computer Programming (Python)  
**Instructor:** Professor Richard Sullivan  
**Based on:** 18-lesson schedule (Weeks 1-14, Final Week 15)  
**Created:** October 20, 2025

---

## 📚 COMPLETE CONCEPT MAP (18 Lessons)

### **By December 9, 2025 (Final Exam), students should know:**

---

## 1️⃣ **FOUNDATIONAL PROGRAMMING CONCEPTS**

### **What Programming Is:**
- ✅ Programming is giving instructions to a computer
- ✅ Code is written in human-readable form (source code)
- ✅ Computer translates code into machine-readable form
- ✅ Python is an interpreted language (runs line-by-line)
- ✅ Programs execute from top to bottom (unless told otherwise)

**From Lessons:** 1 (First Program), 2 (How Code Gets Executed)

---

## 2️⃣ **VARIABLES & DATA TYPES**

### **Variables:**
- ✅ Variables store data for later use
- ✅ Variable names must follow rules (no spaces, can't start with number, etc.)
- ✅ Use descriptive names (`batting_average` not `ba`)
- ✅ Variables can be reassigned new values

### **Data Types:**
- ✅ **Integers (int):** Whole numbers (42, -10, 0)
- ✅ **Floats (float):** Decimal numbers (3.14, -0.5, 2.0)
- ✅ **Strings (str):** Text in quotes ("Hello", 'Python')
- ✅ **Booleans (bool):** True or False

### **Type Conversion:**
- ✅ Why conversion is needed (can't mix types in operations)
- ✅ `int()` - Convert to integer
- ✅ `float()` - Convert to decimal
- ✅ `str()` - Convert to string
- ✅ Common errors: `TypeError` when mixing incompatible types

**From Lessons:** 3 (Variables), 5 (Type Conversion)

---

## 3️⃣ **INPUT & OUTPUT**

### **Output (Displaying Information):**
- ✅ `print()` function displays text to screen
- ✅ Can print multiple items: `print("Hello", name)`
- ✅ Can format output nicely with f-strings
- ✅ Escape characters: `\n` (new line), `\t` (tab)

### **Input (Getting Information from User):**
- ✅ `input()` function gets user text
- ✅ `input()` always returns a string (must convert if needed)
- ✅ Can include prompt message: `input("What's your name? ")`
- ✅ Store input in variable for later use

### **Formatted Strings:**
- ✅ f-strings for readable output: `f"Hello, {name}!"`
- ✅ Can include expressions: `f"Total: {price * quantity}"`
- ✅ Can format numbers: `f"{average:.2f}"` (2 decimal places)

**From Lessons:** 1 (print), 4 (input), 7 (formatted strings)

---

## 4️⃣ **STRINGS (TEXT MANIPULATION)**

### **String Basics:**
- ✅ Strings are sequences of characters
- ✅ Can use single or double quotes
- ✅ Concatenation: `"Hello" + " " + "World"`
- ✅ Repetition: `"Ha" * 3` → "HaHaHa"
- ✅ Indexing: `name[0]` (first character)
- ✅ Length: `len(name)`

### **String Methods:**
- ✅ `.upper()` - Convert to uppercase
- ✅ `.lower()` - Convert to lowercase
- ✅ `.title()` - Capitalize first letter of each word
- ✅ `.strip()` - Remove whitespace from ends
- ✅ `.replace(old, new)` - Replace text
- ✅ `.find(text)` - Find position of text
- ✅ `.split()` - Split into list

### **Why Strings Matter:**
- ✅ Most user input is text
- ✅ Processing names, messages, data
- ✅ Formatting output nicely

**From Lessons:** 6 (Strings), 7 (String Methods)

---

## 5️⃣ **ARITHMETIC & MATH**

### **Arithmetic Operators:**
- ✅ `+` Addition
- ✅ `-` Subtraction
- ✅ `*` Multiplication
- ✅ `/` Division (always returns float)
- ✅ `//` Integer division (whole number result)
- ✅ `%` Modulus (remainder)
- ✅ `**` Exponentiation (power)

### **Operator Precedence:**
- ✅ Order of operations: PEMDAS
- ✅ Parentheses force order
- ✅ `2 + 3 * 4` = 14, not 20
- ✅ `(2 + 3) * 4` = 20

### **Math Functions:**
- ✅ `abs(x)` - Absolute value
- ✅ `round(x, digits)` - Round to decimal places
- ✅ `min(a, b, c)` - Find minimum
- ✅ `max(a, b, c)` - Find maximum
- ✅ Import `math` module for more functions

### **Augmented Assignment:**
- ✅ `x += 5` same as `x = x + 5`
- ✅ `-=`, `*=`, `/=` also work

**From Lesson:** 8 (Arithmetic Operations, Precedence, Math Functions)

---

## 6️⃣ **CONDITIONAL LOGIC (DECISION MAKING)**

### **If Statements:**
- ✅ Make programs respond differently to conditions
- ✅ Basic: `if condition:`
- ✅ If-else: Choose between two options
- ✅ If-elif-else: Multiple options
- ✅ Nested if: Decisions within decisions

### **Comparison Operators:**
- ✅ `==` Equal to (NOT single `=`)
- ✅ `!=` Not equal to
- ✅ `>` Greater than
- ✅ `<` Less than
- ✅ `>=` Greater than or equal to
- ✅ `<=` Less than or equal to

### **Logical Operators:**
- ✅ `and` - Both conditions must be True
- ✅ `or` - At least one condition must be True
- ✅ `not` - Reverse the condition
- ✅ Combining: `if age >= 18 and has_license:`

### **Boolean Expressions:**
- ✅ Expressions that evaluate to True or False
- ✅ Used in if statements and while loops
- ✅ `temperature > 30` → True or False

**From Lessons:** 9 (If Statements), 10 (Logical & Comparison Operators)

---

## 7️⃣ **LOOPS (REPETITION)**

### **While Loops:**
- ✅ Repeat code while condition is True
- ✅ `while condition:` body of loop
- ✅ Must have way to eventually stop (avoid infinite loops)
- ✅ Use for unknown number of repetitions
- ✅ Example: Keep asking until valid input

### **For Loops:**
- ✅ Iterate over sequences (lists, ranges)
- ✅ `for item in sequence:` body of loop
- ✅ `range(n)` - Numbers from 0 to n-1
- ✅ `range(start, stop)` - Numbers from start to stop-1
- ✅ `range(start, stop, step)` - Custom intervals
- ✅ Use for known number of repetitions

### **Nested Loops:**
- ✅ Loops inside loops
- ✅ Outer loop runs once, inner loop runs completely each time
- ✅ Used for 2D patterns, grids, tables
- ✅ Example: Print multiplication table

### **Loop Control:**
- ✅ `break` - Exit loop immediately
- ✅ `continue` - Skip to next iteration
- ✅ Used to handle special cases

**From Lessons:** 12 (While Loops), 13 (For Loops), 14 (Nested Loops)

---

## 8️⃣ **LISTS (DATA COLLECTIONS)**

### **List Basics:**
- ✅ Lists store multiple values: `[1, 2, 3]`
- ✅ Can hold different types: `["Alice", 25, True]`
- ✅ Indexing: `scores[0]` (first item)
- ✅ Negative indexing: `scores[-1]` (last item)
- ✅ Length: `len(scores)`
- ✅ Mutable: Can change items after creation

### **List Operations:**
- ✅ Slicing: `scores[1:3]` (get subset)
- ✅ Concatenation: `list1 + list2`
- ✅ Repetition: `[0] * 5` → `[0, 0, 0, 0, 0]`
- ✅ Check membership: `5 in scores` → True/False

### **List Methods:**
- ✅ `.append(item)` - Add to end
- ✅ `.insert(index, item)` - Add at position
- ✅ `.remove(item)` - Remove first occurrence
- ✅ `.pop()` - Remove and return last item
- ✅ `.pop(index)` - Remove and return item at index
- ✅ `.clear()` - Remove all items
- ✅ `.sort()` - Sort in place
- ✅ `.reverse()` - Reverse order
- ✅ `.count(item)` - Count occurrences
- ✅ `.index(item)` - Find position

### **2D Lists:**
- ✅ Lists of lists: `[[1,2], [3,4], [5,6]]`
- ✅ Represent grids, tables, matrices
- ✅ Access: `grid[row][col]`
- ✅ Iterate with nested loops

**From Lessons:** 15 (Lists), 16 (2D Lists), 17 (List Methods)

---

## 9️⃣ **TUPLES (IMMUTABLE SEQUENCES)**

### **Tuple Basics:**
- ✅ Similar to lists but immutable (can't change after creation)
- ✅ Created with parentheses: `(1, 2, 3)`
- ✅ Can index and slice like lists
- ✅ Can iterate over with loops

### **When to Use Tuples:**
- ✅ Data that shouldn't change (coordinates, RGB colors)
- ✅ Multiple return values from functions
- ✅ Dictionary keys (lists can't be keys)
- ✅ Slightly faster than lists

### **Key Difference:**
- ✅ Lists: Mutable (can modify)
- ✅ Tuples: Immutable (can't modify)
- ✅ `list[0] = 10` ✅ Works
- ✅ `tuple[0] = 10` ❌ Error

**From Lesson:** 18 (Tuples)

---

## 🔟 **PROGRAM STRUCTURE & DESIGN**

### **Comments:**
- ✅ `#` for single-line comments
- ✅ Explain what code does
- ✅ Help others (and future you) understand code
- ✅ Don't comment obvious things

### **Code Organization:**
- ✅ Logical flow from top to bottom
- ✅ Group related code together
- ✅ Use blank lines for readability
- ✅ Consistent indentation (4 spaces in Python)

### **Indentation:**
- ✅ Python uses indentation to define blocks
- ✅ Must be consistent (all spaces or all tabs)
- ✅ Used after `if`, `for`, `while`, `def`
- ✅ `IndentationError` if incorrect

### **Problem-Solving Process:**
- ✅ Understand the problem
- ✅ Break into smaller steps
- ✅ Write pseudocode or plan
- ✅ Implement in Python
- ✅ Test with different inputs
- ✅ Debug errors
- ✅ Refine and improve

**From:** All lessons (consistent practice)

---

## 1️⃣1️⃣ **DEBUGGING & ERROR HANDLING**

### **Common Syntax Errors:**
- ✅ `SyntaxError: invalid syntax` - Missing colon, parenthesis, quote
- ✅ `IndentationError` - Incorrect indentation
- ✅ `NameError` - Using undefined variable
- ✅ `TypeError` - Wrong type for operation (e.g., "5" + 5)

### **Debugging Strategies:**
- ✅ Read error message (tells you line and problem)
- ✅ Check for missing colons after `if`, `for`, `while`
- ✅ Check indentation alignment
- ✅ Use `print()` to see variable values
- ✅ Test small sections at a time
- ✅ Compare to working examples

### **Testing:**
- ✅ Test with different inputs
- ✅ Test edge cases (0, negative, empty)
- ✅ Test expected behavior
- ✅ Test error conditions

**From:** "Debug the Bug" sections in all lessons

---

## 1️⃣2️⃣ **PRACTICAL APPLICATION**

### **Real-World Programs:**
- ✅ Weight Converter (Lesson 11)
  - Get user input
  - Perform calculation
  - Display result
  - Combine: input, logic, output

### **Problem-Solving Patterns:**
- ✅ Input → Process → Output
- ✅ Initialize → Loop → Accumulate
- ✅ Condition → Action
- ✅ Iterate → Modify → Collect

### **Code Reusability:**
- ✅ Recognize similar patterns
- ✅ Modify existing code for new problems
- ✅ Build on previous solutions

**From:** Lesson 11 (Weight Converter) + "Try It Yourself" sections

---

## 📊 SUMMARY: CORE PROGRAMMING KNOWLEDGE

### **By Course End, Students Should Know:**

**Conceptual Understanding:**
1. ✅ What programming is and how computers execute code
2. ✅ How to break problems into logical steps
3. ✅ How to design algorithms (step-by-step solutions)
4. ✅ When to use different programming constructs

**Python Fundamentals:**
5. ✅ Variables and data types (int, float, string, bool)
6. ✅ Input and output operations
7. ✅ Type conversion
8. ✅ String manipulation
9. ✅ Arithmetic operations

**Control Flow:**
10. ✅ Conditional logic (if/elif/else)
11. ✅ Comparison and logical operators
12. ✅ While loops (condition-based repetition)
13. ✅ For loops (count-based repetition)
14. ✅ Nested loops

**Data Structures:**
15. ✅ Lists (creation, indexing, modification)
16. ✅ List methods (append, remove, sort, etc.)
17. ✅ 2D lists (grids and tables)
18. ✅ Tuples (immutable sequences)

**Professional Skills:**
19. ✅ Reading and understanding error messages
20. ✅ Debugging code systematically
21. ✅ Testing programs with different inputs
22. ✅ Writing clear comments
23. ✅ Using proper programming terminology
24. ✅ Following code conventions (indentation, naming)
25. ✅ Learning independently from resources

---

## 🎯 PRACTICAL ABILITIES (What Students Can DO)

### **Level 1: Basic Programs (Lessons 1-5)**
**Students can:**
- ✅ Write "Hello, World!" and variations
- ✅ Get user input and display it
- ✅ Store data in variables
- ✅ Convert between types
- ✅ Perform simple calculations

**Example:** Ask user's name and age, calculate birth year

---

### **Level 2: Text & Math (Lessons 6-8)**
**Students can:**
- ✅ Format output nicely
- ✅ Manipulate strings (uppercase, replace, find)
- ✅ Perform complex calculations
- ✅ Use math functions
- ✅ Build simple calculators

**Example:** Calculate batting average with formatted output

---

### **Level 3: Decision Making (Lessons 9-11)**
**Students can:**
- ✅ Write programs that respond differently to input
- ✅ Validate user input
- ✅ Create multi-option menus
- ✅ Combine conditions with and/or
- ✅ Build practical applications

**Example:** Weight converter that handles kg/lbs conversion both ways

---

### **Level 4: Repetition (Lessons 12-14)**
**Students can:**
- ✅ Repeat actions until condition met
- ✅ Count and iterate over sequences
- ✅ Create patterns and tables
- ✅ Process multiple items
- ✅ Build games and simulations

**Example:** Calculate team statistics for all players

---

### **Level 5: Collections (Lessons 15-18)**
**Students can:**
- ✅ Store and organize multiple values
- ✅ Process lists of data
- ✅ Sort and search data
- ✅ Work with 2D grids
- ✅ Choose appropriate data structures

**Example:** Track scores for entire season, find highs/lows/averages

---

## 💼 VOCABULARY & TERMINOLOGY

**Students should know these terms:**

**General Programming:**
- Source code, interpreter, execute
- Algorithm, logic, syntax
- Debug, error, bug
- Comment, documentation

**Data & Types:**
- Variable, assignment, value
- Integer, float, string, boolean
- Type conversion, casting
- Immutable vs mutable

**Operations:**
- Operator, expression, operand
- Concatenation, arithmetic
- Comparison, logical operator
- Augmented assignment

**Control Flow:**
- Conditional, if statement
- Boolean expression, condition
- Loop, iteration, iterate
- Nested, break, continue

**Data Structures:**
- List, index, element
- Slice, append, remove
- 2D list, grid, matrix
- Tuple, sequence

**Input/Output:**
- Print, output, display
- Input, prompt, user input
- Format, f-string

**Debugging:**
- Error message, exception
- Syntax error, indentation error
- Name error, type error
- Test, validate

---

## 📈 LEARNING PROGRESSION

### **Week 1-4: "I can make it work!"**
- Basic programs that print and calculate
- Store data in variables
- Get user input

### **Week 5-6: "I can make it useful!"**
- Format output nicely
- Process text
- Build calculators

### **Week 7-8: "I can make it smart!"**
- Programs that make decisions
- Respond to different inputs
- Validate data

### **Week 9-10: "I can make it repeat!"**
- Automate repetitive tasks
- Process multiple items
- Create patterns

### **Week 11-14: "I can work with data!"**
- Store collections
- Organize information
- Analyze data

### **Week 15: "I understand programming!"**
- Confident in fundamentals
- Ready for Programming I (if interested)
- Can learn more independently

---

## ✅ FINAL COMPETENCY CHECKLIST

**By December 9, 2025, students should be able to:**

**Foundational:**
- [ ] Write and run Python programs
- [ ] Use variables to store data
- [ ] Get input from users
- [ ] Display formatted output
- [ ] Convert between data types

**Computational Thinking:**
- [ ] Break problems into steps
- [ ] Design simple algorithms
- [ ] Use conditional logic
- [ ] Implement repetition
- [ ] Organize data in structures

**Python Syntax:**
- [ ] Write correct Python syntax
- [ ] Use proper indentation
- [ ] Write meaningful comments
- [ ] Follow naming conventions
- [ ] Use appropriate data types

**Problem Solving:**
- [ ] Read and understand error messages
- [ ] Debug syntax errors
- [ ] Debug logical errors
- [ ] Test programs systematically
- [ ] Modify code for new purposes

**Professional Skills:**
- [ ] Read existing code
- [ ] Explain what code does
- [ ] Use programming terminology
- [ ] Learn from documentation
- [ ] Ask for help effectively

**Meta-Skills:**
- [ ] Confidence: "I can learn this"
- [ ] Awareness: "I know if I want more"
- [ ] Resilience: "Errors are normal"
- [ ] Independence: "I can figure it out"

---

## 🎓 BOTTOM LINE

### **When students finish your course, they should:**

**KNOW:**
- ✅ What programming is and how it works
- ✅ Variables, types, input/output
- ✅ Conditional logic and loops
- ✅ Lists and basic data structures
- ✅ How to debug and test code

**BE ABLE TO:**
- ✅ Write simple Python programs (20-30 lines)
- ✅ Solve basic problems with code
- ✅ Modify existing code for new uses
- ✅ Debug common errors
- ✅ Explain code to others

**FEEL:**
- ✅ Confident they can learn programming
- ✅ Not intimidated by code
- ✅ Informed about whether to continue
- ✅ Proud of what they accomplished

**DECIDE:**
- ✅ "Do I want to take Programming I?"
- ✅ "Is CS a potential career path?"
- ✅ "Can I use programming in my field?"

---

## 📚 REFERENCE

**Full schedule:** `Templates/COURSE_SCHEDULE_AND_OBJECTIVES.md`  
**Course goals:** `Course Planning/COURSE_GOALS_AND_CONCEPTS.md`  
**Student reality:** `Course Planning/STUDENT_PROFILE_AND_CONSTRAINTS.md`

---

**Created:** October 20, 2025  
**Based on:** 18-lesson Code with Mosh curriculum (6:08 - 2:15:28)  
**End Date:** December 9, 2025 (Final Exam)

---

**Success = Students complete course with confidence and informed decision about continuing!** 🎯
