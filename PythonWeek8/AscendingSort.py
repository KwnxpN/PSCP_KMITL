"""KKK"""

def ascsort():
    """ascsort"""
    mylist = []
    for _ in range(5):
        mylist.append(int(input()))
        mylist.sort()
    for i in mylist:
        print(i)
ascsort()
