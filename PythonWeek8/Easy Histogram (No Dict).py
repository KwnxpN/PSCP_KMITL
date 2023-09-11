"""KKK"""

def easyhistogram_withrestrict(word):
    """count amount of each character and print them all"""

    mylist, amount_list, pair_list, result_list = [], [], [], []
    #sort here
    for alpha in word:
        if alpha != " ":
            mylist.append(alpha)
    mylist.sort(key=lambda v: (v.lower(), v[0].isupper()))
    #get list of alpha amount
    for alpha in mylist:
        count = mylist.count(alpha)
        amount_list.append(count)
    #merch alpha list and amount list
    for i in range(len(mylist)):
        pair_list.append([mylist[i], amount_list[i]])
    for j in pair_list:
        if j not in result_list:
            result_list.append(j)
    #print list into string
    for k in range(len(result_list)):
        print(str(result_list[k][0]), "=", str(result_list[k][1]))

easyhistogram_withrestrict(input())
