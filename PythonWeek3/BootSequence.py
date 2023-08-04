"""KKKK"""
def bootseq(goal):
    """count the number"""
    nnn = 1
    while nnn <= goal:
        if nnn == goal:
            print(nnn, end="")
        else:
            print(nnn, end="_")
        nnn += 1
bootseq(int(input()))
