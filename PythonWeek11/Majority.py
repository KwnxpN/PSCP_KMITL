"""KKK"""

def majority(priminister, amount):
    "I'm the king of this jungle!"
    score_list, total_list = [], []
    for _ in range(amount):
        score_list.append(int(input()))
    for i in range(1, priminister+1):
        total = score_list.count(i)
        total_list.append(total)
        winner_score = max(total_list)
        winner = total_list.index(max(total_list))+1
    if winner_score > amount/2:
        print(winner, winner_score)
    else:
        print(0, winner_score)
majority(int(input()), int(input()))
