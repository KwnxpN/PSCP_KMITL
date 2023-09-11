"""KKK"""

def missingnumber(amount):
    """kwnxp.n"""
    full_list = []
    for i in range(1, amount+1):
        full_list.append(i)
    while True:
        num = int(input())
        if num == 0:
            break
        elif num in full_list:
            full_list.remove(num)
    full_list.sort()
    for j in full_list:
        print(j)
missingnumber(int(input()))
