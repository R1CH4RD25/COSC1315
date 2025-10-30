import json

# Minimal test notebook with collapsible sections
nb = {
    "cells": [
        # Title
        {"cell_type": "markdown", "metadata": {}, "source": [
            "# Lesson 03: Variables - TEST\n",
            "\n",
            "**Video Source:** Code with Mosh\n",
            "\n",
            "---\n"
        ]},
        
        # Objectives Section
        {"cell_type": "markdown", "metadata": {}, "source": [
            "## 📚 Objectives and Learning Goals\n",
            "\n",
            "Test notebook for component-based grading system.\n",
            "\n",
            "---\n"
        ]},
        
        # Setup Section Header
        {"cell_type": "markdown", "metadata": {}, "source": [
            "## ⚙️ Run This First - Setup\n",
            "\n",
            "**Instructions:** Click play ▶️ below and authorize Google Drive.\n",
            "\n",
            "---\n"
        ]},
        
        # Setup Code
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [
            "from google.colab import drive\n",
            "drive.mount('/content/drive')\n",
            "import sys, importlib\n",
            "verif_path='/content/drive/My Drive/Colab Notebooks/COSC1315/Lessons/Verifications'\n",
            "sys.path.insert(0,verif_path)\n",
            "import lesson_03_verification\n",
            "importlib.reload(lesson_03_verification)\n",
            "from lesson_03_verification import *\n",
            "print('✅ Setup complete!')"
        ]},
        
        # Walk-Along Section Header
        {"cell_type": "markdown", "metadata": {}, "source": [
            "---\n",
            "\n",
            "## 📺 Walk-Along Tasks\n",
            "\n",
            "**Total Points:** 20 points\n",
            "\n",
            "---\n"
        ]},
        
        # Walk-Along Task 1
        {"cell_type": "markdown", "metadata": {}, "source": ["### Walk-Along Task 1: Follow Mosh (20 pts)\n"]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["# Your code:\n"]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["verify_task_1()"]},
        
        # Try It Yourself Section Header
        {"cell_type": "markdown", "metadata": {}, "source": [
            "---\n",
            "\n",
            "## 🎯 Try It Yourself\n",
            "\n",
            "**Total Points:** 40 points\n",
            "\n",
            "---\n"
        ]},
        
        # Try It Yourself Task 1
        {"cell_type": "markdown", "metadata": {}, "source": ["### Try It Yourself 1: Create Your Own (40 pts)\n"]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["# Your code:\n"]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["verify_try_it_yourself()"]},
        
        # Grade Section Header
        {"cell_type": "markdown", "metadata": {}, "source": [
            "---\n",
            "\n",
            "## 📊 What's My Grade?\n",
            "\n",
            "**Total Points:** 100 (60 in this test notebook)\n",
            "\n",
            "Run the cell below to see your grade!\n",
            "\n",
            "---\n"
        ]},
        
        # Grade Calculator
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["calculate_grade()"]}
    ],
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
    "nbformat": 4,
    "nbformat_minor": 0
}

with open("g:/My Drive/Colab Notebooks/COSC1315/Sample Lessons/Lesson_03_Test_Verification.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2)

print("✅ Test notebook created!")
