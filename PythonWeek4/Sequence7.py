"""KKKK"""

def sequencevii(num):
    """docstr"""
    start = 1
    for col in range(num):
        for row in range(start, col+2):
            print(row, end=" ")
        print()
    for col in range(num-1):
        for row in range(start, num-col):
            print(row, end=" ")
        print()
sequencevii(int(input()))
