"""
Extract Mosh's "Walk-Along" coding examples from lesson transcripts.
Creates structured Walk-Along sections for easy Colab notebook extraction.

Format for each walk-along task:
- Task Title
- Coding Block (starts with # Type your code below:)
- Expected Output (what Mosh shows when running the code)
"""

import os
import re

BASE_DIR = r"G:\My Drive\Colab Notebooks\COSC1315\Resources\Code with Mosh - Source Lessons"

# Manually defined walk-alongs based on transcript analysis
# Each lesson can have multiple walk-along coding tasks
WALK_ALONGS = {
    "01": {
        "title": "Your First Python Program",
        "tasks": [
            {
                "task_title": "Print Your Name",
                "description": "Create a Python program that prints your name to the screen using the print() function.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'print("Mosh Hamedani")',
                "expected_output": "Mosh Hamedani"
            }
        ]
    },
    
    "02": {
        "title": "How Python Code Gets Executed",
        "tasks": [
            {
                "task_title": "Draw ASCII Art with Your Initial",
                "description": "Use multiple print() statements with string repetition to draw a letter or shape using text characters.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'print("*" * 10)\nprint("*")\nprint("*")\nprint("*")\nprint("*" * 10)',
                "expected_output": "**********\n*\n*\n*\n**********"
            }
        ]
    },
    
    "03": {
        "title": "Variables",
        "tasks": [
            {
                "task_title": "Store and Display a Price",
                "description": "Create a variable called price, assign it the value 10, then print it.",
                "starter_code": "# Type your code below:\n",
                "solution_code": "price = 10\nprint(price)",
                "expected_output": "10"
            },
            {
                "task_title": "Update a Variable Value",
                "description": "Set price to 10, then update it to 20, and print the result.",
                "starter_code": "# Type your code below:\n",
                "solution_code": "price = 10\nprice = 20\nprint(price)",
                "expected_output": "20"
            },
            {
                "task_title": "Work with Different Data Types",
                "description": "Create variables for different data types: an integer (price), a float (rating), a string (name), and a boolean (is_published).",
                "starter_code": "# Type your code below:\n",
                "solution_code": "price = 10\nrating = 4.9\nname = 'Mosh'\nis_published = True\nprint(price)\nprint(rating)\nprint(name)\nprint(is_published)",
                "expected_output": "10\n4.9\nMosh\nTrue"
            },
            {
                "task_title": "Patient Information System",
                "description": "Create three variables for a hospital patient: name (John Smith), age (20), and is_new (True for new patient).",
                "starter_code": "# Type your code below:\n",
                "solution_code": "name = 'John Smith'\nage = 20\nis_new = True\nprint(name)\nprint(age)\nprint(is_new)",
                "expected_output": "John Smith\n20\nTrue"
            }
        ]
    },
    
    "04": {
        "title": "Receiving Input",
        "tasks": [
            {
                "task_title": "Ask for User's Name",
                "description": "Use the input() function to ask the user for their name, store it in a variable, and print a greeting.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'name = input("What is your name? ")\nprint("Hi " + name)',
                "expected_output": "What is your name? Mosh\nHi Mosh"
            },
            {
                "task_title": "Name and Favorite Color",
                "description": "Ask for the user's name and favorite color, then print a message like 'Mosh likes blue'.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'name = input("What is your name? ")\ncolor = input("What is your favorite color? ")\nprint(name + " likes " + color)',
                "expected_output": "What is your name? Mosh\nWhat is your favorite color? blue\nMosh likes blue"
            }
        ]
    },
    
    "05": {
        "title": "Type Conversion",
        "tasks": [
            {
                "task_title": "Calculate Age from Birth Year",
                "description": "Ask for birth year, convert it to an integer, calculate age, and display it.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'birth_year = input("Birth year: ")\nage = 2024 - int(birth_year)\nprint("Age: " + str(age))',
                "expected_output": "Birth year: 2000\nAge: 24"
            },
            {
                "task_title": "Simple Weight Converter",
                "description": "Ask for weight in pounds, convert to kilograms (divide by 2.205), and display the result.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'weight_lbs = input("Weight (lbs): ")\nweight_kg = float(weight_lbs) / 2.205\nprint("Weight (kg): " + str(weight_kg))',
                "expected_output": "Weight (lbs): 165\nWeight (kg): 74.82993197278912"
            }
        ]
    },
    
    "06": {
        "title": "Strings",
        "tasks": [
            {
                "task_title": "String Manipulation Basics",
                "description": "Create a string variable, use string methods like .upper(), .lower(), and check if a substring exists.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'course = "Python for Beginners"\nprint(course.upper())\nprint(course.lower())\nprint(course.find("Python"))\nprint("Python" in course)',
                "expected_output": "PYTHON FOR BEGINNERS\npython for beginners\n0\nTrue"
            },
            {
                "task_title": "String Indexing and Slicing",
                "description": "Access individual characters and extract substrings using indexing and slicing.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'course = "Python for Beginners"\nprint(course[0])\nprint(course[-1])\nprint(course[0:6])\nprint(course[:6])',
                "expected_output": "P\ns\nPython\nPython"
            }
        ]
    },
    
    "07": {
        "title": "Formatted Strings and String Methods",
        "tasks": [
            {
                "task_title": "String Concatenation",
                "description": "Create a message by concatenating strings with variables containing first name and last name.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'first = "John"\nlast = "Smith"\nmessage = first + " [" + last + "] is a coder"\nprint(message)',
                "expected_output": "John [Smith] is a coder"
            },
            {
                "task_title": "Formatted Strings",
                "description": "Use an f-string to create the same message more elegantly with placeholders.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'first = "John"\nlast = "Smith"\nmsg = f"{first} [{last}] is a coder"\nprint(msg)',
                "expected_output": "John [Smith] is a coder"
            }
        ]
    },
    
    "08": {
        "title": "Arithmetic Operations, Operator Precedence, and Math Functions",
        "tasks": [
            {
                "task_title": "Basic Arithmetic Operations",
                "description": "Demonstrate addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'print(10 + 3)\nprint(10 - 3)\nprint(10 * 3)\nprint(10 / 3)\nprint(10 // 3)\nprint(10 % 3)\nprint(10 ** 3)',
                "expected_output": "13\n7\n30\n3.3333333333333335\n3\n1\n1000"
            },
            {
                "task_title": "Augmented Assignment Operators",
                "description": "Use augmented assignment operators to increment and decrement variables.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'x = 10\nx += 3\nprint(x)\nx -= 3\nprint(x)',
                "expected_output": "13\n10"
            },
            {
                "task_title": "Operator Precedence",
                "description": "Demonstrate operator precedence with exponentiation, multiplication, and addition.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'x = 10 + 3 * 2 ** 2\nprint(x)',
                "expected_output": "22"
            },
            {
                "task_title": "Using Math Functions",
                "description": "Import the math module and use ceil, floor, and other math functions.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'import math\n\nprint(round(2.9))\nprint(abs(-2.9))\nprint(math.ceil(2.9))\nprint(math.floor(2.9))',
                "expected_output": "3\n2.9\n3\n2"
            }
        ]
    },
    
    "09": {
        "title": "If Statements",
        "tasks": [
            {
                "task_title": "Simple If Statement",
                "description": "Create a program that checks if it's a hot day and prints a message.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'is_hot = True\nif is_hot:\n    print("It\'s a hot day")\n    print("Drink plenty of water")\nprint("Enjoy your day")',
                "expected_output": "It's a hot day\nDrink plenty of water\nEnjoy your day"
            },
            {
                "task_title": "If-Elif-Else Statement",
                "description": "Create a program with multiple conditions for hot, cold, or lovely day.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'is_hot = False\nis_cold = False\nif is_hot:\n    print("It\'s a hot day")\n    print("Drink plenty of water")\nelif is_cold:\n    print("It\'s a cold day")\n    print("Wear warm clothes")\nelse:\n    print("It\'s a lovely day")\nprint("Enjoy your day")',
                "expected_output": "It's a lovely day\nEnjoy your day"
            },
            {
                "task_title": "Down Payment Calculator",
                "description": "Calculate down payment based on credit status (10% for good credit, 20% otherwise).",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'price = 1000000\nhas_good_credit = True\nif has_good_credit:\n    down_payment = 0.1 * price\nelse:\n    down_payment = 0.2 * price\nprint(f"Down payment: ${down_payment}")',
                "expected_output": "Down payment: $100000.0"
            }
        ]
    },
    
    "10": {
        "title": "Logical Operators and Comparison Operators",
        "tasks": [
            {
                "task_title": "Logical AND Operator",
                "description": "Check if an applicant has both high income AND good credit for loan eligibility.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'has_high_income = True\nhas_good_credit = True\nif has_high_income and has_good_credit:\n    print("Eligible for loan")',
                "expected_output": "Eligible for loan"
            },
            {
                "task_title": "Logical OR Operator",
                "description": "Check if an applicant has high income OR good credit for loan eligibility.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'has_high_income = True\nhas_good_credit = False\nif has_high_income or has_good_credit:\n    print("Eligible for loan")',
                "expected_output": "Eligible for loan"
            },
            {
                "task_title": "Logical NOT Operator",
                "description": "Check if applicant has good credit AND does NOT have a criminal record.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'has_good_credit = True\nhas_criminal_record = False\nif has_good_credit and not has_criminal_record:\n    print("Eligible for loan")',
                "expected_output": "Eligible for loan"
            },
            {
                "task_title": "Comparison Operators",
                "description": "Use comparison operators to check temperature and display appropriate messages.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'temperature = 35\nif temperature > 30:\n    print("It\'s a hot day")\nelse:\n    print("It\'s not a hot day")',
                "expected_output": "It's a hot day"
            },
            {
                "task_title": "Name Validation",
                "description": "Validate user name length is between 3 and 50 characters.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'name = "John Smith"\nif len(name) < 3:\n    print("Name must be at least 3 characters")\nelif len(name) > 50:\n    print("Name must be a maximum of 50 characters")\nelse:\n    print("Name looks good")',
                "expected_output": "Name looks good"
            }
        ]
    },
    
    "11": {
        "title": "Weight Converter Program",
        "tasks": [
            {
                "task_title": "Interactive Weight Converter",
                "description": "Create a program that converts weight between pounds and kilograms based on user input.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'weight = int(input("Weight: "))\nunit = input("(L)bs or (K)g: ")\nif unit.upper() == "L":\n    converted = weight * 0.45\n    print(f"You are {converted} kilos")\nelse:\n    converted = weight / 0.45\n    print(f"You are {converted} pounds")',
                "expected_output": "Weight: 160\n(L)bs or (K)g: L\nYou are 72.0 kilos"
            }
        ]
    },
    
    "12": {
        "title": "While Loops",
        "tasks": [
            {
                "task_title": "Basic While Loop",
                "description": "Create a while loop that prints numbers 1 through 5.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'i = 1\nwhile i <= 5:\n    print(i)\n    i += 1\nprint("Done")',
                "expected_output": "1\n2\n3\n4\n5\nDone"
            },
            {
                "task_title": "Print a Triangle Pattern",
                "description": "Use a while loop to print asterisks in a triangle pattern.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'i = 1\nwhile i <= 5:\n    print("*" * i)\n    i += 1',
                "expected_output": "*\n**\n***\n****\n*****"
            },
            {
                "task_title": "Guessing Game",
                "description": "Build a guessing game where the user has 3 tries to guess the secret number.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'secret_number = 9\nguess_count = 0\nguess_limit = 3\nwhile guess_count < guess_limit:\n    guess = int(input("Guess: "))\n    guess_count += 1\n    if guess == secret_number:\n        print("You won!")\n        break\nelse:\n    print("Sorry, you failed")',
                "expected_output": "Guess: 5\nGuess: 8\nGuess: 9\nYou won!"
            }
        ]
    },
    
    "13": {
        "title": "For Loops",
        "tasks": [
            {
                "task_title": "Iterate Over a String",
                "description": "Use a for loop to print each character in a string on a new line.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'for item in "Python":\n    print(item)',
                "expected_output": "P\ny\nt\nh\no\nn"
            },
            {
                "task_title": "Iterate Over a List",
                "description": "Use a for loop to print each name in a list.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'for name in ["Mosh", "John", "Sarah"]:\n    print(name)',
                "expected_output": "Mosh\nJohn\nSarah"
            },
            {
                "task_title": "Using range() Function",
                "description": "Use the range function to generate numbers from 0 to 9.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'for item in range(10):\n    print(item)',
                "expected_output": "0\n1\n2\n3\n4\n5\n6\n7\n8\n9"
            },
            {
                "task_title": "Calculate Shopping Cart Total",
                "description": "Calculate the total cost of all items in a shopping cart using a for loop.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'prices = [10, 20, 30]\ntotal = 0\nfor price in prices:\n    total += price\nprint(f"Total: {total}")',
                "expected_output": "Total: 60"
            }
        ]
    },
    
    "14": {
        "title": "Nested Loops",
        "tasks": [
            {
                "task_title": "Generate Coordinates",
                "description": "Use nested loops to generate a list of (x, y) coordinates.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'for x in range(4):\n    for y in range(3):\n        print(f"({x}, {y})")',
                "expected_output": "(0, 0)\n(0, 1)\n(0, 2)\n(1, 0)\n(1, 1)\n(1, 2)\n(2, 0)\n(2, 1)\n(2, 2)\n(3, 0)\n(3, 1)\n(3, 2)"
            },
            {
                "task_title": "Draw F Shape",
                "description": "Use nested loops to draw an F shape with X's based on a list of numbers.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'numbers = [5, 2, 5, 2, 2]\nfor x_count in numbers:\n    output = ""\n    for count in range(x_count):\n        output += "x"\n    print(output)',
                "expected_output": "xxxxx\nxx\nxxxxx\nxx\nxx"
            }
        ]
    },
    
    "15": {
        "title": "Lists",
        "tasks": [
            {
                "task_title": "Create and Access Lists",
                "description": "Create a list of names and access individual elements using indexing.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'names = ["John", "Bob", "Mosh", "Sarah", "Mary"]\nprint(names[0])\nprint(names[2])\nprint(names[-1])\nprint(names[-2])',
                "expected_output": "John\nMosh\nMary\nSarah"
            },
            {
                "task_title": "Modify List Elements",
                "description": "Change a list element and print the updated list.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'names = ["John", "Bob", "Mosh", "Sarah", "Mary"]\nnames[0] = "Jon"\nprint(names)',
                "expected_output": "['Jon', 'Bob', 'Mosh', 'Sarah', 'Mary']"
            },
            {
                "task_title": "List Slicing",
                "description": "Extract portions of a list using slice notation.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'names = ["John", "Bob", "Mosh", "Sarah", "Mary"]\nprint(names[2:4])\nprint(names[:3])\nprint(names[2:])',
                "expected_output": "['Mosh', 'Sarah']\n['John', 'Bob', 'Mosh']\n['Mosh', 'Sarah', 'Mary']"
            }
        ]
    },
    
    "16": {
        "title": "2D Lists",
        "tasks": [
            {
                "task_title": "Create a 2D List (Matrix)",
                "description": "Create a 2D list representing a 3x3 matrix.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'matrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\nprint(matrix[0][1])\nprint(matrix[1][2])',
                "expected_output": "2\n6"
            },
            {
                "task_title": "Modify 2D List Elements",
                "description": "Change an element in a 2D list and print the row.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'matrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\nmatrix[0][1] = 20\nprint(matrix[0])',
                "expected_output": "[1, 20, 3]"
            },
            {
                "task_title": "Iterate Over 2D List",
                "description": "Use nested loops to print all elements in a 2D list.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'matrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\nfor row in matrix:\n    for item in row:\n        print(item)',
                "expected_output": "1\n2\n3\n4\n5\n6\n7\n8\n9"
            }
        ]
    },
    
    "17": {
        "title": "List Methods",
        "tasks": [
            {
                "task_title": "Adding Items to Lists",
                "description": "Use append() and insert() to add items to a list.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'numbers = [5, 2, 1, 7, 4]\nnumbers.append(20)\nprint(numbers)\nnumbers.insert(0, 10)\nprint(numbers)',
                "expected_output": "[5, 2, 1, 7, 4, 20]\n[10, 5, 2, 1, 7, 4, 20]"
            },
            {
                "task_title": "Removing Items from Lists",
                "description": "Use remove(), pop(), and clear() to remove items from a list.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'numbers = [5, 2, 1, 7, 4]\nnumbers.remove(5)\nprint(numbers)\nnumbers.pop()\nprint(numbers)',
                "expected_output": "[2, 1, 7, 4]\n[2, 1, 7]"
            },
            {
                "task_title": "Finding Items in Lists",
                "description": "Use index() and count() to find items in a list.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'numbers = [5, 2, 5, 7, 4]\nprint(numbers.index(5))\nprint(numbers.count(5))\nprint(50 in numbers)',
                "expected_output": "0\n2\nFalse"
            },
            {
                "task_title": "Sorting Lists",
                "description": "Use sort() and reverse() to reorder lists.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'numbers = [5, 2, 1, 7, 4]\nnumbers.sort()\nprint(numbers)\nnumbers.reverse()\nprint(numbers)',
                "expected_output": "[1, 2, 4, 5, 7]\n[7, 5, 4, 2, 1]"
            }
        ]
    },
    
    "18": {
        "title": "Tuples",
        "tasks": [
            {
                "task_title": "Create and Access Tuples",
                "description": "Create a tuple and access its elements using indexing.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'numbers = (1, 2, 3)\nprint(numbers[0])\nprint(numbers[-1])',
                "expected_output": "1\n3"
            },
            {
                "task_title": "Demonstrate Tuple Immutability",
                "description": "Show that tuples cannot be modified after creation.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'numbers = (1, 2, 3)\nprint(numbers)\n# Attempting to modify will cause an error:\n# numbers[0] = 10  # This would raise a TypeError',
                "expected_output": "(1, 2, 3)"
            },
            {
                "task_title": "Tuple Unpacking",
                "description": "Unpack tuple elements into separate variables.",
                "starter_code": "# Type your code below:\n",
                "solution_code": 'coordinates = (1, 2, 3)\nx, y, z = coordinates\nprint(f"x={x}, y={y}, z={z}")',
                "expected_output": "x=1, y=2, z=3"
            }
        ]
    },
}

def format_walk_along_section(lesson_data):
    """Format the walk-along section for a lesson"""
    
    sections = []
    sections.append("## Walk-Along Coding Tasks")
    sections.append("")
    sections.append("*These are the coding examples that Mosh demonstrates in the video. Follow along and type the code yourself.*")
    sections.append("")
    
    for i, task in enumerate(lesson_data["tasks"], 1):
        sections.append(f"### Task {i}: {task['task_title']}")
        sections.append("")
        sections.append(f"**Description:** {task['description']}")
        sections.append("")
        sections.append("**Coding Task:**")
        sections.append("```python")
        sections.append(task['starter_code'].rstrip())
        sections.append("```")
        sections.append("")
        sections.append("**Mosh's Solution:**")
        sections.append("```python")
        sections.append(task['solution_code'])
        sections.append("```")
        sections.append("")
        sections.append("**Expected Output:**")
        sections.append("```")
        sections.append(task['expected_output'])
        sections.append("```")
        sections.append("")
    
    return "\n".join(sections)

def add_walk_along_to_lesson(lesson_num):
    """Add Walk-Along section to a lesson file"""
    lesson_key = f"{lesson_num:02d}"
    
    if lesson_key not in WALK_ALONGS:
        return False, "No walk-along defined"
    
    # Find the file - it starts with Lesson_XX_
    files = os.listdir(BASE_DIR)
    lesson_file = None
    for f in files:
        if f.startswith(f"Lesson_{lesson_key}_") and f.endswith(".md"):
            lesson_file = f
            break
    
    if not lesson_file:
        return False, f"File not found for lesson {lesson_key}"
    
    filepath = os.path.join(BASE_DIR, lesson_file)
    
    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Walk-Along section already exists
    if "## Walk-Along Coding Tasks" in content:
        return True, "Already has walk-along section"
    
    # Format the walk-along section
    walk_along_text = format_walk_along_section(WALK_ALONGS[lesson_key])
    
    # Insert after Key Terms, before Teaching Notes
    pattern = r'(## Key Terms\s*\n\n(?:.*?\n)*?)(\n---\s*\n\s*## Teaching Notes)'
    
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return False, "Could not find insertion point"
    
    # Insert walk-along section
    new_content = (
        content[:match.end(1)] + 
        "\n\n---\n\n" + 
        walk_along_text + 
        match.group(2) + 
        content[match.end():]
    )
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, f"Added {len(WALK_ALONGS[lesson_key]['tasks'])} tasks"

# Process lessons with walk-alongs defined
print("="*80)
print("ADDING WALK-ALONG CODING TASKS TO LESSONS")
print("="*80)
print()

success = 0
skipped = 0
failed = 0

for lesson_num in range(1, 19):  # Check all 18 lessons
    result, message = add_walk_along_to_lesson(lesson_num)
    
    if result:
        if "Already has" in message:
            print(f"⏭️  Lesson {lesson_num:02d}: {message}")
            skipped += 1
        else:
            print(f"✅ Lesson {lesson_num:02d}: {message}")
            success += 1
    else:
        if "No walk-along" in message:
            print(f"ℹ️  Lesson {lesson_num:02d}: {message} (will add later)")
            skipped += 1
        else:
            print(f"❌ Lesson {lesson_num:02d}: {message}")
            failed += 1

print()
print("="*80)
print(f"✅ Successfully updated: {success} lessons")
print(f"⏭️  Skipped: {skipped} lessons")
if failed > 0:
    print(f"❌ Failed: {failed} lessons")
print("="*80)

