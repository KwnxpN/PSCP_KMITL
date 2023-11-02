"""KKK"""
from json import loads

def find_longest(lst):
    """find long list"""
    return max(lst, key=len)

def find_shortest(lst):
    """find short list"""
    return min(lst, key=len)

def difference(list_a, list_b):
    """find the difference of 2 lists"""
    res_list, res_dict = [], {}
    group = [list_a, list_b]
    if len(list_a) != len(list_b):
        long_list = find_longest(group)
        short_list = find_shortest(group)
    else:
        long_list, short_list = list_a, list_b
    for things in long_list[:]:
        if things in short_list:
            short_list.remove(things)
            long_list.remove(things)
    if long_list == [] and short_list == []:
        print("ONAJI DAYO!")
    else:
        for i in long_list:
            res_list.append(i)
        for j in short_list:
            res_list.append(j)
        res_list = sorted(res_list)
        for things in res_list:
            if things not in res_dict:
                res_dict.update({things: 1})
            else:
                res_dict[things] += 1
        for key, val in res_dict.items():
            print(key, val)
difference(loads(str(input())), loads(str(input())))
