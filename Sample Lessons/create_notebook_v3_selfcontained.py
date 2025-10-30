import json
import os

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
                "**Important:** \n",
                "- Run the setup cell below (Cell 2) FIRST\n",
                "- Type the EXACT code that Mosh types (don't skip steps!)\n",
                "- Use `Shift + Enter` to run each cell\n",
                "- Run verification cells to check your work\n",
                "\n",
                "---"
            ]
        },
        # Setup - Verification Functions (Hidden from students conceptually)
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "# ========================================\n",
                "# SETUP CELL - RUN THIS FIRST!\n",
                "# ========================================\n",
                "# This cell loads the verification functions.\n",
                "# You only need to run it once at the start.\n",
                "\n",
                "def verify_task_1():\n",
                "    \"\"\"Verify Task 1: Store and Display a Price\"\"\"\n",
                "    if 'price' not in globals():\n",
                "        print(\"❌ Error: Variable 'price' not found.\")\n",
                "        print(\"💡 Hint: Create a variable named 'price' and assign it the value 10\")\n",
                "        return False\n",
                "    \n",
                "    price_value = globals()['price']\n",
                "    if price_value != 10:\n",
                "        print(f\"❌ Error: Variable 'price' has value {price_value}, but should be 10\")\n",
                "        return False\n",
                "    \n",
                "    print(\"✅ Perfect! You created the variable 'price' and assigned it the value 10.\")\n",
                "    print(\"✅ Great job!\")\n",
                "    return True\n",
                "\n",
                "def verify_task_2():\n",
                "    \"\"\"Verify Task 2: Update a Variable Value\"\"\"\n",
                "    if 'price' not in globals():\n",
                "        print(\"❌ Error: Variable 'price' not found.\")\n",
                "        print(\"💡 Hint: Create price = 10, then update it to price = 20\")\n",
                "        return False\n",
                "    \n",
                "    price_value = globals()['price']\n",
                "    if price_value != 20:\n",
                "        print(f\"❌ Error: Variable 'price' has value {price_value}, but should be 20\")\n",
                "        print(\"💡 Hint: Remember to reassign the variable: price = 20\")\n",
                "        return False\n",
                "    \n",
                "    print(\"✅ Excellent! You successfully updated the variable 'price' to 20.\")\n",
                "    print(\"✅ This shows that variables can be changed!\")\n",
                "    return True\n",
                "\n",
                "def verify_task_3():\n",
                "    \"\"\"Verify Task 3: Work with Different Data Types\"\"\"\n",
                "    errors = []\n",
                "    \n",
                "    # Check price\n",
                "    if 'price' not in globals():\n",
                "        errors.append(\"❌ Variable 'price' not found\")\n",
                "    else:\n",
                "        price_value = globals()['price']\n",
                "        if price_value != 10:\n",
                "            errors.append(f\"❌ price should be 10, got {price_value}\")\n",
                "        elif not isinstance(price_value, int):\n",
                "            errors.append(f\"❌ price should be an integer (int), got {type(price_value).__name__}\")\n",
                "    \n",
                "    # Check rating\n",
                "    if 'rating' not in globals():\n",
                "        errors.append(\"❌ Variable 'rating' not found\")\n",
                "    else:\n",
                "        rating_value = globals()['rating']\n",
                "        if rating_value != 4.9:\n",
                "            errors.append(f\"❌ rating should be 4.9, got {rating_value}\")\n",
                "        elif not isinstance(rating_value, float):\n",
                "            errors.append(f\"❌ rating should be a float, got {type(rating_value).__name__}\")\n",
                "    \n",
                "    # Check name\n",
                "    if 'name' not in globals():\n",
                "        errors.append(\"❌ Variable 'name' not found\")\n",
                "    else:\n",
                "        name_value = globals()['name']\n",
                "        if name_value != 'Mosh':\n",
                "            errors.append(f\"❌ name should be 'Mosh', got '{name_value}'\")\n",
                "        elif not isinstance(name_value, str):\n",
                "            errors.append(f\"❌ name should be a string (str), got {type(name_value).__name__}\")\n",
                "    \n",
                "    # Check is_published\n",
                "    if 'is_published' not in globals():\n",
                "        errors.append(\"❌ Variable 'is_published' not found\")\n",
                "    else:\n",
                "        is_published_value = globals()['is_published']\n",
                "        if is_published_value != True:\n",
                "            errors.append(f\"❌ is_published should be True, got {is_published_value}\")\n",
                "        elif not isinstance(is_published_value, bool):\n",
                "            errors.append(f\"❌ is_published should be a boolean (bool), got {type(is_published_value).__name__}\")\n",
                "    \n",
                "    if errors:\n",
                "        print(\"Issues found:\")\n",
                "        for error in errors:\n",
                "            print(f\"  {error}\")\n",
                "        print(\"\\n💡 Hint: Make sure you create all four variables with the correct types:\")\n",
                "        print(\"  • price = 10 (integer)\")\n",
                "        print(\"  • rating = 4.9 (float with decimal)\")\n",
                "        print(\"  • name = 'Mosh' (string with quotes)\")\n",
                "        print(\"  • is_published = True (boolean, capitalized)\")\n",
                "        return False\n",
                "    \n",
                "    print(\"✅ Outstanding! You created all four data types correctly!\")\n",
                "    print(\"  ✓ Integer (int): whole numbers\")\n",
                "    print(\"  ✓ Float (float): decimal numbers\")\n",
                "    print(\"  ✓ String (str): text in quotes\")\n",
                "    print(\"  ✓ Boolean (bool): True or False\")\n",
                "    return True\n",
                "\n",
                "def verify_task_4():\n",
                "    \"\"\"Verify Task 4: Patient Information System\"\"\"\n",
                "    errors = []\n",
                "    \n",
                "    # Check name\n",
                "    if 'name' not in globals():\n",
                "        errors.append(\"❌ Variable 'name' not found\")\n",
                "    else:\n",
                "        name_value = globals()['name']\n",
                "        if name_value != 'John Smith':\n",
                "            errors.append(f\"❌ name should be 'John Smith', got '{name_value}'\")\n",
                "    \n",
                "    # Check age\n",
                "    if 'age' not in globals():\n",
                "        errors.append(\"❌ Variable 'age' not found\")\n",
                "    else:\n",
                "        age_value = globals()['age']\n",
                "        if age_value != 20:\n",
                "            errors.append(f\"❌ age should be 20, got {age_value}\")\n",
                "    \n",
                "    # Check is_new\n",
                "    if 'is_new' not in globals():\n",
                "        errors.append(\"❌ Variable 'is_new' not found\")\n",
                "    else:\n",
                "        is_new_value = globals()['is_new']\n",
                "        if is_new_value != True:\n",
                "            errors.append(f\"❌ is_new should be True, got {is_new_value}\")\n",
                "    \n",
                "    if errors:\n",
                "        print(\"Issues found:\")\n",
                "        for error in errors:\n",
                "            print(f\"  {error}\")\n",
                "        print(\"\\n💡 Hint: Create the three variables for the patient information system:\")\n",
                "        print(\"  • name = 'John Smith'\")\n",
                "        print(\"  • age = 20\")\n",
                "        print(\"  • is_new = True\")\n",
                "        return False\n",
                "    \n",
                "    print(\"✅ Perfect! You've completed the Patient Information System!\")\n",
                "    print(\"✅ You now understand how to:\")\n",
                "    print(\"  • Create variables with meaningful names\")\n",
                "    print(\"  • Store different types of data\")\n",
                "    print(\"  • Build simple information systems\")\n",
                "    print(\"\\n🎉 Congratulations! You've completed all Walk-Along tasks for Lesson 03!\")\n",
                "    return True\n",
                "\n",
                "print(\"✅ Verification system loaded!\")\n",
                "print(\"📝 You're ready to start the Walk-Along tasks.\")\n",
                "print(\"\\n💡 Tip: Scroll down to Task 1 and start coding!\")"
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
with open("Lesson_03_Variables_WalkAlong.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print("✅ Created self-contained Lesson_03_Variables_WalkAlong.ipynb")
print("📊 Total cells: 15")
print("   - 1 Header")
print("   - 1 Setup (verification functions embedded)")
print("   - 4 Tasks (each with 3 cells)")
print("   - 1 Summary")
print("\n✨ Benefits:")
print("   ✓ No external files needed")
print("   ✓ No imports required")
print("   ✓ Self-contained - works anywhere")
print("   ✓ Students just run Cell 2 once and they're ready!")
print("\n🚀 Ready to upload to Google Colab!")
