"""Extract vocabulary terms from all lesson quizzes"""
import xml.etree.ElementTree as ET
import html
import re
from pathlib import Path

lessons = ['05', '06', '07', '08', '09', '10']

print("=" * 80)
print("VOCABULARY TERMS FROM QUIZZES")
print("=" * 80)
print()

all_terms = {}

for lesson in lessons:
    print(f"=== LESSON {lesson} ===")
    quiz_path = Path(f"temp_quiz_{lesson}/quiz.xml")

    if not quiz_path.exists():
        print("❌ No quiz found\n")
        continue

    try:
        tree = ET.parse(quiz_path)
        root = tree.getroot()

        # Find all question items
        items = root.findall('.//item')

        print(f"Found {len(items)} questions")
        print("\n10 Vocabulary Terms:")

        terms = []
        for i, item in enumerate(items[:10], 1):
            # Find the question text (first mattext in presentation)
            presentation = item.find('.//presentation')
            if presentation is not None:
                mattext = presentation.find('.//mattext')
                if mattext is not None and mattext.text:
                    # Decode HTML entities
                    question = html.unescape(mattext.text)
                    # Remove HTML tags
                    question = re.sub(r'<[^>]+>', '', question)
                    # Clean up
                    question = question.strip().replace('?', '')

                    # Extract the key term from the question
                    # Questions are usually like "What is X" or "What does X mean"
                    term = question
                    if 'What is' in question:
                        term = question.replace('What is', '').replace('a ', '').replace('an ', '').replace('the ', '').strip()
                    elif 'What does' in question:
                        # Keep "What does X mean" format for complex terms
                        term = question.replace('What does', '').replace(' mean', '').strip()
                        # Clean up quotes
                        term = term.strip('"').strip("'")
                    elif 'Which' in question:
                        # Extract from "Which X" questions
                        term = question.replace('Which', '').strip()

                    terms.append(term)
                    print(f"  {i}. {term}")

        all_terms[lesson] = terms
        print()

    except Exception as e:
        print(f"❌ Error parsing quiz: {e}\n")

# Save to file for reference
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
with open('vocabulary_terms_extracted.txt', 'w', encoding='utf-8') as f:
    for lesson, terms in all_terms.items():
        print(f"Lesson {lesson}: {len(terms)} terms")
        f.write(f"=== LESSON {lesson} ===\n")
        for i, term in enumerate(terms, 1):
            f.write(f"{i}. {term}\n")
        f.write("\n")

print(f"\n✅ Extracted terms saved to: vocabulary_terms_extracted.txt")
