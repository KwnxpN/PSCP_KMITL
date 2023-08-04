"""SumOfNumber"""

def find_sum():
    """find sum of all num and stop at -1"""
    sum_number = 0
    target_num = int(input())
    while True:
        number = int(input())
        if number != -1:
            sum_number += number
        if sum_number == target_num:
            break
        elif number == -1:
            break
    print(sum_number)
find_sum()
