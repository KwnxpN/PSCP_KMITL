"""KKK"""

def catparade():
    """meow meow bark wtf no bark here"""
    origi_list, result_list = [], []
    while True:
        species = input()
        if species == "END":
            break
        elif species == "IT'S A DOG":
            origi_list.pop(-1)
        else:
            origi_list.extend(species.split(", "))
    non_iterate_list = list(set(origi_list))
    for cat in non_iterate_list:
        pos = origi_list.index(cat)+1
        amount = origi_list.count(cat)
        result_list.append([cat, pos, amount])
    result_list.sort()
    for cat_sum in result_list:
        for i in cat_sum:
            print(i, end=' ')
        print()
catparade()
