"""KKKK"""
def stepper2(start, goal):
    """count the number"""
    if start <= goal:
        while start <= goal:
            print(start)
            start += 1
    else:
        while start >= goal:
            print(start)
            start -= 1
stepper2(int(input()), int(input()))
