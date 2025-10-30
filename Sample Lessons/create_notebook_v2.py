import json

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
                "**Important:** \n",
                "- Run each cell using `Shift + Enter` or click the play button\n",
                "- Type the EXACT code that Mosh types (don't skip steps!)\n",
                "- Use the verification cells to check your work\n",
                "\n",
                "---"
            ]
        },
        # Setup verification
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# RUN THIS CELL FIRST - It loads the verification helper\n",
                "# You only need to run this once\n",
                "\n",
                "# Download the verification file\n",
                "!wget -q https://raw.githubusercontent.com/YOUR_REPO/lesson_03_verification.py\n",
                "\n",
                "# OR if file is in same folder:\n",
                "# (Google Colab will have the file available if you upload it)\n",
                "\n",
                "from lesson_03_verification import verify_task_1, verify_task_2, verify_task_3, verify_task_4\n",
                "\n",
                "print(\"✅ Verification system loaded!\")\n",
                "print(\"📝 You're ready to start the Walk-Along tasks.\")"
            ],
            "execution_count": None,
            "outputs": []
        },
        # Task 1
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## Task 1: Store and Display a Price\n",
                "\n",
                "**What Mosh Does:**  \n",
                "Mosh creates a variable to store a price and then displays it.\n",
                "\n",
                "**Watch the video at timestamp 11:27**, then come back and type the EXACT code Mosh types:\n",
                "\n",
                "1. Create a variable named `price`\n",
                "2. Assign it the value `10`\n",
                "3. Print **the variable** (not the number \"10\" in quotes!)\n",
                "\n",
                "**Expected Output:**\n",
                "```\n",
                "10\n",
                "```\n",
                "\n",
                "⚠️ **Common Mistake:** Don't type `print(\"10\")` - that's printing the string \"10\", not the variable!  \n",
                "✅ **Correct Way:** Type `print(price)` - this prints the variable's value."
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
            "source": ["# Run this cell to check your work\nverify_task_1()"],
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
            "source": ["# Run this cell to check your work\nverify_task_2()"],
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
                "**Tips:**\n",
                "- Strings use quotes: `'Mosh'` or `\"Mosh\"`\n",
                "- Booleans are capitalized: `True` or `False`\n",
                "- Floats need a decimal point: `4.9`"
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
            "source": ["# Run this cell to check your work\nverify_task_3()"],
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
                "**Challenge:** After completing this task, try creating variables for yourself with your own name and age!"
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
            "source": ["# Run this cell to check your work\nverify_task_4()"],
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
                "  - `int` (integers): whole numbers like 10, 20, -5\n",
                "  - `float` (floats): decimal numbers like 4.9, 3.14\n",
                "  - `str` (strings): text in quotes like 'Mosh', \"Hello\"\n",
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
import os
os.chdir(r"g:\My Drive\Colab Notebooks\COSC1315\Sample Lessons")

with open("Lesson_03_Variables_WalkAlong.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("✅ Updated Lesson_03_Variables_WalkAlong.ipynb")
print("📊 Total cells: 15")
print("   - 1 Header")
print("   - 1 Setup/Import verification")
print("   - 4 Tasks (each with 3 cells)")
print("   - 1 Summary")
print("\n📁 Files created:")
print("   - Lesson_03_Variables_WalkAlong.ipynb")
print("   - lesson_03_verification.py")
print("\n🚀 Ready to upload BOTH files to Google Colab!")
