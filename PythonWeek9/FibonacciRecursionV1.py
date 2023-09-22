"""KKK"""

def fibona(num):
    """lol"""
    return num if num == 0 or num == 1 else fibona(num-1)+fibona(num-2)
print(fibona(int(input())))
