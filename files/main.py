from pathlib import Path

guest = input('Enter your name: ')

path = Path('files/guest_book.txt')

content = path.read_text()

new_content = content + '\n' + guest

path.write_text(new_content) 

print(content)
