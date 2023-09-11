"""KKKK"""

def blackjack(card_amount):
    """blackjack at las vegas with black label whiskey
    belong with black person playing blackjack"""
    total = 0
    card_a = 0
    for _ in range(card_amount):
        card_number = input()
        if card_number == "A":
            card_a += 11
        elif card_number.isalpha():
            total += 10
        else:
            total += int(card_number)
    sum_score = total + card_a
    while sum_score > 21 and card_a != 0:
        card_a -= 10
        sum_score = total + card_a
    print(sum_score)
blackjack(int(input()))

