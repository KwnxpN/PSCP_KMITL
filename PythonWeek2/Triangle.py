"""l"""

def triangle():
    """k"""
    anum = float(input())
    bnum = float(input())
    cnum = float(input())
    diff1 = (((anum**2) + (bnum**2)) - (cnum**2))
    diff2 = (((bnum**2) + (cnum**2)) - (anum**2))
    diff3 = (((cnum**2) + (anum**2)) - (bnum**2))
    if diff1 <= 0.01 and diff1 >= -0.01 or diff2 <= 0.01 and diff2 >= -0.01 or  diff3 <= 0.01 \
        and diff3 >= -0.01:
        print("Yes")
    else:
        print("No")
triangle()
