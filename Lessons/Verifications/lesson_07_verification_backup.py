"""
Lesson 07: Formatted Strings - Verification System
Auto-grading functions for string formatting tasks
"""

def verify_walk_along_1():
    """Verify Walk-Along Task 1: String Concatenation (5 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for first and last variables
        if 'first' not in user_vars or 'last' not in user_vars:
            print("❌ Task 1 Not Complete")
            print("   Missing variables: 'first' and/or 'last'")
            print("   💡 Hint: Create both variables with string values")
            return False

        first = user_vars['first']
        last = user_vars['last']

        # Check if they're strings
        if not isinstance(first, str) or not isinstance(last, str):
            print("❌ Task 1 Not Complete")
            print("   Both 'first' and 'last' should be strings")
            return False

        # Check for full_name variable
        if 'full_name' not in user_vars:
            print("❌ Task 1 Not Complete")
            print("   Missing variable: 'full_name'")
            print("   💡 Hint: Concatenate first and last with a space")
            return False

        full_name = user_vars['full_name']

        # Check if full_name is correct concatenation
        expected = f"{first} {last}"
        if full_name != expected:
            print("❌ Task 1 Not Complete")
            print(f"   'full_name' should be '{expected}', got '{full_name}'")
            print("   💡 Hint: Use first + ' ' + last")
            return False

        print("✅ Walk-Along Task 1 Complete! (+5 points)")
        print("   Great job! You concatenated strings successfully.")
        print("   🏈 Like joining player first and last names on a roster!")
        return True

    except Exception as e:
        print("❌ Task 1 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_walk_along_2():
    """Verify Walk-Along Task 2: F-Strings (5 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for name and age variables
        if 'name' not in user_vars or 'age' not in user_vars:
            print("❌ Task 2 Not Complete")
            print("   Missing variables: 'name' and/or 'age'")
            print("   💡 Hint: Create both variables")
            return False

        name = user_vars['name']
        age = user_vars['age']

        # Check types
        if not isinstance(name, str):
            print("❌ Task 2 Not Complete")
            print("   'name' should be a string")
            return False

        if not isinstance(age, int):
            print("❌ Task 2 Not Complete")
            print("   'age' should be an integer (number without quotes)")
            return False

        # Check for greeting variable
        if 'greeting' not in user_vars:
            print("❌ Task 2 Not Complete")
            print("   Missing variable: 'greeting'")
            print("   💡 Hint: Create an f-string with name and age")
            return False

        greeting = user_vars['greeting']

        # Check if greeting contains both values
        if str(name) not in greeting or str(age) not in greeting:
            print("❌ Task 2 Not Complete")
            print("   'greeting' should contain both name and age")
            print("   💡 Hint: Use f\"Hi, I am {name}. I am {age} years old.\"")
            return False

        print("✅ Walk-Along Task 2 Complete! (+5 points)")
        print("   Excellent! You created an f-string with variables.")
        print("   🏈 F-strings are like playbooks - clear and organized!")
        return True

    except Exception as e:
        print("❌ Task 2 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_try_it_yourself_1():
    """Verify Try It Yourself 1: Player Stats (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for all required variables
        required_vars = ['player_name', 'points', 'rebounds', 'assists', 'stats_report']
        missing_vars = [var for var in required_vars if var not in user_vars]

        if missing_vars:
            print("❌ Try It Yourself 1 Not Complete")
            print(f"   Missing variable(s): {', '.join(missing_vars)}")
            print("   💡 Hint: Create all required variables")
            return False

        player_name = user_vars['player_name']
        points = user_vars['points']
        rebounds = user_vars['rebounds']
        assists = user_vars['assists']
        stats_report = user_vars['stats_report']

        # Check types
        if not isinstance(player_name, str):
            print("❌ Try It Yourself 1 Not Complete")
            print("   'player_name' should be a string")
            return False

        if not all(isinstance(x, int) for x in [points, rebounds, assists]):
            print("❌ Try It Yourself 1 Not Complete")
            print("   points, rebounds, and assists should be integers")
            return False

        # Check if stats_report contains all values
        if (player_name not in stats_report or
            str(points) not in stats_report or
            str(rebounds) not in stats_report or
            str(assists) not in stats_report):
            print("❌ Try It Yourself 1 Not Complete")
            print("   'stats_report' should contain all four variables")
            print("   💡 Hint: Use an f-string with all variables embedded")
            return False

        # Check for key words in output
        if 'scored' not in stats_report.lower() or 'rebounds' not in stats_report.lower():
            print("❌ Try It Yourself 1 Not Complete")
            print("   'stats_report' should describe the stats (scored, rebounds, assists)")
            return False

        print("✅ Try It Yourself 1 Complete! (+15 points)")
        print(f"   Perfect stats report: {stats_report}")
        print("   🏈 That's how you report game stats - clear and complete!")
        return True

    except Exception as e:
        print("❌ Try It Yourself 1 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_try_it_yourself_2():
    """Verify Try It Yourself 2: Multi-Line Roster (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for all required variables
        required_vars = ['team_name', 'player1', 'player2', 'player3', 'roster']
        missing_vars = [var for var in required_vars if var not in user_vars]

        if missing_vars:
            print("❌ Try It Yourself 2 Not Complete")
            print(f"   Missing variable(s): {', '.join(missing_vars)}")
            print("   💡 Hint: Create all required variables")
            return False

        team_name = user_vars['team_name']
        player1 = user_vars['player1']
        player2 = user_vars['player2']
        player3 = user_vars['player3']
        roster = user_vars['roster']

        # Check if all are strings
        if not all(isinstance(x, str) for x in [team_name, player1, player2, player3, roster]):
            print("❌ Try It Yourself 2 Not Complete")
            print("   All variables should be strings")
            return False

        # Check if roster contains all variables
        if not all(x in roster for x in [team_name, player1, player2, player3]):
            print("❌ Try It Yourself 2 Not Complete")
            print("   'roster' should contain team_name and all three players")
            print("   💡 Hint: Use an f-string with all variables")
            return False

        # Check if roster spans multiple lines
        if '\n' not in roster:
            print("❌ Try It Yourself 2 Not Complete")
            print("   'roster' should span multiple lines")
            print("   💡 Hint: Use triple-quoted f-string: f\"\"\"...\"\"\"")
            return False

        print("✅ Try It Yourself 2 Complete! (+15 points)")
        print("   Excellent roster display!")
        print("   🏈 Multi-line output makes rosters easy to read!")
        return True

    except Exception as e:
        print("❌ Try It Yourself 2 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_try_it_yourself_3():
    """Verify Try It Yourself 3: Score Calculator (20 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for required variables
        required_vars = ['touchdowns', 'field_goals', 'scoreboard']
        missing_vars = [var for var in required_vars if var not in user_vars]

        if missing_vars:
            print("❌ Try It Yourself 3 Not Complete")
            print(f"   Missing variable(s): {', '.join(missing_vars)}")
            print("   💡 Hint: Create touchdowns, field_goals, and scoreboard")
            return False

        touchdowns = user_vars['touchdowns']
        field_goals = user_vars['field_goals']
        scoreboard = user_vars['scoreboard']

        # Check types
        if not isinstance(touchdowns, int) or not isinstance(field_goals, int):
            print("❌ Try It Yourself 3 Not Complete")
            print("   'touchdowns' and 'field_goals' should be integers")
            return False

        if not isinstance(scoreboard, str):
            print("❌ Try It Yourself 3 Not Complete")
            print("   'scoreboard' should be a string")
            return False

        # Calculate expected total
        expected_total = touchdowns * 6 + field_goals * 3

        # Check if scoreboard contains the calculations
        if str(expected_total) not in scoreboard:
            print("❌ Try It Yourself 3 Not Complete")
            print(f"   'scoreboard' should show total points: {expected_total}")
            print("   💡 Hint: Include calculations in your f-string")
            return False

        # Check for multiplication signs or calculations
        if str(touchdowns * 6) not in scoreboard or str(field_goals * 3) not in scoreboard:
            print("❌ Try It Yourself 3 Not Complete")
            print("   'scoreboard' should show individual calculations")
            print("   💡 Hint: Use expressions like {touchdowns * 6} in your f-string")
            return False

        print("✅ Try It Yourself 3 Complete! (+20 points)")
        print(f"   Perfect scoreboard: {scoreboard}")
        print("   🏈 That's how you calculate and display game scores!")
        return True

    except Exception as e:
        print("❌ Try It Yourself 3 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_debug_1():
    """Verify Debug Task 1: Missing F-String Prefix (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for variables
        if 'name' not in user_vars or 'points' not in user_vars or 'message' not in user_vars:
            print("❌ Debug Task 1 Not Complete")
            print("   Missing variables: name, points, and/or message")
            print("   💡 Hint: Copy and fix the buggy code")
            return False

        name = user_vars['name']
        points = user_vars['points']
        message = user_vars['message']

        # Check if message contains the actual values (not the variable names)
        if name not in message or str(points) not in message:
            print("❌ Debug Task 1 Not Complete")
            print("   'message' should contain the actual values, not {name} and {points}")
            print("   💡 Hint: Add the f prefix before the string: f\"...\"")
            return False

        # Check that it's not showing curly braces
        if '{' in message or '}' in message:
            print("❌ Debug Task 1 Not Complete")
            print("   'message' still shows curly braces - add the f prefix!")
            return False

        print("✅ Debug Task 1 Complete! (+15 points)")
        print("   Bug fixed! F-strings need the f prefix.")
        print("   🏈 Like remembering to wear your helmet - essential!")
        return True

    except Exception as e:
        print("❌ Debug Task 1 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_debug_2():
    """Verify Debug Task 2: Concatenation Type Mismatch (10 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for variables
        if 'team' not in user_vars or 'wins' not in user_vars or 'summary' not in user_vars:
            print("❌ Debug Task 2 Not Complete")
            print("   Missing variables: team, wins, and/or summary")
            print("   💡 Hint: Copy and fix the buggy code")
            return False

        team = user_vars['team']
        wins = user_vars['wins']
        summary = user_vars['summary']

        # Check if summary contains both values
        if team not in summary or str(wins) not in summary:
            print("❌ Debug Task 2 Not Complete")
            print("   'summary' should contain both team name and wins")
            return False

        # Check that it's a valid string
        if not isinstance(summary, str):
            print("❌ Debug Task 2 Not Complete")
            print("   'summary' should be a string")
            return False

        print("✅ Debug Task 2 Complete! (+10 points)")
        print("   Bug fixed! F-strings handle type conversion automatically.")
        print("   🏈 No more TypeError - smooth execution!")
        return True

    except Exception as e:
        print("❌ Debug Task 2 Not Complete")
        print(f"   Error: {e}")
        return False


def verify_debug_3():
    """Verify Debug Task 3: Quote Mismatch (15 points)"""
    try:
        import __main__
        user_vars = vars(__main__)

        # Check for variables
        if 'player' not in user_vars or 'message' not in user_vars:
            print("❌ Debug Task 3 Not Complete")
            print("   Missing variables: player and/or message")
            print("   💡 Hint: Copy and fix the buggy code")
            return False

        player = user_vars['player']
        message = user_vars['message']

        # Check if message contains the player name
        if player not in message:
            print("❌ Debug Task 3 Not Complete")
            print("   'message' should contain the player name")
            return False

        # Check if message contains double quotes around the name
        if f'"{player}"' not in message:
            print("❌ Debug Task 3 Not Complete")
            print(f"   'message' should have double quotes around {player}")
            print("   💡 Hint: Use single quotes for the f-string: f'...'")
            return False

        print("✅ Debug Task 3 Complete! (+15 points)")
        print("   Bug fixed! Mix your quotes wisely.")
        print("   🏈 Like choosing the right play for the situation!")
        return True

    except Exception as e:
        print("❌ Debug Task 3 Not Complete")
        print(f"   Error: {e}")
        return False


def calculate_grade():
    """Calculate and display the total grade for Lesson 07"""
    print("\n" + "="*60)
    print("📊 LESSON 07: FORMATTED STRINGS - GRADE REPORT")
    print("="*60 + "\n")

    total_points = 0
    max_points = 100

    # Walk-Along Tasks (10 points total)
    print("📺 Walk-Along Tasks (10 points):")
    walk_along_points = 0

    if verify_walk_along_1():
        walk_along_points += 5
    if verify_walk_along_2():
        walk_along_points += 5

    print(f"   Subtotal: {walk_along_points}/10 points\n")
    total_points += walk_along_points

    # Try It Yourself (50 points total)
    print("🎯 Try It Yourself (50 points):")
    try_it_points = 0

    if verify_try_it_yourself_1():
        try_it_points += 15
    if verify_try_it_yourself_2():
        try_it_points += 15
    if verify_try_it_yourself_3():
        try_it_points += 20

    print(f"   Subtotal: {try_it_points}/50 points\n")
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
        message = "Outstanding! You're an f-string master!"
    elif percentage >= 80:
        letter = "B"
        emoji = "⭐"
        message = "Great work! You've got solid formatting skills!"
    elif percentage >= 70:
        letter = "C"
        emoji = "👍"
        message = "Good job! Keep practicing those f-strings!"
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
        print("   • Watch the Code with Mosh video again (37:28-42:48)")
        print("   • Remember: f-strings need the f prefix!")
        print("   • Practice mixing quotes: f'...\"...\"...'")
        print("   • F-strings auto-convert numbers to strings")
        print("   • Ask for help in Canvas discussions or office hours!")
        print()

    return total_points
