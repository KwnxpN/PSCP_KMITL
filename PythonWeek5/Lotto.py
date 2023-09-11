"""KKK"""

def lotto(prize1, prize2back, prize3front, prize3front2, prize3back):
    """lotto"""
    prize3back2, my_lotto = input(), input()
    if len(str(int(prize1))) < 6:
        prize1 = "%06d"%(int(prize1))
        near_prize1 = "%06d"%(int(prize1)-1)
        near_prize1_2 = "%06d"%(int(prize1)+1)
        if near_prize1 == "-00001":
            near_prize1 = "999999"
    else:
        near_prize1 = "%06d"%(int(prize1)-1)
        near_prize1_2 = "%06d"%(int(prize1)+1)
        if near_prize1_2 == "1000000":
            near_prize1_2 = "000000"
    get_prize = 0
    if my_lotto == prize1:
        get_prize += 6000000
    if my_lotto[-2:] == prize2back:
        get_prize += 2000
    if my_lotto[0:3] == prize3front:
        get_prize += 4000
    if my_lotto[0:3] == prize3front2:
        get_prize += 4000
    if my_lotto[-3:] == prize3back:
        get_prize += 4000
    if my_lotto[-3:] == prize3back2:
        get_prize += 4000
    if my_lotto == near_prize1:
        get_prize += 100000
    if my_lotto == near_prize1_2:
        get_prize += 100000
    print(get_prize)
lotto(input(), input(), input(), input(), input())
