"""KKK"""

def prasomsib(num_group):
    """tf"""
    count = 0
    num_list = []
    for i in range(len(num_group)):
        for j in num_group[i:]:
            num_list.append(int(j))
            if sum(num_list) == 10:
                count += 1
                num_list.clear()
                break
            elif sum(num_list) > 10:
                break
        num_list.clear()
    print(count)
prasomsib(str(input()))
