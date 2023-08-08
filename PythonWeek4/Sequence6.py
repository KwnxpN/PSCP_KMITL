"""KKKK"""

def sequencevi(num):
    """docstr"""
    start = 1
    for col in range(num):
        for row in range(start, col+2):
            print(row, end=" ")
        print()
sequencevi(int(input()))
