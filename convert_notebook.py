import json

# Read the VSCode-style notebook
with open('Lessons/Lesson_05_Type_Conversion.ipynb', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse as JSON if it starts with VSCode.Cell format
if '<VSCode.Cell' in content:
    print("Converting from VSCode format to standard Jupyter format...")
    
    # This is VSCode format, we need to convert it
    # For now, let's just check if there's a standard JSON version
    import re
    
    # Try to extract cells
    cells = []
    cell_pattern = r'<VSCode\.Cell id="([^"]+)" language="([^"]+)">\n(.*?)\n</VSCode\.Cell>'
    matches = re.findall(cell_pattern, content, re.DOTALL)
    
    for cell_id, language, cell_content in matches:
        cell = {
            "cell_type": "markdown" if language == "markdown" else "code",
            "metadata": {
                "id": cell_id.replace("#VSC-", ""),
                "language": language
            },
            "source": [line for line in cell_content.strip().split('\n')]
        }
        
        if cell["cell_type"] == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
            
        cells.append(cell)
    
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            },
            "colab": {
                "provenance": []
            }
        },
        "nbformat": 4,
        "nbformat_minor": 0
    }
    
    # Write standard Jupyter format
    with open('Lessons/Lesson_05_Type_Conversion.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print("✅ Converted to standard Jupyter format!")
else:
    print("Already in standard format or needs manual conversion")
