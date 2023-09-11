"""squid game tug of war"""

def squidgame():
    """tug of war"""
    power_a = 0
    power_b = 0
    for _ in range(0, 10):
        person_power_a = int(input())
        power_a += person_power_a
    for _ in range(0, 10):
        person_power_b = int(input())
        power_b += person_power_b
    if power_a > power_b:
        print("B")
    elif power_a == power_b:
        print("AB")
    else:
        print("A")
squidgame()
