"""KKK"""

def blyadnary(num):
    """make blyadnary"""
    if num == 0:
        print("0")
    mylist = []
    while num != 0:
        mylist.append(num%2)
        num = num//2
    mylist.reverse()
    print(*mylist, sep="")
blyadnary(int(input()))
