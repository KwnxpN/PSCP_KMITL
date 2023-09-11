"""KKK"""

def runlendecode(word_amount):
    """decoding"""
    count = ''
    for letter in word_amount:
        if letter.isdigit():
            count += letter
        else:
            print(letter*int(count), end='')
            count = ''
runlendecode(input())
