# Download verification file from GitHub
!wget -q https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_05_verification.py

# Confirm file is present
import os
print("Current working directory:", os.getcwd())
print("Files:", os.listdir())

# Add current directory to Python path
import sys
sys.path.insert(0, os.getcwd())

# Import verification functions
from lesson_05_verification import (
    verify_walk_along_1,
    verify_walk_along_2,
    verify_walk_along_3,
    verify_walk_along_4,
    verify_try_it_yourself_1,
    verify_try_it_yourself_2,
    verify_try_it_yourself_3,
    verify_debug_1,
    verify_debug_2,
    verify_debug_3,
    calculate_grade
)

print("✅ Setup complete! You're ready to start coding.")
