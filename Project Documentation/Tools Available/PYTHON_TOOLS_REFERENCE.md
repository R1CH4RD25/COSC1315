# Python Tools Reference for COSC 1315 Course Development

**Last Updated:** October 20, 2025  
**Purpose:** Quick reference for all Python tools and packages available for course development

---

## 🎯 Overview

This document catalogs all Python tools, packages, and scripts available for developing COSC 1315 course materials. Use this as a quick reference when you need to perform specific tasks.

---

## 📦 Installed Python Packages

### **Core Python Environment**
- **Python Version:** 3.11
- **Location:** `C:\Users\rsullivan\AppData\Local\Programs\Python\Python311\`

### **Document Conversion & Processing**

#### **MarkItDown** (with all dependencies)
```bash
pip install markitdown[all]
```

**Capabilities:**
- ✅ Convert DOCX to Markdown
- ✅ Convert XLSX/Excel to Markdown
- ✅ Convert PPTX/PowerPoint to Markdown
- ✅ Convert PDF to Markdown
- ✅ Extract YouTube transcripts (text-based)
- ✅ Process images with OCR (with Azure AI)
- ✅ Convert HTML to Markdown

**Dependencies Included:**
- `mammoth` - DOCX conversion
- `openpyxl` - Excel file processing
- `pdfminer-six` - PDF text extraction
- `python-pptx` - PowerPoint processing
- `pandas` - Data manipulation
- `beautifulsoup4` - HTML parsing
- `azure-ai-documentintelligence` - Advanced document AI

**Usage Examples:**
```python
from markitdown import MarkItDown

md = MarkItDown()

# Convert DOCX to Markdown
result = md.convert('template.docx')
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(result.text_content)
```

**Note:** The ffmpeg/avconv warning is harmless - only needed for actual audio/video file processing, not for text transcript extraction.

---

#### **YouTube Transcript API** (v1.2.3+)
```bash
pip install --upgrade youtube-transcript-api
```

**Current Version:** 1.2.3 (Updated October 2025)  
**Note:** API changed significantly from v1.0.3 - see new syntax below

**Capabilities:**
- ✅ Extract transcripts from YouTube videos
- ✅ Filter by time ranges (perfect for lessons!)
- ✅ Get exact timestamps for each sentence
- ✅ Multiple language support
- ✅ No API key required
- ✅ Works with Code with Mosh videos
- ✅ Now works with both course videos!

**New API Syntax (v1.2.3+):**
```python
from youtube_transcript_api import YouTubeTranscriptApi

# MUST create an instance first (new in v1.2.3)
api = YouTubeTranscriptApi()

# Fetch transcript (returns FetchedTranscript object)
transcript = api.fetch('_uQrJ0TkZlc')  # Code with Mosh video

# Access transcript entries (iterable)
print(f"Total entries: {len(transcript)}")

# Iterate through entries
for entry in transcript:
    # Each entry has: text, start, duration
    print(f"[{entry.start:.1f}s] {entry.text}")

# Extract specific time range (Lesson 02: 8:08-11:20)
start_time = 8*60 + 8   # 488 seconds
end_time = 11*60 + 20   # 680 seconds

lesson_entries = [
    entry for entry in transcript 
    if start_time <= entry.start <= end_time
]

for entry in lesson_entries:
    print(f"[{entry.start:.1f}s] {entry.text}")
```

**Old API Syntax (v1.0.3 - DEPRECATED):**
```python
# THIS NO LONGER WORKS in v1.2.3+
from youtube_transcript_api import YouTubeTranscriptApi
transcript = YouTubeTranscriptApi.get_transcript(video_id)  # ❌ AttributeError
```

**Time Conversion Helper:**
```python
def timestamp_to_seconds(timestamp):
    """Convert 'MM:SS' or 'H:MM:SS' to seconds"""
    parts = [int(p) for p in timestamp.split(':')]
    if len(parts) == 2:  # MM:SS
        return parts[0] * 60 + parts[1]
    elif len(parts) == 3:  # H:MM:SS
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
```

---

### **VS Code Extensions Installed**

#### **MarkItDown Extension**
- **ID:** `bioinfo.markitdown-vscode`
- **Purpose:** Convert documents directly in VS Code
- **Usage:** Right-click file → Convert with MarkItDown

#### **DOCX Viewer**
- **ID:** `shahilkumar.docxreader`
- **Purpose:** View DOCX files in VS Code
- **Usage:** Click .docx file to preview

---

## 🛠️ Custom Scripts Available

### **1. YouTube Transcript Extractor**
**Location:** `Project Documentation/Scripts/youtube_transcript_extractor.py`

**Purpose:** Extract transcripts from YouTube videos with time range filtering

**Usage:**
```bash
# Extract specific lesson (6:08 to 8:08)
python "Project Documentation/Scripts/youtube_transcript_extractor.py" _uQrJ0TkZlc 6:08 8:08

# Save to file
python "Project Documentation/Scripts/youtube_transcript_extractor.py" _uQrJ0TkZlc 6:08 8:08 --output lesson_01.txt

# Full video transcript
python "Project Documentation/Scripts/youtube_transcript_extractor.py" _uQrJ0TkZlc
```

**Arguments:**
- `video_id` - YouTube video ID (from URL)
- `start` - Start timestamp (MM:SS or H:MM:SS) [optional]
- `end` - End timestamp (MM:SS or H:MM:SS) [optional]
- `--output` / `-o` - Save to file instead of printing [optional]

---

## 📚 Quick Task Reference

### **Converting Documents**

| Task | Tool | Command |
|------|------|---------|
| DOCX → Markdown | MarkItDown | `python -c "from markitdown import MarkItDown; md=MarkItDown(); r=md.convert('file.docx'); open('out.md','w',encoding='utf-8').write(r.text_content)"` |
| PDF → Markdown | MarkItDown | Same as above, just change extension |
| Excel → Markdown | MarkItDown | Same as above, just change extension |

### **Working with YouTube Videos**

| Task | Tool | Command |
|------|------|---------|
| Extract full transcript | youtube-transcript-api | `python Scripts/youtube_transcript_extractor.py VIDEO_ID` |
| Extract time range | youtube-transcript-api | `python Scripts/youtube_transcript_extractor.py VIDEO_ID START END` |
| Save transcript to file | youtube-transcript-api | Add `--output filename.txt` |

### **Finding Video IDs**

**Code with Mosh - Python for Beginners:**
- **Full URL:** `https://www.youtube.com/watch?v=_uQrJ0TkZlc`
- **Video ID:** `_uQrJ0TkZlc`

---

## 🎓 Educational Use Cases

### **For Creating Lesson Objectives:**

```python
# 1. Extract transcript for specific lesson
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "_uQrJ0TkZlc"
start = 8*60 + 8    # Lesson 02 start: 8:08
end = 11*60 + 20    # Lesson 02 end: 11:20

transcript = YouTubeTranscriptApi.get_transcript(video_id)
lesson_text = ' '.join([
    entry['text'] for entry in transcript 
    if start <= entry['start'] <= end
])

# 2. Identify key concepts
# 3. Extract technical terms
# 4. Find code examples
# 5. Create objectives aligned with video
```

### **For Creating Vocabulary Lists:**

```python
import re

# Extract lesson transcript
transcript_text = "..."  # From YouTube API

# Find capitalized technical terms
terms = re.findall(r'\b(?:print|input|int|float|str|variable|function)\b', 
                   transcript_text, re.IGNORECASE)

# Get unique terms
unique_terms = list(set(terms))
print(f"Found {len(unique_terms)} technical terms")
```

### **For Verifying Lesson Content:**

```python
# Compare your lesson content against Mosh's actual words
your_objectives = [...]
mosh_transcript = "..."  # From YouTube API

# Check alignment
for objective in your_objectives:
    if objective.lower() in mosh_transcript.lower():
        print(f"✓ {objective} - Aligned")
    else:
        print(f"⚠ {objective} - Review needed")
```

---

## 🔄 Workflow Integration

### **Creating New Lesson Materials:**

1. **Extract Video Transcript**
   ```bash
   python Scripts/youtube_transcript_extractor.py _uQrJ0TkZlc START END -o temp_transcript.txt
   ```

2. **Identify Key Concepts**
   - Review transcript
   - Highlight technical terms
   - Note code examples

3. **Create Objectives**
   - Use `LESSON_OBJECTIVES_GUIDELINES.md`
   - Align with transcript content
   - Include exactly 10 vocabulary terms

4. **Build Jupyter Notebook**
   - Use `Colab_Lesson_Template_PromptOnly.md`
   - Include transcript timestamps in "Watch" section
   - Add exercises based on video examples

---

## 📖 Additional Resources

### **Other Useful Python Packages (Not Yet Installed)**

### **Source Video Information**

**Code with Mosh - Python Programming Course for Beginners**
- **Full URL:** https://www.youtube.com/watch?v=_uQrJ0TkZlc&vl=en
- **Video ID:** `_uQrJ0TkZlc`
- **Duration:** ~4 hours 58 minutes
- **Language:** English (with auto-generated captions)

---

**For Advanced Needs:**

- **`pytube`** - Download YouTube videos, extract metadata
  ```bash
  pip install pytube
  ```

- **`openai-whisper`** - AI-powered transcription (for videos without captions)
  ```bash
  pip install openai-whisper
  ```

- **`python-docx`** - Create/edit DOCX files programmatically
  ```bash
  pip install python-docx
  ```

- **`nbformat`** - Programmatically create/edit Jupyter notebooks
  ```bash
  pip install nbformat
  ```

### **Documentation Links:**

- **MarkItDown:** https://github.com/microsoft/markitdown
- **YouTube Transcript API:** https://github.com/jdepoix/youtube-transcript-api
- **Python-PPTX:** https://python-pptx.readthedocs.io/
- **Pandas:** https://pandas.pydata.org/docs/

---

## 🚀 Future Tool Ideas

**Potential Scripts to Create:**

1. **Lesson Content Generator**
   - Input: Video ID + time range
   - Output: Draft lesson notebook with transcript-based content

2. **Vocabulary Extractor**
   - Input: Lesson transcript
   - Output: List of 10 most important technical terms

3. **Objectives Generator**
   - Input: Video transcript + lesson template
   - Output: HTML objectives file draft

4. **Quiz Builder**
   - Input: Lesson transcript + vocabulary
   - Output: Canvas-compatible quiz questions

5. **Timestamp Finder**
   - Input: Search term
   - Output: All timestamps where term appears in video

---

## 💡 Pro Tips

### **Working with Timestamps:**

```python
# Quick timestamp converter
def ts_to_sec(ts):
    """Convert '8:08' or '1:20:40' to seconds"""
    parts = [int(x) for x in ts.split(':')]
    if len(parts) == 2:
        return parts[0]*60 + parts[1]
    return parts[0]*3600 + parts[1]*60 + parts[2]

def sec_to_ts(sec):
    """Convert seconds to 'MM:SS' or 'H:MM:SS'"""
    h, m, s = sec//3600, (sec%3600)//60, sec%60
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"
```

### **Caching Transcripts:**

```python
import json
import os

def get_cached_transcript(video_id):
    """Cache transcripts to avoid repeated API calls"""
    cache_file = f"cache_{video_id}.json"
    
    if os.path.exists(cache_file):
        with open(cache_file) as f:
            return json.load(f)
    
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    with open(cache_file, 'w') as f:
        json.dump(transcript, f)
    
    return transcript
```

### **Batch Processing:**

```python
# Extract all lesson transcripts at once
lessons = [
    ("Lesson_01", "6:08", "8:08"),
    ("Lesson_02", "8:08", "11:20"),
    ("Lesson_03", "12:56", "18:16"),
    # ... etc
]

for name, start, end in lessons:
    # Extract and save each lesson's transcript
    pass
```

---

## 📝 Notes for Future Me

- **ffmpeg warning is harmless** - only affects audio/video processing, not text extraction
- **Always test scripts on one lesson first** before batch processing
- **Cache transcripts** to avoid hitting API rate limits
- **Verify auto-generated captions** - they're usually 80-90% accurate
- **Keep timestamps** in lesson materials for student reference
- **Combine AI tools** with your expertise - don't rely solely on automation

---

**Last Updated:** October 20, 2025  
**Maintained By:** Professor Sullivan  
**Course:** COSC 1315.35 - Programming (Python) - Cisco College
