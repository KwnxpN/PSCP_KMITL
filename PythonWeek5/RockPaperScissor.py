"""KKK"""

def find_winner(choice_a, choice_b):
    """find the winner each round"""
    if choice_a == choice_b:
        return "Draw"
    elif (choice_a == 'R' and choice_b == 'S') or (choice_a == 'P' and choice_b == 'R')\
    or (choice_a == 'S' and choice_b == 'P'):
        return "A"
    else:
        return "B"

def calculate(rps_choice):
    """calculate the score"""
    a_score = 0
    b_score = 0
    for i in range(0, len(rps_choice)-1, 2):
        a_choice = rps_choice[i]
        b_choice = rps_choice[i+1]
        winner = find_winner(a_choice, b_choice)
        if winner == "A":
            a_score += 1
        elif winner == "B":
            b_score += 1
    if a_score > b_score:
        print("A win {0}-{1}".format(a_score, b_score))
    elif b_score > a_score:
        print("B win {1}-{0}".format(a_score, b_score))
    else:
        print("DRAW {0}".format(a_score))
calculate(input())
