"""KKK"""

def backward():
    """backward"""
    mylist = []
    while True:
        word = input()
        if word == "NULL":
            break
        else:
            mylist.append(word)
    mylist.reverse()
    for i in mylist:
        print(i)
backward()
