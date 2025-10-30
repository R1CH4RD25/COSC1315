# Lesson 03 Pilot - Walk-Along Format Update

**Date:** October 20, 2025  
**Status:** ✅ Complete - Ready for Review

---

## Changes Made

### 1. Updated Markdown File Format

**File:** `Lesson_03_Variables.md`

**Changes:**
- ❌ **REMOVED:** "Mosh's Solution" sections
- ✅ **ADDED:** "What Mosh Does" - Brief description
- ✅ **ADDED:** "Your Steps" - Numbered instructions
- ✅ **KEPT:** "When You Run Your Code" - Shows expected output
- ✅ **ADDED:** Tips and challenges for engagement

**Philosophy:**
Students should **discover the solution** by watching Mosh and following the steps, not by copying a pre-written answer.

---

### 2. Created Google Colab Notebook

**File:** `Sample Lessons/Lesson_03_Variables_WalkAlong.ipynb`

**Structure:**
Each task has **3 cells:**

1. **📝 Instructions Cell (Markdown)**
   - What Mosh demonstrates
   - Step-by-step guide
   - Expected output

2. **💻 Code Cell (Python)**
   - Starts with `# Type your code below:`
   - Blank for student to write code

3. **✅ Verification Cell (Python)**
   - Checks if variables exist
   - Validates variable values
   - Validates variable types (int, float, str, bool)
   - Provides helpful error messages
   - Celebrates success! 🎉

---

## Verification Features

### What Gets Checked:

#### Task 1: Store and Display a Price
```python
✅ Variable 'price' exists
✅ Value equals 10
```

#### Task 2: Update a Variable Value
```python
✅ Variable 'price' exists
✅ Value equals 20 (not 10)
```

#### Task 3: Work with Different Data Types
```python
✅ Variable 'price' = 10 (type: int)
✅ Variable 'rating' = 4.9 (type: float)
✅ Variable 'name' = 'Mosh' (type: str)
✅ Variable 'is_published' = True (type: bool)
```

#### Task 4: Patient Information System
```python
✅ Variable 'name' = 'John Smith'
✅ Variable 'age' = 20
✅ Variable 'is_new' = True
```

---

## Error Messages

The verification code provides **specific, helpful errors:**

### Example Error Messages:

**Missing Variable:**
```
❌ Error: Variable 'price' not found.
   Make sure you created a variable named 'price'
```

**Wrong Value:**
```
❌ Error: Variable 'price' has value 10, but should be 20
   Remember: You need to reassign the variable to change its value
```

**Wrong Type:**
```
❌ Error: Variable 'rating' should be a float (decimal), got int
```

**Multiple Issues:**
```
❌ Issues found:
   • Variable 'name' should be 'John Smith', got 'John'
   • Variable 'age' should be 20, got 25
```

---

## Success Messages

When students complete tasks correctly, they get **encouraging feedback:**

### Task 1 Success:
```
✅ Perfect! You created the variable 'price' and assigned it the value 10.
   Great job!
```

### Task 3 Success:
```
✅ Outstanding! You created all four data types correctly!
   • Integer (int): whole numbers
   • Float (float): decimal numbers
   • String (str): text in quotes
   • Boolean (bool): True or False
```

### Final Task Success:
```
✅ Perfect! You've completed the Patient Information System!
   You now understand how to:
   • Create variables with meaningful names
   • Store different types of data
   • Build simple information systems

🎉 Congratulations! You've completed all Walk-Along tasks for Lesson 03!
```

---

## Technical Notes

### Verification Code Approach

**Why Use Verification Cells?**
- Students get **immediate feedback**
- Reduces instructor grading time
- Teaches **debugging skills**
- Builds confidence through success messages

**How It Works:**
1. Uses `try/except` to catch NameError (variable doesn't exist)
2. Checks `locals()` and `globals()` for variable existence
3. Uses `isinstance()` to verify data types
4. Collects all errors before displaying (better UX)

**Limitations:**
- Cannot verify if student used specific syntax (e.g., can't force `print()`)
- Students could create variables in earlier cells and verification would pass
- Type checking strict (e.g., `4.9` is float, `4` is int)

**Future Enhancements:**
- Could add code analysis to check for specific functions
- Could verify number of lines of code
- Could check for specific patterns (e.g., variable reassignment)

---

## Format Comparison

### OLD FORMAT (Showed Solutions):
```markdown
### Task 1: Store and Display a Price

**Description:** Create a variable called price...

**Coding Task:**
```python
# Type your code below:
```

**Mosh's Solution:**  👈 PROBLEM: Students just copy this!
```python
price = 10
print(price)
```

**Expected Output:**
```
10
```
```

### NEW FORMAT (Discovery-Based):
```markdown
### Task 1: Store and Display a Price

**What Mosh Does:**
Mosh creates a variable to store a price and then displays it.

**Your Steps:**
1. Create a variable named `price`
2. Assign it the value `10`
3. Print the variable to see its value

**When You Run Your Code:**
```
10
```
```

---

## Benefits of New Format

### For Students:
✅ **Active Learning** - Must think through the problem  
✅ **Discovery-Based** - Learn by doing, not copying  
✅ **Immediate Feedback** - Know right away if correct  
✅ **Clear Goals** - See expected output upfront  
✅ **Hints Available** - Tips guide without giving away answer  

### For Instructors:
✅ **Auto-Grading** - Verification cells check work automatically  
✅ **Consistent Feedback** - Same error messages for common mistakes  
✅ **Engagement Tracking** - Can see which cells students run  
✅ **Reduced Cheating** - No visible solutions to copy  
✅ **Better Metrics** - Know where students struggle  

---

## Testing Instructions

### To Test This Notebook:

1. **Open in Google Colab:**
   - Navigate to `Sample Lessons/Lesson_03_Variables_WalkAlong.ipynb`
   - Open with Google Colab

2. **Watch the Video:**
   - Go to timestamp 11:27–18:16 in Code with Mosh video
   - Watch Mosh demonstrate Task 1

3. **Follow Along:**
   - Pause video after Mosh codes
   - Type code in the blank cell
   - Run your code cell
   - Run verification cell
   - Check feedback

4. **Try Intentional Errors:**
   - Create wrong variable name (e.g., `prices` instead of `price`)
   - Use wrong value (e.g., `price = 5`)
   - Use wrong type (e.g., `price = "10"` as string)
   - See if error messages are helpful

5. **Complete All Tasks:**
   - Go through all 4 tasks
   - Verify completion message appears

---

## Files Created/Modified

### Modified:
- `Resources/Code with Mosh - Source Lessons/Lesson_03_Variables.md`

### Created:
- `Sample Lessons/` (new directory)
- `Sample Lessons/Lesson_03_Variables_WalkAlong.ipynb`
- `Project Documentation/LESSON_03_PILOT_SUMMARY.md` (this file)

---

## Next Steps

### If Format Approved:

1. ✅ Review Lesson 03 notebook in Colab
2. ⏳ Test with actual students (optional)
3. ⏳ Apply format to remaining 17 lessons
4. ⏳ Create script to automate notebook generation
5. ⏳ Add instructor answer key notebooks

### Potential Improvements:

- **Add Video Embeds** - Embed specific timestamps in Colab
- **Progress Tracking** - Add completion percentage
- **Time Estimates** - Show "~5 minutes" per task
- **Hints System** - Collapsible hints students can reveal
- **Extension Challenges** - Extra tasks for fast learners
- **Code Analysis** - Check for specific functions/patterns

---

## Questions to Consider

1. **Should verification be optional?** (Students could skip)
2. **Should we show partial credit?** (e.g., "3/4 variables correct")
3. **Should we have instructor-only answer notebooks?**
4. **Should verification cells be hidden by default?**
5. **Should we track how many attempts students make?**

---

**Ready for Review!** 🚀

Open the notebook and let me know what you think!
