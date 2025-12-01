#!/usr/bin/env python3
"""
Generate a comprehensive 50-question final exam covering Lessons 1-7.
Questions are sourced from lessons 1-4 content and existing quizzes 5-7.
Format: QTI 1.2 XML for Canvas LMS import.
"""

def create_final_exam_xml():
    """Generate the complete QTI 1.2 XML for the final exam"""
    
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="final_exam_lessons_1_7" title="Final Exam Review: Lessons 1-7">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>3</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>cc_weighting</fieldlabel>
        <fieldentry>not_weighted</fieldentry>
      </qtimetadatafield>
      <qtimetadatafield>
        <fieldlabel>qmd_timelimit</fieldlabel>
        <fieldentry>3600</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
'''

    # LESSON 1 QUESTIONS (5 questions)
    questions = []
    
    # L1-Q1: print() function vocabulary
    questions.append(create_question(
        1, "Lesson 1: Your First Python Program",
        "What is the purpose of the <code>print()</code> function in Python?",
        ["To format text with different fonts", 
         "To display output to the screen",
         "To save data to a file",
         "To get input from the user"],
        "b"
    ))
    
    # L1-Q2: Quotes usage
    questions.append(create_question(
        2, "Lesson 1: Your First Python Program",
        "Which code will successfully print the text: <code>It's Friday</code>?",
        ['print(It\'s Friday)',
         'print(\'It\'s Friday\')',
         'print("It\'s Friday")',
         'Print("It\'s Friday")'],
        "c"
    ))
    
    # L1-Q3: Comments
    questions.append(create_question(
        3, "Lesson 1: Your First Python Program",
        "What symbol is used to create a comment in Python?",
        ["//", "#", "/*", "--"],
        "b"
    ))
    
    # L1-Q4: Case sensitivity
    questions.append(create_question(
        4, "Lesson 1: Your First Python Program",
        "What error will occur when running this code: <code>Print(\"Hello\")</code>?",
        ["SyntaxError due to missing quotes",
         "NameError because Print is not defined",
         "IndentationError",
         "No error, the code will run fine"],
        "b"
    ))
    
    # L1-Q5: Print output
    questions.append(create_question(
        5, "Lesson 1: Your First Python Program",
        "What will be the output of this code: <code>print(\"Python\")</code>?",
        ['"Python" (with quotes)',
         'Python (without quotes)',
         'PYTHON',
         'python'],
        "b"
    ))
    
    # LESSON 2 QUESTIONS (4 questions)
    
    # L2-Q1: Python interpreter vocabulary
    questions.append(create_question(
        6, "Lesson 2: How Python Code Gets Executed",
        "What is the Python interpreter?",
        ["A tool that converts Python code to English",
         "A program that translates Python code into computer instructions and executes it",
         "A text editor for writing Python code",
         "A debugging tool for finding errors"],
        "b"
    ))
    
    # L2-Q2: Execution order
    questions.append(create_question(
        7, "Lesson 2: How Python Code Gets Executed",
        "How does Python execute code in a program?",
        ["All at once, simultaneously",
         "From bottom to top",
         "Line by line from top to bottom",
         "Randomly"],
        "c"
    ))
    
    # L2-Q3: Multi-line output
    questions.append(create_question(
        8, "Lesson 2: How Python Code Gets Executed",
        'What will be the output of this code?<br><pre>print("Hello")\nprint("World")</pre>',
        ["HelloWorld (on one line)",
         "Hello World (on one line with space)",
         "Hello on one line, World on the next line",
         "World on one line, Hello on the next line"],
        "c"
    ))
    
    # L2-Q4: ASCII art
    questions.append(create_question(
        9, "Lesson 2: How Python Code Gets Executed",
        "What is ASCII art?",
        ["Professional digital artwork",
         "Text-based art created using characters and symbols",
         "A type of Python function",
         "A painting technique"],
        "b"
    ))
    
    # LESSON 3 QUESTIONS (6 questions)
    
    # L3-Q1: Variable definition
    questions.append(create_question(
        10, "Lesson 3: Variables",
        "What is a variable in Python?",
        ["A number that never changes",
         "A container that stores a value with a name",
         "A type of function",
         "A mathematical operation"],
        "b"
    ))
    
    # L3-Q2: Integer data type
    questions.append(create_question(
        11, "Lesson 3: Variables",
        "Which data type represents a whole number without a decimal point?",
        ["Float", "String", "Integer", "Boolean"],
        "c"
    ))
    
    # L3-Q3: Variable naming
    questions.append(create_question(
        12, "Lesson 3: Variables",
        "Which variable name follows Python naming conventions?",
        ["player name", "2player", "player_name", "player-name"],
        "c"
    ))
    
    # L3-Q4: Variable reassignment
    questions.append(create_question(
        13, "Lesson 3: Variables",
        'What will be printed by this code?<br><pre>x = 5\nx = 10\nprint(x)</pre>',
        ["5", "10", "5 10", "Error"],
        "b"
    ))
    
    # L3-Q5: Float data type
    questions.append(create_question(
        14, "Lesson 3: Variables",
        "What data type is <code>3.14</code>?",
        ["Integer", "Float", "String", "Boolean"],
        "b"
    ))
    
    # L3-Q6: Boolean values
    questions.append(create_question(
        15, "Lesson 3: Variables",
        "Which code correctly creates a boolean variable?",
        ["is_new = true",
         'is_new = "True"',
         "is_new = True",
         "is_new = TRUE"],
        "c"
    ))
    
    # LESSON 4 QUESTIONS (5 questions)
    
    # L4-Q1: input() function
    questions.append(create_question(
        16, "Lesson 4: Receiving Input",
        "What does the <code>input()</code> function do?",
        ["Displays output to the screen",
         "Prompts the user for input and returns what they type",
         "Performs mathematical calculations",
         "Creates variables automatically"],
        "b"
    ))
    
    # L4-Q2: input() return type
    questions.append(create_question(
        17, "Lesson 4: Receiving Input",
        "What data type does <code>input()</code> always return?",
        ["Integer", "Float", "String", "Boolean"],
        "c"
    ))
    
    # L4-Q3: String concatenation definition
    questions.append(create_question(
        18, "Lesson 4: Receiving Input",
        "What is string concatenation?",
        ["Converting strings to numbers",
         "Joining strings together using the + operator",
         "Splitting strings apart",
         "Comparing two strings"],
        "b"
    ))
    
    # L4-Q4: String concatenation output
    questions.append(create_question(
        19, "Lesson 4: Receiving Input",
        'What will be displayed if the user types "Sarah"?<br><pre>name = input("Name? ")\nprint("Welcome " + name + "!")</pre>',
        ["Welcome Sarah",
         "Welcome Sarah!",
         "WelcomeSarah!",
         "Welcome name!"],
        "b"
    ))
    
    # L4-Q5: Storing input
    questions.append(create_question(
        20, "Lesson 4: Receiving Input",
        "Which code correctly stores user input in a variable?",
        ['input("Name? ") = name',
         'name = input "Name? "',
         'name = input("Name? ")',
         'name input("Name? ")'],
        "c"
    ))
    
    # LESSON 5 QUESTIONS (8 questions - mix of vocab and application)
    
    # L5-Q1: input() return type (from vocab quiz)
    questions.append(create_question(
        21, "Lesson 5: Type Conversion",
        "What data type does the <code>input()</code> function ALWAYS return in Python?",
        ["Integer (whole number)",
         "Float (decimal number)",
         "String (text)",
         "Boolean (True/False)"],
        "c"
    ))
    
    # L5-Q2: int() function (from vocab quiz)
    questions.append(create_question(
        22, "Lesson 5: Type Conversion",
        "What does the <code>int()</code> function do?",
        ["Converts a value to a whole number",
         "Converts a value to a decimal number",
         "Converts a value to text",
         "Gets user input"],
        "a"
    ))
    
    # L5-Q3: type() output (from assignment quiz)
    questions.append(create_question(
        23, "Lesson 5: Type Conversion",
        'What will this code output?<br><pre>birth_year = input("Birth year: ")\nprint(type(birth_year))</pre>',
        ["&lt;class 'str'&gt;",
         "&lt;class 'int'&gt;",
         "&lt;class 'float'&gt;",
         "Birth year:"],
        "a"
    ))
    
    # L5-Q4: Fix TypeError (from assignment quiz)
    questions.append(create_question(
        24, "Lesson 5: Type Conversion",
        'This code produces a TypeError. How do you fix it?<br><pre>birth_year = input("Birth year: ")\nage = 2024 - birth_year\nprint(age)</pre>',
        ["Change line 2 to: age = 2024 - int(birth_year)",
         'Change line 2 to: age = "2024" - birth_year',
         "Change line 3 to: print(str(age))",
         'Add quotation marks: birth_year = "input"("Birth year: ")'],
        "a"
    ))
    
    # L5-Q5: float() vs int() (from assignment quiz)
    questions.append(create_question(
        25, "Lesson 5: Type Conversion",
        "For a Fahrenheit to Celsius converter (formula: (F - 32) * 5/9), which type conversion should you use?",
        ["float() - because the result will have decimals",
         "int() - because temperature is always a whole number",
         "str() - because temperature is text",
         "No conversion needed"],
        "a"
    ))
    
    # L5-Q6: int() behavior (from assignment quiz)
    questions.append(create_question(
        26, "Lesson 5: Type Conversion",
        "What does <code>int(3.7)</code> return?",
        ["3 (truncates the decimal)",
         "4 (rounds up)",
         "3.0 (keeps one decimal)",
         '"3.7" (converts to string)'],
        "a"
    ))
    
    # L5-Q7: Combining conversions (from assignment quiz)
    questions.append(create_question(
        27, "Lesson 5: Type Conversion",
        "You can combine input() and conversion in one line. Which is correct?",
        ['age = int(input("Age: "))',
         'age = input(int("Age: "))',
         'age = input + int("Age: ")',
         'age = "int(input("Age: "))"'],
        "a"
    ))
    
    # L5-Q8: TypeError cause (from vocab quiz)
    questions.append(create_question(
        28, "Lesson 5: Type Conversion",
        "Can you do math operations (like addition or subtraction) between strings and numbers without converting them first?",
        ["Yes, Python automatically converts them",
         "No, you'll get a TypeError",
         "Only with addition",
         "Only with multiplication"],
        "b"
    ))
    
    # LESSON 6 QUESTIONS (8 questions - mix of vocab and application)
    
    # L6-Q1: String definition (vocab)
    questions.append(create_question(
        29, "Lesson 6: Strings",
        "What is a string in Python?",
        ["A sequence of characters enclosed in quotes",
         "A number with a decimal point",
         "A variable that holds integers",
         "A type of list"],
        "a"
    ))
    
    # L6-Q2: upper() method (application)
    questions.append(create_question(
        30, "Lesson 6: Strings",
        'What does this code print?<br><pre>name = "python"\nprint(name.upper())</pre>',
        ["PYTHON", "python", "Python", "pYTHON"],
        "a"
    ))
    
    # L6-Q3: Slicing (application)
    questions.append(create_question(
        31, "Lesson 6: Strings",
        'What does this code print?<br><pre>team = "FOOTBALL"\nprint(team[4:8])</pre>',
        ["BALL", "FOOT", "OTBA", "TBAL"],
        "a"
    ))
    
    # L6-Q4: Negative indexing (application)
    questions.append(create_question(
        32, "Lesson 6: Strings",
        'What does this code print?<br><pre>word = "TOUCHDOWN"\nprint(word[-3])</pre>',
        ["W", "O", "D", "N"],
        "a"
    ))
    
    # L6-Q5: Immutability (vocab)
    questions.append(create_question(
        33, "Lesson 6: Strings",
        "What does it mean that strings are immutable?",
        ["Once created, strings cannot be changed; methods return new strings",
         "Strings can be modified at any time",
         "Strings cannot be printed",
         "Strings are stored permanently in memory"],
        "a"
    ))
    
    # L6-Q6: Fixing immutability error (application)
    questions.append(create_question(
        34, "Lesson 6: Strings",
        'This code has an error. What\'s the correct way to capitalize the first letter of "john" to "John"?<br><pre>name = "john"\nname[0] = "J"  # Error!</pre>',
        ['name = "J" + name[1:]',
         "name[0] = name[0].upper()",
         'name.replace(0, "J")',
         'name.change(0, "J")'],
        "a"
    ))
    
    # L6-Q7: find() method (application)
    questions.append(create_question(
        35, "Lesson 6: Strings",
        'What does this code print?<br><pre>message = "Python Programming"\nprint(message.find("Pro"))</pre>',
        ["7", "6", "Programming", "-1"],
        "a"
    ))
    
    # L6-Q8: Slicing definition (vocab)
    questions.append(create_question(
        36, "Lesson 6: Strings",
        "What is slicing in Python strings?",
        ["Extracting a portion of a string using [start:end] notation",
         "Dividing a string by a delimiter",
         "Removing characters from a string",
         "Converting a string to a list"],
        "a"
    ))
    
    # LESSON 7 QUESTIONS (10 questions - mix of vocab and application)
    
    # L7-Q1: F-string definition (vocab)
    questions.append(create_question(
        37, "Lesson 7: Formatted Strings",
        "What is a Formatted String (f-string)?",
        ["A string prefixed with f that allows embedding expressions inside curly braces",
         "A string that has been formatted with the format() method",
         "A string that contains only numbers",
         "A string that is aligned to the left or right"],
        "a"
    ))
    
    # L7-Q2: F-string syntax (application)
    questions.append(create_question(
        38, "Lesson 7: Formatted Strings",
        "Which code correctly creates an f-string to display a player's name and jersey number?",
        ['message = f"Player {name} wears jersey #{number}"',
         'message = "Player {name} wears jersey #{number}"',
         'message = f"Player " + name + " wears jersey #" + number',
         'message = "Player $name wears jersey #$number"'],
        "a"
    ))
    
    # L7-Q3: lower() method (application)
    questions.append(create_question(
        39, "Lesson 7: Formatted Strings",
        'What will this code output?<br><pre>name = "LEBRON"\nprint(name.lower())</pre>',
        ["lebron", "LEBRON", "Lebron", "LeBron"],
        "a"
    ))
    
    # L7-Q4: title() method (application)
    questions.append(create_question(
        40, "Lesson 7: Formatted Strings",
        'What will this code output?<br><pre>title = "nba finals"\nprint(title.title())</pre>',
        ["Nba Finals", "nba finals", "NBA FINALS", "NBA Finals"],
        "a"
    ))
    
    # L7-Q5: strip() method (application)
    questions.append(create_question(
        41, "Lesson 7: Formatted Strings",
        "Which code correctly removes leading and trailing spaces from a team name?",
        ['team = "  Warriors  "; clean_team = team.strip()',
         'team = "  Warriors  "; clean_team = team.trim()',
         'team = "  Warriors  "; clean_team = team.remove_spaces()',
         'team = "  Warriors  "; clean_team = team.clean()'],
        "a"
    ))
    
    # L7-Q6: F-string error (application)
    questions.append(create_question(
        42, "Lesson 7: Formatted Strings",
        'What is wrong with this code?<br><pre>player = "Durant"\nposition = "Forward"\nprint("Player {player} plays {position}")</pre>',
        ["Missing the f prefix before the string",
         "Variables should use $ instead of {}",
         "The print statement is incorrect",
         "The code is correct as written"],
        "a"
    ))
    
    # L7-Q7: find() method (application)
    questions.append(create_question(
        43, "Lesson 7: Formatted Strings",
        'What will this code output?<br><pre>text = "basketball"\nresult = text.find("ball")\nprint(result)</pre>',
        ["6", "4", "True", "-1"],
        "a"
    ))
    
    # L7-Q8: replace() method (application)
    questions.append(create_question(
        44, "Lesson 7: Formatted Strings",
        'Which code correctly replaces "win" with "victory" in the message?',
        ['message = "Team will win"; new_message = message.replace("win", "victory")',
         'message = "Team will win"; message.replace("win", "victory")',
         'message = "Team will win"; new_message = message.swap("win", "victory")',
         'message = "Team will win"; message = replace(message, "win", "victory")'],
        "a"
    ))
    
    # L7-Q9: String immutability (application)
    questions.append(create_question(
        45, "Lesson 7: Formatted Strings",
        "What happens when you call a string method like .upper() on a string?",
        ["It returns a new string; the original string is unchanged",
         "It modifies the original string permanently",
         "It only works if you assign it back to the same variable",
         "It creates an error because strings cannot be modified"],
        "a"
    ))
    
    # L7-Q10: F-string advantages (vocabulary)
    questions.append(create_question(
        46, "Lesson 7: Formatted Strings",
        "What is the main advantage of f-strings over string concatenation?",
        ["Code is more readable and easier to visualize the output",
         "F-strings are faster to execute",
         "F-strings can include variables, concatenation cannot",
         "F-strings automatically convert numbers to strings"],
        "a"
    ))
    
    # COMPREHENSIVE/MIXED QUESTIONS (4 questions covering multiple lessons)
    
    # Mixed Q1: Variable + input + type conversion
    questions.append(create_question(
        47, "Comprehensive Review",
        'What is the correct complete code to get a user\'s age and calculate birth year?<br><pre># User enters 20\nage = ?\nbirth_year = 2024 - age\nprint(birth_year)</pre>',
        ['age = input("Age: ")',
         'age = int(input("Age: "))',
         'age = "20"',
         'age = float(input("Age: "))'],
        "b"
    ))
    
    # Mixed Q2: String methods + concatenation
    questions.append(create_question(
        48, "Comprehensive Review",
        'What will this code display?<br><pre>name = "  john  "\nclean = name.strip().title()\nprint("Hello " + clean)</pre>',
        ["Hello   john  ",
         "Hello John",
         "Hello john",
         "Hello JOHN"],
        "b"
    ))
    
    # Mixed Q3: Variables + data types
    questions.append(create_question(
        49, "Comprehensive Review",
        "Which line of code will cause an error?",
        ['price = 19.99',
         'name = "Python"',
         'is_valid = True',
         'age = 25 + "5"'],
        "d"
    ))
    
    # Mixed Q4: Print + strings + f-strings
    questions.append(create_question(
        50, "Comprehensive Review",
        'Which is the BEST way to display "Score: 95" where score is a variable?',
        ['print("Score: " + score)',
         'print(f"Score: {score}")',
         'print("Score: ", score)',
         'print("Score: " + str(score))'],
        "b"
    ))
    
    # Combine all questions
    xml_content += "\n".join(questions)
    
    # Close the XML document
    xml_content += '''
    </section>
  </assessment>
</questestinterop>'''
    
    return xml_content


def escape_html(text):
    """Escape HTML entities for XML"""
    import html
    return html.escape(text)


def create_question(num, title, question_text, choices, correct):
    """Create a single question in QTI format"""
    
    # Escape the question text for proper XML encoding
    escaped_question = escape_html(question_text)
    
    question = f'''
      <!-- Question {num}: {title} -->
      <item ident="q{num}" title="Question {num}">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_choice_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>2</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;p&gt;{escaped_question}&lt;/p&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="a">
                <material>
                  <mattext texttype="text/plain">{choices[0]}</mattext>
                </material>
              </response_label>
              <response_label ident="b">
                <material>
                  <mattext texttype="text/plain">{choices[1]}</mattext>
                </material>
              </response_label>
              <response_label ident="c">
                <material>
                  <mattext texttype="text/plain">{choices[2]}</mattext>
                </material>
              </response_label>
              <response_label ident="d">
                <material>
                  <mattext texttype="text/plain">{choices[3]}</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">{correct}</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>
'''
    return question


def create_imsmanifest():
    """Create the imsmanifest.xml content"""
    return '''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://www.imsglobal.org/xsd/imscp_v1p1" xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_v1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" identifier="MANIFEST1" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p1.xsd http://www.imsglobal.org/xsd/imsmd_v1p2 http://www.imsglobal.org/xsd/imsmd_v1p2p2.xsd">
  <organizations/>
  <resources>
    <resource identifier="RES-1" type="imsqti_xmlv1p2" href="quiz.xml">
      <file href="quiz.xml"/>
    </resource>
  </resources>
</manifest>'''


if __name__ == "__main__":
    import os
    import zipfile
    
    print("🎓 Creating Final Exam Review for Lessons 1-7...")
    print("=" * 60)
    
    # Generate the XML
    quiz_xml = create_final_exam_xml()
    
    # Create output directory
    output_dir = "/home/rsullivan/COSC1315/Quizzes"
    final_exam_dir = os.path.join(output_dir, "Final_Exam_Review")
    os.makedirs(final_exam_dir, exist_ok=True)
    
    # Write quiz.xml
    quiz_path = os.path.join(final_exam_dir, "quiz.xml")
    with open(quiz_path, 'w', encoding='utf-8') as f:
        f.write(quiz_xml)
    print(f"✅ Created quiz.xml ({len(quiz_xml)} bytes)")
    
    # Write imsmanifest.xml
    manifest_path = os.path.join(final_exam_dir, "imsmanifest.xml")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write(create_imsmanifest())
    print(f"✅ Created imsmanifest.xml")
    
    # Create ZIP file
    zip_path = os.path.join(output_dir, "Final_Exam_Review_Lessons_1-7.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('imsmanifest.xml', create_imsmanifest())
        zf.writestr('quiz.xml', quiz_xml)
    
    print(f"✅ Created ZIP package: {zip_path}")
    print()
    print("📊 Final Exam Statistics:")
    print("   • Total Questions: 50")
    print("   • Total Points: 100 (2 points each)")
    print("   • Time Limit: 60 minutes (3600 seconds)")
    print("   • Attempts Allowed: 3")
    print()
    print("📋 Question Distribution by Lesson:")
    print("   • Lesson 1 (Your First Python Program): 5 questions")
    print("   • Lesson 2 (How Python Code Gets Executed): 4 questions")
    print("   • Lesson 3 (Variables): 6 questions")
    print("   • Lesson 4 (Receiving Input): 5 questions")
    print("   • Lesson 5 (Type Conversion): 8 questions")
    print("   • Lesson 6 (Strings): 8 questions")
    print("   • Lesson 7 (Formatted Strings): 10 questions")
    print("   • Comprehensive/Mixed: 4 questions")
    print()
    print("💡 To upload to Canvas:")
    print("   1. Go to your Canvas course → Quizzes")
    print("   2. Click 'Options' (⋮) → 'Import Quiz'")
    print("   3. Select 'QTI Package'")
    print(f"   4. Upload: {zip_path}")
    print("   5. Click 'Import' and wait for completion")
    print("   6. Review and publish the quiz")
    print()
    print("✅ All done! Your final exam review is ready!")
