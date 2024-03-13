from pathlib import Path

path = Path('exceptions/alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('No file found')
else:
    print(contents)
