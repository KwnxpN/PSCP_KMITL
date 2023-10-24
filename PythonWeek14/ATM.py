"""KKK"""

def atm_fak_thon(money):
    """pom kor mee tu ra muean kan"""
    action = input()
    while action != "END":
        action = action.split()
        if action[0] == "W":
            money = max(0, money-int(action[1]))
        else:
            money += int(action[1])
        action = input()
    print(money)
atm_fak_thon(int(input()))
