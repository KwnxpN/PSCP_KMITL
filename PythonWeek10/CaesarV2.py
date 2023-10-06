"""KKK"""

def cal(word):
    """cal"""
    mylist = []
    upper_list = [chr(i) for i in range(65, 91)]
    lower_list = [chr(i) for i in range(97, 123)]
    for char in word:
        if char.isalpha():
            if char.islower():
                pos = (lower_list.index(char) + 1)%26
                mylist.append(lower_list[pos])
            elif char.isupper():
                pos = (upper_list.index(char) + 1)%26
                mylist.append(upper_list[pos])
        else:
            mylist.append(char)
    convert = map(str, mylist)
    res = ''.join(convert)
    return res

def caesar(word):
    """sleep when you braindead"""
    proba_word = ["when", "where", "which", "the", "how", "what"]
    for _ in range(26):
        word_list = word.split()
        for j in word_list:
            if j.lower() in proba_word:
                print(word)
                break
        word = cal(word)
caesar(str(input()))
