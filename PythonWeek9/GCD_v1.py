"""KKK"""

def gcd(num1, num2):
    """I hate this"""
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
print(gcd(int(input()), int(input())))
