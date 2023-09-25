"""KKKK"""

def maaxnum(num_1, num_2):
    """max here"""
    return num_1 if num_1 >= num_2 else num_2

def miinnum(num_1, num_2):
    """min here"""
    return num_1 if num_1 <= num_2 else num_2

def soortmaax(keprekars_num):
    """descendant"""
    salted = ""
    for _ in range(len(keprekars_num)):
        biggest = -1
        for num in keprekars_num:
            biggest = maaxnum(biggest, int(num))
        keprekars_num = keprekars_num.replace(str(biggest), "", 1)
        salted += str(biggest)
    return int(salted)

def soortmiin(keprekars_num):
    """ascendant"""
    unsalted = ""
    for _ in range(len(keprekars_num)):
        smallest = 10
        for num in keprekars_num:
            smallest = miinnum(smallest, int(num))
        keprekars_num = keprekars_num.replace(str(smallest), "", 1)
        unsalted += str(smallest)
    return int(unsalted)

def keprekars(keprekars_num):
    """Count how many times you have to use Kaprekars method"""
    the_6174 = 0
    count = 0
    while the_6174 != 6174:
        while len(keprekars_num) < 4:
            keprekars_num += "0"
        salted = soortmaax(keprekars_num)
        unsalted = soortmiin(keprekars_num)
        the_6174 = salted - unsalted
        keprekars_num = str(the_6174)
        count += 1
    print(count)

keprekars(str(input()))
