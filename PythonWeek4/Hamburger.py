"""HamBAGA"""

def hamburger():
    """make hamBAGA"""
    num1 = int(input())
    num2 = int(input())
    hbg = (num1*2) + (num2*2)
    print("{0}{1}{2}".format("|"*num1, "*"*hbg, "|"*num2))
hamburger()
