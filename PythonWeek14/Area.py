"""KKK"""

def area_i_got(rows_amount):
    """count the area that not whitespace"""
    total = 0
    for _ in range(rows_amount):
        block = str(input()).replace(" ", "")
        total += len(block)
    print(total)
area_i_got(int(input()))
