"""KKKK"""
def username(name_from_user):
    """make username to lowercase"""
    if name_from_user.isnumeric():
        print("Number")
    elif name_from_user.isupper():
        print("Uppercase")
    elif name_from_user.islower():
        print("Lowercase")
    elif name_from_user.istitle():
        print("Title")
    elif name_from_user.isspace():
        print("Space")
    else:
        print("Other")
username(input())
