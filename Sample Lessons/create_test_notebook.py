#!/usr/bin/env python3import json

"""Create a test notebook for Lesson 03 verification system"""

# Create a simple test notebook

import jsonnotebook = {

    "cells": [

notebook = {        # Cell 1: Title

    "cells": [        {

        # Cell 1: Title            "cell_type": "markdown",

        {            "metadata": {},

            "cell_type": "markdown",            "source": [

            "metadata": {},                "# Lesson 03: Variables - Test Notebook\n",

            "source": [                "\n",

                "# Lesson 03: Variables - TEST NOTEBOOK\n",                "**Testing:** Specific vs Generic Verification\n",

                "\n",                "\n",

                "This is a simplified test notebook to validate the verification system.\n",                "---"

                "\n",            ]

                "**Contents:**\n",        },

                "- 1 Walk-Along Task (specific verification)\n",        

                "- 1 Try It Yourself Task (generic verification)\n",        # Cell 2: Setup

                "- Component-based grading system\n",        {

                "\n",            "cell_type": "code",

                "---"            "execution_count": None,

            ]            "metadata": {},

        },            "outputs": [],

                    "source": [

        # Cell 2: Setup                "# ========================================\n",

        {                "# SETUP CELL - RUN THIS FIRST!\n",

            "cell_type": "code",                "# ========================================\n",

            "execution_count": None,                "\n",

            "metadata": {},                "from google.colab import drive\n",

            "outputs": [],                "import sys\n",

            "source": [                "import os\n",

                "# Setup: Mount Google Drive and import verification functions\n",                "import importlib\n",

                "from google.colab import drive\n",                "\n",

                "drive.mount('/content/drive')\n",                "# Mount Google Drive\n",

                "\n",                "print(\"📂 Mounting Google Drive...\")\n",

                "import sys\n",                "drive.mount('/content/drive', force_remount=False)\n",

                "import importlib\n",                "\n",

                "\n",                "# Try multiple possible paths for the Verifications folder\n",

                "# Add verification folder to path\n",                "verification_paths = [\n",

                "verif_path = '/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications'\n",                "    '/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications',\n",

                "if verif_path not in sys.path:\n",                "    '/content/drive/.shortcut-targets-by-id/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT',\n",

                "    sys.path.insert(0, verif_path)\n",                "    '/content/drive/Shareddrives/COSC1315/Lessons/Verifications',\n",

                "\n",                "    '/content/drive/My Drive/COSC1315/Lessons/Verifications',\n",

                "# Import and reload verification module\n",                "]\n",

                "import lesson_03_verification\n",                "\n",

                "importlib.reload(lesson_03_verification)\n",                "verification_path = None\n",

                "\n",                "for path in verification_paths:\n",

                "# Import the functions we'll use\n",                "    if os.path.exists(path):\n",

                "from lesson_03_verification import (\n",                "        verification_path = path\n",

                "    verify_task_1,\n",                "        print(f\"✅ Found verification folder!\")\n",

                "    verify_try_it_yourself,\n",                "        break\n",

                "    _get_previous_cell_code,\n",                "\n",

                "    _check_code_uses_variable,\n",                "if verification_path:\n",

                "    _analyze_code_structure,\n",                "    if verification_path not in sys.path:\n",

                "    calculate_grade\n",                "        sys.path.append(verification_path)\n",

                ")\n",                "    \n",

                "\n",                "    try:\n",

                "print(\"✅ Setup complete! Ready to start the lesson.\")"                "        import lesson_03_verification\n",

            ]                "        importlib.reload(lesson_03_verification)\n",

        },                "        from lesson_03_verification import (\n",

                        "            verify_task_1,\n",

        # Cell 3: Walk-Along Instructions                "            verify_try_it_yourself,\n",

        {                "            verify_multiple_variables\n",

            "cell_type": "markdown",                "        )\n",

            "metadata": {},                "        print(\"✅ Verification system loaded!\")\n",

            "source": [                "        print(\"📝 Ready to test!\")\n",

                "---\n",                "    except ImportError as e:\n",

                "\n",                "        print(f\"❌ Error: {e}\")\n",

                "## 📺 Walk-Along Task: Follow Mosh (20 points)\n",                "else:\n",

                "\n",                "    print(\"❌ Could not find Verifications folder!\")\n",

                "**Video:** [Python Tutorial - Variables (11:27)](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=11m27s)\n",                "    print(\"Link: https://drive.google.com/drive/folders/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT\")"

                "\n",            ]

                "### What to Do:\n",        },

                "\n",        

                "Watch Mosh's video at timestamp 11:27. Mosh will show you how to create a variable called `price` and assign it the value `10`, then print the variable.\n",        # Cell 3: Walk-Along Instructions

                "\n",        {

                "**Your job:** Watch him code, then pause and type the same code yourself.\n",            "cell_type": "markdown",

                "\n",            "metadata": {},

                "⚠️ **Remember:** Type what you see in the video - don't skip ahead!\n",            "source": [

                "\n",                "---\n",

                "---"                "\n",

            ]                "## 📺 Walk-Along Task: Follow Mosh (10 points)\n",

        },                "\n",

                        "**Watch Mosh's video at timestamp 11:27**\n",

        # Cell 4: Walk-Along Code                "\n",

        {                "Mosh will show you how to create a variable called `price` with value `10` and print it.\n",

            "cell_type": "code",                "\n",

            "execution_count": None,                "**Your job:** Watch him code, then pause and type the same code yourself.\n",

            "metadata": {},                "\n",

            "outputs": [],                "⚠️ **Remember:** Type what you see in the video - don't skip ahead!\n",

            "source": [                "\n",

                "# Type your code below:\n",                "---"

                "# Follow Mosh and create the price variable\n",            ]

                "\n"        },

            ]        

        },        # Cell 4: Walk-Along Code

                {

        # Cell 5: Walk-Along Verification            "cell_type": "code",

        {            "execution_count": None,

            "cell_type": "code",            "metadata": {},

            "execution_count": None,            "outputs": [],

            "metadata": {},            "source": [

            "outputs": [],                "# Type your code below:\n",

            "source": [                "\n"

                "# Run this to check your work\n",            ]

                "verify_task_1()"        },

            ]        

        },        # Cell 5: Walk-Along Verification

                {

        # Cell 6: Try It Yourself Instructions            "cell_type": "code",

        {            "execution_count": None,

            "cell_type": "markdown",            "metadata": {},

            "metadata": {},            "outputs": [],

            "source": [            "source": [

                "---\n",                "# Run this to check your work\n",

                "\n",                "verify_task_1()"

                "## 🎯 Try It Yourself! (40 points)\n",            ]

                "\n",        },

                "Now it's your turn to create your own variable!\n",        

                "\n",        # Cell 6: Try It Yourself Instructions

                "### Requirements:\n",        {

                "1. Create a variable with YOUR OWN name (not `price`)\n",            "cell_type": "markdown",

                "2. Assign it ANY number you want\n",            "metadata": {},

                "3. Print the variable using `print()`\n",            "source": [

                "\n",                "---\n",

                "### Example Output:\n",                "\n",

                "```\n",                "## 🎯 Try It Yourself! (10 points)\n",

                "42\n",                "\n",

                "```\n",                "Now create YOUR OWN variable!\n",

                "*(Your output will show whatever number you chose)*\n",                "\n",

                "\n",                "**Your Task:**\n",

                "---"                "- Create a variable to store your favorite number\n",

            ]                "- Print that variable\n",

        },                "\n",

                        "**Requirements:**\n",

        # Cell 7: Try It Yourself Code                "- ✅ Use a meaningful variable name (not just `x` or `num`)\n",

        {                "- ✅ Assign it any number you like\n",

            "cell_type": "code",                "- ✅ Print the variable (not the literal number)\n",

            "execution_count": None,                "\n",

            "metadata": {},                "**Example Output:**\n",

            "outputs": [],                "```\n",

            "source": [                "42\n",

                "# Type your code below:\n",                "```\n",

                "# Create a variable with your favorite number and print it\n",                "*(Your output will show whatever number you chose)*\n",

                "\n"                "\n",

            ]                "---"

        },            ]

                },

        # Cell 8: Try It Yourself Verification        

        {        # Cell 7: Try It Yourself Code

            "cell_type": "code",        {

            "execution_count": None,            "cell_type": "code",

            "metadata": {},            "execution_count": None,

            "outputs": [],            "metadata": {},

            "source": [            "outputs": [],

                "# Run this to check your work\n",            "source": [

                "verify_try_it_yourself()"                "# Type your code below:\n",

            ]                "# Create a variable with your favorite number and print it\n",

        },                "\n"

                    ]

        # Cell 9: What's My Grade?        },

        {        

            "cell_type": "markdown",        # Cell 8: Try It Yourself Verification

            "metadata": {},        {

            "source": [            "cell_type": "code",

                "---\n",            "execution_count": None,

                "\n",            "metadata": {},

                "## 📊 What's My Grade?\n",            "outputs": [],

                "\n",            "source": [

                "Run the cell below to calculate your grade for this lesson.\n",                "# Run this to check your work\n",

                "\n",                "verify_try_it_yourself()"

                "**Total Points: 100**\n",            ]

                "- Walk-Along Task: 20 points (5 points per component)\n",        },

                "- Try It Yourself: 40 points (detailed component grading)\n",        

                "- Debugging: 40 points (not in this test notebook)\n",        # Cell 9: What's My Grade?

                "\n",        {

                "After running this, you can:\n",            "cell_type": "markdown",

                "- ✅ Submit if you're happy with your grade\n",            "metadata": {},

                "- 🔄 Go back and fix tasks to improve your grade\n",            "source": [

                "\n",                "---\n",

                "---"                "\n",

            ]                "## 📊 What's My Grade?\n",

        },                "\n",

                        "Run the cell below to calculate your grade for this lesson.\n",

        # Cell 10: Grade Calculator (SIMPLE!)                "\n",

        {                "**Total Points: 100**\n",

            "cell_type": "code",                "- Walk-Along Task: 20 points (10 points per requirement)\n",

            "execution_count": None,                "- Try It Yourself: 40 points (detailed component grading)\n",

            "metadata": {},                "- Debugging: 40 points (detailed component grading)\n",

            "outputs": [],                "\n",

            "source": [                "After running this, you can:\n",

                "# Calculate your grade\n",                "- ✅ Submit if you're happy with your grade\n",

                "calculate_grade()"                "- 🔄 Go back and fix tasks to improve your grade\n",

            ]                "\n",

        },                "---"

                    ]

        # Cell 11: Completion        },

        {        

            "cell_type": "markdown",        # Cell 10: Grade Calculator (Simple!)

            "metadata": {},        {

            "source": [            "cell_type": "code",

                "---\n",            "execution_count": None,

                "\n",            "metadata": {},

                "## 🎉 Lesson Complete!\n",            "outputs": [],

                "\n",            "source": [

                "### What You Learned:\n",                "# Calculate your grade\n",

                "\n",                "calculate_grade()"

                "**Walk-Along (Specific Verification):**\n",            ]

                "- ✅ Following Mosh's exact instructions\n",        },

                "- ✅ Creating variables with specific names and values\n",        

                "- ✅ Printing variables correctly\n",        # Cell 11: Completion

                "\n",                "total_points += task1_points\n",

                "**Try It Yourself (Generic Verification):**\n",                "print()\n",

                "- ✅ Creating your own variables\n",                "\n",

                "- ✅ Using meaningful variable names\n",                "# ========================================\n",

                "- ✅ Understanding variables vs literals\n",                "# Task 2: Try It Yourself (40 points total)\n",

                "\n",                "# ========================================\n",

                "---\n",                "print(\"🎯 TRY IT YOURSELF (40 points possible)\")\n",

                "\n",                "print(\"-\" * 60)\n",

                "## 🚀 Next Steps:\n",                "\n",

                "\n",                "task2_points = 0\n",

                "1. ✅ Check your grade above\n",                "task2_max = 40\n",

                "2. 🔄 If needed, go back and improve your work\n",                "\n",

                "3. 💾 Save this notebook (File → Save)\n",                "try:\n",

                "4. 📤 Submit when ready\n",                "    code = _get_previous_cell_code()\n",

                "\n",                "    analysis = _analyze_code_structure(code) if code else {}\n",

                "---\n",                "    ns = get_ipython().user_ns\n",

                "\n",                "    \n",

                "**Questions?** Ask your instructor for help!\n"                "    # Component 1: Created at least one variable (10 points)\n",

            ]                "    if analysis.get('has_assignment', False):\n",

        }                "        print(\"   ✅ Created a variable: +10 points\")\n",

    ],                "        task2_points += 10\n",

    "metadata": {                "    else:\n",

        "kernelspec": {                "        print(\"   ❌ No variable created: 0 points\")\n",

            "display_name": "Python 3",                "    \n",

            "language": "python",                "    # Component 2: Used print() function (10 points)\n",

            "name": "python3"                "    if analysis.get('has_print', False):\n",

        },                "        print(\"   ✅ Used print() function: +10 points\")\n",

        "language_info": {                "        task2_points += 10\n",

            "codemirror_mode": {                "    else:\n",

                "name": "ipython",                "        print(\"   ❌ Did not use print(): 0 points\")\n",

                "version": 3                "    \n",

            },                "    # Component 3: Printed a variable (not literal) (15 points)\n",

            "file_extension": ".py",                "    vars_in_print = analysis.get('variables_used_in_print', [])\n",

            "mimetype": "text/x-python",                "    if len(vars_in_print) > 0:\n",

            "name": "python",                "        print(f\"   ✅ Printed variable '{vars_in_print[0]}': +15 points\")\n",

            "nbconvert_exporter": "python",                "        task2_points += 15\n",

            "pygments_lexer": "ipython3",                "    else:\n",

            "version": "3.10.12"                "        print(\"   ❌ Did not print a variable: 0 points\")\n",

        }                "    \n",

    },                "    # Component 4: No literals in print (5 points)\n",

    "nbformat": 4,                "    literals_in_print = analysis.get('literals_in_print', [])\n",

    "nbformat_minor": 0                "    if analysis.get('has_print', False) and len(literals_in_print) == 0:\n",

}                "        print(\"   ✅ No literals in print (correct!): +5 points\")\n",

                "        task2_points += 5\n",

# Write notebook to file                "    elif len(literals_in_print) > 0:\n",

output_path = "g:/My Drive/Colab Notebooks/COSC1315/Sample Lessons/Lesson_03_Test_Verification.ipynb"                "        print(\"   ❌ Used literal in print: 0 points\")\n",

                "    \n",

with open(output_path, 'w', encoding='utf-8') as f:                "except Exception as e:\n",

    json.dump(notebook, f, indent=2, ensure_ascii=False)                "    print(f\"   ⚠️  ERROR: Could not verify ({e})\")\n",

                "\n",

print("✅ Test notebook created!")                "print(f\"\\n   📊 Try It Yourself Score: {task2_points}/{task2_max} points\")\n",

print(f"📁 Location: {output_path}")                "total_points += task2_points\n",

print()                "print()\n",

print("🧪 This notebook has:")                "\n",

print("  - 1 Walk-Along task (specific verification)")                "# ========================================\n",

print("  - 1 Try It Yourself task (generic verification)")                "# Task 3: Debugging (40 points) - PLACEHOLDER\n",

print("  - Simple grading system (just call calculate_grade())")                "# ========================================\n",

print()                "print(\"🐛 DEBUGGING (40 points possible)\")\n",

print("📝 Next: Open it in Google Colab and test!")                "print(\"-\" * 60)\n",

                "print(\"   ⚠️  No debugging task in this test notebook\")\n",
                "print(\"   📊 Debugging Score: 0/40 points (not included)\")\n",
                "task3_points = 0\n",
                "task3_max = 40\n",
                "# Note: In full lesson, would have 40 points from debugging section\n",
                "# For this test, we're only grading the first 60 points\n",
                "max_points = task1_max + task2_max  # 60 for this test\n",
                "print()\n",
                "\n",
                "# ========================================\n",
                "# FINAL GRADE CALCULATION\n",
                "# ========================================\n",
                "print(\"=\"*60)\n",
                "print(f\"📈 TOTAL SCORE: {total_points}/{max_points} points\")\n",
                "\n",
                "percentage = (total_points / max_points) * 100\n",
                "print(f\"📊 PERCENTAGE: {percentage:.1f}%\")\n",
                "\n",
                "# Letter grade\n",
                "if percentage >= 90:\n",
                "    letter_grade = \"A\"\n",
                "    emoji = \"🌟\"\n",
                "elif percentage >= 80:\n",
                "    letter_grade = \"B\"\n",
                "    emoji = \"😊\"\n",
                "elif percentage >= 70:\n",
                "    letter_grade = \"C\"\n",
                "    emoji = \"😐\"\n",
                "elif percentage >= 60:\n",
                "    letter_grade = \"D\"\n",
                "    emoji = \"😟\"\n",
                "else:\n",
                "    letter_grade = \"F\"\n",
                "    emoji = \"😞\"\n",
                "\n",
                "print(f\"📝 LETTER GRADE: {letter_grade} {emoji}\")\n",
                "print(\"=\"*60)\n",
                "print()\n",
                "\n",
                "# Detailed feedback\n",
                "if total_points == max_points:\n",
                "    print(\"🎉 PERFECT SCORE! Excellent work!\")\n",
                "    print(\"✅ You're ready to submit this lesson.\")\n",
                "elif total_points >= max_points * 0.8:\n",
                "    print(\"👍 Great job! You're doing well!\")\n",
                "    if task1_points < task1_max:\n",
                "        print(f\"💡 Walk-Along: You earned {task1_points}/{task1_max} points\")\n",
                "    if task2_points < task2_max:\n",
                "        print(f\"💡 Try It Yourself: You earned {task2_points}/{task2_max} points\")\n",
                "elif total_points >= max_points * 0.6:\n",
                "    print(\"😐 You passed, but there's room for improvement!\")\n",
                "    if task1_points < task1_max:\n",
                "        print(f\"� Walk-Along needs work: {task1_points}/{task1_max} points\")\n",
                "    if task2_points < task2_max:\n",
                "        print(f\"📚 Try It Yourself needs work: {task2_points}/{task2_max} points\")\n",
                "else:\n",
                "    print(\"📚 Keep working! You can do better!\")\n",
                "    print(\"🔄 Go back and complete the tasks that failed\")\n",
                "    print(\"💪 Then run this cell again to see your new grade\")\n",
                "    print()\n",
                "    if task1_points == 0:\n",
                "        print(\"⚠️  Walk-Along: No points earned - start here!\")\n",
                "    if task2_points == 0:\n",
                "        print(\"⚠️  Try It Yourself: No points earned - review requirements!\")\n",
                "\n",
                "print()\n",
                "print(\"💾 When you're happy with your grade, save and submit this notebook.\")\n",
                "print(\"🔄 You can revise your work and run this grader again anytime!\")"
            ]
        },
        
        # Cell 11: Completion
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## 🎉 Lesson Complete!\n",
                "\n",
                "### What You Learned:\n",
                "\n",
                "**Walk-Along (Specific Verification):**\n",
                "- ✅ Following Mosh's exact instructions\n",
                "- ✅ Creating variables with specific names and values\n",
                "- ✅ Printing variables correctly\n",
                "\n",
                "**Try It Yourself (Generic Verification):**\n",
                "- ✅ Creating your own variables\n",
                "- ✅ Using meaningful variable names\n",
                "- ✅ Understanding variables vs literals\n",
                "\n",
                "---\n",
                "\n",
                "## 🚀 Next Steps:\n",
                "\n",
                "1. ✅ Check your grade above\n",
                "2. 🔄 If needed, go back and improve your work\n",
                "3. 💾 Save this notebook (File → Save)\n",
                "4. 📤 Submit when ready\n",
                "\n",
                "---\n",
                "\n",
                "**Questions?** Ask your instructor for help!\n"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.10.0"
        },
        "colab": {
            "provenance": [],
            "name": "Lesson_03_Test_Verification.ipynb"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 0
}

# Write the notebook
output_path = "g:/My Drive/Colab Notebooks/COSC1315/Sample Lessons/Lesson_03_Test_Verification.ipynb"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)

print("✅ Test notebook created!")
print(f"📁 Location: {output_path}")
print("\n🧪 This notebook has:")
print("  - 1 Walk-Along task (specific verification)")
print("  - 1 Try It Yourself task (generic verification)")
print("  - Clear instructions for testing both")
print("\n📝 Next: Open it in Google Colab and test!")
