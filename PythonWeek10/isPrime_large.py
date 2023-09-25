"""KKK"""

def isprime_large(num):
    """lmao"""
    if num == 1:
        print("NO")
    elif num > 0:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
isprime_large(int(input()))
