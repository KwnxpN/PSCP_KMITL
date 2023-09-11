"""KKK"""

def missingcard():
    """oh I get it now"""
    cards = [str(i) for i in range(2, 11, 1)] + list("JQKA")
    rank = "SHDC"
    all_cards = set([i+j for i in cards for j in rank])
    get_card = set()
    for _ in range(51):
        get_card.add(input())
    result = all_cards.difference(get_card)
    print(result.pop())
missingcard()
