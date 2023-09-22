"""KKK"""

def letterfreq(word):
    """find the most usage alphabet"""
    mydict = {}
    word = word.lower().replace(".", "").replace(" ", "")
    for char in word:
        if char not in mydict:
            mydict.update({char: word.count(char)})
    mydict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
    result = list(mydict.keys())[0]
    print(str(result))
letterfreq(str(input()))
