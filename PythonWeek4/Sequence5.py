"""ssss"""
def sequencev(number):
    """code"""
    space = 0
    for colum in range(number, 0, -1):
        print(colum, end=" ")
        space += 1
        if space == 7:
            print()
            space = 0
sequencev(int(input()))
