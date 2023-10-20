"""KKK"""

def coin_changev1(money_get):
    """selected the best way to change money"""
    coins = [25, 10, 5, 1]
    total = 0
    for coin in coins:
        total = total + money_get//coin
        money_get = money_get%coin
    print(total)
coin_changev1(int(input()))
