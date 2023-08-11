'''inflation'''
import math
def inflate(money, years):
    '''find current value of money'''
    for _ in range(years):
        new_money = money + (money*0.0381)
        money = new_money
    print("%.2f"%(math.floor(money*100)/100.0))
inflate(float(input()), int(input()))
