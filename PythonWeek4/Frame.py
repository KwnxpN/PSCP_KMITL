"""KKKK"""

def frame(text_input):
    """make * frame around input"""
    obeject_length = len(text_input)+2
    print("*" * obeject_length)
    print("*"+text_input+"*")
    print("*" * obeject_length)
frame(str(input()))
