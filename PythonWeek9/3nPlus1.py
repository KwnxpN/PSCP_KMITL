"""KKK"""

def calcu(num):
    """calculate here"""
    if num%2 == 0:
        return num/2
    return (num*3)+1

def threeplusone():
    """ching chiang chang chi"""
    count = 1
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            while num != 1:
                num = calcu(num)
                count += 1
            print(count)
            count = 1
threeplusone()
