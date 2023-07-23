1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
"""Largest Number"""
def largest_num():
    """Find the largest number"""
    print(place_member(int(input()), int(input()), int(input())))
def place_member(num1, num2, num3):
    """Place the number"""
    style1 = "%d%d%d" %(num1, num2, num3)
    style2 = "%d%d%d" %(num1, num3, num2)
    style3 = "%d%d%d" %(num2, num1, num3)
    style4 = "%d%d%d" %(num2, num3, num1)
    style5 = "%d%d%d" %(num3, num2, num1)
    style6 = "%d%d%d" %(num3, num1, num2)
    style1, style2, style3 = int(style1), int(style2), int(style3)
    style4, style5, style6 = int(style4), int(style5), int(style6)
    return compare(compare(compare(style1, style2),\
                           compare(style3, style4)), compare(style5, style6))
def compare(style1, style2):
    """Compare number"""
    if style1 > style2:
        return style1
    return style2
largest_num()