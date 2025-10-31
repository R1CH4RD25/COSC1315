#!/usr/bin/env python3
"""
Convert raw QTI XML quiz files into Canvas-compatible ZIP packages.
Each ZIP must contain: imsmanifest.xml + the quiz XML file (renamed to quiz.xml)
"""

import os
import zipfile
from pathlib import Path

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

def create_qti_zip(xml_file_path, output_dir):
    """
    Create a Canvas-compatible QTI ZIP from an XML quiz file.
    
    Args:
        xml_file_path: Path to the XML quiz file
        output_dir: Directory to save the ZIP file
    """
    xml_file = Path(xml_file_path)
    
    if not xml_file.exists():
        print(f"❌ File not found: {xml_file}")
        return False
    
    # Read the XML content
    with open(xml_file, 'r', encoding='utf-8') as f:
        quiz_xml_content = f.read()
    
    # Create ZIP filename (same as XML but with .zip extension)
    zip_filename = xml_file.stem + '.zip'
    zip_path = Path(output_dir) / zip_filename
    
    # Create the ZIP file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add imsmanifest.xml
        zf.writestr('imsmanifest.xml', create_imsmanifest())
        
        # Add quiz.xml (renamed from the original file)
        zf.writestr('quiz.xml', quiz_xml_content)
    
    print(f"✅ Created: {zip_path.name}")
    return True

def process_quiz_directory(quiz_dir):
    """
    Process all XML files in a quiz directory and create ZIP packages.
    
    Args:
        quiz_dir: Path to directory containing quiz XML files
    """
    quiz_path = Path(quiz_dir)
    
    if not quiz_path.exists():
        print(f"❌ Directory not found: {quiz_path}")
        return
    
    # Find all XML files
    xml_files = list(quiz_path.glob('*.xml'))
    
    if not xml_files:
        print(f"⚠️  No XML files found in {quiz_path}")
        return
    
    print(f"\n📦 Processing {len(xml_files)} quiz files in {quiz_path.name}/...")
    print("=" * 70)
    
    success_count = 0
    for xml_file in sorted(xml_files):
        if create_qti_zip(xml_file, quiz_path):
            success_count += 1
    
    print("=" * 70)
    print(f"✅ Successfully created {success_count} ZIP files\n")

def main():
    """Main function to process both vocabulary and assignment quizzes"""
    
    base_dir = Path("g:/My Drive/Colab Notebooks/COSC1315/Quizzes")
    
    print("\n" + "=" * 70)
    print("🎯 QTI Quiz ZIP Package Creator for Canvas")
    print("=" * 70)
    
    # Process Vocabulary Quizzes
    vocab_dir = base_dir / "Vocabulary Quizzes - QTI - Canvas"
    if vocab_dir.exists():
        process_quiz_directory(vocab_dir)
    else:
        print(f"⚠️  Vocabulary quiz directory not found: {vocab_dir}")
    
    # Process Assignment Quizzes
    assignment_dir = base_dir / "Assignment Quizzes - QTI - Canvas"
    if assignment_dir.exists():
        process_quiz_directory(assignment_dir)
    else:
        print(f"⚠️  Assignment quiz directory not found: {assignment_dir}")
    
    print("=" * 70)
    print("✅ All done! ZIP files are ready to upload to Canvas.")
    print("=" * 70)
    print("\n💡 To upload to Canvas:")
    print("   1. Go to your Canvas course")
    print("   2. Navigate to Quizzes")
    print("   3. Click 'Import Quiz'")
    print("   4. Upload the .zip file")
    print("   5. Canvas will automatically extract and import the quiz\n")

if __name__ == "__main__":
    main()
