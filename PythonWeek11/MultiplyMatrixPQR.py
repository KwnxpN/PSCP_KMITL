"""KKK"""

def matrixpqr(first_rows, same, second_colu):
    """mutiply matrix"""
    first_matrix, second_matrix = [], []
    first_inside, second_inside = [], []
    lol = []
    first_matrix = [[int(input()) for _ in range(same)] for _ in range(first_rows)]
    second_matrix = [[int(input()) for _ in range(second_colu)] for _ in range(same)]
    print(first_matrix)
    print(second_matrix)
    
matrixpqr(int(input()), int(input()), int(input()))
