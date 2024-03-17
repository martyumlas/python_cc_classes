from pathlib import Path
import json

def get_stored_username(path):
    try:
        if(path.exists()):
            contents = path.read_text()
            username = json.loads(contents)
            return username
        else:
            return None
    except json.JSONDecodeError:
        return None

def get_new_userame(path):
    username = input('What is your name? ')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():

    path = Path('storing_data/username.json')
    username = get_stored_username(path)

    if username:
        print(f'Welcome back {username}')
    else:
        username = get_new_userame(path)
        print(f'We\'ll remember you when you come back, {username}')

greet_user()
