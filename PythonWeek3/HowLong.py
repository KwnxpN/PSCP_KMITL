"""KKKK"""
def howlong(number):
    """find digit of number"""
    abs_num = abs(number)
    digit = 0
    if abs_num > 0:
        while abs_num > 0:
            digit += 1
            abs_num //= 10
    elif abs_num == 0:
        digit += 1
    print(digit)
howlong(int(input()))
