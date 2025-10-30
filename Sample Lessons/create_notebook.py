import json
import os

# Change to Sample Lessons directory
os.chdir(r"g:\My Drive\Colab Notebooks\COSC1315\Sample Lessons")

notebook = {
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {
            "name": "Lesson_03_Variables_WalkAlong.ipynb",
            "provenance": []
        },
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "cells": [
        # Header
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Lesson 03: Variables - Walk-Along Tasks\n",
                "\n",
                "**Course:** COSC 1315 - Introduction to Computer Programming  \n",
                "**Source:** Code with Mosh - Python for Beginners  \n",
                "**Video Timestamp:** 11:27–18:16\n",
                "\n",
                "---\n",
                "\n",
                "## Instructions\n",
                "\n",
                "Watch the video and follow along with Mosh as he demonstrates each task. After watching him code, pause the video and type the code yourself in the cells below.\n",
                "\n",
                "**Important:** Run each cell using `Shift + Enter` or click the play button.\n",
                "\n",
                "---"
            ]
        },
        # Task 1
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Task 1: Store and Display a Price\n",
                "\n",
                "**What Mosh Does:**  \n",
                "Mosh creates a variable to store a price and then displays it.\n",
                "\n",
                "**Your Steps:**\n",
                "1. Create a variable named `price`\n",
                "2. Assign it the value `10`\n",
                "3. Print the variable to see its value\n",
                "\n",
                "**Expected Output:**\n",
                "```\n",
                "10\n",
                "```"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": ["# Type your code below:\n"],
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# VERIFICATION CODE - Run this cell to check your work\n",
                "try:\n",
                "    if 'price' not in dir():\n",
                "        print(\"Error: Variable 'price' not found.\")\n",
                "        print(\"Make sure you created a variable named 'price'\")\n",
                "    elif price != 10:\n",
                "        print(f\"Error: Variable 'price' has value {price}, but should be 10\")\n",
                "    else:\n",
                "        print(\"Perfect! You created the variable 'price' and assigned it the value 10.\")\n",
                "        print(\"Great job!\")\n",
                "except NameError:\n",
                "    print(\"Error: Variable 'price' not found.\")\n",
                "    print(\"Did you run the code cell above?\")"
            ],
            "execution_count": None,
            "outputs": []
        },
        # Task 2
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## Task 2: Update a Variable Value\n",
                "\n",
                "**What Mosh Does:**  \n",
                "Mosh shows that you can change the value of a variable after creating it.\n",
                "\n",
                "**Your Steps:**\n",
                "1. Create a variable `price` with value `10`\n",
                "2. Change `price` to `20`\n",
                "3. Print the updated value\n",
                "\n",
                "**Expected Output:**\n",
                "```\n",
                "20\n",
                "```"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": ["# Type your code below:\n"],
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# VERIFICATION CODE\n",
                "try:\n",
                "    if 'price' not in dir():\n",
                "        print(\"Error: Variable 'price' not found.\")\n",
                "    elif price != 20:\n",
                "        print(f\"Error: Variable 'price' has value {price}, but should be 20\")\n",
                "        print(\"Remember: You need to reassign the variable to change its value\")\n",
                "    else:\n",
                "        print(\"Excellent! You successfully updated the variable 'price' to 20.\")\n",
                "        print(\"This shows that variables can be changed!\")\n",
                "except NameError:\n",
                "    print(\"Error: Variable 'price' not found.\")"
            ],
            "execution_count": None,
            "outputs": []
        },
        # Task 3
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## Task 3: Work with Different Data Types\n",
                "\n",
                "**What Mosh Does:**  \n",
                "Mosh demonstrates the four main data types in Python.\n",
                "\n",
                "**Your Steps:**\n",
                "1. Create `price` as an integer with value `10`\n",
                "2. Create `rating` as a float (decimal) with value `4.9`\n",
                "3. Create `name` as a string with value `'Mosh'`\n",
                "4. Create `is_published` as a boolean with value `True`\n",
                "5. Print all four variables\n",
                "\n",
                "**Expected Output:**\n",
                "```\n",
                "10\n",
                "4.9\n",
                "Mosh\n",
                "True\n",
                "```\n",
                "\n",
                "**Tip:** Strings use quotes, booleans are True/False (capitalized)"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": ["# Type your code below:\n"],
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# VERIFICATION CODE\n",
                "errors = []\n",
                "\n",
                "try:\n",
                "    if 'price' not in dir() or price != 10 or not isinstance(price, int):\n",
                "        errors.append(\"price should be 10 (integer)\")\n",
                "    if 'rating' not in dir() or rating != 4.9 or not isinstance(rating, float):\n",
                "        errors.append(\"rating should be 4.9 (float)\")\n",
                "    if 'name' not in dir() or name != 'Mosh' or not isinstance(name, str):\n",
                "        errors.append(\"name should be 'Mosh' (string)\")\n",
                "    if 'is_published' not in dir() or is_published != True or not isinstance(is_published, bool):\n",
                "        errors.append(\"is_published should be True (boolean)\")\n",
                "    \n",
                "    if errors:\n",
                "        print(\"Issues found:\")\n",
                "        for error in errors:\n",
                "            print(f\"  - {error}\")\n",
                "    else:\n",
                "        print(\"Outstanding! You created all four data types correctly!\")\n",
                "        print(\"  - Integer (int): whole numbers\")\n",
                "        print(\"  - Float (float): decimal numbers\")\n",
                "        print(\"  - String (str): text in quotes\")\n",
                "        print(\"  - Boolean (bool): True or False\")\n",
                "        \n",
                "except NameError as e:\n",
                "    print(f\"Error: One or more variables not found.\")\n",
                "    print(f\"Details: {e}\")"
            ],
            "execution_count": None,
            "outputs": []
        },
        # Task 4
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## Task 4: Patient Information System\n",
                "\n",
                "**What Mosh Does:**  \n",
                "Mosh creates a simple system to store patient information using three variables.\n",
                "\n",
                "**Your Steps:**\n",
                "1. Create a variable `name` with value `'John Smith'`\n",
                "2. Create a variable `age` with value `20`\n",
                "3. Create a variable `is_new` with value `True`\n",
                "4. Print all three variables\n",
                "\n",
                "**Expected Output:**\n",
                "```\n",
                "John Smith\n",
                "20\n",
                "True\n",
                "```\n",
                "\n",
                "**Challenge:** Try creating variables for yourself with your own name and age!"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": ["# Type your code below:\n"],
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# VERIFICATION CODE\n",
                "errors = []\n",
                "\n",
                "try:\n",
                "    if 'name' not in dir() or name != 'John Smith':\n",
                "        errors.append(\"name should be 'John Smith'\")\n",
                "    if 'age' not in dir() or age != 20:\n",
                "        errors.append(\"age should be 20\")\n",
                "    if 'is_new' not in dir() or is_new != True:\n",
                "        errors.append(\"is_new should be True\")\n",
                "    \n",
                "    if errors:\n",
                "        print(\"Issues found:\")\n",
                "        for error in errors:\n",
                "            print(f\"  - {error}\")\n",
                "    else:\n",
                "        print(\"Perfect! You've completed the Patient Information System!\")\n",
                "        print(\"You now understand how to:\")\n",
                "        print(\"  - Create variables with meaningful names\")\n",
                "        print(\"  - Store different types of data\")\n",
                "        print(\"  - Build simple information systems\")\n",
                "        print(\"\")\n",
                "        print(\"Congratulations! You've completed all Walk-Along tasks for Lesson 03!\")\n",
                "        \n",
                "except NameError as e:\n",
                "    print(f\"Error: One or more variables not found.\")\n",
                "    print(f\"Details: {e}\")"
            ],
            "execution_count": None,
            "outputs": []
        },
        # Summary
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## Summary\n",
                "\n",
                "In this lesson, you learned:\n",
                "\n",
                "- **Variables** store data in memory  \n",
                "- **Assignment** uses the `=` operator  \n",
                "- **Data Types** include:\n",
                "  - `int` (integers): whole numbers\n",
                "  - `float` (floats): decimal numbers\n",
                "  - `str` (strings): text in quotes\n",
                "  - `bool` (booleans): True or False\n",
                "\n",
                "- **Variables can be updated** by reassigning them  \n",
                "- **Descriptive names** make code easier to understand\n",
                "\n",
                "---\n",
                "\n",
                "## Next Steps\n",
                "\n",
                "Practice creating your own variables! Try:\n",
                "- Your name, age, and whether you're a student\n",
                "- A product name, price, and stock quantity\n",
                "- A city name, population, and temperature\n",
                "\n",
                "**Ready for more?** Move on to Lesson 04: Receiving Input!"
            ]
        }
    ]
}

# Write the notebook
with open("Lesson_03_Variables_WalkAlong.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("✅ Created Lesson_03_Variables_WalkAlong.ipynb")
print("📊 Total cells: 14")
print("   - 1 Header")
print("   - 4 Tasks (each with 3 cells)")
print("   - 1 Summary")
print("\n🚀 Ready to upload to Google Colab!")
