"""KKK"""

def gcdv2(num1, num2):
    """I hate this"""
    if num2 == 0:
        return num1
    else:
        return gcdv2(num2, num1 % num2)
print(gcdv2(int(input()), int(input())))
