"""KKKK"""

def sequence1(goal):
    """drawing square 1"""
    start = 0
    for _ in range(goal):
        for row in range(start, goal):
            print(row+1, end=" ")
        print()
sequence1(int(input()))
