from name_function import get_formatted_name

def test_first_last_name():
    assert get_formatted_name('emperor', 'amedeka') == 'Emperor Amedeka'

def test_first_last_middle_name():
    assert get_formatted_name('emperor', 'amedeka', 'cofie') == 'Emperor Cofie Amedeka'
    