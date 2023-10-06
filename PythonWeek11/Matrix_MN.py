"""KKK"""

def make_matrix(rows, colu):
    """get a lot of numbers then make it into matrix"""
    res, inside = [], []
    for _ in range(rows):
        for _ in range(colu):
            inside.append(int(input()))
        res.append(inside)
        inside = []
    for things in res:
        for num in things:
            print(num, end=" ")
        print()
make_matrix(int(input()), int(input()))
