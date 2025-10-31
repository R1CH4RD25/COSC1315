"""
Lesson 08: Arithmetic Operations - Verification Functions
COSC 1315 - Introduction to Computer Programming

This module provides automated verification for student code in the Arithmetic Operations lesson.

Grading Breakdown:
- Walk-Along Tasks: 15 points (4 tasks: 4 + 3 + 4 + 4 points)
- Try It Yourself: 50 points (15 + 20 + 15)
- Debug Exercises: 40 points (15 + 15 + 10)
Total: 105 points
"""

import ast
import inspect
import math

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
    """Check if code uses a specific function"""
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

def _check_code_uses_operator(code, operator):
    """Check if code uses a specific operator"""
    if not code:
        return False
    
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False
    
    op_map = {
        '+': ast.Add,
        '-': ast.Sub,
        '*': ast.Mult,
        '/': ast.Div,
        '//': ast.FloorDiv,
        '%': ast.Mod,
        '**': ast.Pow,
        '+=': ast.AugAssign,
        '-=': ast.AugAssign,
    }
    
    target_op = op_map.get(operator)
    if not target_op:
        return False
    
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, target_op):
            return True
        if operator in ['+=', '-='] and isinstance(node, ast.AugAssign):
            return True
    
    return False

# ============================================================================
# WALK-ALONG TASKS (15 points total: 4 + 3 + 4 + 4 points)
# ============================================================================

def verify_walk_along_1():
    """
    Verify Walk-Along Task 1: Basic Arithmetic Operations (4 points)
    Components:
    - Code prints 7 lines of output (2 pts)
    - Code uses all operators: +, -, *, /, //, %, ** (2 pts)
    """
    code = _get_previous_cell_code()
    points = 0
    max_points = 4
    feedback = []
    
    # Component 1: Prints results (2 pts)
    if code and code.count('print(') >= 7:
        points += 2
        feedback.append("✅ Code prints all 7 operations (+2 pts)")
        feedback.append("🏈 TOUCHDOWN! You mastered all seven arithmetic operators!")
    else:
        feedback.append("❌ Code should print 7 lines (one for each operator) (0 pts)")
        feedback.append("💡 Hint: print(10 + 3), print(10 - 3), etc.")
    
    # Component 2: Uses operators (2 pts)
    operators_used = 0
    if code:
        if '+' in code: operators_used += 1
        if '-' in code: operators_used += 1
        if '*' in code: operators_used += 1
        if '/' in code: operators_used += 1
        if '//' in code: operators_used += 1
        if '%' in code: operators_used += 1
        if '**' in code: operators_used += 1
    
    if operators_used >= 7:
        points += 2
        feedback.append("✅ Code uses all operators: +, -, *, /, //, %, ** (+2 pts)")
    else:
        feedback.append(f"❌ Found {operators_used}/7 operators (0 pts)")
        feedback.append("💡 Hint: Make sure to use +, -, *, /, //, %, **")
    
    print(f"\\n{'='*60}")
    print(f"Walk-Along Task 1: Basic Arithmetic Operations")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _walk_along_results['task_1'] = points
    return points == max_points

def verify_walk_along_2():
    """
    Verify Walk-Along Task 2: Augmented Assignment Operators (3 points)
    Components:
    - Variable 'x' exists and starts at 10 (1 pt)
    - Code uses += operator (1 pt)
    - Code uses -= operator (1 pt)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 3
    feedback = []
    
    # Component 1: Variable x (1 pt)
    if 'x' in user_ns:
        points += 1
        feedback.append("✅ Variable 'x' exists (+1 pt)")
    else:
        feedback.append("❌ Variable 'x' not found (0 pts)")
    
    # Component 2: Uses += (1 pt)
    if code and '+=' in code:
        points += 1
        feedback.append("✅ Code uses += operator (+1 pt)")
        feedback.append("🏈 FIELD GOAL! Augmented assignment makes code cleaner!")
    else:
        feedback.append("❌ Code should use += operator (0 pts)")
    
    # Component 3: Uses -= (1 pt)
    if code and '-=' in code:
        points += 1
        feedback.append("✅ Code uses -= operator (+1 pt)")
    else:
        feedback.append("❌ Code should use -= operator (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Walk-Along Task 2: Augmented Assignment Operators")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _walk_along_results['task_2'] = points
    return points == max_points

def verify_walk_along_3():
    """
    Verify Walk-Along Task 3: Operator Precedence (4 points)
    Components:
    - Variable 'x' exists (2 pts)
    - x equals 22 (correct precedence calculation) (2 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 4
    feedback = []
    
    # Component 1: Variable x exists (2 pts)
    if 'x' in user_ns:
        points += 2
        feedback.append("✅ Variable 'x' exists (+2 pts)")
        
        # Component 2: x equals 22 (2 pts)
        if user_ns['x'] == 22:
            points += 2
            feedback.append("✅ x equals 22 - correct operator precedence! (+2 pts)")
            feedback.append("🏈 TOUCHDOWN! You understand PEMDAS!")
            feedback.append("💡 Breakdown: 2**2=4, then 3*4=12, then 10+12=22")
        else:
            feedback.append(f"❌ x equals {user_ns['x']}, should be 22 (0 pts)")
            feedback.append("💡 Remember: Exponentiation first, then multiplication, then addition")
    else:
        feedback.append("❌ Variable 'x' not found (0 pts)")
        feedback.append("💡 Hint: x = 10 + 3 * 2 ** 2")
    
    print(f"\\n{'='*60}")
    print(f"Walk-Along Task 3: Operator Precedence")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _walk_along_results['task_3'] = points
    return points == max_points

def verify_walk_along_4():
    """
    Verify Walk-Along Task 4: Using Math Functions (4 points)
    Components:
    - Code imports math module (1 pt)
    - Code uses round() (1 pt)
    - Code uses abs() (1 pt)
    - Code uses math.ceil() or math.floor() (1 pt)
    """
    code = _get_previous_cell_code()
    points = 0
    max_points = 4
    feedback = []
    
    # Component 1: Imports math (1 pt)
    if code and 'import math' in code:
        points += 1
        feedback.append("✅ Code imports math module (+1 pt)")
    else:
        feedback.append("❌ Code should import math module (0 pts)")
    
    # Component 2: Uses round() (1 pt)
    if code and _check_code_uses_function(code, 'round'):
        points += 1
        feedback.append("✅ Code uses round() function (+1 pt)")
    else:
        feedback.append("❌ Code should use round() (0 pts)")
    
    # Component 3: Uses abs() (1 pt)
    if code and _check_code_uses_function(code, 'abs'):
        points += 1
        feedback.append("✅ Code uses abs() function (+1 pt)")
    else:
        feedback.append("❌ Code should use abs() (0 pts)")
    
    # Component 4: Uses math.ceil or math.floor (1 pt)
    if code and ('math.ceil' in code or 'math.floor' in code):
        points += 1
        feedback.append("✅ Code uses math.ceil() or math.floor() (+1 pt)")
        feedback.append("🏈 FIELD GOAL! You can use advanced math functions!")
    else:
        feedback.append("❌ Code should use math.ceil() or math.floor() (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Walk-Along Task 4: Using Math Functions")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _walk_along_results['task_4'] = points
    return points == max_points

# ============================================================================
# TRY IT YOURSELF (50 points total: 15 + 20 + 15 points)
# ============================================================================

def verify_try_it_yourself_1():
    """
    Verify Try It Yourself 1: Quarterback Passer Rating (15 points)
    Components:
    - Variables completions, attempts, passing_yards exist (3 pts)
    - completion_percentage calculated correctly (4 pts)
    - yards_per_attempt calculated correctly (4 pts)
    - Both results printed (4 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: Required variables exist (3 pts)
    required_vars = ['completions', 'attempts', 'passing_yards']
    all_exist = all(var in user_ns for var in required_vars)
    
    if all_exist:
        points += 3
        feedback.append("✅ All required variables exist (+3 pts)")
    else:
        missing = [var for var in required_vars if var not in user_ns]
        feedback.append(f"❌ Missing variables: {', '.join(missing)} (0 pts)")
    
    # Component 2: completion_percentage (4 pts)
    if 'completion_percentage' in user_ns and all_exist:
        expected = (user_ns['completions'] / user_ns['attempts']) * 100
        actual = user_ns['completion_percentage']
        
        if abs(actual - expected) < 0.01:
            points += 4
            feedback.append("✅ completion_percentage calculated correctly (+4 pts)")
            feedback.append("🏈 PASS COMPLETE! Great quarterback stats!")
        else:
            feedback.append(f"❌ completion_percentage is {actual:.2f}, should be {expected:.2f} (0 pts)")
    elif 'completion_percentage' not in user_ns:
        feedback.append("❌ completion_percentage variable not found (0 pts)")
        feedback.append("💡 Hint: (completions / attempts) * 100")
    
    # Component 3: yards_per_attempt (4 pts)
    if 'yards_per_attempt' in user_ns and all_exist:
        expected = user_ns['passing_yards'] / user_ns['attempts']
        actual = user_ns['yards_per_attempt']
        
        if abs(actual - expected) < 0.01:
            points += 4
            feedback.append("✅ yards_per_attempt calculated correctly (+4 pts)")
        else:
            feedback.append(f"❌ yards_per_attempt is {actual:.2f}, should be {expected:.2f} (0 pts)")
    elif 'yards_per_attempt' not in user_ns:
        feedback.append("❌ yards_per_attempt variable not found (0 pts)")
        feedback.append("💡 Hint: passing_yards / attempts")
    
    # Component 4: Prints results (4 pts)
    if code and code.count('print(') >= 2:
        points += 4
        feedback.append("✅ Code prints both results (+4 pts)")
    else:
        feedback.append("❌ Code should print both percentages (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Try It Yourself 1: Quarterback Passer Rating")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _try_it_yourself_results['task_1'] = points
    return points == max_points

def verify_try_it_yourself_2():
    """
    Verify Try It Yourself 2: Basketball Scoring Calculator (20 points)
    Components:
    - All required variables exist (4 pts)
    - total_points calculated correctly (6 pts)
    - shooting_percentage calculated and rounded (6 pts)
    - Both results printed (4 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 20
    feedback = []
    
    # Component 1: Required variables exist (4 pts)
    required_vars = [
        'field_goals_made', 'three_pointers_made', 'free_throws_made',
        'field_goals_attempted', 'three_pointers_attempted'
    ]
    all_exist = all(var in user_ns for var in required_vars)
    
    if all_exist:
        points += 4
        feedback.append("✅ All required variables exist (+4 pts)")
    else:
        missing = [var for var in required_vars if var not in user_ns]
        feedback.append(f"❌ Missing variables: {', '.join(missing)} (0 pts)")
    
    # Component 2: total_points (6 pts)
    if 'total_points' in user_ns and all_exist:
        expected = (user_ns['field_goals_made'] * 2) + (user_ns['three_pointers_made'] * 3) + user_ns['free_throws_made']
        actual = user_ns['total_points']
        
        if actual == expected:
            points += 6
            feedback.append("✅ total_points calculated correctly (+6 pts)")
            feedback.append("🏈 SLAM DUNK! Perfect scoring calculation!")
        else:
            feedback.append(f"❌ total_points is {actual}, should be {expected} (0 pts)")
            feedback.append("💡 Hint: (FGs * 2) + (3Ps * 3) + FTs")
    elif 'total_points' not in user_ns:
        feedback.append("❌ total_points variable not found (0 pts)")
    
    # Component 3: shooting_percentage (6 pts)
    if 'shooting_percentage' in user_ns and all_exist:
        total_made = user_ns['field_goals_made'] + user_ns['three_pointers_made']
        total_attempted = user_ns['field_goals_attempted'] + user_ns['three_pointers_attempted']
        expected = round((total_made / total_attempted) * 100, 1)
        actual = user_ns['shooting_percentage']
        
        if abs(actual - expected) < 0.1:
            points += 6
            feedback.append("✅ shooting_percentage calculated and rounded correctly (+6 pts)")
        else:
            feedback.append(f"❌ shooting_percentage is {actual}, should be {expected} (0 pts)")
    elif 'shooting_percentage' not in user_ns:
        feedback.append("❌ shooting_percentage variable not found (0 pts)")
        feedback.append("💡 Hint: Use round() to round to 1 decimal place")
    
    # Component 4: Prints results (4 pts)
    if code and code.count('print(') >= 2:
        points += 4
        feedback.append("✅ Code prints both results (+4 pts)")
    else:
        feedback.append("❌ Code should print both total points and percentage (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Try It Yourself 2: Basketball Scoring Calculator")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _try_it_yourself_results['task_2'] = points
    return points == max_points

def verify_try_it_yourself_3():
    """
    Verify Try It Yourself 3: Team Season Statistics (15 points)
    Components:
    - All required variables exist (3 pts)
    - win_percentage calculated and rounded (4 pts)
    - points_per_game uses floor division (4 pts)
    - remaining_points uses modulus (4 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: Required variables exist (3 pts)
    required_vars = ['wins', 'losses', 'total_points', 'total_games']
    all_exist = all(var in user_ns for var in required_vars)
    
    if all_exist:
        points += 3
        feedback.append("✅ All required variables exist (+3 pts)")
    else:
        missing = [var for var in required_vars if var not in user_ns]
        feedback.append(f"❌ Missing variables: {', '.join(missing)} (0 pts)")
    
    # Component 2: win_percentage (4 pts)
    if 'win_percentage' in user_ns and all_exist:
        expected = round((user_ns['wins'] / user_ns['total_games']) * 100, 1)
        actual = user_ns['win_percentage']
        
        if abs(actual - expected) < 0.1:
            points += 4
            feedback.append("✅ win_percentage calculated and rounded correctly (+4 pts)")
        else:
            feedback.append(f"❌ win_percentage is {actual}, should be {expected} (0 pts)")
    elif 'win_percentage' not in user_ns:
        feedback.append("❌ win_percentage variable not found (0 pts)")
    
    # Component 3: points_per_game uses // (4 pts)
    if 'points_per_game' in user_ns and all_exist:
        expected = user_ns['total_points'] // user_ns['total_games']
        actual = user_ns['points_per_game']
        
        if actual == expected and isinstance(actual, int):
            points += 4
            feedback.append("✅ points_per_game uses floor division correctly (+4 pts)")
            feedback.append("🏈 INTERCEPTION! You caught the floor division operator!")
        else:
            feedback.append(f"❌ points_per_game should use // operator (0 pts)")
            feedback.append("💡 Hint: Use // for floor division, not /")
    elif 'points_per_game' not in user_ns:
        feedback.append("❌ points_per_game variable not found (0 pts)")
    
    # Component 4: remaining_points uses % (4 pts)
    if 'remaining_points' in user_ns and all_exist:
        expected = user_ns['total_points'] % user_ns['total_games']
        actual = user_ns['remaining_points']
        
        if actual == expected:
            points += 4
            feedback.append("✅ remaining_points uses modulus correctly (+4 pts)")
        else:
            feedback.append(f"❌ remaining_points should use % operator (0 pts)")
            feedback.append("💡 Hint: Use % to get the remainder")
    elif 'remaining_points' not in user_ns:
        feedback.append("❌ remaining_points variable not found (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Try It Yourself 3: Team Season Statistics")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _try_it_yourself_results['task_3'] = points
    return points == max_points

# ============================================================================
# DEBUG TASKS (40 points total: 15 + 15 + 10 points)
# ============================================================================

def verify_debug_1():
    """
    Verify Debug Task 1: Wrong Division Operator (15 points)
    Components:
    - Variable total_players exists and equals 45 (3 pts)
    - Variable num_teams exists and equals 3 (3 pts)
    - Variable players_per_team exists (3 pts)
    - players_per_team equals 15 (integer, not float) (6 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: total_players (3 pts)
    if 'total_players' in user_ns and user_ns['total_players'] == 45:
        points += 3
        feedback.append("✅ total_players = 45 (+3 pts)")
    else:
        feedback.append("❌ total_players should be 45 (0 pts)")
    
    # Component 2: num_teams (3 pts)
    if 'num_teams' in user_ns and user_ns['num_teams'] == 3:
        points += 3
        feedback.append("✅ num_teams = 3 (+3 pts)")
    else:
        feedback.append("❌ num_teams should be 3 (0 pts)")
    
    # Component 3: players_per_team exists (3 pts)
    if 'players_per_team' in user_ns:
        points += 3
        feedback.append("✅ players_per_team variable exists (+3 pts)")
        
        # Component 4: players_per_team equals 15 and is int (6 pts)
        if user_ns['players_per_team'] == 15 and isinstance(user_ns['players_per_team'], int):
            points += 6
            feedback.append("✅ players_per_team = 15 (integer) - BUG FIXED! (+6 pts)")
            feedback.append("🏈 FUMBLE RECOVERY! You fixed the division operator!")
            feedback.append("💡 Great job using // instead of /")
        elif user_ns['players_per_team'] == 15.0:
            feedback.append("❌ players_per_team is 15.0 (float), should be 15 (int) (0 pts)")
            feedback.append("💡 Hint: Use // for floor division to get an integer")
        else:
            feedback.append(f"❌ players_per_team is {user_ns['players_per_team']}, should be 15 (0 pts)")
    else:
        feedback.append("❌ players_per_team variable not found (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Debug Task 1: Wrong Division Operator")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _debug_results['task_1'] = points
    return points == max_points

def verify_debug_2():
    """
    Verify Debug Task 2: Operator Precedence Error (15 points)
    Components:
    - Variables ticket_price, num_tickets, parking_fee exist (3 pts)
    - Variable total_cost exists (3 pts)
    - total_cost equals 220 (correct calculation) (9 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 15
    feedback = []
    
    # Component 1: Required variables (3 pts)
    required_vars = ['ticket_price', 'num_tickets', 'parking_fee']
    if all(var in user_ns for var in required_vars):
        points += 3
        feedback.append("✅ All required variables exist (+3 pts)")
    else:
        feedback.append("❌ Missing required variables (0 pts)")
    
    # Component 2: total_cost exists (3 pts)
    if 'total_cost' in user_ns:
        points += 3
        feedback.append("✅ total_cost variable exists (+3 pts)")
        
        # Component 3: total_cost equals 220 (9 pts)
        if user_ns['total_cost'] == 220:
            points += 9
            feedback.append("✅ total_cost = 220 - BUG FIXED! (+9 pts)")
            feedback.append("🏈 TOUCHDOWN! You mastered operator precedence!")
            feedback.append("💡 Perfect: (50 * 4) + 20 = 220")
        else:
            feedback.append(f"❌ total_cost is {user_ns['total_cost']}, should be 220 (0 pts)")
            feedback.append("💡 Hint: (ticket_price * num_tickets) + parking_fee")
    else:
        feedback.append("❌ total_cost variable not found (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Debug Task 2: Operator Precedence Error")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _debug_results['task_2'] = points
    return points == max_points

def verify_debug_3():
    """
    Verify Debug Task 3: Wrong Augmented Assignment Operator (10 points)
    Components:
    - Variable score exists and starts at 10 (3 pts)
    - Final score equals 15 (7 pts)
    """
    user_ns = _get_user_namespace()
    code = _get_previous_cell_code()
    points = 0
    max_points = 10
    feedback = []
    
    # Component 1: score exists (3 pts)
    if 'score' in user_ns:
        points += 3
        feedback.append("✅ score variable exists (+3 pts)")
        
        # Component 2: score equals 15 (7 pts)
        if user_ns['score'] == 15:
            points += 7
            feedback.append("✅ score = 15 - BUG FIXED! (+7 pts)")
            feedback.append("🏈 EXTRA POINT! You fixed the augmented operator!")
            feedback.append("💡 Great job using += instead of *=")
        elif user_ns['score'] == 50:
            feedback.append("❌ score is 50 (still using *=), should be 15 (0 pts)")
            feedback.append("💡 Hint: Change *= to += to add instead of multiply")
        else:
            feedback.append(f"❌ score is {user_ns['score']}, should be 15 (0 pts)")
    else:
        feedback.append("❌ score variable not found (0 pts)")
    
    print(f"\\n{'='*60}")
    print(f"Debug Task 3: Wrong Augmented Assignment Operator")
    print(f"{'='*60}")
    for line in feedback:
        print(line)
    print(f"\\n📊 Score: {points}/{max_points} points")
    print(f"{'='*60}\\n")
    
    _debug_results['task_3'] = points
    return points == max_points

# ============================================================================
# GRADE CALCULATION
# ============================================================================

def calculate_grade():
    """Calculate and display the total grade for the lesson"""
    walk_along_total = sum(_walk_along_results.values())
    try_it_yourself_total = sum(_try_it_yourself_results.values())
    debug_total = sum(_debug_results.values())
    
    total_points = walk_along_total + try_it_yourself_total + debug_total
    max_points = 105  # 15 + 50 + 40 + 5 bonus
    
    # Calculate percentage
    percentage = (total_points / max_points) * 100
    
    # Determine letter grade
    if percentage >= 90:
        letter_grade = "A"
        performance = "MVP! CHAMPIONSHIP PERFORMANCE!"
    elif percentage >= 80:
        letter_grade = "B"
        performance = "ALL-STAR! Great work!"
    elif percentage >= 70:
        letter_grade = "C"
        performance = "STARTER! Solid effort!"
    elif percentage >= 60:
        letter_grade = "D"
        performance = "BENCH PLAYER - Keep practicing!"
    else:
        letter_grade = "F"
        performance = "ROOKIE - Review the lesson and try again!"
    
    # Display grade report
    print("\\n" + "="*70)
    print("🏆 LESSON 08: ARITHMETIC OPERATIONS - FINAL STATS 🏆")
    print("="*70)
    print(f"\\n📊 SCORING BREAKDOWN:\\n")
    print(f"  Walk-Along Tasks:     {walk_along_total:>3}/15 points")
    print(f"  Try It Yourself:      {try_it_yourself_total:>3}/50 points")
    print(f"  Debug Challenges:     {debug_total:>3}/40 points")
    print(f"  {'-'*40}")
    print(f"  TOTAL SCORE:          {total_points:>3}/{max_points} points")
    print(f"\\n  Percentage:           {percentage:.1f}%")
    print(f"  Letter Grade:         {letter_grade}")
    print(f"\\n  🏈 {performance}")
    print("\\n" + "="*70)
    
    # Provide feedback based on performance
    if percentage >= 90:
        print("\\n🌟 Outstanding! You've mastered arithmetic operations!")
        print("You're ready to tackle more complex calculations!")
    elif percentage >= 80:
        print("\\n✨ Great job! You have a solid understanding of arithmetic.")
        print("Review any missed concepts and you'll be at 100%!")
    elif percentage >= 70:
        print("\\n👍 Good effort! You understand the basics.")
        print("Review operator precedence and practice more complex expressions.")
    else:
        print("\\n📚 Keep practicing! Here's what to focus on:")
        if walk_along_total < 12:
            print("  • Review the video lessons for basic operators")
        if try_it_yourself_total < 35:
            print("  • Practice applying operators to real-world problems")
        if debug_total < 25:
            print("  • Work on debugging operator errors")
    
    print("\\n" + "="*70)
    print("\\n💡 TIP: Review any sections where you lost points.")
    print("The verification feedback shows exactly what to improve!")
    print("\\n🎯 Next up: Lesson 09 - If Statements (making decisions in code!)")
    print("="*70 + "\\n")
    
    return total_points, percentage, letter_grade
