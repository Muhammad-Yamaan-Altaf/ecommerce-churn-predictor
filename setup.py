import os

# Folders and Files list
folders = ['data/raw', 'data/processed', 'src']
files = [
    'src/ingest.py', 
    'src/clean.py', 
    'src/train.py', 
    'src/app.py',
    '.gitignore',
    'requirements.txt',
    'README.md'
]

# 1. Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Folders created: {folder}")

# 2. Create files
for file in files:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            pass 
        print(f"Files created: {file}")

# 3. .gitignore content
with open('.gitignore', 'w') as f:
    f.write("env/\n__pycache__/\n*.csv\n*.pkl\n")
