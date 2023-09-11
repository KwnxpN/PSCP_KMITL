"""KKKK"""

def christmastree(top, body):
    """the top of xmas tree"""
    for i in range(1, top+1):
        for _ in range(top-i):
            print(" ", end='')
        for _ in range(i):
            print("*", end='')
        for _ in range(i-1, 0, -1):
            print("*", end='')
        print()
    #the body of xmas tree
    for _ in range(1, body+1):
        for _ in range(top-2):
            print(" ", end='')
        for _ in range(1):
            print("---", end='')
        print()
christmastree(int(input()), int(input()))
