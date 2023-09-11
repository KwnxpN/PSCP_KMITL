"""KKK"""

def digcal(num):
    """bruh"""
    if num%9 == 0:
        return 9
    else:
        return num%9
def dignity():
    """pls stop"""
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            result = digcal(num)
        print(result)
dignity()
