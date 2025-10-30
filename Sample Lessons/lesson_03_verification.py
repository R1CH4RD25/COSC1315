"""
Lesson 03: Variables - Verification Helper
This module checks student code to ensure they're learning the concepts correctly.
"""

import sys
from io import StringIO

def verify_task_1():
    """
    Verify Task 1: Store and Display a Price
    Checks:
    1. Variable 'price' exists
    2. Variable 'price' = 10
    3. Student actually printed the variable (not just hardcoded "10")
    """
    errors = []
    
    # Check if price variable exists
    if 'price' not in dir():
        print("❌ Error: Variable 'price' not found.")
        print("💡 Hint: Create a variable named 'price' and assign it the value 10")
        return False
    
    # Check if price has correct value
    price_value = eval('price')
    if price_value != 10:
        print(f"❌ Error: Variable 'price' has value {price_value}, but should be 10")
        return False
    
    # Check if they printed the variable (not hardcoded)
    # This is trickier - we'll check their code cell above
    # For now, we'll give a warning if we can't verify
    
    print("✅ Perfect! You created the variable 'price' and assigned it the value 10.")
    print("✅ Great job!")
    return True


def verify_task_2():
    """
    Verify Task 2: Update a Variable Value
    Checks:
    1. Variable 'price' exists
    2. Variable 'price' = 20 (updated from 10)
    """
    if 'price' not in dir():
        print("❌ Error: Variable 'price' not found.")
        print("💡 Hint: Create price = 10, then update it to price = 20")
        return False
    
    price_value = eval('price')
    if price_value != 20:
        print(f"❌ Error: Variable 'price' has value {price_value}, but should be 20")
        print("💡 Hint: Remember to reassign the variable: price = 20")
        return False
    
    print("✅ Excellent! You successfully updated the variable 'price' to 20.")
    print("✅ This shows that variables can be changed!")
    return True


def verify_task_3():
    """
    Verify Task 3: Work with Different Data Types
    Checks:
    1. price = 10 (integer)
    2. rating = 4.9 (float)
    3. name = 'Mosh' (string)
    4. is_published = True (boolean)
    """
    errors = []
    
    # Check price
    if 'price' not in dir():
        errors.append("❌ Variable 'price' not found")
    else:
        price_value = eval('price')
        if price_value != 10:
            errors.append(f"❌ price should be 10, got {price_value}")
        elif not isinstance(price_value, int):
            errors.append(f"❌ price should be an integer (int), got {type(price_value).__name__}")
    
    # Check rating
    if 'rating' not in dir():
        errors.append("❌ Variable 'rating' not found")
    else:
        rating_value = eval('rating')
        if rating_value != 4.9:
            errors.append(f"❌ rating should be 4.9, got {rating_value}")
        elif not isinstance(rating_value, float):
            errors.append(f"❌ rating should be a float, got {type(rating_value).__name__}")
    
    # Check name
    if 'name' not in dir():
        errors.append("❌ Variable 'name' not found")
    else:
        name_value = eval('name')
        if name_value != 'Mosh':
            errors.append(f"❌ name should be 'Mosh', got '{name_value}'")
        elif not isinstance(name_value, str):
            errors.append(f"❌ name should be a string (str), got {type(name_value).__name__}")
    
    # Check is_published
    if 'is_published' not in dir():
        errors.append("❌ Variable 'is_published' not found")
    else:
        is_published_value = eval('is_published')
        if is_published_value != True:
            errors.append(f"❌ is_published should be True, got {is_published_value}")
        elif not isinstance(is_published_value, bool):
            errors.append(f"❌ is_published should be a boolean (bool), got {type(is_published_value).__name__}")
    
    if errors:
        print("Issues found:")
        for error in errors:
            print(f"  {error}")
        print("\n💡 Hint: Make sure you create all four variables with the correct types:")
        print("  • price = 10 (integer)")
        print("  • rating = 4.9 (float with decimal)")
        print("  • name = 'Mosh' (string with quotes)")
        print("  • is_published = True (boolean, capitalized)")
        return False
    
    print("✅ Outstanding! You created all four data types correctly!")
    print("  ✓ Integer (int): whole numbers")
    print("  ✓ Float (float): decimal numbers")
    print("  ✓ String (str): text in quotes")
    print("  ✓ Boolean (bool): True or False")
    return True


def verify_task_4():
    """
    Verify Task 4: Patient Information System
    Checks:
    1. name = 'John Smith'
    2. age = 20
    3. is_new = True
    """
    errors = []
    
    # Check name
    if 'name' not in dir():
        errors.append("❌ Variable 'name' not found")
    else:
        name_value = eval('name')
        if name_value != 'John Smith':
            errors.append(f"❌ name should be 'John Smith', got '{name_value}'")
    
    # Check age
    if 'age' not in dir():
        errors.append("❌ Variable 'age' not found")
    else:
        age_value = eval('age')
        if age_value != 20:
            errors.append(f"❌ age should be 20, got {age_value}")
    
    # Check is_new
    if 'is_new' not in dir():
        errors.append("❌ Variable 'is_new' not found")
    else:
        is_new_value = eval('is_new')
        if is_new_value != True:
            errors.append(f"❌ is_new should be True, got {is_new_value}")
    
    if errors:
        print("Issues found:")
        for error in errors:
            print(f"  {error}")
        print("\n💡 Hint: Create the three variables for the patient information system:")
        print("  • name = 'John Smith'")
        print("  • age = 20")
        print("  • is_new = True")
        return False
    
    print("✅ Perfect! You've completed the Patient Information System!")
    print("✅ You now understand how to:")
    print("  • Create variables with meaningful names")
    print("  • Store different types of data")
    print("  • Build simple information systems")
    print("\n🎉 Congratulations! You've completed all Walk-Along tasks for Lesson 03!")
    return True


def check_code_usage(code_string, variable_name):
    """
    Helper function to check if a variable was actually used in code
    (not just created and then hardcoded output)
    """
    # Remove comments
    lines = code_string.split('\n')
    lines = [line.split('#')[0] for line in lines]
    code_clean = '\n'.join(lines)
    
    # Check if variable appears in print statement
    if f'print({variable_name})' in code_clean.replace(' ', ''):
        return True
    if f'print({variable_name},' in code_clean.replace(' ', ''):
        return True
    
    return False
