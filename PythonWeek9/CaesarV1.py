"""KKK"""

def caesar(move, word):
    """sleep when you braindead"""
    upper_list = [chr(i) for i in range(65, 91)]
    lower_list = [chr(i) for i in range(97, 123)]
    mylist = []
    for char in word:
        if char.isalpha():
            if char.islower():
                pos = (lower_list.index(char) + move)%26
                mylist.append(lower_list[pos])
            elif char.isupper():
                pos = (upper_list.index(char) + move)%26
                mylist.append(upper_list[pos])
        else:
            mylist.append(char)
    print(''.join(mylist))
caesar(int(input()), str(input()))
