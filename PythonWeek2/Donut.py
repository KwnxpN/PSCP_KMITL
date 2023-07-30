"""KKK"""

def donut():
    """sell donut"""
    price = int(input())
    piece = int(input())
    bonus = int(input())
    needed = int(input())
    box = piece + bonus
    price_per_box = price*piece
    get_box = needed//box
    remain = needed - (get_box*box)
    if remain >= piece:
        get_box += 1
        remain = 0
    price_result = get_box*price_per_box + remain*price
    piece_result = get_box*box + remain
    print(price_result, piece_result)
donut()
