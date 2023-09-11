"""KKK"""

def tuple_sad_life(get_tuple, val_tuple):
    """I'm not even understand what the question said
    but I'll pretend like I'm understand"""

    mytuple = tuple(get_tuple.split())
    position = mytuple.index(val_tuple)
    amount = mytuple.count(val_tuple)
    for _ in range(amount):
        for _ in range(amount):
            print(position, end=' ')
        print()
tuple_sad_life(input(), input())
