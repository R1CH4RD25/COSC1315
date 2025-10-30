# Scripts Directory

This directory contains Python scripts used for course development and content management for COSC 1315.

## 📂 Active Scripts

### Content Extraction & Organization

#### `youtube_transcript_extractor.py`
**Purpose:** Extract transcripts from YouTube videos using the YouTube Transcript API  
**Usage:** Run to download transcripts for educational videos  
**Status:** ✅ Working - Use for future video transcript needs  
**Dependencies:** `youtube-transcript-api`

#### `extract_all_mosh_lessons.py`
**Purpose:** Parse the master Code with Mosh markdown file and create individual lesson files  
**Usage:** Already completed - created all 18 lesson files in `Resources/Code with Mosh - Source Lessons/`  
**Status:** ✅ Complete - Keep for reference or future re-extraction  
**Output:** 18 individual lesson markdown files with transcripts and metadata

### Document Creation

#### `recreate_syllabus.py`
**Purpose:** Recreate the course syllabus in DOCX format from PDF source  
**Usage:** Generates formatted Word document with tables, course information, schedule  
**Status:** ✅ Working - Successfully created `COSC_1315_Syllabus_RECREATED.docx`  
**Dependencies:** `pdfplumber`, `python-docx`

### Learning Objectives Management

#### `add_objectives_to_lessons.py`
**Purpose:** Add comprehensive Learning Objectives and Key Terms sections to all lesson files  
**Usage:** Already completed - added structured objectives to all 18 lessons  
**Status:** ✅ Complete - Final working version with duplicate detection  
**Features:**
- Adds Learning Objectives with 4-7 categories per lesson
- Adds Key Terms with definitions
- HTML-convertible markdown syntax
- Checks for existing objectives to prevent duplicates

#### `remove_duplicate_objectives.py`
**Purpose:** Clean up duplicate Learning Objectives sections that were accidentally added multiple times  
**Usage:** One-time cleanup script  
**Status:** ✅ Complete - Successfully removed all duplicates from 18 files  
**Note:** Keep for reference in case of future similar issues

#### `add_missing_key_terms.py`
**Purpose:** Add additional key terms to lessons with fewer than 10 terms (minimum requirement for quizzes)  
**Usage:** Already completed - brought all lessons up to minimum 10 key terms  
**Status:** ✅ Complete - All 18 lessons now have 10+ terms  
**Terms Added:** 10 lessons received 1-5 additional terms each

#### `add_walk_along_sections.py`
**Purpose:** Extract and structure Mosh's "Walk-Along" coding examples from lesson transcripts  
**Usage:** Already completed - added Walk-Along sections to all 18 lessons  
**Status:** ✅ Complete - 47 total coding tasks across 18 lessons  
**Features:**
- Identifies coding examples Mosh demonstrates in videos
- Formats with Task Title, Description, Starter Code, Solution, Expected Output
- Structured for easy extraction into Colab notebooks
- Prevents duplicate insertion

## 📊 Completed Tasks Summary

### ✅ Syllabus Recreation
- Extracted content from 9-page PDF
- Created formatted DOCX with all tables and content
- Output: `COSC_1315_Syllabus_RECREATED.docx`

### ✅ Code with Mosh Lesson Extraction
- Parsed master lesson document
- Created 18 individual lesson files
- Each includes: title, timestamp, week number, transcript, teaching notes template
- Location: `Resources/Code with Mosh - Source Lessons/`

### ✅ Learning Objectives Addition
- Added Learning Objectives sections to all 18 lessons
- Added Key Terms sections with minimum 10 terms each
- All use HTML-convertible markdown syntax
- Ready for Canvas import and quiz generation

### ✅ Walk-Along Coding Tasks
- Extracted 47 coding examples from Mosh's video demonstrations
- Added structured Walk-Along sections to all 18 lessons
- Format: Task Title → Description → Starter Code → Solution → Expected Output
- Prepared for Colab notebook integration
- Report: `../WALK_ALONG_SECTIONS_SUMMARY.md`

## 🗑️ Removed Scripts (October 20, 2025)

The following scripts were removed as obsolete or broken:

- ❌ `add_all_objectives.py` - Had syntax errors, replaced by `add_objectives_to_lessons.py`
- ❌ `extract_syllabus.py` - One-time use script, task completed
- ❌ `create_mosh_lesson_files.py` - Replaced by `extract_all_mosh_lessons.py`

## 🔧 Dependencies

Install required packages:
```bash
pip install youtube-transcript-api pdfplumber python-docx reportlab pypdfium2
```

## 📝 Script Development Notes

### Best Practices Applied
1. **UTF-8 Encoding:** All scripts use `encoding='utf-8'` for file operations
2. **Error Handling:** Scripts check for existing content before adding duplicates
3. **Regex Patterns:** Use `re.DOTALL` for multiline content matching
4. **Verification:** Count and report results after operations
5. **Backup Strategy:** Test on single files before batch processing

### Lessons Learned
- Always check for existing content before inserting
- Use `## Key Terms` as duplicate check (more reliable than `## Learning Objectives`)
- Test regex patterns on small samples first
- Keep cleanup scripts even after use (helpful for future issues)
- Document what worked for future reference

## 📂 Related Documentation

- `../OBJECTIVES_COMPLETION_REPORT.md` - Full report on objectives addition
- `../OBJECTIVES_PROGRESS.md` - Progress tracking document
- `../MASTER_REFERENCE_GUIDE.md` - Complete course development guide
- `../SCHEDULE_STATUS_URGENT.md` - Current schedule and priorities

---

**Last Updated:** October 20, 2025  
**Maintained By:** Course Development Team
