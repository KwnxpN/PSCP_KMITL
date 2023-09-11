"""KKK"""

def linesorting(word_amount):
    """sorting group of word by length from short to long"""
    mylist = []
    for _ in range(word_amount):
        mylist.append(input())
    mylist.sort(key=len)
    for word in mylist:
        print(word)
linesorting(int(input()))
