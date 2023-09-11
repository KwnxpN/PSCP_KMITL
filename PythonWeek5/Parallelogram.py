"""KKK"""

def parallel(word):
    """upper half"""
    length = len(word)
    for i in range(1, length+1):
        print((" "*(length-1))+ word[0:i])
        length -= 1
    length = len(word)
    for i in range(1, length):
        print(word[i:len(word)] +(" "*i))
parallel(input())
