# Lesson 6: Strings - Build Plan

**Status:** Objectives HTML Complete ✅  
**Next:** Create remaining 4 components  
**Video:** Code with Mosh 29:28-37:28

---

## ✅ Completed

### 1. Objectives HTML
- **File:** `Objectives/Lesson_06_Strings_Objectives.html`
- **Status:** ✅ Created and saved locally
- **Key Terms:** 10 (exactly as required)
- **Objective Categories:** 6
- **Ready for:** Canvas import

---

## 📋 To Build

### 2. Lesson Notebook (`Lessons/Lesson_06_Strings.ipynb`)

**Structure:**
```
Cell 1: Title - # Lesson 06 — Strings (29:28–37:28)
Cell 2: Watch Section - Video link with timestamp
Cell 3: Objectives - Copy from objectives HTML
Cell 4: Setup Cell - Download lesson_06_verification.py from GitHub

WALK-ALONG TASKS (15 points total):
  Task 1: String Methods (5 pts)
    - Use .upper(), .lower(), .find()
    - Check "in" operator
  
  Task 2: Indexing (5 pts)
    - Access characters with [0], [-1]
    - Understand zero-based indexing
  
  Task 3: Slicing (5 pts)
    - Extract substrings with [start:end]
    - Practice [:end] and [start:]

TRY IT YOURSELF (45 points total):
  Task 1: Player Name Formatter (15 pts)
    - Input: player name
    - Output: UPPERCASE for jersey
    - Use: .upper() method
  
  Task 2: Team Chant Generator (15 pts)
    - Input: team name (e.g., "WARRIORS")
    - Extract first 3 letters: "WAR"
    - Repeat 3 times: "WAR WAR WAR!"
    - Use: slicing and string concatenation
  
  Task 3: Player Stats Display (15 pts)
    - Input: name, position, number
    - Use f-string: f"{number}: {name} - {position}"
    - Output: "23: Jordan - Guard"

DEBUG THE BUG (40 points total):
  Task 1: Off-by-One Error (15 pts)
    - Bug: name[1:5] gets "ames" instead of "James"
    - Fix: name[0:5]
  
  Task 2: Missing Slice End (10 pts)
    - Bug: team[:] returns whole string, not first 4
    - Fix: team[:4]
  
  Task 3: Immutable String (15 pts)
    - Bug: name[0] = "J" causes error
    - Fix: name = "J" + name[1:]

GRADE CALCULATION & HELP SECTIONS
```

### 3. Verification System (`Lessons/Verifications/lesson_06_verification.py`)

**Functions Needed:**
```python
verify_walk_along_1()  # String methods (5 pts)
verify_walk_along_2()  # Indexing (5 pts)
verify_walk_along_3()  # Slicing (5 pts)
verify_try_it_yourself_1()  # Player formatter (15 pts)
verify_try_it_yourself_2()  # Team chant (15 pts)
verify_try_it_yourself_3()  # Stats display (15 pts)
verify_debug_1()  # Off-by-one (15 pts)
verify_debug_2()  # Missing slice (10 pts)
verify_debug_3()  # Immutable string (15 pts)
calculate_grade()  # Total: 100 points
```

**Verification Checks:**
- Variable existence and types
- Correct use of .upper(), .lower(), .find()
- Proper indexing (positive and negative)
- Correct slicing syntax
- F-string formatting
- Code uses required methods

### 4. Vocabulary Quiz (`Quizzes/Vocabulary Quizzes - QTI - Canvas/Lesson_06_Strings_Vocabulary.xml`)

**10 Questions (1 point each, 10 minutes, 3 attempts):**

1. What is a string in Python?
   - ✅ A sequence of characters enclosed in quotes
   
2. What is zero-based indexing?
   - ✅ Counting positions starting from 0; first character is at index 0
   
3. What does negative indexing do?
   - ✅ Counts from the end (-1 is last character)
   
4. What is slicing?
   - ✅ Extracting a substring using [start:end] notation
   
5. What does immutable mean for strings?
   - ✅ Cannot be changed after creation; methods return new strings
   
6. What is a string method?
   - ✅ A function that belongs to string objects
   
7. What is an f-string?
   - ✅ Formatted string literal with f prefix allowing expressions in {}
   
8. What is a substring?
   - ✅ A portion or slice of a larger string
   
9. What causes an IndexError?
   - ✅ Attempting to access an invalid string index
   
10. In slicing [start:end], is end included?
    - ✅ No, end is exclusive (not included)

### 5. Assignment Quiz (`Quizzes/Assignment Quizzes - QTI - Canvas/Lesson_06_Strings_Assignment.xml`)

**10 Questions (1 point each, 15 minutes, 3 attempts):**

1. Code Output: What does `name = "Python"; print(name[0])` output?
   - ✅ P
   
2. Code Output: What does `word = "Hello"; print(word[-1])` output?
   - ✅ o
   
3. Slicing: `team = "WARRIORS"; print(team[0:3])` outputs what?
   - ✅ WAR
   
4. Debug: Fix `name = "John"; name[0] = "D"` (TypeError)
   - ✅ name = "D" + name[1:]
   
5. String Method: Convert "warriors" to uppercase for jersey
   - ✅ "warriors".upper()
   
6. Find Method: `text = "Python"; text.find("th")` returns?
   - ✅ 2
   
7. Slicing Default: `word = "Python"; word[:3]` outputs?
   - ✅ Pyt
   
8. F-string: Show player #23 named Jordan
   - ✅ f"{23}: Jordan"
   
9. Immutable: Why doesn't `name.upper()` change name?
   - ✅ Strings are immutable; must assign result to variable
   
10. Sports Example: Extract "TD" from "TOUCHDOWN"
    - ✅ word[0:2] or word[:2]

---

## 🎯 Sports Theme Examples

**Player Names:**
- "CURRY" → jersey display
- "Durant" → "DURANT"
- Position formatting

**Team Names:**
- "WARRIORS" → "WAR WAR WAR!"
- "COWBOYS" → "COW COW COW!"
- Team chants

**Stats Display:**
- "#23: Jordan - Guard"
- "#30: Curry - Guard"
- "#34: Giannis - Forward"

**Game Terms:**
- "TOUCHDOWN" → "TD"
- "FIELD GOAL" → "FG"
- Abbreviations

---

## ⚠️ Common Student Errors (Address in lesson)

1. **Off-by-One Errors**
   - Thinking first character is [1]
   - Forgetting end is exclusive in slicing

2. **Trying to Modify Strings**
   - `name[0] = "J"` → TypeError
   - Must create new string

3. **Forgetting Method Returns New String**
   - `name.upper()` without assignment
   - Original unchanged

4. **Invalid Indices**
   - Accessing beyond string length
   - Gets IndexError

---

## 📊 Point Distribution

| Section | Tasks | Points | Notes |
|---------|-------|--------|-------|
| Walk-Along | 3 | 15 | Follow Mosh video |
| Try It Yourself | 3 | 45 | Independent coding |
| Debug | 3 | 40 | Find and fix errors |
| **Total** | **9** | **100** | Notebook grade |
| Vocabulary Quiz | 10 | 10 | Canvas quiz |
| Assignment Quiz | 10 | 10 | Canvas quiz |
| **Lesson Total** | | **120** | Complete package |

---

## 🔗 GitHub URLs (After Upload)

- **Notebook:** `https://colab.research.google.com/github/R1CH4RD25/COSC1315/blob/main/Lessons/Lesson_06_Strings.ipynb`
- **Verification:** `https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_06_verification.py`

---

## ✅ Quality Checklist (Before Commit)

- [ ] Objectives HTML: 10 key terms, 6 categories
- [ ] Notebook: Setup cell uses urllib.request
- [ ] Notebook: 9 tasks with verification cells
- [ ] Notebook: Sports-themed examples
- [ ] Verification: 10 functions (9 tasks + calculate_grade)
- [ ] Vocabulary Quiz: 10 questions from key terms
- [ ] Assignment Quiz: 10 questions from tasks
- [ ] All files tested in Colab
- [ ] Files committed to C:\Dev\COSC1315
- [ ] Pushed to GitHub

---

**Next Steps:**
1. Create remaining 4 files for Lesson 6
2. Test complete workflow in Colab
3. Push to GitHub
4. Repeat process for Lessons 7-18

**Estimated Time per Lesson:** 2-3 hours (once template established)
