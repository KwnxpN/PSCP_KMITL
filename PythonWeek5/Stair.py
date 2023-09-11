"""KKKK"""

def stair(person_steps, stair_steps):
    """he want to walk to upstairs"""
    base_stair_height = int(input())
    count = 0
    for _ in range(stair_steps-1):
        stair_height = int(input())
        if (base_stair_height + stair_height) > person_steps:
            base_stair_height = stair_height
            count += 1
        elif (base_stair_height + stair_height) == person_steps:
            base_stair_height = 0
            count += 1
        else:
            base_stair_height += stair_height
    print(count)
stair(int(input()), int(input()))
"""
    if base_stair_height > person_steps:
        print("NO")
    elif base_stair_height <= person_steps:
"""