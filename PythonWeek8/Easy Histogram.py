"""KKK"""

def ezhisto(word):
    """why P'Tae do this to me"""
    amount = {}
    word = word.replace(" ", "")
    for char in word:
        if char not in amount:
            amount[char] = 1
        else:
            amount[char] += 1
    result = sorted(amount.items(), key=lambda v: (v[0].lower(), v[0].isupper()))
    for char, amount in result:
        print(char, "=", amount)
ezhisto(str(input()))
