import json

notebook = {
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {
            "provenance": [],
            "toc_visible": True
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
        {
            "cell_type": "markdown",
            "source": [
                "# Lesson 03: Variables - Walk-Along Tasks\\n",
                "\\n",
                "**Course:** COSC 1315 - Introduction to Computer Programming  \\n",
                "**Source:** Code with Mosh - Python for Beginners  \\n",
                "**Video Timestamp:** 11:27–18:16\\n",
                "\\n",
                "---\\n",
                "\\n",
                "## Instructions\\n",
                "\\n",
                "Watch the video and follow along with Mosh as he demonstrates each task. After watching him code, pause the video and type the code yourself in the cells below.\\n",
                "\\n",
                "**Important:** Run each cell using `Shift + Enter` or click the ▶️ play button to see your output.\\n",
                "\\n",
                "---"
            ],
            "metadata": {
                "id": "header"
            }
        },
        {
            "cell_type": "markdown",
            "source": [
                "## Task 1: Store and Display a Price\\n",
                "\\n",
                "**What Mosh Does:**  \\n",
                "Mosh creates a variable to store a price and then displays it.\\n",
                "\\n",
                "**Your Steps:**\\n",
                "1. Create a variable named `price`\\n",
                "2. Assign it the value `10`\\n",
                "3. Print the variable to see its value\\n",
                "\\n",
                "**Expected Output:**\\n",
                "```\\n",
                "10\\n",
                "```"
            ],
            "metadata": {
                "id": "task1-instructions"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "# Type your code below:\\n"
            ],
            "metadata": {
                "id": "task1-code"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                "# ✅ VERIFICATION CODE - Run this cell to check your work\\n",
                "try:\\n",
                "    # Check if variable exists\\n",
                "    if 'price' not in dir():\\n",
                "        print(\\"❌ Error: Variable 'price' not found.\\")\\n",
                "        print(\\"   Make sure you created a variable named 'price'\\")\\n",
                "    # Check if value is correct\\n",
                "    elif price != 10:\\n",
                "        print(f\\"❌ Error: Variable 'price' has value {price}, but should be 10\\")\\n",
                "    else:\\n",
                "        print(\\"✅ Perfect! You created the variable 'price' and assigned it the value 10.\\")\\n",
                "        print(\\"   Great job!\\")\\n",
                "except NameError:\\n",
                "    print(\\"❌ Error: Variable 'price' not found.\\")\\n",
                "    print(\\"   Did you run the code cell above? Make sure to execute it first.\\")"
            ],
            "metadata": {
                "id": "task1-verify"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "markdown",
            "source": [
                "---\\n",
                "\\n",
                "## Task 2: Update a Variable Value\\n",
                "\\n",
                "**What Mosh Does:**  \\n",
                "Mosh shows that you can change the value of a variable after creating it.\\n",
                "\\n",
                "**Your Steps:**\\n",
                "1. Create a variable `price` with value `10`\\n",
                "2. Change `price` to `20`\\n",
                "3. Print the updated value\\n",
                "\\n",
                "**Expected Output:**\\n",
                "```\\n",
                "20\\n",
                "```"
            ],
            "metadata": {
                "id": "task2-instructions"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "# Type your code below:\\n"
            ],
            "metadata": {
                "id": "task2-code"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                "# ✅ VERIFICATION CODE - Run this cell to check your work\\n",
                "try:\\n",
                "    if 'price' not in dir():\\n",
                "        print(\\"❌ Error: Variable 'price' not found.\\")\\n",
                "    elif price != 20:\\n",
                "        print(f\\"❌ Error: Variable 'price' has value {price}, but should be 20\\")\\n",
                "        print(\\"   Remember: You need to reassign the variable to change its value\\")\\n",
                "    else:\\n",
                "        print(\\"✅ Excellent! You successfully updated the variable 'price' to 20.\\")\\n",
                "        print(\\"   This shows that variables can be changed (they're 'variable'!)\\")\\n",
                "except NameError:\\n",
                "    print(\\"❌ Error: Variable 'price' not found.\\")"
            ],
            "metadata": {
                "id": "task2-verify"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "markdown",
            "source": [
                "---\\n",
                "\\n",
                "## Task 3: Work with Different Data Types\\n",
                "\\n",
                "**What Mosh Does:**  \\n",
                "Mosh demonstrates the four main data types in Python by creating variables of each type.\\n",
                "\\n",
                "**Your Steps:**\\n",
                "1. Create `price` as an integer with value `10`\\n",
                "2. Create `rating` as a float (decimal) with value `4.9`\\n",
                "3. Create `name` as a string with value `'Mosh'`\\n",
                "4. Create `is_published` as a boolean with value `True`\\n",
                "5. Print all four variables\\n",
                "\\n",
                "**Expected Output:**\\n",
                "```\\n",
                "10\\n",
                "4.9\\n",
                "Mosh\\n",
                "True\\n",
                "```\\n",
                "\\n",
                "**Tip:** Strings use quotes, booleans are True/False (capitalized), floats have decimals"
            ],
            "metadata": {
                "id": "task3-instructions"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "# Type your code below:\\n"
            ],
            "metadata": {
                "id": "task3-code"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                "# ✅ VERIFICATION CODE - Run this cell to check your work\\n",
                "errors = []\\n",
                "\\n",
                "try:\\n",
                "    # Check price\\n",
                "    if 'price' not in dir():\\n",
                "        errors.append(\\"Variable 'price' not found\\")\\n",
                "    elif price != 10:\\n",
                "        errors.append(f\\"Variable 'price' should be 10, got {price}\\")\\n",
                "    elif not isinstance(price, int):\\n",
                "        errors.append(f\\"Variable 'price' should be an integer (int), got {type(price).__name__}\\")\\n",
                "    \\n",
                "    # Check rating\\n",
                "    if 'rating' not in dir():\\n",
                "        errors.append(\\"Variable 'rating' not found\\")\\n",
                "    elif rating != 4.9:\\n",
                "        errors.append(f\\"Variable 'rating' should be 4.9, got {rating}\\")\\n",
                "    elif not isinstance(rating, float):\\n",
                "        errors.append(f\\"Variable 'rating' should be a float (decimal), got {type(rating).__name__}\\")\\n",
                "    \\n",
                "    # Check name\\n",
                "    if 'name' not in dir():\\n",
                "        errors.append(\\"Variable 'name' not found\\")\\n",
                "    elif name != 'Mosh':\\n",
                "        errors.append(f\\"Variable 'name' should be 'Mosh', got '{name}'\\")\\n",
                "    elif not isinstance(name, str):\\n",
                "        errors.append(f\\"Variable 'name' should be a string (str), got {type(name).__name__}\\")\\n",
                "    \\n",
                "    # Check is_published\\n",
                "    if 'is_published' not in dir():\\n",
                "        errors.append(\\"Variable 'is_published' not found\\")\\n",
                "    elif is_published != True:\\n",
                "        errors.append(f\\"Variable 'is_published' should be True, got {is_published}\\")\\n",
                "    elif not isinstance(is_published, bool):\\n",
                "        errors.append(f\\"Variable 'is_published' should be a boolean (bool), got {type(is_published).__name__}\\")\\n",
                "    \\n",
                "    if errors:\\n",
                "        print(\\"❌ Issues found:\\")\\n",
                "        for error in errors:\\n",
                "            print(f\\"   • {error}\\")\\n",
                "    else:\\n",
                "        print(\\"✅ Outstanding! You created all four data types correctly!\\")\\n",
                "        print(\\"   • Integer (int): whole numbers\\")\\n",
                "        print(\\"   • Float (float): decimal numbers\\")\\n",
                "        print(\\"   • String (str): text in quotes\\")\\n",
                "        print(\\"   • Boolean (bool): True or False\\")\\n",
                "        \\n",
                "except NameError as e:\\n",
                "    print(f\\"❌ Error: One or more variables not found.\\")\\n",
                "    print(f\\"   Details: {e}\\")"
            ],
            "metadata": {
                "id": "task3-verify"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "markdown",
            "source": [
                "---\\n",
                "\\n",
                "## Task 4: Patient Information System\\n",
                "\\n",
                "**What Mosh Does:**  \\n",
                "Mosh creates a simple system to store patient information using three variables.\\n",
                "\\n",
                "**Your Steps:**\\n",
                "1. Create a variable `name` with value `'John Smith'`\\n",
                "2. Create a variable `age` with value `20`\\n",
                "3. Create a variable `is_new` with value `True` (indicating a new patient)\\n",
                "4. Print all three variables\\n",
                "\\n",
                "**Expected Output:**\\n",
                "```\\n",
                "John Smith\\n",
                "20\\n",
                "True\\n",
                "```\\n",
                "\\n",
                "**Challenge:** Try creating variables for yourself with your own name and age!"
            ],
            "metadata": {
                "id": "task4-instructions"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "# Type your code below:\\n"
            ],
            "metadata": {
                "id": "task4-code"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "code",
            "source": [
                "# ✅ VERIFICATION CODE - Run this cell to check your work\\n",
                "errors = []\\n",
                "\\n",
                "try:\\n",
                "    # Check name\\n",
                "    if 'name' not in dir():\\n",
                "        errors.append(\\"Variable 'name' not found\\")\\n",
                "    elif name != 'John Smith':\\n",
                "        errors.append(f\\"Variable 'name' should be 'John Smith', got '{name}'\\")\\n",
                "    \\n",
                "    # Check age\\n",
                "    if 'age' not in dir():\\n",
                "        errors.append(\\"Variable 'age' not found\\")\\n",
                "    elif age != 20:\\n",
                "        errors.append(f\\"Variable 'age' should be 20, got {age}\\")\\n",
                "    \\n",
                "    # Check is_new\\n",
                "    if 'is_new' not in dir():\\n",
                "        errors.append(\\"Variable 'is_new' not found\\")\\n",
                "    elif is_new != True:\\n",
                "        errors.append(f\\"Variable 'is_new' should be True, got {is_new}\\")\\n",
                "    \\n",
                "    if errors:\\n",
                "        print(\\"❌ Issues found:\\")\\n",
                "        for error in errors:\\n",
                "            print(f\\"   • {error}\\")\\n",
                "    else:\\n",
                "        print(\\"✅ Perfect! You've completed the Patient Information System!\\")\\n",
                "        print(\\"   You now understand how to:\\")\\n",
                "        print(\\"   • Create variables with meaningful names\\")\\n",
                "        print(\\"   • Store different types of data\\")\\n",
                "        print(\\"   • Build simple information systems\\")\\n",
                "        print(\\"\\\\n🎉 Congratulations! You've completed all Walk-Along tasks for Lesson 03!\\")\\n",
                "        \\n",
                "except NameError as e:\\n",
                "    print(f\\"❌ Error: One or more variables not found.\\")\\n",
                "    print(f\\"   Details: {e}\\")"
            ],
            "metadata": {
                "id": "task4-verify"
            },
            "execution_count": None,
            "outputs": []
        },
        {
            "cell_type": "markdown",
            "source": [
                "---\\n",
                "\\n",
                "## 🎓 Summary\\n",
                "\\n",
                "In this lesson, you learned:\\n",
                "\\n",
                "✅ **Variables** store data in memory  \\n",
                "✅ **Assignment** uses the `=` operator  \\n",
                "✅ **Data Types** include:\\n",
                "   - `int` (integers): whole numbers\\n",
                "   - `float` (floats): decimal numbers\\n",
                "   - `str` (strings): text in quotes\\n",
                "   - `bool` (booleans): True or False\\n",
                "\\n",
                "✅ **Variables can be updated** by reassigning them  \\n",
                "✅ **Descriptive names** make code easier to understand\\n",
                "\\n",
                "---\\n",
                "\\n",
                "## 🚀 Next Steps\\n",
                "\\n",
                "Practice creating your own variables! Try:\\n",
                "- Your name, age, and whether you're a student\\n",
                "- A product name, price, and stock quantity\\n",
                "- A city name, population, and temperature\\n",
                "\\n",
                "**Ready for more?** Move on to Lesson 04: Receiving Input!"
            ],
            "metadata": {
                "id": "summary"
            }
        }
    ]
}

# Write the notebook
output_path = r"g:\My Drive\Colab Notebooks\COSC1315\Sample Lessons\Lesson_03_Variables_WalkAlong.ipynb"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print(f"✅ Created notebook: {output_path}")
