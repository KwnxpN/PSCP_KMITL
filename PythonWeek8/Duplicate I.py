"""KKK"""

def duplicate(first_group, second_group):
    """I want to sleep so bad"""

    first_g_id, second_g_id = set(), set()
    for _ in range(first_group):
        first_g_id.add(input())
    for _ in range(second_group):
        second_g_id.add(input())
    result = sorted(first_g_id.intersection(second_g_id), reverse=True)
    if result == []:
        print("Nope")
    for i in result:
        print(i)
duplicate(int(input()), int(input()))
