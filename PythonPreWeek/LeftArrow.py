"""KKKK"""

def main():
    """eiei"""
    num1 = int(input())
    num2 = int(input())
    num3 = num2 // 2
    while num3 != -1:
        print(" " * num3 + "*" * num1)
        num3 -= 1

    num3 = 1
    num4 = (num2 // 2)
    for _ in range(0, num4):
        print(" " * num3 + "*" * num1)
        num3 += 1

main()
