'''inflation'''
import math

def round_down(n, decimals=0):
    """lol"""
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def inflate(money, years):
    '''find current value of money'''
    for _ in range(years):
        new_money = money + (money*0.0381)
        new_money = round_down(new_money, 2)
        money = new_money
    print(new_money)
inflate(float(input()), int(input()))
