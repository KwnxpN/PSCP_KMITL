"""KKK"""

def hed_n_lek(heads, legs):
    """count heads and legs then count rabbit and bird amount"""
    rabbits, smth = divmod(legs - 2*heads, 2)
    birds = heads - rabbits
    if rabbits >= 0 and birds >= 0 and smth == 0:
        print(rabbits, birds)
    else:
        print("Impossible")
hed_n_lek(int(input()), int(input()))
