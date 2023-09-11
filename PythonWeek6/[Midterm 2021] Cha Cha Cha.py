"""Im supershy supershy but wait a minutes"""
import math
def chachacha(days):
    """calculate how much money haerin make"""
    money = 0
    for _ in range(days):
        hours = math.ceil(float(input()))
        money += hours * 8720
    print(money)
chachacha(int(input()))
