'''inflation'''
import math
def inflate(price, years):
    '''find current value of money'''
    price *= 100
    price = int(price)
    for _ in range(years):
        price = price + ((price*381)//10000)
    print(f"{price//100}.{price%100}")
inflate(float(input()), int(input()))
