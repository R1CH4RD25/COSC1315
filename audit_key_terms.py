"""
Audit Key Terms in Lesson Notebooks vs Vocabulary Quiz Terms
Checks if each lesson's Key Terms section matches the 10 vocabulary terms expected
"""

import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Define lesson numbers to audit
LESSONS = ['05', '06', '07', '08', '09', '10']

def extract_vocab_terms_from_zip(zip_path):
    """Extract vocabulary terms from QTI quiz zip file"""
    terms = []
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Read assessment_meta.xml to get question info
            if 'assessment_meta.xml' in zip_ref.namelist():
                xml_content = zip_ref.read('assessment_meta.xml')
                root = ET.fromstring(xml_content)

                # Find all questions
                for question in root.findall('.//question'):
                    title = question.find('.//title')
                    if title is not None and title.text:
                        # Extract term from title (usually "Define: Term")
                        term_text = title.text
                        if 'Define:' in term_text:
                            term = term_text.split('Define:')[1].strip()
                            terms.append(term)
                        elif 'What is' in term_text:
                            # Some might be phrased as questions
                            term = term_text.replace('What is', '').replace('?', '').strip()
                            terms.append(term)
    except Exception as e:
        print(f"  ⚠️  Error reading {zip_path.name}: {e}")

    return terms

def extract_key_terms_from_notebook(notebook_path):
    """Extract Key Terms from lesson notebook"""
    terms = []
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Find the Key Terms cell (usually a markdown cell near the beginning)
        in_key_terms = False
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))

                # Check if this is the Key Terms section
                if '### 📚 Key Terms' in source or '## Key Terms' in source or '**Key Terms' in source:
                    in_key_terms = True
                    # Extract terms from this cell
                    lines = source.split('\n')
                    for line in lines:
                        # Look for bullet points or numbered lists
                        line = line.strip()
                        if line.startswith('- **') or line.startswith('* **'):
                            # Format: - **Term**: definition
                            term = line.split('**')[1] if '**' in line else None
                            if term and term not in ['Key Terms', 'Learning Objectives']:
                                terms.append(term)
                        elif line.startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ')):
                            # Numbered format: 1. **Term**: definition
                            if '**' in line:
                                term = line.split('**')[1]
                                terms.append(term)

                    if terms:  # If we found terms, we're done
                        break
                elif in_key_terms and line.startswith('#'):
                    # Hit next section, stop looking
                    break

    except Exception as e:
        print(f"  ⚠️  Error reading {notebook_path.name}: {e}")

    return terms

def main():
    """Main audit function"""
    print("=" * 80)
    print("🔍 KEY TERMS AUDIT: Notebooks vs Vocabulary Quizzes")
    print("=" * 80)
    print()

    base_path = Path(__file__).parent
    vocab_path = base_path / "Quizzes" / "Vocabulary Quizzes - QTI - Canvas"
    lessons_path = base_path / "Lessons"

    all_good = True

    for lesson_num in LESSONS:
        print(f"\n{'='*80}")
        print(f"LESSON {lesson_num}")
        print(f"{'='*80}")

        # Get vocabulary terms from quiz
        vocab_zip = vocab_path / f"Lesson_{lesson_num}_*_Vocabulary.zip"
        vocab_files = list(vocab_path.glob(f"Lesson_{lesson_num}_*_Vocabulary.zip"))

        vocab_terms = []
        if vocab_files:
            vocab_terms = extract_vocab_terms_from_zip(vocab_files[0])

        # Get key terms from notebook
        notebook_file = lessons_path / f"Lesson_{lesson_num}_*.ipynb"
        notebook_files = list(lessons_path.glob(f"Lesson_{lesson_num}_*.ipynb"))

        # Filter out backup files
        notebook_files = [f for f in notebook_files if 'backup' not in f.name.lower()]

        notebook_terms = []
        if notebook_files:
            notebook_terms = extract_key_terms_from_notebook(notebook_files[0])

        print(f"\n📝 VOCABULARY QUIZ ({len(vocab_terms)} terms):")
        if vocab_terms:
            for i, term in enumerate(vocab_terms, 1):
                print(f"   {i}. {term}")
        else:
            print("   ⚠️  No terms found in vocabulary quiz")

        print(f"\n📘 NOTEBOOK KEY TERMS ({len(notebook_terms)} terms):")
        if notebook_terms:
            for i, term in enumerate(notebook_terms, 1):
                print(f"   {i}. {term}")
        else:
            print("   ⚠️  No Key Terms section found in notebook")

        # Compare
        print(f"\n{'='*40}")
        print("VALIDATION:")
        print(f"{'='*40}")

        if not vocab_terms:
            print("⚠️  Cannot validate - no vocabulary quiz found")
        elif not notebook_terms:
            print("❌ MISSING: Notebook has no Key Terms section")
            all_good = False
        elif len(notebook_terms) != 10:
            print(f"❌ MISMATCH: Notebook has {len(notebook_terms)} terms (expected 10)")
            all_good = False
        else:
            # Check if terms match (case-insensitive)
            vocab_lower = [t.lower() for t in vocab_terms]
            notebook_lower = [t.lower() for t in notebook_terms]

            missing_in_notebook = []
            for term in vocab_terms:
                if term.lower() not in notebook_lower:
                    missing_in_notebook.append(term)

            extra_in_notebook = []
            for term in notebook_terms:
                if term.lower() not in vocab_lower:
                    extra_in_notebook.append(term)

            if not missing_in_notebook and not extra_in_notebook:
                print("✅ PERFECT MATCH: All 10 vocabulary terms present in notebook")
            else:
                print("❌ MISMATCH:")
                if missing_in_notebook:
                    print(f"   Missing from notebook ({len(missing_in_notebook)}):")
                    for term in missing_in_notebook:
                        print(f"      - {term}")
                if extra_in_notebook:
                    print(f"   Extra in notebook (not in quiz) ({len(extra_in_notebook)}):")
                    for term in extra_in_notebook:
                        print(f"      - {term}")
                all_good = False

    # Final summary
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    if all_good:
        print("✅ All lessons have matching Key Terms!")
    else:
        print("❌ Some lessons need Key Terms updates")
        print("\n💡 Next Steps:")
        print("   1. Review mismatches above")
        print("   2. Update notebook Key Terms sections to match vocabulary quizzes")
        print("   3. Ensure each lesson has exactly 10 terms")
    print()

if __name__ == "__main__":
    main()
