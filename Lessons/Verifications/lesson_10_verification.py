"""
Verification System for Lesson 10: Logical Operators
Auto-grading functions with detailed feedback
"""

import ast
import inspect

# Points tracking
_walk_along_points = {}
_try_it_yourself_points = {}
_debug_points = {}

def _get_code_from_notebook():
    """Extract code from the calling cell"""
    frame = inspect.currentframe().f_back.f_back
    if 'In' in frame.f_globals:
        cell_number = len(frame.f_globals['In']) - 2
        if cell_number >= 0:
            return frame.f_globals['In'][cell_number]
    return None

def _check_code_content(code, required_elements):
    """Check if code contains required elements"""
    if code is None:
        return False, "Could not read your code"
    
    code_lower = code.lower()
    missing = [elem for elem in required_elements if elem.lower() not in code_lower]
    
    if missing:
        return False, f"Missing required element(s): {', '.join(missing)}"
    return True, "All required elements found"

def _check_variables_exist(var_names):
    """Check if variables exist in the calling scope"""
    frame = inspect.currentframe().f_back.f_back
    missing = [var for var in var_names if var not in frame.f_locals]
    return len(missing) == 0, missing

# Walk-Along Verifications

def verify_walk_along_1():
    """Verify Walk-Along Task 1: AND operator"""
    print("🔍 Checking Walk-Along Task 1...")
    
    code = _get_code_from_notebook()
    required = ['has_high_income', 'has_good_credit', 'and', 'if', 'eligible for loan']
    
    success, msg = _check_code_content(code, required)
    if not success:
        print(f"❌ {msg}")
        _walk_along_points['task1'] = 0
        return
    
    # Check variables exist
    frame = inspect.currentframe().f_back
    if 'has_high_income' not in frame.f_locals or 'has_good_credit' not in frame.f_locals:
        print("❌ Variables not found. Did you create has_high_income and has_good_credit?")
        _walk_along_points['task1'] = 0
        return
    
    has_high_income = frame.f_locals.get('has_high_income')
    has_good_credit = frame.f_locals.get('has_good_credit')
    
    if not isinstance(has_high_income, bool) or not isinstance(has_good_credit, bool):
        print("❌ Variables must be boolean (True/False)")
        _walk_along_points['task1'] = 0
        return
    
    if 'and' not in code.lower():
        print("❌ You must use the 'and' operator")
        _walk_along_points['task1'] = 0
        return
    
    print("✅ Perfect! You correctly used the 'and' operator")
    print("   💡 Both conditions must be True for the overall result to be True")
    _walk_along_points['task1'] = 5
    print("   📊 Points earned: 5/5")

def verify_walk_along_2():
    """Verify Walk-Along Task 2: OR operator"""
    print("🔍 Checking Walk-Along Task 2...")
    
    code = _get_code_from_notebook()
    required = ['has_high_income', 'has_good_credit', 'or']
    
    success, msg = _check_code_content(code, required)
    if not success:
        print(f"❌ {msg}")
        _walk_along_points['task2'] = 0
        return
    
    frame = inspect.currentframe().f_back
    if 'has_high_income' not in frame.f_locals or 'has_good_credit' not in frame.f_locals:
        print("❌ Variables not found")
        _walk_along_points['task2'] = 0
        return
    
    if 'or' not in code.lower():
        print("❌ You must use the 'or' operator (not 'and')")
        _walk_along_points['task2'] = 0
        return
    
    if 'and' in code.lower() and 'or' not in code.lower():
        print("❌ This task requires 'or', not 'and'")
        _walk_along_points['task2'] = 0
        return
    
    print("✅ Great! You correctly used the 'or' operator")
    print("   💡 At least one condition must be True for the overall result to be True")
    _walk_along_points['task2'] = 5
    print("   📊 Points earned: 5/5")

def verify_walk_along_3():
    """Verify Walk-Along Task 3: NOT operator"""
    print("🔍 Checking Walk-Along Task 3...")
    
    code = _get_code_from_notebook()
    required = ['has_good_credit', 'has_criminal_record', 'not']
    
    success, msg = _check_code_content(code, required)
    if not success:
        print(f"❌ {msg}")
        _walk_along_points['task3'] = 0
        return
    
    frame = inspect.currentframe().f_back
    if 'has_good_credit' not in frame.f_locals or 'has_criminal_record' not in frame.f_locals:
        print("❌ Variables not found")
        _walk_along_points['task3'] = 0
        return
    
    if 'not' not in code.lower():
        print("❌ You must use the 'not' operator")
        _walk_along_points['task3'] = 0
        return
    
    print("✅ Excellent! You correctly used the 'not' operator")
    print("   💡 'not' inverts boolean values (True becomes False, False becomes True)")
    _walk_along_points['task3'] = 5
    print("   📊 Points earned: 5/5")

# Try It Yourself Verifications

def verify_try_it_1():
    """Verify Try It Yourself 1: Playoff eligibility"""
    print("🔍 Checking Try It Yourself 1...")
    
    code = _get_code_from_notebook()
    required = ['wins', 'win_percentage', 'and', 'if']
    
    success, msg = _check_code_content(code, required)
    if not success:
        print(f"❌ {msg}")
        _try_it_yourself_points['task1'] = 0
        return
    
    frame = inspect.currentframe().f_back
    if 'wins' not in frame.f_locals or 'win_percentage' not in frame.f_locals:
        print("❌ Variables 'wins' and 'win_percentage' not found")
        _try_it_yourself_points['task1'] = 0
        return
    
    if 'and' not in code.lower():
        print("❌ You must use the 'and' operator (both conditions must be true)")
        _try_it_yourself_points['task1'] = 0
        return
    
    # Check if they have proper comparison
    if '>=' not in code and '> ' not in code:
        print("⚠️ Make sure you're checking if values meet the minimum requirements")
        _try_it_yourself_points['task1'] = 10
        print("   📊 Partial credit: 10/15")
        return
    
    print("✅ Perfect! Your playoff eligibility checker works correctly!")
    print("   🏀 Both wins AND win_percentage must meet requirements")
    _try_it_yourself_points['task1'] = 15
    print("   📊 Points earned: 15/15")

def verify_try_it_2():
    """Verify Try It Yourself 2: All-Star selection"""
    print("🔍 Checking Try It Yourself 2...")
    
    code = _get_code_from_notebook()
    required = ['points_per_game', 'assists_per_game', 'or', 'if']
    
    success, msg = _check_code_content(code, required)
    if not success:
        print(f"❌ {msg}")
        _try_it_yourself_points['task2'] = 0
        return
    
    frame = inspect.currentframe().f_back
    if 'points_per_game' not in frame.f_locals or 'assists_per_game' not in frame.f_locals:
        print("❌ Variables not found")
        _try_it_yourself_points['task2'] = 0
        return
    
    if 'or' not in code.lower():
        print("❌ You must use the 'or' operator (at least ONE condition must be true)")
        _try_it_yourself_points['task2'] = 0
        return
    
    if 'and' in code.lower() and 'or' not in code.lower():
        print("❌ This scenario requires 'or', not 'and' (player needs high points OR assists)")
        _try_it_yourself_points['task2'] = 0
        return
    
    print("✅ Excellent! Your All-Star selection logic is correct!")
    print("   ⭐ Player qualifies if they meet EITHER threshold")
    _try_it_yourself_points['task2'] = 20
    print("   📊 Points earned: 20/20")

def verify_try_it_3():
    """Verify Try It Yourself 3: Player availability"""
    print("🔍 Checking Try It Yourself 3...")
    
    code = _get_code_from_notebook()
    required = ['is_injured', 'is_suspended', 'not']
    
    success, msg = _check_code_content(code, required)
    if not success:
        print(f"❌ {msg}")
        _try_it_yourself_points['task3'] = 0
        return
    
    frame = inspect.currentframe().f_back
    if 'is_injured' not in frame.f_locals or 'is_suspended' not in frame.f_locals:
        print("❌ Variables not found")
        _try_it_yourself_points['task3'] = 0
        return
    
    if 'not' not in code.lower():
        print("❌ You must use the 'not' operator")
        _try_it_yourself_points['task3'] = 0
        return
    
    # Check for proper logic (should check NOT injured AND NOT suspended)
    not_count = code.lower().count('not')
    if not_count < 2:
        print("⚠️ You should use 'not' for both conditions (NOT injured AND NOT suspended)")
        _try_it_yourself_points['task3'] = 10
        print("   📊 Partial credit: 10/15")
        return
    
    print("✅ Perfect! Your player availability checker is correct!")
    print("   ✅ Player must be NOT injured AND NOT suspended")
    _try_it_yourself_points['task3'] = 15
    print("   📊 Points earned: 15/15")

# Debug Verifications

def verify_debug_1():
    """Verify Debug Task 1: Wrong operator"""
    print("🔍 Checking Debug Task 1...")
    
    code = _get_code_from_notebook()
    
    if code is None:
        print("❌ Could not read your code")
        _debug_points['task1'] = 0
        return
    
    # Check if they fixed it to 'and'
    if 'not is_injured and completed_training' in code or 'completed_training and not is_injured' in code:
        print("✅ Bug fixed! You correctly changed 'or' to 'and'")
        print("   💡 Both conditions must be True (NOT injured AND completed training)")
        _debug_points['task1'] = 10
        print("   📊 Points earned: 10/10")
    elif 'or' in code.lower():
        print("❌ The bug is still there! You need to change 'or' to 'and'")
        print("   💡 Think: Do we need BOTH conditions or just ONE?")
        _debug_points['task1'] = 0
    else:
        print("⚠️ Make sure you're checking both conditions correctly")
        _debug_points['task1'] = 5
        print("   📊 Partial credit: 5/10")

def verify_debug_2():
    """Verify Debug Task 2: Incorrect NOT usage"""
    print("🔍 Checking Debug Task 2...")
    
    code = _get_code_from_notebook()
    
    if code is None:
        print("❌ Could not read your code")
        _debug_points['task2'] = 0
        return
    
    # Check if they moved 'not' to apply only to season_over
    if ('has_wins and not season_over' in code or 'not season_over and has_wins' in code):
        print("✅ Bug fixed! You correctly moved 'not' to apply only to season_over")
        print("   💡 'not' should only invert season_over, not the entire condition")
        _debug_points['task2'] = 15
        print("   📊 Points earned: 15/15")
    elif 'not (has_wins and season_over)' in code or 'not(has_wins and season_over)' in code:
        print("❌ The bug is still there! 'not' is applied to the entire condition")
        print("   💡 Hint: Remove the parentheses and apply 'not' only to season_over")
        _debug_points['task2'] = 0
    else:
        print("⚠️ Code structure doesn't match expected solution")
        _debug_points['task2'] = 8
        print("   📊 Partial credit: 8/15")

def verify_debug_3():
    """Verify Debug Task 3: Missing parentheses"""
    print("🔍 Checking Debug Task 3...")
    
    code = _get_code_from_notebook()
    
    if code is None:
        print("❌ Could not read your code")
        _debug_points['task3'] = 0
        return
    
    # Check if they added parentheses around (high_score or many_assists)
    if '(high_score or many_assists) and not fouled_out' in code or '(many_assists or high_score) and not fouled_out' in code:
        print("✅ Bug fixed! You correctly added parentheses")
        print("   💡 Parentheses ensure (high_score OR many_assists) is evaluated first")
        _debug_points['task3'] = 10
        print("   📊 Points earned: 10/10")
    elif '(' not in code or ')' not in code:
        print("❌ The bug is still there! You need to add parentheses")
        print("   💡 Hint: Put parentheses around (high_score or many_assists)")
        _debug_points['task3'] = 0
    else:
        print("⚠️ Parentheses placement might not be correct")
        _debug_points['task3'] = 5
        print("   📊 Partial credit: 5/10")

def calculate_grade():
    """Calculate and display the final grade"""
    walk_along_total = sum(_walk_along_points.values())
    try_it_total = sum(_try_it_yourself_points.values())
    debug_total = sum(_debug_points.values())
    
    total_points = walk_along_total + try_it_total + debug_total
    
    print("\n" + "="*60)
    print("📊 LESSON 10 GRADE REPORT")
    print("="*60)
    print(f"\n📺 Walk-Along Tasks: {walk_along_total}/15 points")
    for task, points in _walk_along_points.items():
        status = "✅" if points > 0 else "❌"
        print(f"   {status} {task}: {points} points")
    
    print(f"\n🎯 Try It Yourself: {try_it_total}/50 points")
    for task, points in _try_it_yourself_points.items():
        status = "✅" if points > 0 else "❌"
        print(f"   {status} {task}: {points} points")
    
    print(f"\n🐞 Debug Challenges: {debug_total}/35 points")
    for task, points in _debug_points.items():
        status = "✅" if points > 0 else "❌"
        print(f"   {status} {task}: {points} points")
    
    print(f"\n{'='*60}")
    print(f"🎯 TOTAL SCORE: {total_points}/100 points")
    
    # Letter grade
    if total_points >= 90:
        letter = "A"
        emoji = "🌟"
    elif total_points >= 80:
        letter = "B"
        emoji = "👍"
    elif total_points >= 70:
        letter = "C"
        emoji = "✓"
    elif total_points >= 60:
        letter = "D"
        emoji = "📝"
    else:
        letter = "F"
        emoji = "📚"
    
    print(f"{emoji} Letter Grade: {letter}")
    print(f"{'='*60}\n")
    
    if total_points < 100:
        print("💡 TIP: Review tasks where you lost points and try again!")
        print("   The verification messages tell you exactly what to fix.\n")
    else:
        print("🎉 PERFECT SCORE! You've mastered logical operators!\n")
