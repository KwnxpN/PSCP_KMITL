"""KKKK"""

def count_chickens_in_range(num_chickens):
    """llll"""
    if num_chickens == 0:
        return 0

    weight = int(input())
    count = count_chickens_in_range(num_chickens - 1)

    if 50 <= weight <= 70:
        count += 1

    return count

def main():
    """lll"""
    chick_num = 24
    total_count = count_chickens_in_range(chick_num)
    print(total_count)
main()
