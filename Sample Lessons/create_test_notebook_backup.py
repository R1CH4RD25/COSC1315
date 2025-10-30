import json

# Create a simple test notebook
notebook = {
    "cells": [
        # Cell 1: Title
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Lesson 03: Variables - Test Notebook\n",
                "\n",
                "**Testing:** Specific vs Generic Verification\n",
                "\n",
                "---"
            ]
        },
        
        # Cell 2: Setup
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# ========================================\n",
                "# SETUP CELL - RUN THIS FIRST!\n",
                "# ========================================\n",
                "\n",
                "from google.colab import drive\n",
                "import sys\n",
                "import os\n",
                "import importlib\n",
                "\n",
                "# Mount Google Drive\n",
                "print(\"📂 Mounting Google Drive...\")\n",
                "drive.mount('/content/drive', force_remount=False)\n",
                "\n",
                "# Try multiple possible paths for the Verifications folder\n",
                "verification_paths = [\n",
                "    '/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications',\n",
                "    '/content/drive/.shortcut-targets-by-id/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT',\n",
                "    '/content/drive/Shareddrives/COSC1315/Lessons/Verifications',\n",
                "    '/content/drive/My Drive/COSC1315/Lessons/Verifications',\n",
                "]\n",
                "\n",
                "verification_path = None\n",
                "for path in verification_paths:\n",
                "    if os.path.exists(path):\n",
                "        verification_path = path\n",
                "        print(f\"✅ Found verification folder!\")\n",
                "        break\n",
                "\n",
                "if verification_path:\n",
                "    if verification_path not in sys.path:\n",
                "        sys.path.append(verification_path)\n",
                "    \n",
                "    try:\n",
                "        import lesson_03_verification\n",
                "        importlib.reload(lesson_03_verification)\n",
                "        from lesson_03_verification import (\n",
                "            verify_task_1,\n",
                "            verify_try_it_yourself,\n",
                "            verify_multiple_variables\n",
                "        )\n",
                "        print(\"✅ Verification system loaded!\")\n",
                "        print(\"📝 Ready to test!\")\n",
                "    except ImportError as e:\n",
                "        print(f\"❌ Error: {e}\")\n",
                "else:\n",
                "    print(\"❌ Could not find Verifications folder!\")\n",
                "    print(\"Link: https://drive.google.com/drive/folders/1rdngjz1JtlRMHz7X_S_rFBRLEzQgXqfT\")"
            ]
        },
        
        # Cell 3: Walk-Along Instructions
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## 📺 Walk-Along Task: Follow Mosh (10 points)\n",
                "\n",
                "**Watch Mosh's video at timestamp 11:27**\n",
                "\n",
                "Mosh will show you how to create a variable called `price` with value `10` and print it.\n",
                "\n",
                "**Your job:** Watch him code, then pause and type the same code yourself.\n",
                "\n",
                "⚠️ **Remember:** Type what you see in the video - don't skip ahead!\n",
                "\n",
                "---"
            ]
        },
        
        # Cell 4: Walk-Along Code
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Type your code below:\n",
                "\n"
            ]
        },
        
        # Cell 5: Walk-Along Verification
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Run this to check your work\n",
                "verify_task_1()"
            ]
        },
        
        # Cell 6: Try It Yourself Instructions
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## 🎯 Try It Yourself! (10 points)\n",
                "\n",
                "Now create YOUR OWN variable!\n",
                "\n",
                "**Your Task:**\n",
                "- Create a variable to store your favorite number\n",
                "- Print that variable\n",
                "\n",
                "**Requirements:**\n",
                "- ✅ Use a meaningful variable name (not just `x` or `num`)\n",
                "- ✅ Assign it any number you like\n",
                "- ✅ Print the variable (not the literal number)\n",
                "\n",
                "**Example Output:**\n",
                "```\n",
                "42\n",
                "```\n",
                "*(Your output will show whatever number you chose)*\n",
                "\n",
                "---"
            ]
        },
        
        # Cell 7: Try It Yourself Code
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Type your code below:\n",
                "# Create a variable with your favorite number and print it\n",
                "\n"
            ]
        },
        
        # Cell 8: Try It Yourself Verification
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Run this to check your work\n",
                "verify_try_it_yourself()"
            ]
        },
        
        # Cell 9: What's My Grade?
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n",
                "\n",
                "## 📊 What's My Grade?\n",
                "\n",
                "Run the cell below to calculate your grade for this lesson.\n",
                "\n",
                "**Total Points: 100**\n",
                "- Walk-Along Task: 20 points (10 points per requirement)\n",
                "- Try It Yourself: 40 points (detailed component grading)\n",
                "- Debugging: 40 points (detailed component grading)\n",
                "\n",
                "After running this, you can:\n",
                "- ✅ Submit if you're happy with your grade\n",
                "- 🔄 Go back and fix tasks to improve your grade\n",
                "\n",
                "---"
            ]
        },
        
        # Cell 10: Grade Calculator (Simple!)
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Calculate your grade\n",
                "calculate_grade()"
            ]
        },
        
        # Cell 11: Completion
                "total_points += task1_points\n",
                "print()\n",
                "\n",
                "# ========================================\n",
                "# Task 2: Try It Yourself (40 points total)\n",
                "# ========================================\n",
                "print(\"🎯 TRY IT YOURSELF (40 points possible)\")\n",
                "print(\"-\" * 60)\n",
                "\n",
                "task2_points = 0\n",
                "task2_max = 40\n",
                "\n",
                "try:\n",
                "    code = _get_previous_cell_code()\n",
                "    analysis = _analyze_code_structure(code) if code else {}\n",
                "    ns = get_ipython().user_ns\n",
                "    \n",
                "    # Component 1: Created at least one variable (10 points)\n",
                "    if analysis.get('has_assignment', False):\n",
                "        print(\"   ✅ Created a variable: +10 points\")\n",
                "        task2_points += 10\n",
                "    else:\n",
                "        print(\"   ❌ No variable created: 0 points\")\n",
                "    \n",
                "    # Component 2: Used print() function (10 points)\n",
                "    if analysis.get('has_print', False):\n",
                "        print(\"   ✅ Used print() function: +10 points\")\n",
                "        task2_points += 10\n",
                "    else:\n",
                "        print(\"   ❌ Did not use print(): 0 points\")\n",
                "    \n",
                "    # Component 3: Printed a variable (not literal) (15 points)\n",
                "    vars_in_print = analysis.get('variables_used_in_print', [])\n",
                "    if len(vars_in_print) > 0:\n",
                "        print(f\"   ✅ Printed variable '{vars_in_print[0]}': +15 points\")\n",
                "        task2_points += 15\n",
                "    else:\n",
                "        print(\"   ❌ Did not print a variable: 0 points\")\n",
                "    \n",
                "    # Component 4: No literals in print (5 points)\n",
                "    literals_in_print = analysis.get('literals_in_print', [])\n",
                "    if analysis.get('has_print', False) and len(literals_in_print) == 0:\n",
                "        print(\"   ✅ No literals in print (correct!): +5 points\")\n",
                "        task2_points += 5\n",
                "    elif len(literals_in_print) > 0:\n",
                "        print(\"   ❌ Used literal in print: 0 points\")\n",
                "    \n",
                "except Exception as e:\n",
                "    print(f\"   ⚠️  ERROR: Could not verify ({e})\")\n",
                "\n",
                "print(f\"\\n   📊 Try It Yourself Score: {task2_points}/{task2_max} points\")\n",
                "total_points += task2_points\n",
                "print()\n",
                "\n",
                "# ========================================\n",
                "# Task 3: Debugging (40 points) - PLACEHOLDER\n",
                "# ========================================\n",
                "print(\"🐛 DEBUGGING (40 points possible)\")\n",
                "print(\"-\" * 60)\n",
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
