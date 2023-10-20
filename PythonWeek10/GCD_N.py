"""KKK"""

def gcd_recur(num1, num2):
    "recursive"
    return num1 if num2 == 0 else gcd_recur(num2, num1 % num2)

def gcd_n(amount):
    """main"""
    num_list = []
    for _ in range(amount):
        num_list.append(int(input()))
    gcd = num_list[0]
    for i in range(amount):
        gcd = gcd_recur(gcd, num_list[i])
    print(gcd)
gcd_n(int(input()))
