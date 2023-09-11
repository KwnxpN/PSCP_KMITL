"""KKK"""

def missingcard():
    """wtf is this"""
    rank_list = ["S", "H", "D", "C"]
    num_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    all_cards = [num + rank for num in num_list for rank in rank_list]
    for _ in range(51):
        get_cards = input()
        if get_cards in all_cards:
            all_cards.remove(get_cards)
    print(all_cards.pop())
missingcard()
