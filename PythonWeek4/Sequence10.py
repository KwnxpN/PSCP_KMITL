"""kkKK"""

def main(val):
    """seq10"""
    for i in range(1, val+1):
        for _ in range(val-i):
            print("  ", end=' ')
        for j in range(i):
            print("%02d"% (j+1), end=' ')
        for j in range(i-1, 0, -1):
            print("%02d"% j, end=' ')
        print()
    for i in range(1, val):
        for _ in range(i):
            print("  ", end=' ')
        for j in range(1, val-(i-1)):
            print("%02d"% (j), end=' ')
        for j in range(val-i, 1, -1):
            print("%02d"%(j-1), end=' ')
        print()
main(int(input()))
