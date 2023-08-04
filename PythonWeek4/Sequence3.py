"""KKKK"""

def sequence1(goal):
    """drawing square 1"""
    start = 1
    for _ in range(start, goal+1):
        for row in range(start, goal+1):
            print(row+1, end=" ")
        print()
        start += 1
        goal += 1
sequence1(int(input()))
