"""KKKK"""

def coke(price, fah, discount, need_coke):
    """I'm gonna hate coca cola this day"""
    res = 0
    if fah != 0 and need_coke > fah:
        need_coke -= fah+1
        res += (price*fah)+discount
        calcu = need_coke//fah
        need_coke -= calcu
        res += calcu*discount
    res += need_coke*price
    print(res)
coke(int(input()), int(input()), int(input()), int(input()))
