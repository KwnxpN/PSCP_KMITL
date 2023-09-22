"""KKK"""

def diamond(deep, _):
    """I love P'Tae"""
    diamond_list, result_list = [], []
    for _ in range(deep):
        diamond_list = input().split()
        for i in range(len(diamond_list)):
            diamond_list[i] = int(diamond_list[i])
        if result_list == []:
            for i in diamond_list:
                result_list.append(i)
        else:
            result_list = [sum(i) for i in zip(result_list, diamond_list)]
    result_list.sort()
    print(result_list[-1])
diamond(int(input()), int(input()))
