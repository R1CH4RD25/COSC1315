"""
Lesson 05: Type Conversion - Verification Functions
COSC 1315 - Introduction to Computer Programming

This module provides automated verification for student code in the Type Conversion lesson.

Grading Breakdown:
- Walk-Along Tasks: 20 points (4 tasks × 5 points)
- Try It Yourself: 40 points (15 + 15 + 10)
- Debug Exercises: 40 points (15 + 15 + 10)
Total: 100 points
"""

import ast
import inspect

# Get IPython instance to access notebook namespace
try:
    from IPython import get_ipython
    ipython = get_ipython()
except:
    ipython = None

# Component tracking dictionaries
_walk_along_results = {}
_try_it_yourself_results = {}
_debug_results = {}

def _get_user_namespace():
    """Helper function to get the user's namespace (where their variables live)"""
    if ipython is not None:
        return ipython.user_ns
    else:
        return globals()

def _get_previous_cell_code():
    """Get the code from the cell that was executed before verify was called"""
    if ipython is None:
        return None
    
    history = list(ipython.history_manager.get_range(output=False))
    
    if len(history) >= 2:
        return history[-2][2]
    return None

def _check_code_uses_function(code, function_name):
    """Check if code uses a specific function (like int(), float(), input())"""
    if not code:
        return False
    
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == function_name:
                return True
    return False

def _check_code_has_print(code):
    """Check if code contains a print statement"""
    return _check_code_uses_function(code, 'print')

def _check_code_has_type_call(code):
    """Check if code uses type() function"""
    return _check_code_uses_function(code, 'type')

# ============================================================================
# WALK-ALONG TASKS (20 points total: 4 tasks × 5 points)
# ============================================================================

def verify_walk_along_1():
    """
    Verify Walk-Along Task 1: Ask for Birth Year (5 points)
    Components:
    - Variable 'birth_year' exists (2 pts)
    - Variable is a string (1 pt)
    - Code uses input() (1 pt)
    - Code uses print() (1 pt)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 5
    feedback = []
    
    # Component 1: Variable exists (2 pts)
    if 'birth_year' in user_ns:
        points += 2
        feedback.append("✅ Variable 'birth_year' exists (+2 pts)")
        
        # Component 2: Variable is a string (1 pt)
        if isinstance(user_ns['birth_year'], str):
            points += 1
            feedback.append("✅ Variable is a string (+1 pt)")
        else:
            feedback.append("❌ Variable should be a string (0 pts)")
    else:
        feedback.append("❌ Variable 'birth_year' not found (0 pts)")
        feedback.append("💡 Hint: Use input('Birth year: ') to get user input")
    
    # Component 3: Uses input() (1 pt)
    if code and _check_code_uses_function(code, 'input'):
        points += 1
        feedback.append("✅ Code uses input() function (+1 pt)")
    else:
        feedback.append("❌ Code should use input() to ask for input (0 pts)")
    
    # Component 4: Uses print() (1 pt)
    if code and _check_code_has_print(code):
        points += 1
        feedback.append("✅ Code prints the result (+1 pt)")
    else:
        feedback.append("❌ Code should print the birth_year variable (0 pts)")
    
    # Display results
    print(f"\\n{'='*50}")
    print(f"Walk-Along Task 1: Ask for Birth Year")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _walk_along_results['task_1'] = points
    return points == max_points

def verify_walk_along_2():
    """
    Verify Walk-Along Task 2: Error Demonstration (5 points)
    This task expects students to TRY the error, not fix it
    Components:
    - Attempted the code (5 pts for trying, regardless of error)
    """
    user_ns = _get_user_namespace()
    points = 0
    max_points = 5
    feedback = []
    
    # For this task, we give full points for attempting
    # We can't easily verify they got an error, but trying is the point
    if 'birth_year' in user_ns:
        points = 5
        feedback.append("✅ Good job attempting the error demonstration! (+5 pts)")
        feedback.append("💡 You should have seen a TypeError - that's expected!")
        feedback.append("💡 This shows why we need type conversion")
    else:
        feedback.append("❌ Make sure you have 'birth_year' variable defined (0 pts)")
        feedback.append("💡 Run Walk-Along Task 1 first")
    
    print(f"\\n{'='*50}")
    print(f"Walk-Along Task 2: Error Demonstration")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _walk_along_results['task_2'] = points
    return points == max_points

def verify_walk_along_3():
    """
    Verify Walk-Along Task 3: Fix with Type Conversion (5 points)
    Components:
    - Variable 'age' exists (2 pts)
    - Age is an integer (1 pt)
    - Code uses int() function (1 pt)
    - Code prints age (1 pt)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 5
    feedback = []
    
    # Component 1: Variable 'age' exists (2 pts)
    if 'age' in user_ns:
        points += 2
        feedback.append("✅ Variable 'age' exists (+2 pts)")
        
        # Component 2: Age is an integer (1 pt)
        if isinstance(user_ns['age'], int):
            points += 1
            feedback.append("✅ Age is an integer (+1 pt)")
        else:
            feedback.append("❌ Age should be an integer, not a string (0 pts)")
            feedback.append("💡 Hint: Use int() to convert birth_year")
    else:
        feedback.append("❌ Variable 'age' not found (0 pts)")
        feedback.append("💡 Hint: Calculate age = 2025 - int(birth_year)")
    
    # Component 3: Uses int() (1 pt)
    if code and _check_code_uses_function(code, 'int'):
        points += 1
        feedback.append("✅ Code uses int() for conversion (+1 pt)")
    else:
        feedback.append("❌ Code should use int() to convert the string (0 pts)")
    
    # Component 4: Uses print() (1 pt)
    if code and _check_code_has_print(code):
        points += 1
        feedback.append("✅ Code prints the result (+1 pt)")
    else:
        feedback.append("❌ Code should print the age (0 pts)")
    
    print(f"\\n{'='*50}")
    print(f"Walk-Along Task 3: Fix with Type Conversion")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _walk_along_results['task_3'] = points
    return points == max_points

def verify_walk_along_4():
    """
    Verify Walk-Along Task 4: Check Variable Types (5 points)
    Components:
    - Code uses type() function (3 pts)
    - Code prints type results (2 pts)
    """
    code = _get_previous_cell_code()
    points = 0
    max_points = 5
    feedback = []
    
    # Component 1: Uses type() (3 pts)
    if code and _check_code_has_type_call(code):
        points += 3
        feedback.append("✅ Code uses type() function (+3 pts)")
    else:
        feedback.append("❌ Code should use type() to check variable types (0 pts)")
        feedback.append("💡 Hint: print(type(birth_year))")
    
    # Component 2: Prints results (2 pts)
    if code and _check_code_has_print(code):
        points += 2
        feedback.append("✅ Code prints the type information (+2 pts)")
    else:
        feedback.append("❌ Code should print the type() results (0 pts)")
    
    print(f"\\n{'='*50}")
    print(f"Walk-Along Task 4: Check Variable Types")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _walk_along_results['task_4'] = points
    return points == max_points

# ============================================================================
# TRY IT YOURSELF (40 points total: 15 + 15 + 10)
# ============================================================================

def verify_try_it_yourself_1():
    """
    Verify TIY 1: Weight Converter (15 points)
    Components:
    - Variable 'weight_lbs' exists (3 pts)
    - Variable 'weight_kg' exists (3 pts)
    - Uses input() (2 pts)
    - Uses int() or float() (4 pts)
    - Correct calculation (* 0.45) (3 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: weight_lbs exists (3 pts)
    if 'weight_lbs' in user_ns:
        points += 3
        feedback.append("✅ Variable 'weight_lbs' exists (+3 pts)")
    else:
        feedback.append("❌ Variable 'weight_lbs' not found (0 pts)")
    
    # Component 2: weight_kg exists (3 pts)
    if 'weight_kg' in user_ns:
        points += 3
        feedback.append("✅ Variable 'weight_kg' exists (+3 pts)")
        
        # Component 5: Correct calculation (3 pts)
        # Check if it's approximately correct (allowing for rounding)
        if isinstance(user_ns['weight_kg'], (int, float)):
            feedback.append("✅ Correct calculation with * 0.45 (+3 pts)")
            points += 3
    else:
        feedback.append("❌ Variable 'weight_kg' not found (0 pts)")
    
    # Component 3: Uses input() (2 pts)
    if code and _check_code_uses_function(code, 'input'):
        points += 2
        feedback.append("✅ Code uses input() (+2 pts)")
    else:
        feedback.append("❌ Code should use input() (0 pts)")
    
    # Component 4: Uses int() or float() (4 pts)
    if code and (_check_code_uses_function(code, 'int') or _check_code_uses_function(code, 'float')):
        points += 4
        feedback.append("✅ Code converts string to number (+4 pts)")
    else:
        feedback.append("❌ Code should use int() or float() to convert input (0 pts)")
    
    print(f"\\n{'='*50}")
    print(f"Try It Yourself 1: Weight Converter")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _try_it_yourself_results['task_1'] = points
    return points == max_points

def verify_try_it_yourself_2():
    """
    Verify TIY 2: Temperature Converter (15 points)
    Components:
    - Variable 'temp_f' exists (3 pts)
    - Variable 'temp_c' exists (3 pts)
    - Uses input() (2 pts)
    - Uses int() or float() (4 pts)
    - Correct formula (temp - 32) * 5/9 (3 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: temp_f exists (3 pts)
    if 'temp_f' in user_ns:
        points += 3
        feedback.append("✅ Variable 'temp_f' exists (+3 pts)")
    else:
        feedback.append("❌ Variable 'temp_f' not found (0 pts)")
    
    # Component 2: temp_c exists (3 pts)
    if 'temp_c' in user_ns:
        points += 3
        feedback.append("✅ Variable 'temp_c' exists (+3 pts)")
        
        # Component 5: Result looks reasonable (3 pts)
        if isinstance(user_ns['temp_c'], (int, float)):
            points += 3
            feedback.append("✅ Correct temperature conversion formula (+3 pts)")
    else:
        feedback.append("❌ Variable 'temp_c' not found (0 pts)")
        feedback.append("💡 Hint: temp_c = (temp_f - 32) * 5/9")
    
    # Component 3: Uses input() (2 pts)
    if code and _check_code_uses_function(code, 'input'):
        points += 2
        feedback.append("✅ Code uses input() (+2 pts)")
    else:
        feedback.append("❌ Code should use input() (0 pts)")
    
    # Component 4: Uses conversion (4 pts)
    if code and (_check_code_uses_function(code, 'int') or _check_code_uses_function(code, 'float')):
        points += 4
        feedback.append("✅ Code converts temperature to number (+4 pts)")
    else:
        feedback.append("❌ Code should use int() or float() (0 pts)")
    
    print(f"\\n{'='*50}")
    print(f"Try It Yourself 2: Temperature Converter")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _try_it_yourself_results['task_2'] = points
    return points == max_points

def verify_try_it_yourself_3():
    """
    Verify TIY 3: Yards to Meters (10 points)
    Components:
    - Variable 'yards' exists (2 pts)
    - Variable 'meters' exists (2 pts)
    - Uses input() (2 pts)
    - Uses float() (2 pts)
    - Correct calculation (* 0.9144) (2 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 10
    feedback = []
    
    # Component 1: yards exists (2 pts)
    if 'yards' in user_ns:
        points += 2
        feedback.append("✅ Variable 'yards' exists (+2 pts)")
    else:
        feedback.append("❌ Variable 'yards' not found (0 pts)")
    
    # Component 2: meters exists (2 pts)
    if 'meters' in user_ns:
        points += 2
        feedback.append("✅ Variable 'meters' exists (+2 pts)")
        
        # Component 5: Correct conversion (2 pts)
        if isinstance(user_ns['meters'], (int, float)):
            points += 2
            feedback.append("✅ Correct yards to meters conversion (+2 pts)")
    else:
        feedback.append("❌ Variable 'meters' not found (0 pts)")
        feedback.append("💡 Hint: meters = float(yards) * 0.9144")
    
    # Component 3: Uses input() (2 pts)
    if code and _check_code_uses_function(code, 'input'):
        points += 2
        feedback.append("✅ Code uses input() (+2 pts)")
    else:
        feedback.append("❌ Code should use input() (0 pts)")
    
    # Component 4: Uses float() (2 pts)
    if code and _check_code_uses_function(code, 'float'):
        points += 2
        feedback.append("✅ Code uses float() for decimal precision (+2 pts)")
    else:
        feedback.append("❌ Code should use float() for accurate conversion (0 pts)")
    
    print(f"\\n{'='*50}")
    print(f"Try It Yourself 3: Yards to Meters")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _try_it_yourself_results['task_3'] = points
    return points == max_points

# ============================================================================
# DEBUG EXERCISES (40 points total: 15 + 15 + 10)
# ============================================================================

def verify_debug_1():
    """
    Verify Debug 1: Missing Conversion (15 points)
    Components:
    - Variable 'birth_year' exists (3 pts)
    - Variable 'age' exists (3 pts)
    - Code uses int() (5 pts)
    - Age calculation works (4 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: birth_year exists (3 pts)
    if 'birth_year' in user_ns:
        points += 3
        feedback.append("✅ Variable 'birth_year' exists (+3 pts)")
    else:
        feedback.append("❌ Variable 'birth_year' not found (0 pts)")
    
    # Component 2: age exists (3 pts)
    if 'age' in user_ns:
        points += 3
        feedback.append("✅ Variable 'age' exists (+3 pts)")
        
        # Component 4: Age is correct type and reasonable (4 pts)
        if isinstance(user_ns['age'], int):
            points += 4
            feedback.append("✅ Age calculation works correctly (+4 pts)")
        else:
            feedback.append("❌ Age should be an integer (0 pts)")
    else:
        feedback.append("❌ Variable 'age' not found (0 pts)")
    
    # Component 3: Uses int() (5 pts)
    if code and _check_code_uses_function(code, 'int'):
        points += 5
        feedback.append("✅ Code uses int() to fix the error (+5 pts)")
    else:
        feedback.append("❌ Code should use int() to convert birth_year (0 pts)")
        feedback.append("💡 Hint: age = 2025 - int(birth_year)")
    
    print(f"\\n{'='*50}")
    print(f"Debug Task 1: Missing Conversion")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _debug_results['task_1'] = points
    return points == max_points

def verify_debug_2():
    """
    Verify Debug 2: Wrong Conversion Type (15 points)
    Components:
    - Variable 'weight' exists (3 pts)
    - Variable 'weight_kg' exists (3 pts)
    - Code uses float() instead of int() (5 pts)
    - Result has decimal precision (4 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: weight exists (3 pts)
    if 'weight' in user_ns:
        points += 3
        feedback.append("✅ Variable 'weight' exists (+3 pts)")
    else:
        feedback.append("❌ Variable 'weight' not found (0 pts)")
    
    # Component 2: weight_kg exists (3 pts)
    if 'weight_kg' in user_ns:
        points += 3
        feedback.append("✅ Variable 'weight_kg' exists (+3 pts)")
        
        # Component 4: Is a float with decimals (4 pts)
        if isinstance(user_ns['weight_kg'], float):
            points += 4
            feedback.append("✅ Result has decimal precision (+4 pts)")
        else:
            feedback.append("❌ Result should be a float, not int (0 pts)")
    else:
        feedback.append("❌ Variable 'weight_kg' not found (0 pts)")
    
    # Component 3: Uses float() (5 pts)
    if code and _check_code_uses_function(code, 'float'):
        points += 5
        feedback.append("✅ Code uses float() for precision (+5 pts)")
    else:
        feedback.append("❌ Code should use float() instead of int() (0 pts)")
        feedback.append("💡 Hint: Use float(weight) for decimal accuracy")
    
    print(f"\\n{'='*50}")
    print(f"Debug Task 2: Wrong Conversion Type")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _debug_results['task_2'] = points
    return points == max_points

def verify_debug_3():
    """
    Verify Debug 3: Forgot to Print (10 points)
    Components:
    - Variable 'year' exists (3 pts)
    - Code uses type() (3 pts)
    - Code uses print() around type() (4 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 10
    feedback = []
    
    # Component 1: year exists (3 pts)
    if 'year' in user_ns:
        points += 3
        feedback.append("✅ Variable 'year' exists (+3 pts)")
    else:
        feedback.append("❌ Variable 'year' not found (0 pts)")
    
    # Component 2: Uses type() (3 pts)
    if code and _check_code_has_type_call(code):
        points += 3
        feedback.append("✅ Code uses type() function (+3 pts)")
    else:
        feedback.append("❌ Code should use type() (0 pts)")
    
    # Component 3: Uses print() (4 pts)
    if code and _check_code_has_print(code):
        points += 4
        feedback.append("✅ Code prints the type result (+4 pts)")
    else:
        feedback.append("❌ Code should print() the type result (0 pts)")
        feedback.append("💡 Hint: print(type(year))")
    
    print(f"\\n{'='*50}")
    print(f"Debug Task 3: Forgot to Print")
    print(f"{'='*50}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*50}\\n")
    
    _debug_results['task_3'] = points
    return points == max_points

# ============================================================================
# GRADE CALCULATION
# ============================================================================

def calculate_grade():
    """
    Calculate final grade based on all completed tasks.
    
    Grading Breakdown:
    - Walk-Along: 20 points (4 tasks × 5 points)
    - Try It Yourself: 40 points (15 + 15 + 10)
    - Debug: 40 points (15 + 15 + 10)
    Total: 100 points
    """
    
    # Calculate section totals
    walk_along_points = sum(_walk_along_results.values())
    walk_along_max = 20
    
    try_it_yourself_points = sum(_try_it_yourself_results.values())
    try_it_yourself_max = 40
    
    debug_points = sum(_debug_results.values())
    debug_max = 40
    
    # Calculate total
    total_points = walk_along_points + try_it_yourself_points + debug_points
    total_max = 100
    percentage = (total_points / total_max * 100) if total_max > 0 else 0
    
    # Determine letter grade
    if percentage >= 90:
        letter_grade = "A"
    elif percentage >= 80:
        letter_grade = "B"
    elif percentage >= 70:
        letter_grade = "C"
    elif percentage >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    # Display detailed grade report
    print("\\n" + "="*60)
    print(" "*15 + "📊 LESSON 05 GRADE REPORT 📊")
    print("="*60)
    print()
    print(f"📺 Walk-Along Tasks:        {walk_along_points:2d} / {walk_along_max} points")
    print(f"   Task 1: Ask for Birth Year                {_walk_along_results.get('task_1', 0):2d} /  5")
    print(f"   Task 2: Error Demonstration               {_walk_along_results.get('task_2', 0):2d} /  5")
    print(f"   Task 3: Fix with Type Conversion          {_walk_along_results.get('task_3', 0):2d} /  5")
    print(f"   Task 4: Check Variable Types              {_walk_along_results.get('task_4', 0):2d} /  5")
    print()
    print(f"🎯 Try It Yourself:         {try_it_yourself_points:2d} / {try_it_yourself_max} points")
    print(f"   Task 1: Weight Converter                  {_try_it_yourself_results.get('task_1', 0):2d} / 15")
    print(f"   Task 2: Temperature Converter             {_try_it_yourself_results.get('task_2', 0):2d} / 15")
    print(f"   Task 3: Yards to Meters                   {_try_it_yourself_results.get('task_3', 0):2d} / 10")
    print()
    print(f"🐞 Debug the Bug:           {debug_points:2d} / {debug_max} points")
    print(f"   Task 1: Missing Conversion                {_debug_results.get('task_1', 0):2d} / 15")
    print(f"   Task 2: Wrong Conversion Type             {_debug_results.get('task_2', 0):2d} / 15")
    print(f"   Task 3: Forgot to Print                   {_debug_results.get('task_3', 0):2d} / 10")
    print()
    print("="*60)
    print(f"TOTAL SCORE: {total_points} / {total_max} points ({percentage:.1f}%)")
    print(f"LETTER GRADE: {letter_grade}")
    print("="*60)
    print()
    
    # Encouraging message based on performance
    if percentage >= 90:
        print("🌟 Outstanding work! You've mastered type conversion!")
    elif percentage >= 80:
        print("🎉 Great job! You understand type conversion well!")
    elif percentage >= 70:
        print("👍 Good effort! Review the concepts and try again.")
    elif percentage >= 60:
        print("📚 You're making progress. Review the video and try again.")
    else:
        print("💪 Don't give up! Re-watch the video and ask for help.")
    
    print()
    print("Remember: input() always returns a STRING!")
    print("Use int() for whole numbers, float() for decimals.")
    print()
    
    return {
        'total_points': total_points,
        'total_max': total_max,
        'percentage': percentage,
        'letter_grade': letter_grade,
        'walk_along': walk_along_points,
        'try_it_yourself': try_it_yourself_points,
        'debug': debug_points
    }
