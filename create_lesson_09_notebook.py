"""
Create complete Lesson 09: If Statements notebook
"""
import json

# Complete notebook structure
notebook = {
    "cells": [
        # Title
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# Lesson 09 — If Statements (58:16–1:06:24)"]
        },
        # Watch
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 🎥 Watch\n\n"
                "**Clip:** 58:16–1:06:24  \n"
                "**Video:** [Code with Mosh - Python for Beginners](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=3496s)\n\n"
                "**Focus:** Mosh teaches how to write if statements for decision-making in Python. You'll learn comparison operators, if-elif-else chains, and how to control program flow based on conditions."
            ]
        },
        # Objectives
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 📚 Objectives and Learning Goals\n\n"
                "By the end of this lesson, you will be able to:\n"
                "- Write basic if statements to make decisions in code\n"
                "- Use comparison operators (>, <, >=, <=, ==, !=) to create conditions\n"
                "- Build if-elif-else chains for multiple conditions\n"
                "- Apply proper indentation in conditional blocks\n"
                "- Solve real-world problems using conditional logic\n\n"
                "### Key Concepts:\n"
                "- **If Statement:** Executes code only if a condition is True\n"
                "- **Comparison Operators:** Test relationships between values\n"
                "- **Indentation:** Python uses indentation to define code blocks\n"
                "- **Elif:** Checks additional conditions if previous ones are False\n"
                "- **Else:** Runs when all previous conditions are False\n"
                "- **Boolean Values:** True or False results from comparisons"
            ]
        },
        # Setup header
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## ⚙️ Setup\n\n**Run this cell first!** It downloads the verification system from GitHub."]
        },
        # Setup code
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import urllib.request\n"
                "import os\n\n"
                "url = 'https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_09_verification.py'\n"
                "filename = 'lesson_09_verification.py'\n\n"
                "print('Downloading verification file...')\n"
                "urllib.request.urlretrieve(url, filename)\n\n"
                "# Verify download\n"
                "if os.path.exists(filename):\n"
                "    print(f'✅ Downloaded {filename} successfully!')\n"
                "    print(f'File size: {os.path.getsize(filename)} bytes')\n\n"
                "# Show current directory and files (for debugging)\n"
                "print(f'Current directory: {os.getcwd()}')\n"
                "print(f'Files in directory: {os.listdir()}')\n\n"
                "# Add current directory to Python path\n"
                "import sys\n"
                "if os.getcwd() not in sys.path:\n"
                "    sys.path.insert(0, os.getcwd())\n\n"
                "# Import verification functions\n"
                "from lesson_09_verification import (\n"
                "    verify_walk_along_1,\n"
                "    verify_walk_along_2,\n"
                "    verify_walk_along_3,\n"
                "    verify_try_it_1,\n"
                "    verify_try_it_2,\n"
                "    verify_try_it_3,\n"
                "    verify_debug_1,\n"
                "    verify_debug_2,\n"
                "    verify_debug_3,\n"
                "    calculate_grade\n"
                ")\n\n"
                "print('✅ Setup complete! You\\'re ready to start coding.')"
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
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.11.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Save to file
with open('Lessons/Lesson_09_If_Statements.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"✅ Created notebook with {len(notebook['cells'])} cells (partial - needs walk-along, try-it, debug sections)")
