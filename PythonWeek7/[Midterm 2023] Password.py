"""KKK"""
from math import log2
def password(password_get):
    """https://open.spotify.com/track/7lzBosqmvUZz5j5ReADkxq?si=a8312319880b4837"""

    lower_pool = 0
    upper_pool = 0
    number_pool = 0
    printable_pool = 0
    length = len(password_get)
    for i in password_get:
        if i.islower() == True:
            lower_pool = 26
        elif i.isupper() == True:
            upper_pool = 26
        elif i.isdigit() == True:
            number_pool = 10
        elif i.isprintable() == True:
            printable_pool = 32
    pool = lower_pool + upper_pool + number_pool + printable_pool
    entropy = int(log2(pool**length))
    if entropy < 28:
        print(entropy)
        print("Very Weak")
    elif 28 <= entropy <= 35:
        print(entropy)
        print("Weak")
    elif 36 <= entropy <= 59:
        print(entropy)
        print("Reasonable")
    elif 60 <= entropy <= 127:
        print(entropy)
        print("Strong")
    elif entropy >= 128:
        print(entropy)
        print("Very Strong")
password(input())
