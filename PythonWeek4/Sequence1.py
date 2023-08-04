"""KKKK"""

def sequence1(goal):
    """drawing square 1"""
    for _ in range(goal):
        for rows in range(goal):
            print(rows+1, end=" ")
        print()
sequence1(int(input()))
