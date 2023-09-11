"""KKKK"""

def seqn(val):
    """seqn"""
    for i in range(val):
        for j in range(val):
            if j == 0 or j == val - 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
seqn(int(input()))
