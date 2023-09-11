"""KKK"""

def median(number_amount):
    """find middle value from group of number
    (with no math)"""

    mylist = []
    for _ in range(number_amount):
        mylist.append(int(input()))
    mylist.sort()
    if number_amount%2 != 0:
        print("%.1f"%mylist[int(number_amount/2)])
    else:
        val1 = int(number_amount/2)-1
        val2 = int(number_amount/2)
        result = (mylist[val1] + mylist[val2])/2
        print("%.1f"%result)
median(int(input()))
