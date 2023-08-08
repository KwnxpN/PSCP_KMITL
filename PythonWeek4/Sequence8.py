"""Sequence VIII"""
def sequence(num):
    """code"""
    space_needed = num - 1
    for _ in range(num):
        start = 1
        space = space_needed
        for _ in range(num):
            if space > 0:
                print("  ", end=" ")
                space -= 1
            else:
                print("%02d"%start, end=" ")
                start += 1
        print()
        space_needed -= 1
sequence(int(input()))
