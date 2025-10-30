# COSC 1315 Quizzes

This folder contains auto-graded quizzes for Canvas LMS in QTI 1.2 format.

## 📁 Folder Structure

```
Quizzes/
├── Vocabulary Quizzes - QTI - Canvas/    # 10-question vocabulary quizzes
└── Assignment Quizzes - QTI - Canvas/    # 10-question application quizzes
```

## 📋 Quiz Standards

Each lesson has **two quizzes**:

### 1. Vocabulary Quiz
- **Questions:** 10 multiple-choice questions
- **Content:** Key terms, definitions, and concepts from the lesson
- **Time Limit:** 10 minutes (600 seconds)
- **Attempts:** 3 attempts allowed
- **Purpose:** Assess understanding of terminology and basic concepts
- **Points:** 10 points (1 point per question)

### 2. Assignment Quiz
- **Questions:** 10 multiple-choice questions
- **Content:** Practical application of lesson tasks (code prediction, debugging, problem-solving)
- **Time Limit:** 15 minutes (900 seconds)
- **Attempts:** 3 attempts allowed
- **Purpose:** Assess ability to apply concepts and write code
- **Points:** 10 points (1 point per question)

## 📤 Importing to Canvas

### Method 1: Individual Quiz Import
1. In Canvas, go to your course → **Quizzes**
2. Click **Options** (⋮) → **Import Quiz**
3. Select **QTI Package**
4. Upload the `.xml` file
5. Click **Import**
6. Review and publish the quiz

### Method 2: Course Import (Multiple Quizzes)
1. Go to **Settings** → **Import Course Content**
2. Select **QTI .zip file** as content type
3. Upload a `.zip` containing multiple quiz XML files
4. Click **Import**
5. Wait for import to complete
6. Review all imported quizzes

## 🎯 Quiz Design Philosophy

**Low-Stakes, Learning-Focused:**
- Multiple attempts encourage learning from mistakes
- Auto-graded for zero instructor workload
- Questions directly tied to lesson content
- Clear, unambiguous answer choices
- Real-world examples (sports themes where appropriate)

**Alignment with Course Goals:**
- Students can pass with 70%+ (realistic for low-motivation learners)
- Questions test practical skills, not memorization
- Format matches verification system in lessons
- Builds confidence through familiar content

## 📝 Quiz Naming Convention

Files are named: `Lesson_XX_Topic_Name_[Vocabulary|Assignment].xml`

Examples:
- `Lesson_05_Type_Conversion_Vocabulary.xml`
- `Lesson_05_Type_Conversion_Assignment.xml`

## ✅ Quality Checklist

Before importing each quiz:
- [ ] 10 questions total
- [ ] All questions have correct answers marked
- [ ] Time limits set (10 min vocab, 15 min assignment)
- [ ] 3 attempts allowed
- [ ] Points configured (1 point per question)
- [ ] Questions align with lesson objectives
- [ ] Code examples use proper formatting
- [ ] Sports/relatable examples included where appropriate

## 🔧 Troubleshooting

**Quiz won't import:**
- Verify XML is valid QTI 1.2 format
- Check that file has `.xml` extension
- Try uploading as .zip if individual import fails

**Questions display incorrectly:**
- Canvas may need HTML entities encoded (`&lt;` for `<`, `&gt;` for `>`)
- Code blocks should use `<pre>` or `<code>` tags
- Check that special characters are properly escaped

**Students can't see quiz:**
- Verify quiz is **published** (not just imported)
- Check availability dates/times
- Ensure quiz is assigned to correct section

## 📊 Current Status

### Completed Quizzes:
- ✅ **Lesson 5: Type Conversion** (Vocabulary + Assignment)

### Pending Quizzes:
- ⏳ Lessons 1-4 (to be created)
- ⏳ Lessons 6-36 (to be created)

## 📚 Related Documentation

- **Lesson Template:** `Project Documentation/Templates/TEACHING_INSTRUCTIONS.md`
- **Course Structure:** `Project Documentation/README.md`
- **Quiz Creation Guidelines:** `Project Documentation/Templates/LESSON_OBJECTIVES_GUIDELINES.md`

---

**Last Updated:** October 30, 2025  
**Format:** QTI 1.2 (Canvas Compatible)  
**Course:** COSC 1315 - Python Programming (Dual Credit)  
**Instructor:** Professor Sullivan, Woodson ISD / Cisco College
