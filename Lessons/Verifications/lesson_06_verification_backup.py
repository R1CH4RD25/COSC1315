"""
Lesson 06: Strings - Verification System
Auto-grading functions for string manipulation tasks
"""

def verify_walk_along_1():
    """Verify Walk-Along Task 1: String Methods (5 points)"""
    try:
        # Get user's namespace
        import __main__
        user_vars = vars(__main__)
        
        # Check if course variable exists
        if 'course' not in user_vars:
            print("❌ Task 1 Not Complete")
            print("   Missing variable: 'course'")
            print("   💡 Hint: Create a variable called 'course' and set it to 'Python for Beginners'")
            return False
        
        course = user_vars['course']
        
        # Check if it's the right value
        if course != "Python for Beginners":
            print("❌ Task 1 Not Complete")
            print(f"   Variable 'course' has value: '{course}'")
            print("   Expected: 'Python for Beginners'")
            return False
        
        # Check if it's a string
        if not isinstance(course, str):
            print("❌ Task 1 Not Complete")
            print("   Variable 'course' should be a string")
            return False
        
        print("✅ Walk-Along Task 1 Complete! (+5 points)")
        print("   Great job! You created the course string and used string methods.")
        print("   🏈 Like a quarterback calling plays, you're mastering string operations!")
        return True
        
    except Exception as e:
        print("❌ Task 1 Not Complete")
        print(f"   Error: {e}")
        print("   💡 Hint: Make sure to create the 'course' variable")
        return False


def verify_walk_along_2():
    """Verify Walk-Along Task 2: String Indexing (5 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        if 'course' not in user_vars:
            print("❌ Task 2 Not Complete")
            print("   Missing variable: 'course'")
            print("   💡 Hint: You need the 'course' variable from Task 1")
            return False
        
        course = user_vars['course']
        
        # Verify the variable is correct
        if course != "Python for Beginners":
            print("❌ Task 2 Not Complete")
            print("   Variable 'course' should be 'Python for Beginners'")
            return False
        
        print("✅ Walk-Along Task 2 Complete! (+5 points)")
        print("   Excellent! You accessed characters using indexing.")
        print("   🏈 Remember: Index 0 is the first character, like the first yard on the field!")
        return True
        
    except Exception as e:
        print("❌ Task 2 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_walk_along_3():
    """Verify Walk-Along Task 3: String Slicing (5 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        if 'course' not in user_vars:
            print("❌ Task 3 Not Complete")
            print("   Missing variable: 'course'")
            print("   💡 Hint: You need the 'course' variable")
            return False
        
        course = user_vars['course']
        
        if course != "Python for Beginners":
            print("❌ Task 3 Not Complete")
            print("   Variable 'course' should be 'Python for Beginners'")
            return False
        
        print("✅ Walk-Along Task 3 Complete! (+5 points)")
        print("   Outstanding! You extracted substrings using slicing.")
        print("   🏈 Slicing strings is like marking off yard lines - start and end points!")
        return True
        
    except Exception as e:
        print("❌ Task 3 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_try_it_yourself_1():
    """Verify Try It Yourself 1: Player Name Formatter (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        # Check for player_name variable
        if 'player_name' not in user_vars:
            print("❌ Try It Yourself 1 Not Complete")
            print("   Missing variable: 'player_name'")
            print("   💡 Hint: Create a variable called 'player_name' with a player's last name")
            return False
        
        # Check for jersey_name variable
        if 'jersey_name' not in user_vars:
            print("❌ Try It Yourself 1 Not Complete")
            print("   Missing variable: 'jersey_name'")
            print("   💡 Hint: Create 'jersey_name' as the uppercase version of 'player_name'")
            return False
        
        player_name = user_vars['player_name']
        jersey_name = user_vars['jersey_name']
        
        # Check if they're strings
        if not isinstance(player_name, str):
            print("❌ Try It Yourself 1 Not Complete")
            print("   'player_name' should be a string")
            return False
        
        if not isinstance(jersey_name, str):
            print("❌ Try It Yourself 1 Not Complete")
            print("   'jersey_name' should be a string")
            return False
        
        # Check if jersey_name is uppercase version
        if jersey_name != player_name.upper():
            print("❌ Try It Yourself 1 Not Complete")
            print(f"   'jersey_name' should be uppercase version of 'player_name'")
            print(f"   Your player_name: '{player_name}'")
            print(f"   Your jersey_name: '{jersey_name}'")
            print(f"   Expected: '{player_name.upper()}'")
            print("   💡 Hint: Use the .upper() method")
            return False
        
        # Check if jersey_name is actually uppercase
        if not jersey_name.isupper():
            print("❌ Try It Yourself 1 Not Complete")
            print("   'jersey_name' should be in UPPERCASE")
            print("   💡 Hint: Use the .upper() method on player_name")
            return False
        
        print("✅ Try It Yourself 1 Complete! (+15 points)")
        print(f"   Perfect! Jersey will display: {jersey_name}")
        print("   🏈 Just like jerseys on game day - bold and UPPERCASE!")
        return True
        
    except Exception as e:
        print("❌ Try It Yourself 1 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_try_it_yourself_2():
    """Verify Try It Yourself 2: Team Chant Generator (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        # Check for team_name variable
        if 'team_name' not in user_vars:
            print("❌ Try It Yourself 2 Not Complete")
            print("   Missing variable: 'team_name'")
            print("   💡 Hint: Create 'team_name' with a team name in UPPERCASE")
            return False
        
        # Check for chant_part variable
        if 'chant_part' not in user_vars:
            print("❌ Try It Yourself 2 Not Complete")
            print("   Missing variable: 'chant_part'")
            print("   💡 Hint: Use slicing to extract the first 3 letters")
            return False
        
        # Check for full_chant variable
        if 'full_chant' not in user_vars:
            print("❌ Try It Yourself 2 Not Complete")
            print("   Missing variable: 'full_chant'")
            print("   💡 Hint: Repeat 'chant_part' 3 times with spaces and add '!'")
            return False
        
        team_name = user_vars['team_name']
        chant_part = user_vars['chant_part']
        full_chant = user_vars['full_chant']
        
        # Check if they're strings
        if not isinstance(team_name, str):
            print("❌ Try It Yourself 2 Not Complete")
            print("   'team_name' should be a string")
            return False
        
        # Check if chant_part is first 3 letters
        if chant_part != team_name[:3]:
            print("❌ Try It Yourself 2 Not Complete")
            print(f"   'chant_part' should be first 3 letters of '{team_name}'")
            print(f"   Your chant_part: '{chant_part}'")
            print(f"   Expected: '{team_name[:3]}'")
            print("   💡 Hint: Use slicing [:3] to get first 3 characters")
            return False
        
        # Check if full_chant repeats 3 times
        expected_chant = f"{chant_part} {chant_part} {chant_part}!"
        if full_chant != expected_chant:
            print("❌ Try It Yourself 2 Not Complete")
            print(f"   'full_chant' should repeat '{chant_part}' 3 times with spaces")
            print(f"   Your full_chant: '{full_chant}'")
            print(f"   Expected: '{expected_chant}'")
            print("   💡 Hint: Format should be 'XXX XXX XXX!' with spaces")
            return False
        
        print("✅ Try It Yourself 2 Complete! (+15 points)")
        print(f"   Awesome! The crowd chants: {full_chant}")
        print("   🏈 The stadium is roaring! Perfect chant generation!")
        return True
        
    except Exception as e:
        print("❌ Try It Yourself 2 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_try_it_yourself_3():
    """Verify Try It Yourself 3: Player Stats Display (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        # Check for required variables
        required_vars = ['player_number', 'player_name', 'position', 'stats_display']
        missing_vars = [var for var in required_vars if var not in user_vars]
        
        if missing_vars:
            print("❌ Try It Yourself 3 Not Complete")
            print(f"   Missing variable(s): {', '.join(missing_vars)}")
            print("   💡 Hint: Create all required variables (player_number, player_name, position, stats_display)")
            return False
        
        player_number = user_vars['player_number']
        player_name = user_vars['player_name']
        position = user_vars['position']
        stats_display = user_vars['stats_display']
        
        # Check types
        if not isinstance(player_number, int):
            print("❌ Try It Yourself 3 Not Complete")
            print("   'player_number' should be an integer (number without quotes)")
            return False
        
        if not isinstance(player_name, str):
            print("❌ Try It Yourself 3 Not Complete")
            print("   'player_name' should be a string")
            return False
        
        if not isinstance(position, str):
            print("❌ Try It Yourself 3 Not Complete")
            print("   'position' should be a string")
            return False
        
        # Check if stats_display uses the correct format
        expected_format = f"#{player_number}: {player_name} - {position}"
        if stats_display != expected_format:
            print("❌ Try It Yourself 3 Not Complete")
            print(f"   Format doesn't match expected pattern")
            print(f"   Your stats_display: '{stats_display}'")
            print(f"   Expected format: '#{player_number}: {player_name} - {position}'")
            print("   💡 Hint: Use an f-string with format: f\"#{player_number}: {player_name} - {position}\"")
            return False
        
        # Check if it looks like an f-string was used (contains the values)
        if str(player_number) not in stats_display or player_name not in stats_display or position not in stats_display:
            print("❌ Try It Yourself 3 Not Complete")
            print("   'stats_display' should contain all three variables")
            print("   💡 Hint: Use an f-string to embed the variables")
            return False
        
        print("✅ Try It Yourself 3 Complete! (+15 points)")
        print(f"   Perfect stats display: {stats_display}")
        print("   🏈 Like a professional scoreboard - clean and informative!")
        return True
        
    except Exception as e:
        print("❌ Try It Yourself 3 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_debug_1():
    """Verify Debug Task 1: Off-by-One Index Error (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        # Check for name and first_name variables
        if 'name' not in user_vars:
            print("❌ Debug Task 1 Not Complete")
            print("   Missing variable: 'name'")
            print("   💡 Hint: Copy the buggy code and fix the slicing")
            return False
        
        if 'first_name' not in user_vars:
            print("❌ Debug Task 1 Not Complete")
            print("   Missing variable: 'first_name'")
            print("   💡 Hint: Extract 'James' from 'James Smith' using slicing")
            return False
        
        name = user_vars['name']
        first_name = user_vars['first_name']
        
        # Check if name is correct
        if name != "James Smith":
            print("❌ Debug Task 1 Not Complete")
            print(f"   Variable 'name' should be 'James Smith', got '{name}'")
            return False
        
        # Check if first_name is correct
        if first_name != "James":
            print("❌ Debug Task 1 Not Complete")
            print(f"   Variable 'first_name' should be 'James', got '{first_name}'")
            print("   💡 Hint: Use [0:5] to get 'James' (indices 0, 1, 2, 3, 4)")
            print("   Remember: Indexing starts at 0!")
            return False
        
        print("✅ Debug Task 1 Complete! (+15 points)")
        print("   Bug squashed! You fixed the off-by-one error.")
        print("   🏈 Like avoiding a false start penalty - proper positioning matters!")
        return True
        
    except Exception as e:
        print("❌ Debug Task 1 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_debug_2():
    """Verify Debug Task 2: Missing Slice End Index (10 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        # Check for team and abbreviation variables
        if 'team' not in user_vars:
            print("❌ Debug Task 2 Not Complete")
            print("   Missing variable: 'team'")
            print("   💡 Hint: Copy the buggy code and fix the slicing")
            return False
        
        if 'abbreviation' not in user_vars:
            print("❌ Debug Task 2 Not Complete")
            print("   Missing variable: 'abbreviation'")
            print("   💡 Hint: Extract first 4 letters using [:4]")
            return False
        
        team = user_vars['team']
        abbreviation = user_vars['abbreviation']
        
        # Check if team is correct
        if team != "COWBOYS":
            print("❌ Debug Task 2 Not Complete")
            print(f"   Variable 'team' should be 'COWBOYS', got '{team}'")
            return False
        
        # Check if abbreviation is correct
        if abbreviation != "COWB":
            print("❌ Debug Task 2 Not Complete")
            print(f"   Variable 'abbreviation' should be 'COWB', got '{abbreviation}'")
            print("   💡 Hint: Use [:4] to get first 4 characters")
            return False
        
        print("✅ Debug Task 2 Complete! (+10 points)")
        print("   Bug fixed! You specified the correct slice end index.")
        print("   🏈 Like calling the right play - precision is key!")
        return True
        
    except Exception as e:
        print("❌ Debug Task 2 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_debug_3():
    """Verify Debug Task 3: Trying to Modify Immutable String (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)
        
        # Check for name variable
        if 'name' not in user_vars:
            print("❌ Debug Task 3 Not Complete")
            print("   Missing variable: 'name'")
            print("   💡 Hint: Create a new string by combining 'J' with name[1:]")
            return False
        
        name = user_vars['name']
        
        # Check if name is correct (should be "John" after fix)
        if name != "John":
            print("❌ Debug Task 3 Not Complete")
            print(f"   Variable 'name' should be 'John', got '{name}'")
            print("   💡 Hint: Reassign name using: name = 'J' + name[1:]")
            print("   Remember: Strings are immutable - you can't change characters in place!")
            return False
        
        print("✅ Debug Task 3 Complete! (+15 points)")
        print("   Bug fixed! You created a new string instead of trying to modify the old one.")
        print("   🏈 Like replacing a player on the field - you can't change them, but you can swap them out!")
        return True
        
    except Exception as e:
        print("❌ Debug Task 3 Not Complete")
        print(f"   Error: {e}")
        return False


def calculate_grade():
    """Calculate and display the total grade for Lesson 06"""
    print("\n" + "="*60)
    print("📊 LESSON 06: STRINGS - GRADE REPORT")
    print("="*60 + "\n")
    
    total_points = 0
    max_points = 100
    
    # Walk-Along Tasks (15 points total)
    print("📺 Walk-Along Tasks (15 points):")
    walk_along_points = 0
    
    if verify_walk_along_1():
        walk_along_points += 5
    if verify_walk_along_2():
        walk_along_points += 5
    if verify_walk_along_3():
        walk_along_points += 5
    
    print(f"   Subtotal: {walk_along_points}/15 points\n")
    total_points += walk_along_points
    
    # Try It Yourself (45 points total)
    print("🎯 Try It Yourself (45 points):")
    try_it_points = 0
    
    if verify_try_it_yourself_1():
        try_it_points += 15
    if verify_try_it_yourself_2():
        try_it_points += 15
    if verify_try_it_yourself_3():
        try_it_points += 15
    
    print(f"   Subtotal: {try_it_points}/45 points\n")
    total_points += try_it_points
    
    # Debug Tasks (40 points total)
    print("🐞 Debug Tasks (40 points):")
    debug_points = 0
    
    if verify_debug_1():
        debug_points += 15
    if verify_debug_2():
        debug_points += 10
    if verify_debug_3():
        debug_points += 15
    
    print(f"   Subtotal: {debug_points}/40 points\n")
    total_points += debug_points
    
    # Final Grade
    print("="*60)
    print(f"🎯 TOTAL SCORE: {total_points}/{max_points} points")
    
    percentage = (total_points / max_points) * 100
    print(f"📈 PERCENTAGE: {percentage:.1f}%")
    
    # Letter grade
    if percentage >= 90:
        letter = "A"
        emoji = "🏆"
        message = "Outstanding! You're a string manipulation champion!"
    elif percentage >= 80:
        letter = "B"
        emoji = "⭐"
        message = "Great work! You've got solid string skills!"
    elif percentage >= 70:
        letter = "C"
        emoji = "👍"
        message = "Good job! Keep practicing those string operations!"
    elif percentage >= 60:
        letter = "D"
        emoji = "📚"
        message = "You're getting there! Review the concepts and try again!"
    else:
        letter = "F"
        emoji = "💪"
        message = "Don't give up! Review the lesson and practice more!"
    
    print(f"🔤 LETTER GRADE: {letter}")
    print(f"\n{emoji} {message}")
    print("="*60 + "\n")
    
    if total_points < max_points:
        print("💡 Tips for Success:")
        print("   • Review tasks marked with ❌")
        print("   • Watch the Code with Mosh video again (29:28-37:28)")
        print("   • Remember: Strings are immutable and indexing starts at 0")
        print("   • Practice slicing with [start:end] notation")
        print("   • Use string methods like .upper(), .lower(), .find()")
        print("   • Ask for help in Canvas discussions or office hours!")
        print()
    
    return total_points
