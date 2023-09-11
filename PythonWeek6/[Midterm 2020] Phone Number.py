"""phone number"""

def phonenumber(phonenum, phonetype):
    """convert phone number"""
    phonenum = str(phonenum)
    numberlen = len(phonenum)
    if numberlen == 9:
        zero = phonenum[0]
        middle = phonenum[1:5]
        last = phonenum[5:10]
        if phonetype == "Domestic":
            print(zero, middle, last)
        elif phonetype == "International":
            print("+66", middle, last)
    elif numberlen == 10:
        zero = phonenum[0]
        first = phonenum[1]
        middle = phonenum[2:6]
        last = phonenum[6:11]
        if phonetype == "Domestic":
            print(zero+first, middle, last)
        elif phonetype == "International":
            print("+66"+first, middle, last)
phonenumber(input(), input())
