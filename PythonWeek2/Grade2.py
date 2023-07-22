"""KKKK"""

def grade2():
    """lll"""

    score = float(input())
    if score <= 100 and score >= 95:
        print("A")
    elif score <= 95 and score >= 90:
        print("B+")
    elif score <= 90 and score >= 85:
        print("B")
    elif score <= 85 and score >= 80:
        print("C+")
    elif score <= 80 and score >= 75:
        print("C")
    elif score <= 75 and score >= 70:
        print("D+")
    elif score <= 70 and score >= 65:
        print("D")
    elif score <= 65 and score >= 60:
        print("F+")
    elif score <= 60 and score >= 0:
        print("F")
    else:
        print("ERR")
grade2()
