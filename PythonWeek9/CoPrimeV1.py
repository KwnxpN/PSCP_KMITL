"""KKK"""

def gcd(num1, num2):
    """I hate this"""
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

def coprime(num1, num2):
    """hor ror mor hor ror mor I here (Dajim)"""
    hrm = gcd(num1, num2)
    if hrm == 1:
        print("YES")
        print(hrm)
    else:
        print("NO")
        print(hrm)
coprime(int(input()), int(input()))
