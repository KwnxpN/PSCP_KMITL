"""KKK"""

def point_sorting(group_amount):
    """sort the linear"""
    lin_list = []
    for _ in range(group_amount):
        linear_amount = int(input())
        for _ in range(linear_amount):
            linear = input().split()
            linear = list(map(int, linear))
            total = sum(linear)
            everything = [total]
            everything.extend(linear)
            lin_list.append(everything)
        lin_list.sort()
        for i in range(len(lin_list)):
            print(lin_list[i][1], lin_list[i][2])
        lin_list.clear()
point_sorting(int(input()))
