"""KKK"""
import json
def pickthem(get_list):
    """pickthem"""
    mylist = json.loads(get_list)
    new_list = []
    for num in mylist:
        if num % 2 == 0:
            new_list.append(num)
    if new_list == []:
        print("Nope")
    for num in new_list:    
        print(num)
pickthem(str(input()))
