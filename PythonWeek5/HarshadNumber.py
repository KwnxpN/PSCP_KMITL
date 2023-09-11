"""KKK"""

def find_mod_num(number):
    """find module number"""
    mod_num = sum([(int(nnn)) for nnn in str(number)])
    return mod_num
def check():
    """check harshad"""
    for _ in range(10):
        num = abs(int(input()))
        result = find_mod_num(num)
        if result != 0 and num%result == 0:
            print("Yes")
        else:
            print("No")
check()

#another def find mod
"""
def find_mod_num(number):
    mod_num = 0
    for digit in str(number):
        mod_num += int(digit)
    return mod_num
"""