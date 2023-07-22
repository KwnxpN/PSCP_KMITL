"""KKK"""

def largestnum(num1, num2, num3):
    """lll"""
    first_num1 = float(str(num1)[0])
    first_num2 = float(str(num2)[0])
    first_num3 = float(str(num3)[0])
    if first_num1 < first_num2:
        num1, num2 = num2, num1
    elif num1 < num2:
        num1, num2 = num2, num1
    if first_num2 < first_num3:
        num2, num3 = num3, num2
    elif num2 < num3:
        num2, num3 = num3, num2
    if first_num1 < first_num2:
        num1, num2 = num2, num1
    elif num1 < num2:
        num1, num2 = num2, num1
    print("%d%d%d" %(num1, num2, num3))
largestnum(float(input()), float(input()), float(input()))
