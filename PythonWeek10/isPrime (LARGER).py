"""KKK"""

def isprime_larger(num):
    """lmao"""
    if num <= 1:
        print("False")
    elif num <= 1000000:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0 or num%(i + 2) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        for i in range(5, int(num**0.5)+1, 6):
            if num%i == 0 or num%(i + 2) == 0:
                print("False")
                break
        else:
            print("True")
isprime_larger(int(input()))
