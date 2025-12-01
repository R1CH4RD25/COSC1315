#!/usr/bin/env python3
"""
Create a Google Form for the Final Exam Review (Lessons 1-7)
Generates a 50-question multiple-choice quiz in Google Forms format.

This script creates the form structure. You can either:
1. Use Google Forms API (requires OAuth setup)
2. Or use the output to manually create the form
"""

def create_form_questions():
    """Generate all 50 questions for the final exam"""
    questions = []
    
    # LESSON 1 QUESTIONS (5 questions)
    questions.append({
        "question": "What is the purpose of the print() function in Python?",
        "choices": [
            "To format text with different fonts",
            "To display output to the screen",  # CORRECT
            "To save data to a file",
            "To get input from the user"
        ],
        "correct": 1,
        "lesson": "Lesson 1: Your First Python Program"
    })
    
    questions.append({
        "question": "Which code will successfully print the text: It's Friday?",
        "choices": [
            "print(It's Friday)",
            "print('It's Friday')",
            'print("It\'s Friday")',  # CORRECT
            'Print("It\'s Friday")'
        ],
        "correct": 2,
        "lesson": "Lesson 1: Your First Python Program"
    })
    
    questions.append({
        "question": "What symbol is used to create a comment in Python?",
        "choices": [
            "//",
            "#",  # CORRECT
            "/*",
            "--"
        ],
        "correct": 1,
        "lesson": "Lesson 1: Your First Python Program"
    })
    
    questions.append({
        "question": 'What error will occur when running this code: Print("Hello")?',
        "choices": [
            "SyntaxError due to missing quotes",
            "NameError because Print is not defined",  # CORRECT
            "IndentationError",
            "No error, the code will run fine"
        ],
        "correct": 1,
        "lesson": "Lesson 1: Your First Python Program"
    })
    
    questions.append({
        "question": 'What will be the output of this code: print("Python")?',
        "choices": [
            '"Python" (with quotes)',
            'Python (without quotes)',  # CORRECT
            'PYTHON',
            'python'
        ],
        "correct": 1,
        "lesson": "Lesson 1: Your First Python Program"
    })
    
    # LESSON 2 QUESTIONS (4 questions)
    questions.append({
        "question": "What is the Python interpreter?",
        "choices": [
            "A tool that converts Python code to English",
            "A program that translates Python code into computer instructions and executes it",  # CORRECT
            "A text editor for writing Python code",
            "A debugging tool for finding errors"
        ],
        "correct": 1,
        "lesson": "Lesson 2: How Python Code Gets Executed"
    })
    
    questions.append({
        "question": "How does Python execute code in a program?",
        "choices": [
            "All at once, simultaneously",
            "From bottom to top",
            "Line by line from top to bottom",  # CORRECT
            "Randomly"
        ],
        "correct": 2,
        "lesson": "Lesson 2: How Python Code Gets Executed"
    })
    
    questions.append({
        "question": 'What will be the output of this code?\nprint("Hello")\nprint("World")',
        "choices": [
            "HelloWorld (on one line)",
            "Hello World (on one line with space)",
            "Hello on one line, World on the next line",  # CORRECT
            "World on one line, Hello on the next line"
        ],
        "correct": 2,
        "lesson": "Lesson 2: How Python Code Gets Executed"
    })
    
    questions.append({
        "question": "What is ASCII art?",
        "choices": [
            "Professional digital artwork",
            "Text-based art created using characters and symbols",  # CORRECT
            "A type of Python function",
            "A painting technique"
        ],
        "correct": 1,
        "lesson": "Lesson 2: How Python Code Gets Executed"
    })
    
    # LESSON 3 QUESTIONS (6 questions)
    questions.append({
        "question": "What is a variable in Python?",
        "choices": [
            "A number that never changes",
            "A container that stores a value with a name",  # CORRECT
            "A type of function",
            "A mathematical operation"
        ],
        "correct": 1,
        "lesson": "Lesson 3: Variables"
    })
    
    questions.append({
        "question": "Which data type represents a whole number without a decimal point?",
        "choices": [
            "Float",
            "String",
            "Integer",  # CORRECT
            "Boolean"
        ],
        "correct": 2,
        "lesson": "Lesson 3: Variables"
    })
    
    questions.append({
        "question": "Which variable name follows Python naming conventions?",
        "choices": [
            "player name",
            "2player",
            "player_name",  # CORRECT
            "player-name"
        ],
        "correct": 2,
        "lesson": "Lesson 3: Variables"
    })
    
    questions.append({
        "question": "What will be printed by this code?\nx = 5\nx = 10\nprint(x)",
        "choices": [
            "5",
            "10",  # CORRECT
            "5 10",
            "Error"
        ],
        "correct": 1,
        "lesson": "Lesson 3: Variables"
    })
    
    questions.append({
        "question": "What data type is 3.14?",
        "choices": [
            "Integer",
            "Float",  # CORRECT
            "String",
            "Boolean"
        ],
        "correct": 1,
        "lesson": "Lesson 3: Variables"
    })
    
    questions.append({
        "question": "Which code correctly creates a boolean variable?",
        "choices": [
            "is_new = true",
            'is_new = "True"',
            "is_new = True",  # CORRECT
            "is_new = TRUE"
        ],
        "correct": 2,
        "lesson": "Lesson 3: Variables"
    })
    
    # LESSON 4 QUESTIONS (5 questions)
    questions.append({
        "question": "What does the input() function do?",
        "choices": [
            "Displays output to the screen",
            "Prompts the user for input and returns what they type",  # CORRECT
            "Performs mathematical calculations",
            "Creates variables automatically"
        ],
        "correct": 1,
        "lesson": "Lesson 4: Receiving Input"
    })
    
    questions.append({
        "question": "What data type does input() always return?",
        "choices": [
            "Integer",
            "Float",
            "String",  # CORRECT
            "Boolean"
        ],
        "correct": 2,
        "lesson": "Lesson 4: Receiving Input"
    })
    
    questions.append({
        "question": "What is string concatenation?",
        "choices": [
            "Converting strings to numbers",
            "Joining strings together using the + operator",  # CORRECT
            "Splitting strings apart",
            "Comparing two strings"
        ],
        "correct": 1,
        "lesson": "Lesson 4: Receiving Input"
    })
    
    questions.append({
        "question": 'What will be displayed if the user types "Sarah"?\nname = input("Name? ")\nprint("Welcome " + name + "!")',
        "choices": [
            "Welcome Sarah",
            "Welcome Sarah!",  # CORRECT
            "WelcomeSarah!",
            "Welcome name!"
        ],
        "correct": 1,
        "lesson": "Lesson 4: Receiving Input"
    })
    
    questions.append({
        "question": "Which code correctly stores user input in a variable?",
        "choices": [
            'input("Name? ") = name',
            'name = input "Name? "',
            'name = input("Name? ")',  # CORRECT
            'name input("Name? ")'
        ],
        "correct": 2,
        "lesson": "Lesson 4: Receiving Input"
    })
    
    # LESSON 5 QUESTIONS (8 questions)
    questions.append({
        "question": "What data type does the input() function ALWAYS return in Python?",
        "choices": [
            "Integer (whole number)",
            "Float (decimal number)",
            "String (text)",  # CORRECT
            "Boolean (True/False)"
        ],
        "correct": 2,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    questions.append({
        "question": "What does the int() function do?",
        "choices": [
            "Converts a value to a whole number",  # CORRECT
            "Converts a value to a decimal number",
            "Converts a value to text",
            "Gets user input"
        ],
        "correct": 0,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    questions.append({
        "question": 'What will this code output?\nbirth_year = input("Birth year: ")\nprint(type(birth_year))',
        "choices": [
            "<class 'str'>",  # CORRECT
            "<class 'int'>",
            "<class 'float'>",
            "Birth year:"
        ],
        "correct": 0,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    questions.append({
        "question": 'This code produces a TypeError. How do you fix it?\nbirth_year = input("Birth year: ")\nage = 2024 - birth_year\nprint(age)',
        "choices": [
            "Change line 2 to: age = 2024 - int(birth_year)",  # CORRECT
            'Change line 2 to: age = "2024" - birth_year',
            "Change line 3 to: print(str(age))",
            'Add quotation marks: birth_year = "input"("Birth year: ")'
        ],
        "correct": 0,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    questions.append({
        "question": "For a Fahrenheit to Celsius converter (formula: (F - 32) * 5/9), which type conversion should you use?",
        "choices": [
            "float() - because the result will have decimals",  # CORRECT
            "int() - because temperature is always a whole number",
            "str() - because temperature is text",
            "No conversion needed"
        ],
        "correct": 0,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    questions.append({
        "question": "What does int(3.7) return?",
        "choices": [
            "3 (truncates the decimal)",  # CORRECT
            "4 (rounds up)",
            "3.0 (keeps one decimal)",
            '"3.7" (converts to string)'
        ],
        "correct": 0,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    questions.append({
        "question": "You can combine input() and conversion in one line. Which is correct?",
        "choices": [
            'age = int(input("Age: "))',  # CORRECT
            'age = input(int("Age: "))',
            'age = input + int("Age: ")',
            'age = "int(input("Age: "))"'
        ],
        "correct": 0,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    questions.append({
        "question": "Can you do math operations (like addition or subtraction) between strings and numbers without converting them first?",
        "choices": [
            "Yes, Python automatically converts them",
            "No, you'll get a TypeError",  # CORRECT
            "Only with addition",
            "Only with multiplication"
        ],
        "correct": 1,
        "lesson": "Lesson 5: Type Conversion"
    })
    
    # LESSON 6 QUESTIONS (8 questions)
    questions.append({
        "question": "What is a string in Python?",
        "choices": [
            "A sequence of characters enclosed in quotes",  # CORRECT
            "A number with a decimal point",
            "A variable that holds integers",
            "A type of list"
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    questions.append({
        "question": 'What does this code print?\nname = "python"\nprint(name.upper())',
        "choices": [
            "PYTHON",  # CORRECT
            "python",
            "Python",
            "pYTHON"
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    questions.append({
        "question": 'What does this code print?\nteam = "FOOTBALL"\nprint(team[4:8])',
        "choices": [
            "BALL",  # CORRECT
            "FOOT",
            "OTBA",
            "TBAL"
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    questions.append({
        "question": 'What does this code print?\nword = "TOUCHDOWN"\nprint(word[-3])',
        "choices": [
            "W",  # CORRECT
            "O",
            "D",
            "N"
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    questions.append({
        "question": "What does it mean that strings are immutable?",
        "choices": [
            "Once created, strings cannot be changed; methods return new strings",  # CORRECT
            "Strings can be modified at any time",
            "Strings cannot be printed",
            "Strings are stored permanently in memory"
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    questions.append({
        "question": 'This code has an error. What\'s the correct way to capitalize the first letter of "john" to "John"?\nname = "john"\nname[0] = "J"  # Error!',
        "choices": [
            'name = "J" + name[1:]',  # CORRECT
            "name[0] = name[0].upper()",
            'name.replace(0, "J")',
            'name.change(0, "J")'
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    questions.append({
        "question": 'What does this code print?\nmessage = "Python Programming"\nprint(message.find("Pro"))',
        "choices": [
            "7",  # CORRECT
            "6",
            "Programming",
            "-1"
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    questions.append({
        "question": "What is slicing in Python strings?",
        "choices": [
            "Extracting a portion of a string using [start:end] notation",  # CORRECT
            "Dividing a string by a delimiter",
            "Removing characters from a string",
            "Converting a string to a list"
        ],
        "correct": 0,
        "lesson": "Lesson 6: Strings"
    })
    
    # LESSON 7 QUESTIONS (10 questions)
    questions.append({
        "question": "What is a Formatted String (f-string)?",
        "choices": [
            "A string prefixed with f that allows embedding expressions inside curly braces",  # CORRECT
            "A string that has been formatted with the format() method",
            "A string that contains only numbers",
            "A string that is aligned to the left or right"
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": "Which code correctly creates an f-string to display a player's name and jersey number?",
        "choices": [
            'message = f"Player {name} wears jersey #{number}"',  # CORRECT
            'message = "Player {name} wears jersey #{number}"',
            'message = f"Player " + name + " wears jersey #" + number',
            'message = "Player $name wears jersey #$number"'
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": 'What will this code output?\nname = "LEBRON"\nprint(name.lower())',
        "choices": [
            "lebron",  # CORRECT
            "LEBRON",
            "Lebron",
            "LeBron"
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": 'What will this code output?\ntitle = "nba finals"\nprint(title.title())',
        "choices": [
            "Nba Finals",  # CORRECT
            "nba finals",
            "NBA FINALS",
            "NBA Finals"
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": "Which code correctly removes leading and trailing spaces from a team name?",
        "choices": [
            'team = "  Warriors  "; clean_team = team.strip()',  # CORRECT
            'team = "  Warriors  "; clean_team = team.trim()',
            'team = "  Warriors  "; clean_team = team.remove_spaces()',
            'team = "  Warriors  "; clean_team = team.clean()'
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": 'What is wrong with this code?\nplayer = "Durant"\nposition = "Forward"\nprint("Player {player} plays {position}")',
        "choices": [
            "Missing the f prefix before the string",  # CORRECT
            "Variables should use $ instead of {}",
            "The print statement is incorrect",
            "The code is correct as written"
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": 'What will this code output?\ntext = "basketball"\nresult = text.find("ball")\nprint(result)',
        "choices": [
            "6",  # CORRECT
            "4",
            "True",
            "-1"
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": 'Which code correctly replaces "win" with "victory" in the message?',
        "choices": [
            'message = "Team will win"; new_message = message.replace("win", "victory")',  # CORRECT
            'message = "Team will win"; message.replace("win", "victory")',
            'message = "Team will win"; new_message = message.swap("win", "victory")',
            'message = "Team will win"; message = replace(message, "win", "victory")'
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": "What happens when you call a string method like .upper() on a string?",
        "choices": [
            "It returns a new string; the original string is unchanged",  # CORRECT
            "It modifies the original string permanently",
            "It only works if you assign it back to the same variable",
            "It creates an error because strings cannot be modified"
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    questions.append({
        "question": "What is the main advantage of f-strings over string concatenation?",
        "choices": [
            "Code is more readable and easier to visualize the output",  # CORRECT
            "F-strings are faster to execute",
            "F-strings can include variables, concatenation cannot",
            "F-strings automatically convert numbers to strings"
        ],
        "correct": 0,
        "lesson": "Lesson 7: Formatted Strings"
    })
    
    # COMPREHENSIVE/MIXED QUESTIONS (4 questions)
    questions.append({
        "question": "What is the correct complete code to get a user's age and calculate birth year?\nage = ?\nbirth_year = 2024 - age\nprint(birth_year)",
        "choices": [
            'age = input("Age: ")',
            'age = int(input("Age: "))',  # CORRECT
            'age = "20"',
            'age = float(input("Age: "))'
        ],
        "correct": 1,
        "lesson": "Comprehensive Review"
    })
    
    questions.append({
        "question": 'What will this code display?\nname = "  john  "\nclean = name.strip().title()\nprint("Hello " + clean)',
        "choices": [
            "Hello   john  ",
            "Hello John",  # CORRECT
            "Hello john",
            "Hello JOHN"
        ],
        "correct": 1,
        "lesson": "Comprehensive Review"
    })
    
    questions.append({
        "question": "Which line of code will cause an error?",
        "choices": [
            'price = 19.99',
            'name = "Python"',
            'is_valid = True',
            'age = 25 + "5"'  # CORRECT
        ],
        "correct": 3,
        "lesson": "Comprehensive Review"
    })
    
    questions.append({
        "question": 'Which is the BEST way to display "Score: 95" where score is a variable?',
        "choices": [
            'print("Score: " + score)',
            'print(f"Score: {score}")',  # CORRECT
            'print("Score: ", score)',
            'print("Score: " + str(score))'
        ],
        "correct": 1,
        "lesson": "Comprehensive Review"
    })
    
    return questions


def print_manual_instructions():
    """Print instructions for manually creating the form"""
    questions = create_form_questions()
    
    print("=" * 80)
    print("FINAL EXAM REVIEW: LESSONS 1-7")
    print("Manual Google Forms Creation Guide")
    print("=" * 80)
    print()
    print("Total Questions: 50")
    print("Format: Multiple Choice")
    print("Points: 2 points per question (100 total)")
    print()
    print("INSTRUCTIONS:")
    print("1. Go to https://forms.google.com")
    print("2. Create a new form titled: 'Final Exam Review: Lessons 1-7'")
    print("3. Make it a Quiz (Settings → Quizzes → Make this a quiz)")
    print("4. Set each question to 2 points")
    print("5. Add all 50 questions below")
    print()
    print("=" * 80)
    print()
    
    for i, q in enumerate(questions, 1):
        print(f"\n{'='*80}")
        print(f"QUESTION {i} - {q['lesson']}")
        print(f"{'='*80}")
        print(f"\n{q['question']}\n")
        
        for j, choice in enumerate(q['choices']):
            marker = " ✓ CORRECT" if j == q['correct'] else ""
            print(f"  {chr(65+j)}. {choice}{marker}")
        
        print()
    
    print("=" * 80)
    print("\nDONE! Add all questions to your Google Form.")
    print("Remember to:")
    print("  - Set each question to 2 points")
    print("  - Mark the correct answer for each question")
    print("  - Set as 'Required' for all questions")
    print("=" * 80)


def export_to_csv():
    """Export questions to CSV format for easy import"""
    import csv
    
    questions = create_form_questions()
    
    filename = "/home/rsullivan/COSC1315/Quizzes/final_exam_questions.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow(['Question Number', 'Lesson', 'Question', 'Choice A', 'Choice B', 'Choice C', 'Choice D', 'Correct Answer'])
        
        # Questions
        for i, q in enumerate(questions, 1):
            correct_letter = chr(65 + q['correct'])  # 0=A, 1=B, etc.
            writer.writerow([
                i,
                q['lesson'],
                q['question'],
                q['choices'][0],
                q['choices'][1],
                q['choices'][2],
                q['choices'][3],
                correct_letter
            ])
    
    print(f"✅ Exported to: {filename}")
    print("You can use this CSV to help create the Google Form")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "csv":
        export_to_csv()
    else:
        print_manual_instructions()
