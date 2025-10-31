"""
Convert simple XML quiz format to full QTI 1.2 format for Canvas
This script converts Lessons 7, 9, and 10 quizzes to the proper format
"""

import xml.etree.ElementTree as ET
import zipfile
import os
from html import escape

def convert_simple_to_qti(simple_xml_path, lesson_num, topic_name, quiz_type, time_limit=600):
    """
    Convert simple quiz XML to full QTI 1.2 format
    
    Args:
        simple_xml_path: Path to the simple format quiz.xml
        lesson_num: Lesson number (e.g., "07", "09", "10")
        topic_name: Topic name (e.g., "Formatted Strings", "If Statements")
        quiz_type: Either "vocabulary" or "assignment"
        time_limit: Time limit in seconds (600 for vocab, 900 for assignment)
    """
    
    # Parse the simple format XML
    tree = ET.parse(simple_xml_path)
    root = tree.getroot()
    
    # Extract questions
    questions = []
    for question_elem in root.findall('question'):
        question_text = question_elem.find('questiontext/text').text
        
        answers = []
        correct_answer = None
        for idx, answer_elem in enumerate(question_elem.findall('answer')):
            fraction = answer_elem.get('fraction')
            answer_text = answer_elem.find('text').text
            label = chr(97 + idx)  # a, b, c, d
            answers.append({
                'label': label,
                'text': answer_text,
                'correct': fraction == '100'
            })
            if fraction == '100':
                correct_answer = label
        
        questions.append({
            'text': question_text,
            'answers': answers,
            'correct': correct_answer
        })
    
    # Build QTI XML
    qti_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    qti_xml += '<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" '
    qti_xml += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
    qti_xml += 'xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 '
    qti_xml += 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">\n'
    
    # Assessment header
    quiz_title = f"Lesson {lesson_num}: {topic_name} - {quiz_type.title()} Quiz"
    ident = f"lesson_{lesson_num}_{quiz_type}_quiz"
    qti_xml += f'  <assessment ident="{ident}" title="{quiz_title}">\n'
    
    # Metadata
    qti_xml += '    <qtimetadata>\n'
    qti_xml += '      <qtimetadatafield>\n'
    qti_xml += '        <fieldlabel>cc_maxattempts</fieldlabel>\n'
    qti_xml += '        <fieldentry>3</fieldentry>\n'
    qti_xml += '      </qtimetadatafield>\n'
    qti_xml += '      <qtimetadatafield>\n'
    qti_xml += '        <fieldlabel>cc_weighting</fieldlabel>\n'
    qti_xml += '        <fieldentry>not_weighted</fieldentry>\n'
    qti_xml += '      </qtimetadatafield>\n'
    qti_xml += '      <qtimetadatafield>\n'
    qti_xml += '        <fieldlabel>qmd_timelimit</fieldlabel>\n'
    qti_xml += f'        <fieldentry>{time_limit}</fieldentry>\n'
    qti_xml += '      </qtimetadatafield>\n'
    qti_xml += '    </qtimetadata>\n'
    
    # Section start
    qti_xml += '    <section ident="root_section">\n\n'
    
    # Add each question
    for idx, q in enumerate(questions, 1):
        qti_xml += f'      <!-- Question {idx} -->\n'
        qti_xml += f'      <item ident="q{idx}" title="Question {idx}">\n'
        
        # Item metadata
        qti_xml += '        <itemmetadata>\n'
        qti_xml += '          <qtimetadata>\n'
        qti_xml += '            <qtimetadatafield>\n'
        qti_xml += '              <fieldlabel>question_type</fieldlabel>\n'
        qti_xml += '              <fieldentry>multiple_choice_question</fieldentry>\n'
        qti_xml += '            </qtimetadatafield>\n'
        qti_xml += '            <qtimetadatafield>\n'
        qti_xml += '              <fieldlabel>points_possible</fieldlabel>\n'
        qti_xml += '              <fieldentry>10</fieldentry>\n'
        qti_xml += '            </qtimetadatafield>\n'
        qti_xml += '          </qtimetadata>\n'
        qti_xml += '        </itemmetadata>\n'
        
        # Presentation
        qti_xml += '        <presentation>\n'
        qti_xml += '          <material>\n'
        # Escape HTML in question text
        escaped_text = escape(q['text']).replace('&lt;', '<').replace('&gt;', '>')
        qti_xml += f'            <mattext texttype="text/html">&lt;p&gt;{escaped_text}&lt;/p&gt;</mattext>\n'
        qti_xml += '          </material>\n'
        qti_xml += '          <response_lid ident="response1" rcardinality="Single">\n'
        qti_xml += '            <render_choice>\n'
        
        # Add answer choices
        for answer in q['answers']:
            qti_xml += f'              <response_label ident="{answer["label"]}">\n'
            qti_xml += '                <material>\n'
            qti_xml += f'                  <mattext texttype="text/plain">{escape(answer["text"])}</mattext>\n'
            qti_xml += '                </material>\n'
            qti_xml += '              </response_label>\n'
        
        qti_xml += '            </render_choice>\n'
        qti_xml += '          </response_lid>\n'
        qti_xml += '        </presentation>\n'
        
        # Response processing (correct answer)
        qti_xml += '        <resprocessing>\n'
        qti_xml += '          <outcomes>\n'
        qti_xml += '            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>\n'
        qti_xml += '          </outcomes>\n'
        qti_xml += '          <respcondition continue="No">\n'
        qti_xml += '            <conditionvar>\n'
        qti_xml += f'              <varequal respident="response1">{q["correct"]}</varequal>\n'
        qti_xml += '            </conditionvar>\n'
        qti_xml += '            <setvar action="Set" varname="SCORE">100</setvar>\n'
        qti_xml += '          </respcondition>\n'
        qti_xml += '        </resprocessing>\n'
        
        qti_xml += '      </item>\n\n'
    
    # Close section and assessment
    qti_xml += '    </section>\n'
    qti_xml += '  </assessment>\n'
    qti_xml += '</questestinterop>\n'
    
    return qti_xml


def create_imsmanifest():
    """Create the imsmanifest.xml file required by Canvas"""
    manifest = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="quiz_export" xmlns="http://www.imsglobal.org/xsd/imscp_v1p1" 
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
          xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p1.xsd">
  <metadata>
    <schema>QTI Package</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <resources>
    <resource identifier="quiz_resource" type="imsqti_xmlv1p2">
      <file href="quiz.xml"/>
    </resource>
  </resources>
</manifest>
'''
    return manifest


def process_quiz(lesson_num, topic_name, quiz_type):
    """Process a single quiz file"""
    print(f"\nProcessing Lesson {lesson_num} {quiz_type.title()} Quiz...")
    
    # Determine directories
    if quiz_type == "vocabulary":
        quiz_dir = "Quizzes/Vocabulary Quizzes - QTI - Canvas"
    else:
        quiz_dir = "Quizzes/Assignment Quizzes - QTI - Canvas"
    
    # File names
    if quiz_type == "vocabulary":
        topic_slug = topic_name.replace(" ", "_")
        zip_filename = f"Lesson_{lesson_num}_{topic_slug}_Vocabulary.zip"
    else:
        topic_slug = topic_name.replace(" ", "_")
        zip_filename = f"Lesson_{lesson_num}_{topic_slug}_Assignment.zip"
    
    zip_path = os.path.join(quiz_dir, zip_filename)
    
    # Extract existing zip
    temp_dir = f"temp_{lesson_num}_{quiz_type}"
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(quiz_dir, temp_dir))
    
    simple_xml_path = os.path.join(quiz_dir, temp_dir, "quiz.xml")
    
    # Convert to QTI format
    time_limit = 600 if quiz_type == "vocabulary" else 900
    qti_xml = convert_simple_to_qti(simple_xml_path, lesson_num, topic_name, quiz_type, time_limit)
    
    # Write new quiz.xml
    with open(simple_xml_path, 'w', encoding='utf-8') as f:
        f.write(qti_xml)
    
    # Create imsmanifest.xml
    manifest_path = os.path.join(quiz_dir, temp_dir, "imsmanifest.xml")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write(create_imsmanifest())
    
    # Repackage as zip
    os.remove(zip_path)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        zip_ref.write(manifest_path, "imsmanifest.xml")
        zip_ref.write(simple_xml_path, "quiz.xml")
    
    # Cleanup temp directory
    import shutil
    shutil.rmtree(os.path.join(quiz_dir, temp_dir))
    
    print(f"✓ Created {zip_filename}")


if __name__ == "__main__":
    # Convert all quizzes that need updating
    quizzes_to_convert = [
        ("07", "Formatted_Strings", "vocabulary"),
        ("07", "Formatted_Strings", "assignment"),
        ("09", "If_Statements", "vocabulary"),
        ("09", "If_Statements", "assignment"),
        ("10", "Logical_Operators", "vocabulary"),
        ("10", "Logical_Operators", "assignment"),
    ]
    
    for lesson_num, topic_name, quiz_type in quizzes_to_convert:
        process_quiz(lesson_num, topic_name, quiz_type)
    
    print("\n✅ All quizzes converted to QTI 1.2 format!")
