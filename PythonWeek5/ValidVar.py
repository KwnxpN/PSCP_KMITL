"""KKK"""
def find_punctuation(str_input):
    """punctuation here"""
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~"
    for char in str_input:
        if char in punctuation_chars:
            return True
    return False

def find_reserved_word(input_str):
    """reserved word here"""
    python_keywords = [
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else", "except",
        "finally", "for", "from", "global", "if", "import", "in", "is",
        "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
        "while", "with", "yield"
    ]
    words = input_str.split()
    for word in words:
        if word in python_keywords:
            return True
    return False

def validvar(times):
    """check username no pucntuation no space
    no start with num no reserved word"""
    for _ in range(times):
        username = input()
        if find_punctuation(username) or ' ' in username.strip() or username[0].isnumeric()\
            or find_reserved_word(username):
            print("Invalid")
        else:
            print("Valid")
validvar(int(input()))
