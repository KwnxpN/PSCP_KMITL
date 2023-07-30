"""brickbridge"""

def brickbridge():
    """หาจำนวนอิฐ"""
    small_brick, big_brick, goal = int(input()), int(input()), int(input())
    big_need = min(big_brick, goal // 5)
    remain_length = goal - big_need * 5
    small_need = remain_length if remain_length <= small_brick else -1
    if small_need == -1:
        print(-1)
    else:
        print(small_need)
brickbridge()
