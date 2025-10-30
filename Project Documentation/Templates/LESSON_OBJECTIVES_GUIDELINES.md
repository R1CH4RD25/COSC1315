# Lesson Objectives Creation Guidelines

## Purpose
This document provides specific instructions for creating **Lesson Objectives** pages that will be posted to Canvas as HTML content. These objectives serve as the student-facing introduction to each lesson and establish clear learning expectations.

---

## File Organization & Naming

### File Location
- **Lesson Objectives (HTML)**: `Objectives/` folder
- **Lesson Notebooks (.ipynb)**: `Lessons/` folder
- **Project Notebooks (.ipynb)**: `Projects/` folder
- **Quiz Files**: `Quizzes/` folder
- **Assessment Files**: `Assessments/` folder
- **Documentation**: `Project Documentation/` folder

### Naming Convention
- **Objectives**: `Lesson_XX_Topic_Name_Objectives.html` (e.g., `Lesson_02_How_Python_Code_Gets_Executed_Objectives.html`)
- **Lessons**: `Lesson_XX_Topic_Name.ipynb` (e.g., `Lesson_02_How_Python_Code_Gets_Executed.ipynb`)
- **Projects**: `Project_XX_Project_Name.ipynb` (e.g., `Project_01_My_Pet_Info.ipynb`)

**Important**: Keep all files organized in their proper folders to maintain a clean workspace structure.

---

## Required Structure

Every Lesson Objectives page must include these **three main sections** in this exact order:

1. **Learning Objectives**
2. **Assignment Instructions**
3. **Key Terms**

---

## Section 1: Learning Objectives

### Format Template
```html
<h1>Lesson XX — [Topic Name]</h1>
<p>&nbsp;</p>

<h2>Learning Objectives</h2>
<p>By the end of this lesson, students will be able to:</p>

<p><strong>[High-level skill/concept category]</strong></p>
<ul>
  <li><p>[Specific measurable objective with code examples when applicable]</p></li>
  <li><p>[Specific measurable objective with code examples when applicable]</p></li>
</ul>

<p><strong>[High-level skill/concept category]</strong></p>
<ul>
  <li><p>[Specific measurable objective with code examples when applicable]</p></li>
</ul>
```

### Content Requirements

**High-level Categories:**
- Must begin with an **action verb** (Understand, Call, Store, Format, Build, Recognize, etc.)
- Should represent a major skill or concept cluster from the lesson
- Use **bold** formatting: `<p><strong>Category name</strong></p>`
- Typically 4-7 categories per lesson

**Specific Objectives (bullets under each category):**
- Begin with action verbs: Explain, Distinguish, Correctly call, Describe, Capture, Use, Manage, Create, Remember, Avoid, etc.
- Include **code examples** wrapped in `<code>` tags when referencing:
  - Functions: `<code>input()</code>`, `<code>print()</code>`
  - Operators: `<code>+</code>`, `<code>==</code>`, `<code>=</code>`
  - Variables: `<code>name</code>`, `<code>age</code>`
  - Data types: `<code>"text"</code>`, `<code>123</code>`
- Use **bold** for important terms: `<strong>variable</strong>`, `<strong>string</strong>`, `<strong>parentheses</strong>`
- Be specific and measurable (students should know exactly what they can do)
- Include practical context where appropriate (e.g., "add a space after `?` in the prompt")

**Number of Objectives:**
- Typically 2-4 specific objectives per category
- Total of 10-20 specific objectives per lesson
- Balance breadth (covering all topics) with depth (meaningful detail)

**Last Category - Common Pitfalls:**
- Usually titled: `<p><strong>Recognize common pitfalls</strong></p>` or `<p><strong>Avoid common errors</strong></p>`
- List typical mistakes students make
- Include what to do instead or what to remember

---

## Section 2: Assignment Instructions

### Format Template
```html
<hr />

<h2>Assignment Instructions</h2>
<p>For this activity, you will:</p>
<ul>
  <li><p>Open a new notebook in Google Colab and give it a title that reflects <strong>Lesson XX — [Topic Name]</strong>.</p></li>
  <li>
    <p>[Main task description]:</p>
    <ul>
      <li><p>[Specific step with code example if applicable]</p></li>
      <li><p>[Specific step with code example if applicable]</p></li>
    </ul>
  </li>
  <li>
    <p>[Extension or additional task]:</p>
    <ul>
      <li><p>[Specific step]</p></li>
      <li><p>[Specific step]</p></li>
    </ul>
  </li>
  <li><p>[Additional requirement - comments, testing, etc.]</p></li>
  <li><p>[Final requirement - debugging exercise, verification, etc.]</p></li>
  <li><p>Run all cells top-to-bottom to ensure there are no errors.</p></li>
  <li><p>Save and submit your completed notebook through <strong>Google Classroom</strong>.</p></li>
</ul>
```

### Content Requirements

**Opening Bullet:**
- Always starts with: "Open a new notebook in Google Colab and give it a title that reflects **Lesson XX — [Topic Name]**."

**Main Task Bullets:**
- Break complex tasks into nested sub-bullets
- Include exact code examples where helpful: `<code>input("What is your name? ")</code>`
- Specify variable names: "Store the result in a variable named `<code>name</code>`"
- Show expected output format: "Print a greeting like `<code>Hi &lt;name&gt;</code>`"
- Use HTML entities for special characters: `&lt;` for `<`, `&gt;` for `>`, `&rarr;` for →, `&rsquo;` for '

**Progressive Structure:**
- Start with basic implementation
- "Extend the program to..." for building on previous work
- "Add brief comments..." for documentation practice
- "Create one short 'broken' example..." for debugging practice

**Closing Bullets:**
- Second-to-last: "Run all cells top-to-bottom to ensure there are no errors."
- Last: "Save and submit your completed notebook through **Google Classroom**."

---

## Section 3: Key Terms (Vocabulary)

### Purpose
The Key Terms section serves as the **vocabulary list** for the lesson. These terms:
- Are the essential vocabulary students must learn and understand
- Will be used throughout the lesson in explanations and examples
- Will appear on vocabulary quizzes for this lesson
- Help students build a strong foundation of programming terminology
- Give students a preview of what concepts they'll encounter

### Format Template
```html
<hr />

<h2>Key Terms</h2>
<ul>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
  <li><p><strong>[Term]</strong> &mdash; [Clear, concise definition with examples if needed].</p></li>
</ul>
```

### Content Requirements

**CRITICAL: Exactly 10 Terms Per Lesson**
- Every lesson must have **exactly 10 key terms** - no more, no less
- These are the vocabulary words students will be quizzed on
- If a lesson has more than 10 important terms, select the 10 most essential
- If a lesson has fewer than 10 obvious terms, include related foundational terms or expand to closely related concepts

**Term Selection Priority:**
1. **New Python-specific terms** introduced in this lesson (`input`, `print`, `variable`, `int`, `float`, `str`, etc.)
2. **New programming concepts** taught in this lesson (`function`, `argument`, `concatenation`, `expression`, etc.)
3. **Technical terminology** students must understand (`syntax`, `return value`, `data type`, etc.)
4. **Important operators or symbols** used in the lesson (if they have names worth learning)
5. **Foundational terms** that support understanding of new concepts
6. **Related terms** that provide context or prevent confusion

**Definition Format:**
- Begin with term in **bold**: `<strong>Input</strong>`
- Use em dash: `&mdash;` (not hyphen or regular dash)
- Write clear, student-friendly definitions that students can understand and remember
- Include code examples in definitions when helpful: `<code>input("...")</code>`
- End each definition with a period
- Use `<code>` tags for any code: `<code>()</code>`, `<code>"text"</code>`, `<code>+</code>`
- Keep definitions focused and practical (students will be tested on these)

**Definition Quality:**
- **Length**: One or two sentences maximum
- **Clarity**: Avoid circular definitions (don't define "variable" as "a place to store variables")
- **Context**: Include practical context when possible: "Built-in function that shows a prompt and returns what the user types (as a string)"
- **Relationships**: Show how terms relate to each other when helpful
- **Examples**: Provide concrete examples that clarify meaning
- **Testable**: Write definitions that students can learn and recall for quizzes

**Ordering Terms:**
- Order terms logically based on how they appear in the lesson (introduction sequence)
- OR group related concepts together (all functions, then all data types, etc.)
- OR alphabetize for easy reference
- Be consistent within your course materials

---

## HTML Formatting Standards

### Required HTML Tags
- `<h1>` for lesson title
- `<h2>` for section headers
- `<p>` for all paragraph text (even single sentences)
- `<ul>` and `<li>` for all lists
- `<strong>` for bold text (terms, important concepts)
- `<code>` for all code snippets, functions, variables, operators
- `<hr />` for section dividers

### HTML Entities
- `&mdash;` for em dash (—)
- `&lt;` for less-than (<)
- `&gt;` for greater-than (>)
- `&rarr;` for right arrow (→)
- `&rsquo;` for right single quotation mark (')
- `&ldquo;` and `&rdquo;` for left and right double quotation marks (" ")
- `&nbsp;` for non-breaking space

### Nesting Rules
- Nested lists must have proper structure:
```html
<li>
  <p>Outer item text:</p>
  <ul>
    <li><p>Inner item text</p></li>
  </ul>
</li>
```
- Every `<p>` must have closing `</p>`
- Every list item must contain `<p>` tags

---

## Quality Checklist

Before finalizing any Lesson Objectives page, verify:

**Content Completeness:**
- [ ] All three sections present (Learning Objectives, Assignment Instructions, Key Terms)
- [ ] Learning objectives cover all major concepts from the lesson
- [ ] Assignment instructions are clear, step-by-step, and actionable
- [ ] Exactly 10 vocabulary terms defined in Key Terms section
- [ ] All key terms are relevant to the lesson and will be quizzed
- [ ] Code examples are accurate and properly formatted

**Structure:**
- [ ] Lesson title matches format: `<h1>Lesson XX — Topic Name</h1>`
- [ ] Learning objectives grouped into logical categories
- [ ] Each category has 2-4 specific, measurable objectives
- [ ] Assignment instructions progress from simple to complex
- [ ] Key terms are clearly defined with examples

**HTML Formatting:**
- [ ] All tags properly opened and closed
- [ ] Proper nesting (especially in nested lists)
- [ ] `<code>` tags used for all code references
- [ ] `<strong>` tags used for important terms and bold text
- [ ] HTML entities used for special characters
- [ ] `<hr />` dividers between sections
- [ ] `<p>&nbsp;</p>` after title (for spacing)

**Clarity & Pedagogy:**
- [ ] Language is student-friendly and clear
- [ ] Objectives use action verbs and are measurable
- [ ] Instructions are specific enough to follow without confusion
- [ ] Definitions avoid jargon or explain technical terms
- [ ] Examples illuminate rather than confuse

---

## Assistant's Creation Process

When asked to create Lesson Objectives, you will:

1. **Analyze the lesson content** from the corresponding Jupyter notebook in `Lessons/` folder
2. **Identify 4-7 major skill/concept categories** for Learning Objectives
3. **Write 2-4 specific, measurable objectives** under each category
4. **Add a "Recognize common pitfalls" category** with typical errors
5. **Design progressive assignment instructions** that build from basic to advanced
6. **Include a debugging exercise** in assignment instructions
7. **Extract and define exactly 10 key terms** from the lesson (the vocabulary words for quizzes)
8. **Format everything in proper HTML** following the standards above
9. **Verify against the quality checklist** before presenting
10. **Save the file** in the `Objectives/` folder with proper naming: `Lesson_XX_Topic_Name_Objectives.html`

### Output Expectations

Your output must be:
- **Complete HTML** ready to paste directly into Canvas
- **Properly formatted** with correct nesting and entities
- **Content-rich** with specific code examples and clear explanations
- **Pedagogically sound** with measurable objectives and logical progression
- **Consistent** with the structure and style shown in the example
- **Error-free** HTML that will render correctly in Canvas
- **Saved in the correct location**: `Objectives/Lesson_XX_Topic_Name_Objectives.html`

---

## Example Reference

The example provided (Lesson 04 — Receiving Input) demonstrates all requirements:
- 6 learning objective categories
- 14 specific measurable objectives
- Progressive assignment instructions with nested steps
- **Exactly 10 key terms** (vocabulary words) with clear, testable definitions
- Proper HTML formatting throughout
- Code examples in `<code>` tags
- Bold terms in `<strong>` tags
- Correct use of HTML entities

**Use this example as your quality standard for all lesson objectives you create.**
