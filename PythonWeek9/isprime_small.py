"""KKK"""

def isprime_small(num):
    """lmao"""
    if num == 1:
        print("No")
    elif num > 0:
        for i in range(2, int(num/2)+1):
            if num%i == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
isprime_small(int(input()))
