"""KKK"""

def missingnumber(amount):
    """hello blyad"""
    full_set, get_set = set(), set()
    for i in range(1, amount+1):
        full_set.add(i)
    while True:
        num = int(input())
        if num == 0:
            break
        get_set.add(num)
    result = sorted(full_set.difference(get_set))
    for i in result:
        print(i)
missingnumber(int(input()))
