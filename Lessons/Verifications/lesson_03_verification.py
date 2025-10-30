"""
Lesson 03: Variables - Verification Functions
COSC 1315 - Introduction to Computer Programming

This module provides automated verification for student code in the Variables lesson.
"""

import ast
import inspect

# Get IPython instance to access notebook namespace
try:
    from IPython import get_ipython
    ipython = get_ipython()
except:
    ipython = None

def _get_user_namespace():
    """Helper function to get the user's namespace (where their variables live)"""
    if ipython is not None:
        return ipython.user_ns
    else:
        # Fallback to globals if not in IPython (shouldn't happen in Colab)
        return globals()

def _get_previous_cell_code():
    """Get the code from the cell that was executed before verify was called"""
    if ipython is None:
        return None
    
    # Get the execution history
    history = list(ipython.history_manager.get_range(output=False))
    
    # The last entry is the verify_task_X() call itself
    # The second-to-last entry is the student's code
    if len(history) >= 2:
        # history entries are tuples: (session, line_number, code)
        return history[-2][2]  # Get the code from second-to-last execution
    return None

def _check_code_uses_variable(code, variable_name):
    """
    Check if the code actually uses the specified variable (not just creates it).
    Returns (True, "") if variable is used correctly, or (False, "error message") if not.
    """
    if not code:
        return True, ""  # Can't verify without code, give benefit of doubt
    
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return True, ""  # Syntax error, but that's a different issue
    
    # Look for print() calls
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # Check if it's a print function call
            if isinstance(node.func, ast.Name) and node.func.id == 'print':
                # Check the arguments to print()
                for arg in node.args:
                    # Check for literal values (strings, numbers, etc.)
                    if isinstance(arg, ast.Constant):
                        # Student is printing a literal value, not the variable!
                        return False, f"💡 Hint: Type print({variable_name}), not print({repr(arg.value)})"
                    elif isinstance(arg, ast.Name) and arg.id == variable_name:
                        # Found the variable being used in print()!
                        return True, ""
    
    return True, ""  # No print found, or it's complex - give benefit of doubt

def verify_task_1():
    """
    Verify Task 1: Store and Display a Price
    Checks:
    - Variable 'price' exists in global scope
    - Variable 'price' equals 10
    - Student actually USES the variable in print() (not just prints "10")
    """
    user_ns = _get_user_namespace()
    
    # Check 1: Does the variable exist?
    if 'price' not in user_ns:
        print("❌ Error: Variable 'price' not found.")
        print("💡 Hint: Create a variable named 'price' and assign it the value 10")
        return False

    # Check 2: Does it have the correct value?
    price_value = user_ns['price']
    if price_value != 10:
        print(f"❌ Error: Variable 'price' has value {price_value}, but should be 10")
        return False

    # Check 3: Did the student actually USE the variable in their code?
    code = _get_previous_cell_code()
    uses_variable, error_msg = _check_code_uses_variable(code, 'price')
    if not uses_variable:
        print("❌ Error: You printed the number directly, not the variable!")
        print("⚠️  Common Mistake: Don't type print(\"10\") or print(10)")
        print("✅  Correct Way: Type print(price) - this prints the variable's value")
        if error_msg:
            print(error_msg)
        return False

    print("✅ Perfect! You created the variable 'price' and assigned it the value 10.")
    print("✅ Great job! You used the variable correctly in print()!")
    return True


def verify_task_2():
    """
    Verify Task 2: Update a Variable Value
    Checks:
    - Variable 'price' exists
    - Variable 'price' equals 20 (updated from 10)
    - Student actually USES the variable in print()
    """
    user_ns = _get_user_namespace()
    
    # Check 1: Does the variable exist?
    if 'price' not in user_ns:
        print("❌ Error: Variable 'price' not found.")
        print("💡 Hint: Create price = 10, then update it to price = 20")
        return False

    # Check 2: Does it have the correct value?
    price_value = user_ns['price']
    if price_value != 20:
        print(f"❌ Error: Variable 'price' has value {price_value}, but should be 20")
        print("💡 Hint: Remember to reassign the variable: price = 20")
        return False

    # Check 3: Did the student actually USE the variable in their code?
    code = _get_previous_cell_code()
    uses_variable, error_msg = _check_code_uses_variable(code, 'price')
    if not uses_variable:
        print("❌ Error: You printed the number directly, not the variable!")
        print("⚠️  Remember: Type print(price), not print(20)")
        if error_msg:
            print(error_msg)
        return False

    print("✅ Excellent! You successfully updated the variable 'price' to 20.")
    print("✅ Great job using the variable correctly!")
    return True


def verify_task_3():
    """
    Verify Task 3: Work with Different Data Types
    Checks:
    - price = 10 (integer type)
    - rating = 4.9 (float type)
    - name = 'Mosh' (string type)
    - is_published = True (boolean type)
    """
    user_ns = _get_user_namespace()
    errors = []

    # Check price
    if 'price' not in user_ns:
        errors.append("❌ Variable 'price' not found")
    else:
        price_value = user_ns['price']
        if price_value != 10:
            errors.append(f"❌ price should be 10, got {price_value}")
        elif not isinstance(price_value, int):
            errors.append(f"❌ price should be an integer (int), got {type(price_value).__name__}")

    # Check rating
    if 'rating' not in user_ns:
        errors.append("❌ Variable 'rating' not found")
    else:
        rating_value = user_ns['rating']
        if rating_value != 4.9:
            errors.append(f"❌ rating should be 4.9, got {rating_value}")
        elif not isinstance(rating_value, float):
            errors.append(f"❌ rating should be a float, got {type(rating_value).__name__}")

    # Check name
    if 'name' not in user_ns:
        errors.append("❌ Variable 'name' not found")
    else:
        name_value = user_ns['name']
        if name_value != 'Mosh':
            errors.append(f"❌ name should be 'Mosh', got '{name_value}'")
        elif not isinstance(name_value, str):
            errors.append(f"❌ name should be a string (str), got {type(name_value).__name__}")

    # Check is_published
    if 'is_published' not in user_ns:
        errors.append("❌ Variable 'is_published' not found")
    else:
        is_published_value = user_ns['is_published']
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
    - name = 'John Smith'
    - age = 20
    - is_new = True
    """
    user_ns = _get_user_namespace()
    errors = []

    # Check name
    if 'name' not in user_ns:
        errors.append("❌ Variable 'name' not found")
    else:
        name_value = user_ns['name']
        if name_value != 'John Smith':
            errors.append(f"❌ name should be 'John Smith', got '{name_value}'")

    # Check age
    if 'age' not in user_ns:
        errors.append("❌ Variable 'age' not found")
    else:
        age_value = user_ns['age']
        if age_value != 20:
            errors.append(f"❌ age should be 20, got {age_value}")

    # Check is_new
    if 'is_new' not in user_ns:
        errors.append("❌ Variable 'is_new' not found")
    else:
        is_new_value = user_ns['is_new']
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


# ============================================================================
# ADVANCED VERIFICATION FUNCTIONS
# For "Try It Yourself" exercises where we don't know variable names
# ============================================================================

def _analyze_code_structure(code):
    """
    Analyze code structure to detect programming patterns.
    Returns a dictionary with detected patterns.
    """
    if not code:
        return None
    
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    
    analysis = {
        'has_assignment': False,
        'has_print': False,
        'variables_created': [],
        'variables_used_in_print': [],
        'literals_in_print': [],
        'print_statements': 0,
        'assignment_statements': 0,
    }
    
    for node in ast.walk(tree):
        # Detect variable assignments
        if isinstance(node, ast.Assign):
            analysis['has_assignment'] = True
            analysis['assignment_statements'] += 1
            for target in node.targets:
                if isinstance(target, ast.Name):
                    analysis['variables_created'].append(target.id)
        
        # Detect print() calls
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == 'print':
                analysis['has_print'] = True
                analysis['print_statements'] += 1
                
                # Check what's being printed
                for arg in node.args:
                    # Literal values (numbers, strings, etc.)
                    if isinstance(arg, ast.Constant):
                        analysis['literals_in_print'].append(arg.value)
                    # Variable names
                    elif isinstance(arg, ast.Name):
                        analysis['variables_used_in_print'].append(arg.id)
    
    return analysis


def verify_generic_variable_usage(min_variables=1, require_print=True, require_variable_in_print=True):
    """
    Generic verification for "Try It Yourself" exercises.
    Checks that students use variables correctly WITHOUT knowing exact names.
    
    Args:
        min_variables: Minimum number of variables that should be created
        require_print: Whether a print statement is required
        require_variable_in_print: Whether print must use a variable (not literal)
    
    Returns:
        True if verification passes, False otherwise
    """
    code = _get_previous_cell_code()
    analysis = _analyze_code_structure(code)
    
    if not analysis:
        print("⚠️  Could not analyze your code. Please make sure it's valid Python.")
        return False
    
    errors = []
    
    # Check 1: Did they create any variables?
    if not analysis['has_assignment']:
        errors.append("❌ No variables found. You need to create a variable!")
        errors.append("   Example: my_variable = 10")
    elif len(analysis['variables_created']) < min_variables:
        errors.append(f"❌ You created {len(analysis['variables_created'])} variable(s), but need at least {min_variables}")
        errors.append(f"   Variables found: {', '.join(analysis['variables_created'])}")
    
    # Check 2: Did they print anything?
    if require_print and not analysis['has_print']:
        errors.append("❌ No print() statement found. You need to display your variable!")
        errors.append("   Example: print(my_variable)")
    
    # Check 3: Did they use a variable in print (not a literal)?
    if require_variable_in_print and analysis['has_print']:
        if not analysis['variables_used_in_print'] and analysis['literals_in_print']:
            errors.append("❌ You're printing a literal value, not a variable!")
            errors.append(f"   You printed: {analysis['literals_in_print']}")
            errors.append("   ⚠️  Remember: Create a variable FIRST, then print the variable")
            errors.append("   ✅ Correct: my_variable = 10; print(my_variable)")
        elif not analysis['variables_used_in_print']:
            errors.append("❌ Your print() statement doesn't use any variables")
            errors.append("   Make sure you're printing a variable, not just text")
    
    # Check 4: Are they using the variables they created?
    if analysis['variables_created'] and analysis['variables_used_in_print']:
        unused_vars = set(analysis['variables_created']) - set(analysis['variables_used_in_print'])
        if unused_vars:
            # This is just a warning, not an error
            print(f"💡 Note: You created {', '.join(unused_vars)} but didn't use them in print()")
            print("   That's okay for now, but remember: variables are meant to be used!")
    
    # Report results
    if errors:
        print("Issues found:\n")
        for error in errors:
            print(error)
        return False
    
    # Success!
    print("✅ Excellent! You're using variables correctly!")
    if analysis['variables_created']:
        print(f"   Variables created: {', '.join(analysis['variables_created'])}")
    if analysis['variables_used_in_print']:
        print(f"   Variables used in print: {', '.join(analysis['variables_used_in_print'])}")
    print("\n🎉 Great job demonstrating your understanding of variables!")
    return True


def verify_try_it_yourself():
    """
    Verification for the "Try It Yourself" exercise.
    Students create their own variable with their own name and value.
    We don't know what they'll call it or what value it will have.
    """
    print("🔍 Checking your 'Try It Yourself' code...\n")
    
    # We just need to verify:
    # 1. They created at least one variable
    # 2. They printed something
    # 3. They used a variable in print (not a literal)
    
    return verify_generic_variable_usage(
        min_variables=1,
        require_print=True,
        require_variable_in_print=True
    )


def verify_multiple_variables(count=2):
    """
    Verify student created multiple variables (for more advanced exercises).
    Example: "Create 2 variables and print both of them"
    """
    print(f"🔍 Checking that you created {count} variables...\n")
    
    return verify_generic_variable_usage(
        min_variables=count,
        require_print=True,
        require_variable_in_print=True
    )


# ============================================================================
# GRADING SYSTEM
# Component-based grading with detailed feedback
# ============================================================================

def calculate_grade():
    """
    Calculate grade with component-based scoring.
    This provides detailed feedback on what the student got right/wrong.
    
    Returns a tuple: (total_points, max_points, details_dict)
    """
    print("="*60)
    print("📊 GRADE REPORT - Lesson 03: Variables")
    print("="*60)
    print()

    total_points = 0
    max_points = 100
    details = {
        'walk_along': {'earned': 0, 'possible': 20, 'components': []},
        'try_it_yourself': {'earned': 0, 'possible': 40, 'components': []},
        'debugging': {'earned': 0, 'possible': 40, 'components': []}
    }

    # ========================================
    # Task 1: Walk-Along (20 points total)
    # ========================================
    print("📺 WALK-ALONG: Follow Mosh (20 points possible)")
    print("-" * 60)

    task1_points = 0
    task1_max = 20

    # Component grading for Walk-Along
    try:
        ns = _get_user_namespace()
        
        # Component 1: Variable exists (5 points)
        if 'price' in ns:
            print("   ✅ Variable 'price' created: +5 points")
            task1_points += 5
            details['walk_along']['components'].append({'name': 'Variable created', 'earned': 5, 'possible': 5})
        else:
            print("   ❌ Variable 'price' not found: 0 points")
            details['walk_along']['components'].append({'name': 'Variable created', 'earned': 0, 'possible': 5})
        
        # Component 2: Correct value (5 points)
        if 'price' in ns and ns['price'] == 10:
            print("   ✅ Correct value (10): +5 points")
            task1_points += 5
            details['walk_along']['components'].append({'name': 'Correct value', 'earned': 5, 'possible': 5})
        else:
            print("   ❌ Incorrect value: 0 points")
            details['walk_along']['components'].append({'name': 'Correct value', 'earned': 0, 'possible': 5})
        
        # Component 3: Code uses print() (5 points)
        code = _get_previous_cell_code()
        if code and 'print' in code.lower():
            print("   ✅ Used print() function: +5 points")
            task1_points += 5
            details['walk_along']['components'].append({'name': 'Used print()', 'earned': 5, 'possible': 5})
        else:
            print("   ❌ Did not use print(): 0 points")
            details['walk_along']['components'].append({'name': 'Used print()', 'earned': 0, 'possible': 5})
        
        # Component 4: Printed the variable (not literal) (5 points)
        if code and _check_code_uses_variable(code, 'price')[0]:
            print("   ✅ Printed variable (not literal): +5 points")
            task1_points += 5
            details['walk_along']['components'].append({'name': 'Printed variable', 'earned': 5, 'possible': 5})
        else:
            print("   ❌ Did not print variable correctly: 0 points")
            details['walk_along']['components'].append({'name': 'Printed variable', 'earned': 0, 'possible': 5})
            
    except Exception as e:
        print(f"   ⚠️  ERROR: Could not verify ({e})")

    print(f"\n   📊 Walk-Along Score: {task1_points}/{task1_max} points")
    details['walk_along']['earned'] = task1_points
    total_points += task1_points
    print()

    # ========================================
    # Task 2: Try It Yourself (40 points total)
    # ========================================
    print("🎯 TRY IT YOURSELF (40 points possible)")
    print("-" * 60)

    task2_points = 0
    task2_max = 40

    try:
        code = _get_previous_cell_code()
        analysis = _analyze_code_structure(code) if code else {}
        ns = _get_user_namespace()
        
        # Component 1: Created at least one variable (10 points)
        if analysis.get('has_assignment', False):
            print("   ✅ Created a variable: +10 points")
            task2_points += 10
            details['try_it_yourself']['components'].append({'name': 'Created variable', 'earned': 10, 'possible': 10})
        else:
            print("   ❌ No variable created: 0 points")
            details['try_it_yourself']['components'].append({'name': 'Created variable', 'earned': 0, 'possible': 10})
        
        # Component 2: Used print() function (10 points)
        if analysis.get('has_print', False):
            print("   ✅ Used print() function: +10 points")
            task2_points += 10
            details['try_it_yourself']['components'].append({'name': 'Used print()', 'earned': 10, 'possible': 10})
        else:
            print("   ❌ Did not use print(): 0 points")
            details['try_it_yourself']['components'].append({'name': 'Used print()', 'earned': 0, 'possible': 10})
        
        # Component 3: Printed a variable (not literal) (15 points)
        vars_in_print = analysis.get('variables_used_in_print', [])
        if len(vars_in_print) > 0:
            print(f"   ✅ Printed variable '{vars_in_print[0]}': +15 points")
            task2_points += 15
            details['try_it_yourself']['components'].append({'name': 'Printed variable', 'earned': 15, 'possible': 15})
        else:
            print("   ❌ Did not print a variable: 0 points")
            details['try_it_yourself']['components'].append({'name': 'Printed variable', 'earned': 0, 'possible': 15})
        
        # Component 4: No literals in print (5 points)
        literals_in_print = analysis.get('literals_in_print', [])
        if analysis.get('has_print', False) and len(literals_in_print) == 0:
            print("   ✅ No literals in print (correct!): +5 points")
            task2_points += 5
            details['try_it_yourself']['components'].append({'name': 'No literals', 'earned': 5, 'possible': 5})
        elif len(literals_in_print) > 0:
            print("   ❌ Used literal in print: 0 points")
            details['try_it_yourself']['components'].append({'name': 'No literals', 'earned': 0, 'possible': 5})
        
    except Exception as e:
        print(f"   ⚠️  ERROR: Could not verify ({e})")

    print(f"\n   📊 Try It Yourself Score: {task2_points}/{task2_max} points")
    details['try_it_yourself']['earned'] = task2_points
    total_points += task2_points
    print()

    # ========================================
    # Task 3: Debugging (40 points) - PLACEHOLDER
    # ========================================
    print("🐛 DEBUGGING (40 points possible)")
    print("-" * 60)
    print("   ⚠️  No debugging task in this test notebook")
    print("   📊 Debugging Score: 0/40 points (not included)")
    task3_points = 0
    task3_max = 40
    details['debugging']['earned'] = 0
    # Note: In full lesson, would have 40 points from debugging section
    # For this test, we're only grading the first 60 points
    max_points = task1_max + task2_max  # 60 for this test
    print()

    # ========================================
    # FINAL GRADE CALCULATION
    # ========================================
    print("="*60)
    print(f"📈 TOTAL SCORE: {total_points}/{max_points} points")

    percentage = (total_points / max_points) * 100
    print(f"📊 PERCENTAGE: {percentage:.1f}%")

    # Letter grade
    if percentage >= 90:
        letter_grade = "A"
        emoji = "🌟"
    elif percentage >= 80:
        letter_grade = "B"
        emoji = "😊"
    elif percentage >= 70:
        letter_grade = "C"
        emoji = "😐"
    elif percentage >= 60:
        letter_grade = "D"
        emoji = "😟"
    else:
        letter_grade = "F"
        emoji = "😞"

    print(f"📝 LETTER GRADE: {letter_grade} {emoji}")
    print("="*60)
    print()

    # Detailed feedback
    if total_points == max_points:
        print("🎉 PERFECT SCORE! Excellent work!")
        print("✅ You're ready to submit this lesson.")
    elif total_points >= max_points * 0.8:
        print("👍 Great job! You're doing well!")
        if task1_points < task1_max:
            print(f"💡 Walk-Along: You earned {task1_points}/{task1_max} points")
        if task2_points < task2_max:
            print(f"💡 Try It Yourself: You earned {task2_points}/{task2_max} points")
    elif total_points >= max_points * 0.6:
        print("😐 You passed, but there's room for improvement!")
        if task1_points < task1_max:
            print(f"📚 Walk-Along needs work: {task1_points}/{task1_max} points")
        if task2_points < task2_max:
            print(f"📚 Try It Yourself needs work: {task2_points}/{task2_max} points")
    else:
        print("📚 Keep working! You can do better!")
        print("🔄 Go back and complete the tasks that failed")
        print("💪 Then run this cell again to see your new grade")
        print()
        if task1_points == 0:
            print("⚠️  Walk-Along: No points earned - start here!")
        if task2_points == 0:
            print("⚠️  Try It Yourself: No points earned - review requirements!")

    print()
    print("💾 When you're happy with your grade, save and submit this notebook.")
    print("🔄 You can revise your work and run this grader again anytime!")
    
    return total_points, max_points, details


# Module metadata
__version__ = "2.1.0"
__author__ = "Professor Richard Joseph Sullivan"
__course__ = "COSC 1315 - Introduction to Computer Programming"
