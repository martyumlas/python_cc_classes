from name_function import get_formatted_name

def test_first_last_name():
    formated_name = get_formatted_name('janis', 'joplin')
    assert formated_name == 'Janis Joplin'
