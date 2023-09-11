"""KKK"""
import json
def laststand(number_list):
    """check for the last digit of each number from list(as str)"""

    real_list = json.loads(number_list)
    for num in real_list:
        print(str(num)[-1])
laststand(str(input()))
