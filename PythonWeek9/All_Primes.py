"""KKK"""

def all_prime(limit):
    """I'm braindead"""
    count = 0
    for num in range(1, limit+1):
        if num > 1:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                count += 1
    print(count)
all_prime(int(input()))
