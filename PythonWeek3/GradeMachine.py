"""KKKK"""
def counter(start, goal):
    """count the number"""
    result = "pass : "
    total_sum = 0
    if start <= goal:
        for i in range(start, goal+1):
            if i%2 == 0:
                result += str(i) + " "
                total_sum += i
    else:
        for i in range(start, goal-1, -1):
            if i%2 == 0:
                result += str(i) + " "
                total_sum += i
    result += "\nSum : " + str(total_sum)
    print(result)
counter(int(input()), int(input()))
