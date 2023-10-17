"""KKK"""

def scalematrix(rows, colu):
    """normalize the number between 0-1 and put them into matrix"""
    num_list, matrix, inside = [], [], []
    max_num, min_num = 0, 0
    num_list = [[float(input()) for _ in range(colu)] for _ in range(rows)]
    for num in num_list:
        max_num = max(max_num, max(num))
        min_num = min(min_num, min(num))
    for i in range(rows):
        for j in range(colu):
            scale = (num_list[i][j] - max_num) / (max_num - min_num) + 1
            inside.append("%.2f" %scale)
        matrix.append(inside)
        inside = []
    for things in matrix:
        for num in things:
            print(num, end=" ")
        print()
scalematrix(int(input()), int(input()))
