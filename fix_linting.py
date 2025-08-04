#!/usr/bin/env python3
"""
Script to fix common linting issues in the ShellRosetta codebase.
"""

import os
import re
import glob

def fix_file(filepath):
    """Fix common linting issues in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix trailing whitespace
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # Fix blank lines with whitespace
    content = re.sub(r'^\s+$', '', content, flags=re.MULTILINE)
    
    # Ensure file ends with newline
    if not content.endswith('\n'):
        content += '\n'
    
    # Fix double blank lines (reduce to single)
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    # Fix function/class spacing (ensure 2 blank lines before)
    content = re.sub(r'(\n)(def |class )', r'\1\n\2', content)
    
    # Fix imports spacing
    content = re.sub(r'(\n)(from |import )', r'\1\n\2', content)
    
    # Remove unused imports (basic cleanup)
    lines = content.split('\n')
    cleaned_lines = []
    in_imports = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines in import section
        if in_imports and not stripped:
            continue
            
        # Check if we're in import section
        if stripped.startswith(('import ', 'from ')):
            in_imports = True
            # Keep only essential imports for now
            if any(essential in stripped for essential in [
                'typing', 'os', 'sys', 'json', 're', 'collections'
            ]):
                cleaned_lines.append(line)
        elif in_imports and not stripped.startswith(('import ', 'from ')):
            in_imports = False
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    
    content = '\n'.join(cleaned_lines)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    """Fix linting issues in all Python files."""
    python_files = []
    
    # Find all Python files
    for pattern in ['shellrosetta/*.py', 'tests/*.py']:
        python_files.extend(glob.glob(pattern))
    
    print(f"Found {len(python_files)} Python files to fix")
    
    for filepath in python_files:
        fix_file(filepath)
    
    print("Linting fixes completed!")

if __name__ == '__main__':
    main() 