"""
Add Key Terms sections to Lesson notebooks 05-10
Inserts after the Objectives cell and before the Setup cell
"""

import json
from pathlib import Path

# Define Key Terms for each lesson
KEY_TERMS = {
    "05": {
        "title": "Type Conversion",
        "terms": [
            ("Type Conversion", "The process of changing a value from one data type to another."),
            ("int()", "Converts a string or number to an integer (whole number)."),
            ("float()", "Converts a string or number to a floating-point (decimal) value."),
            ("bool()", "Converts a value to a Boolean (`True` or `False`)."),
            ("type()", "Returns the data type (class) of a given value or variable."),
            ("TypeError", "An error that occurs when an operation uses mismatched data types."),
            ("String (str)", "A sequence of text characters enclosed in quotes."),
            ("Integer (int)", "A whole number without a decimal point."),
            ("Float (float)", "A number that includes a decimal point."),
            ("Debugging", "The process of finding and fixing errors in a program.")
        ]
    },
    "06": {
        "title": "Strings",
        "terms": [
            ("String", "A sequence of characters enclosed in quotes (single, double, or triple)."),
            ("Zero-based indexing", "A system where the first element in a sequence is at position 0."),
            ("Negative index", "An index that counts from the end of a string (-1 is the last character)."),
            ("Slicing", "Extracting a portion of a string using `[start:end]` notation."),
            ("String method", "A built-in function that performs operations on strings (e.g., `.upper()`, `.lower()`)."),
            ("F-string", "A formatted string literal that allows embedding expressions inside strings using `f\"...\"`"),
            ("Immutable", "Cannot be changed after creation; strings cannot be modified in place."),
            ("Substring", "A portion or section of a larger string."),
            ("IndexError", "An error that occurs when trying to access an index that doesn't exist."),
            ("Indexing", "Accessing individual characters in a string using square brackets `[position]`.")
        ]
    },
    "07": {
        "title": "Formatted Strings",
        "terms": [
            ("F-string (formatted string literal)", "A string prefixed with 'f' that allows embedding expressions: `f\"Hello {name}\"`"),
            ("String interpolation", "The process of inserting values into string placeholders."),
            ("Placeholder", "A spot in an f-string where a variable or expression will be inserted (inside `{}`)."),
            ("Expression", "Any valid Python code that produces a value (can be used inside f-string `{}`)."),
            ("Format specifier", "Special codes that control how values are displayed (e.g., `:.2f` for 2 decimals)."),
            ("Concatenation", "Joining strings together using the `+` operator."),
            ("Legacy string formatting", "Older methods like `%` formatting and `.format()` (still valid but less common)."),
            (".format() method", "An older string formatting method: `\"Hello {}\".format(name)`"),
            ("Escape sequence", "Special character combinations like `\\n` (newline) or `\\\"` (quote inside string)."),
            ("String literal", "Text written directly in code, enclosed in quotes.")
        ]
    },
    "08": {
        "title": "Arithmetic Operations",
        "terms": [
            ("Arithmetic operator", "A symbol used to perform mathematical calculations (+, -, *, /, //, %, **)."),
            ("Addition (+)", "Adds two numbers together or concatenates strings."),
            ("Subtraction (-)", "Subtracts the second number from the first."),
            ("Multiplication (*)", "Multiplies two numbers or repeats strings/lists."),
            ("Division (/)", "Divides two numbers and always returns a float (decimal result)."),
            ("Floor division (//)", "Divides two numbers and returns only the whole number part (rounds down)."),
            ("Modulus (%)", "Returns the remainder after division (e.g., `10 % 3` returns `1`)."),
            ("Exponentiation (**)", "Raises a number to a power (e.g., `2 ** 3` returns `8`)."),
            ("Order of operations (PEMDAS)", "The sequence Python follows to evaluate expressions: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction."),
            ("Integer division", "Division that produces a whole number result (using `//` operator).")
        ]
    },
    "09": {
        "title": "If Statements",
        "terms": [
            ("Conditional statement", "Code that executes different actions based on whether a condition is True or False."),
            ("if statement", "Executes a block of code only if a condition is True."),
            ("elif (else if)", "Checks an additional condition if the previous if/elif was False."),
            ("else clause", "Executes a block of code when all previous conditions are False."),
            ("Boolean expression", "An expression that evaluates to either True or False."),
            ("Comparison operator", "Symbols used to compare values: `==`, `!=`, `<`, `>`, `<=`, `>=`"),
            ("Indentation", "Spaces at the beginning of lines that define code blocks in Python (required!)."),
            ("Code block", "A group of statements that execute together (indented under if/elif/else)."),
            ("True/False", "The two Boolean values in Python (note the capitalization)."),
            ("Nested if statement", "An if statement inside another if statement (creates more complex logic).")
        ]
    },
    "10": {
        "title": "Logical Operators",
        "terms": [
            ("Logical operator", "Operators that combine multiple conditions: `and`, `or`, `not`"),
            ("and operator", "Returns True only if BOTH conditions are True."),
            ("or operator", "Returns True if AT LEAST ONE condition is True."),
            ("not operator", "Reverses a Boolean value (True becomes False, False becomes True)."),
            ("Boolean logic", "The system of combining True/False values using logical operators."),
            ("Truth table", "A table showing all possible combinations of True/False inputs and their results."),
            ("Short-circuit evaluation", "Python stops checking conditions as soon as the result is determined."),
            ("Compound condition", "Multiple conditions combined with logical operators."),
            ("Logical expression", "An expression using logical operators that evaluates to True or False."),
            ("Precedence", "The order in which operators are evaluated (`not` before `and` before `or`).")
        ]
    }
}

def create_key_terms_cell(lesson_num):
    """Create a Key Terms markdown cell"""
    terms_data = KEY_TERMS[lesson_num]

    content = [
        "## 📚 Key Terms\n",
        "\n",
        "Before starting this lesson, familiarize yourself with these important terms:\n",
        "\n"
    ]

    for i, (term, definition) in enumerate(terms_data["terms"], 1):
        content.append(f"{i}. **{term}** – {definition}\n")

    content.append("\n---")

    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": content
    }

def add_key_terms_to_notebook(lesson_num):
    """Add Key Terms section to a lesson notebook"""
    notebook_path = Path(f"Lessons/Lesson_{lesson_num}_{KEY_TERMS[lesson_num]['title'].replace(' ', '_')}.ipynb")

    if not notebook_path.exists():
        print(f"❌ {notebook_path} not found")
        return False

    # Read notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    # Find the Objectives cell
    objectives_index = None
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell.get('source', []))
            if '📚 Objectives' in source or 'Learning Goals' in source or 'Objectives and Learning Goals' in source:
                objectives_index = i
                break

    if objectives_index is None:
        print(f"❌ Could not find Objectives cell in {notebook_path.name}")
        return False

    # Check if Key Terms already exists
    if objectives_index + 1 < len(notebook['cells']):
        next_cell = notebook['cells'][objectives_index + 1]
        if next_cell['cell_type'] == 'markdown':
            source = ''.join(next_cell.get('source', []))
            if 'Key Terms' in source:
                print(f"⚠️  {notebook_path.name} already has Key Terms section - skipping")
                return False

    # Create Key Terms cell
    key_terms_cell = create_key_terms_cell(lesson_num)

    # Insert after Objectives
    notebook['cells'].insert(objectives_index + 1, key_terms_cell)

    # Save backup
    backup_path = notebook_path.with_name(notebook_path.stem + "_backup_before_keyterms.ipynb")
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)
    print(f"  📦 Backup saved: {backup_path.name}")

    # Save modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2)

    print(f"✅ Added Key Terms to {notebook_path.name}")
    return True

def main():
    """Add Key Terms to all lesson notebooks"""
    print("=" * 80)
    print("ADDING KEY TERMS SECTIONS TO LESSON NOTEBOOKS")
    print("=" * 80)
    print()

    added_count = 0
    for lesson_num in ["05", "06", "07", "08", "09", "10"]:
        print(f"\nLesson {lesson_num}:")
        if add_key_terms_to_notebook(lesson_num):
            added_count += 1

    print("\n" + "=" * 80)
    print(f"COMPLETE: Added Key Terms to {added_count}/6 lessons")
    print("=" * 80)

if __name__ == "__main__":
    main()
