"""KKK"""
import re

def seeker(encode_word):
    """find number inside the str (very very long str)"""
    result = 0
    all_numbers = re.findall(r'\d+', encode_word)
    for number in all_numbers:
        result += int(number)
    print(result)
seeker(input())
