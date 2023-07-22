"""KKK"""

def quadrant():
    """lll"""

    xxx = float(input())
    yyy = float(input())

    if xxx >= 1 and yyy >= 1:
        print("Q1")
    elif xxx < 1 and xxx != 0 and yyy >= 1:
        print("Q2")
    elif xxx < 1 and xxx != 0 and yyy < 1 and yyy != 0:
        print("Q3")
    elif xxx >= 1 and yyy < 1 and yyy != 0:
        print("Q4")
    elif xxx != 0 and yyy == 0:
        print("X")
    elif xxx == 0 and yyy != 0:
        print("Y")
    elif xxx == 0 and yyy == 0:
        print("O")
quadrant()
