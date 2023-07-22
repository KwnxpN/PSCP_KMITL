"""KKKK"""

def pointcircle():
    """lll"""
    xxx = float(input())
    yyy = float(input())
    radius = float(input())
    xnpoint = float(input())
    ynpoint = float(input())

    if ((((xxx - xnpoint)**2) + ((yyy - ynpoint)**2)) ** 0.5) <= radius:
        print("True")
    else:
        print("False")
pointcircle()
