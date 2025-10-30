import json

# Read the notebook
with open('Lessons/Lesson_05_Type_Conversion.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Find the setup cell (should be around index 3 based on structure)
setup_cell_index = None
for i, cell in enumerate(notebook['cells']):
    if 'source' in cell and len(cell['source']) > 0:
        # Check if this is the setup cell
        first_line = cell['source'][0] if isinstance(cell['source'], list) else cell['source']
        if 'Download verification' in first_line or 'Mount Google Drive' in first_line or 'Setup' in str(cell.get('source', '')):
            if cell['cell_type'] == 'code':
                setup_cell_index = i
                break

if setup_cell_index is None:
    print("Could not find setup cell!")
else:
    print(f"Found setup cell at index {setup_cell_index}")
    
    # Replace the setup cell content
    notebook['cells'][setup_cell_index]['source'] = [
        "# Download verification file from GitHub\n",
        "import urllib.request\n",
        "import os\n",
        "\n",
        "# Download the verification file\n",
        "url = 'https://raw.githubusercontent.com/R1CH4RD25/COSC1315/main/Lessons/Verifications/lesson_05_verification.py'\n",
        "filename = 'lesson_05_verification.py'\n",
        "\n",
        "print('Downloading verification file...')\n",
        "urllib.request.urlretrieve(url, filename)\n",
        "\n",
        "# Verify download\n",
        "if os.path.exists(filename):\n",
        "    print(f'✅ Downloaded {filename} successfully!')\n",
        "    print(f'File size: {os.path.getsize(filename)} bytes')\n",
        "else:\n",
        "    print('❌ Download failed!')\n",
        "\n",
        "# Show current directory and files\n",
        "print(f'Current directory: {os.getcwd()}')\n",
        "print(f'Files in directory: {os.listdir()}')\n",
        "\n",
        "# Add current directory to Python path\n",
        "import sys\n",
        "if os.getcwd() not in sys.path:\n",
        "    sys.path.insert(0, os.getcwd())\n",
        "\n",
        "# Import verification functions\n",
        "from lesson_05_verification import (\n",
        "    verify_walk_along_1,\n",
        "    verify_walk_along_2,\n",
        "    verify_walk_along_3,\n",
        "    verify_walk_along_4,\n",
        "    verify_try_it_yourself_1,\n",
        "    verify_try_it_yourself_2,\n",
        "    verify_try_it_yourself_3,\n",
        "    verify_debug_1,\n",
        "    verify_debug_2,\n",
        "    verify_debug_3,\n",
        "    calculate_grade\n",
        ")\n",
        "\n",
        "print('✅ Setup complete! You\\'re ready to start coding.')"
    ]
    
    # Save the updated notebook
    with open('Lessons/Lesson_05_Type_Conversion.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print("✅ Updated Lesson_05_Type_Conversion.ipynb successfully!")
    print(f"Setup cell now has {len(notebook['cells'][setup_cell_index]['source'])} lines")
