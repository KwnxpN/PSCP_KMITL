"""KKKK"""

def forifball(pattern):
    """forif ggez"""
    cup = 1
    for i in pattern:
        if i == "A":
            if cup == 1:
                cup = 2
            elif cup == 2:
                cup = 1
        elif i == "B":
            if cup == 2:
                cup = 3
            elif cup == 3:
                cup = 2
        elif i == "C":
            if cup == 1:
                cup = 3
            elif cup == 3:
                cup = 1
    print(cup)
forifball(input())
