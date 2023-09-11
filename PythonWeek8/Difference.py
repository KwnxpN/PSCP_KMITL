"""KKK"""

def difference(a_amount, b_amount):
    """I am mathematician"""

    a_set, b_set = set(), set()
    for _ in range(a_amount):
        a_set.add(int(input()))
    for _ in range(b_amount):
        b_set.add(int(input()))
    result = a_set.difference(b_set)
    result = sorted(result)
    for i in result:
        print(i, end=' ')
difference(int(input()), int(input()))
