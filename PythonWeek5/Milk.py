"""KKKK"""

def milk(price, fah, bonus, money):
    """milk arai wa"""
    get_milk = 0
    get_fah = 0
    while money >= price:
        money -= price
        get_milk += 1
        get_fah += 1
        if get_fah == fah:
            get_milk += bonus
            get_fah = bonus
    print(get_milk)
milk(int(input()), int(input()), int(input()), int(input()))
