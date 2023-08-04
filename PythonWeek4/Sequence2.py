"""KKKK"""

def sequence2(goal):
    """docstring"""
    num = 1
    step = 3
    result = ""
    for _ in range(0, goal):
        result += str(num) + " "
        num += step
        step += 2
    print(result)
sequence2(int(input()))
