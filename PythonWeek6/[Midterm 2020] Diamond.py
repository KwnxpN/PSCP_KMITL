"""KKKK"""

def diamond(size):
    """why tf there is sequence again????"""
    length = size // 2 * -1
    for i in range(length, (size // 2) + 1):
        for j in range(length, (size // 2) + 1):
            if i == 0:
                print("*", end="")
            elif size // 2 in (abs(i + j), abs(i - j)):
                print("*", end="")
            else:
                print(" ", end="")
        print()
diamond(int(input()))
