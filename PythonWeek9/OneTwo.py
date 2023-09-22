"""KKK"""

def onetwo(num):
    """wang toow"""
    return str(num) if num == 1 or num == 2 else onetwo(num-1) + onetwo(num-2)
print(onetwo(int(input())))
