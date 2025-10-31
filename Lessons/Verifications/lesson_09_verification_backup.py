"""
Lesson 09: If Statements - Verification System
Auto-grades student exercises on conditional statements
"""

# Store points for grade calculation
points_earned = {
    'walk_along_1': 0,
    'walk_along_2': 0,
    'walk_along_3': 0,
    'try_it_1': 0,
    'try_it_2': 0,
    'try_it_3': 0,
    'debug_1': 0,
    'debug_2': 0,
    'debug_3': 0
}

def verify_walk_along_1():
    """Verify Walk-Along 1: Basic If Statement"""
    try:
        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code
        temperature = 95
        if temperature > 90:
            print("It's a hot day!")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "It's a hot day!" in output:
            points_earned['walk_along_1'] = 5
            print("✅ Walk-Along 1 Complete! (+5 points)")
            print("Great job! You used an if statement correctly.")
        else:
            print("❌ Not quite. Make sure your if statement prints the exact message.")
            print("Expected: It's a hot day!")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you've written the if statement above.")

def verify_walk_along_2():
    """Verify Walk-Along 2: If-Else Statement"""
    try:
        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code
        temperature = 65
        if temperature > 80:
            print("It's a hot day")
        else:
            print("It's not a hot day")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "It's not a hot day" in output:
            points_earned['walk_along_2'] = 5
            print("✅ Walk-Along 2 Complete! (+5 points)")
            print("Excellent! Your if-else statement works correctly.")
        else:
            print("❌ Not quite. Check your if-else logic.")
            print("For temperature 65, it should print: It's not a hot day")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you've written the if-else statement above.")

def verify_walk_along_3():
    """Verify Walk-Along 3: If-Elif-Else Chain"""
    try:
        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code
        temperature = 75
        if temperature >= 90:
            print("It's a hot day")
        elif temperature >= 70:
            print("It's a nice day")
        else:
            print("It's a cold day")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "It's a nice day" in output:
            points_earned['walk_along_3'] = 5
            print("✅ Walk-Along 3 Complete! (+5 points)")
            print("Perfect! You understand if-elif-else chains.")
        else:
            print("❌ Not quite. Check your elif conditions.")
            print("For temperature 75, it should print: It's a nice day")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you've written the if-elif-else statement above.")

def verify_try_it_1():
    """Verify Try It Yourself 1: Playoff Eligibility"""
    try:
        import sys
        from io import StringIO

        # Check if variables exist
        try:
            wins
            losses
        except NameError:
            print("❌ Missing variables. Create 'wins' and 'losses' variables.")
            return

        # Verify variable values
        if wins != 45 or losses != 37:
            print("❌ Variables have wrong values.")
            print("Make sure: wins = 45 and losses = 37")
            return

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code (simulate)
        if wins > 40:
            print("Team made the playoffs!")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "Team made the playoffs!" in output:
            points_earned['try_it_1'] = 15
            print("✅ Try It Yourself 1 Complete! (+15 points)")
            print("🏀 Great work! The team made it to the playoffs!")
        else:
            print("❌ Not quite. Check your if statement.")
            print("Hint: Check if wins > 40")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you've created the variables and if statement.")

def verify_try_it_2():
    """Verify Try It Yourself 2: Player Performance Rating"""
    try:
        # Check if variable exists
        try:
            points
        except NameError:
            print("❌ Missing variable. Create a 'points' variable.")
            return

        # Verify variable value
        if points != 28:
            print("❌ Variable has wrong value.")
            print("Make sure: points = 28")
            return

        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code (simulate)
        if points >= 30:
            print("Elite performance!")
        elif points >= 20:
            print("Great game!")
        elif points >= 10:
            print("Good effort")
        else:
            print("Needs improvement")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "Great game!" in output:
            points_earned['try_it_2'] = 20
            print("✅ Try It Yourself 2 Complete! (+20 points)")
            print("🏈 Excellent! Your performance rating system works!")
        else:
            print("❌ Not quite. Check your elif conditions.")
            print("For points = 28, it should print: Great game!")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you've created the variable and if-elif-else chain.")

def verify_try_it_3():
    """Verify Try It Yourself 3: Championship Game Winner"""
    try:
        # Check if variables exist
        try:
            team_a_score
            team_b_score
        except NameError:
            print("❌ Missing variables. Create 'team_a_score' and 'team_b_score'.")
            return

        # Verify variable values
        if team_a_score != 98 or team_b_score != 95:
            print("❌ Variables have wrong values.")
            print("Make sure: team_a_score = 98 and team_b_score = 95")
            return

        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code (simulate)
        if team_a_score > team_b_score:
            print("Team A wins the championship!")
        elif team_b_score > team_a_score:
            print("Team B wins the championship!")
        else:
            print("It's a tie! Going to overtime!")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "Team A wins the championship!" in output:
            points_earned['try_it_3'] = 15
            print("✅ Try It Yourself 3 Complete! (+15 points)")
            print("🏆 Team A is the champion! Your logic is perfect!")
        else:
            print("❌ Not quite. Check your if-elif-else conditions.")
            print("For scores 98-95, Team A should win!")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure you've created the variables and if-elif-else statement.")

def verify_debug_1():
    """Verify Debug Challenge 1: Missing Colon"""
    try:
        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code
        age = 16
        if age >= 16:
            print("You can get a driver's license!")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "You can get a driver's license!" in output:
            points_earned['debug_1'] = 15
            print("✅ Debug Challenge 1 Fixed! (+15 points)")
            print("Great debugging! You added the missing colon.")
        else:
            print("❌ Still has issues. Check for the colon after the if statement.")
    except SyntaxError:
        print("❌ Still has a syntax error. Remember: if statements need a colon (:)")
    except Exception as e:
        print(f"❌ Error: {e}")

def verify_debug_2():
    """Verify Debug Challenge 2: Wrong Comparison Operator"""
    try:
        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code
        score = 100
        if score == 100:
            print("Perfect score!")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "Perfect score!" in output:
            points_earned['debug_2'] = 15
            print("✅ Debug Challenge 2 Fixed! (+15 points)")
            print("Excellent! You used == for comparison, not =")
        else:
            print("❌ Still has issues.")
    except Exception as e:
        print("❌ Remember: Use == for comparison, = for assignment")
        print(f"Error: {e}")

def verify_debug_3():
    """Verify Debug Challenge 3: Indentation Error"""
    try:
        import sys
        from io import StringIO

        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run student code
        jersey_number = 23
        if jersey_number == 23:
            print("That's Michael Jordan's number!")

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        # Check output
        if "That's Michael Jordan's number!" in output:
            points_earned['debug_3'] = 10
            print("✅ Debug Challenge 3 Fixed! (+10 points)")
            print("Perfect! You fixed the indentation.")
        else:
            print("❌ Still has issues.")
    except IndentationError:
        print("❌ Still has an indentation error.")
        print("Remember: Code inside if statements must be indented (4 spaces)")
    except Exception as e:
        print(f"❌ Error: {e}")

def calculate_grade():
    """Calculate and display final grade"""
    total_points = sum(points_earned.values())
    max_points = 100
    percentage = (total_points / max_points) * 100

    print("\n" + "="*50)
    print("📊 LESSON 09: IF STATEMENTS - GRADE REPORT")
    print("="*50)

    print("\n🎓 WALK-ALONG TASKS:")
    print(f"   Walk-Along 1: {points_earned['walk_along_1']}/5 points")
    print(f"   Walk-Along 2: {points_earned['walk_along_2']}/5 points")
    print(f"   Walk-Along 3: {points_earned['walk_along_3']}/5 points")

    print("\n🏀 TRY IT YOURSELF:")
    print(f"   Exercise 1 (Playoff Eligibility): {points_earned['try_it_1']}/15 points")
    print(f"   Exercise 2 (Performance Rating): {points_earned['try_it_2']}/20 points")
    print(f"   Exercise 3 (Championship Winner): {points_earned['try_it_3']}/15 points")

    print("\n🐛 DEBUG CHALLENGES:")
    print(f"   Challenge 1 (Missing Colon): {points_earned['debug_1']}/15 points")
    print(f"   Challenge 2 (Wrong Operator): {points_earned['debug_2']}/15 points")
    print(f"   Challenge 3 (Indentation): {points_earned['debug_3']}/10 points")

    print("\n" + "="*50)
    print(f"   TOTAL: {total_points}/{max_points} points ({percentage:.1f}%)")
    print("="*50)

    # Grade letter
    if percentage >= 90:
        grade = "A"
        emoji = "🏆"
        message = "Outstanding work!"
    elif percentage >= 80:
        grade = "B"
        emoji = "🥈"
        message = "Great job!"
    elif percentage >= 70:
        grade = "C"
        emoji = "🥉"
        message = "Good effort!"
    elif percentage >= 60:
        grade = "D"
        emoji = "📚"
        message = "Keep practicing!"
    else:
        grade = "F"
        emoji = "💪"
        message = "Don't give up!"

    print(f"\n{emoji} GRADE: {grade} - {message}")
    print("="*50 + "\n")

    if total_points < max_points:
        print("💡 TIP: Go back and complete the exercises you missed!")
        print("   Each exercise has a verification cell to check your work.")
