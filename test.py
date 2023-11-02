list_a = ["aaa", "bbb"]
list_b = ["bbb", "aaa"]

for i in list_a:
    if i in list_b:
        list_a.remove(i)
        list_b.remove(i)

for j in list_b:
    if j in list_a:
        list_a.remove(j)
        list_b.remove(j)

print(list_a)
print(list_b)




"""KKK"""
from json import loads

def difference(list_a, list_b):
    """find the difference of 2 lists"""
    res_list, res_dict = [], {}
    list_a, list_b = loads(list_a), loads(list_b)
    for i in list_a:
        if i in list_b:
            list_a.remove(i)
            list_b.remove(i)
    for j in list_b:
        if j in list_a:
            list_a.remove(j)
            list_b.remove(j)
    for things in list_a:
        res_list.append(things)
    for things in list_b:
        res_list.append(things)
    res_list.sort()
    if res_list == []:
        print("ONAJI DAYO!")
    else:
        for k in res_list:
            if k not in res_dict:
                res_dict.update({k : 1})
            else:
                res_dict[k] += 1
        for krey, val in res_dict.items():
            print(krey, val)
difference(str(input()), str(input()))