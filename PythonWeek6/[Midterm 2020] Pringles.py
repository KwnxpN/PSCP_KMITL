"""KKKK"""
def pringles(top_box, chips, below_box, hand_length):
    """wtf"""
    res = ""
    count = 0
    for i in chips[:hand_length]:
        if i == ")":
            res += " "
            count += 1
        else:
            res += " "
    res = res+chips[hand_length:]
    print(count)
    if res.count(")") > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(top_box, res, below_box, sep="\n")
pringles(input(), input(), input(), int(input()))
