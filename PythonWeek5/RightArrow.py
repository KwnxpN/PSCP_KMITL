"""KKKK"""

def rightarrow(width, height):
    """make right arrow"""
    for i in range((height//2) + 1):
        for _ in range(i):
            print(" ", end='')
        for _ in range(width):
            print("*", end='')
        print()
    for i in range(height//2):
        for _ in range((height//2) - (i+1)):
            print(" ", end='')
        for _ in range(width):
            print("*", end='')
        print()
rightarrow(int(input()), int(input()))
