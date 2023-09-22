"""KKK"""

def divide3or5(num):
    """I love P'Tae"""
    summary = 0
    for number in range(1, num+1):
        if number%3 == 0 or number%5 == 0:
            summary += number
    print(summary)
divide3or5(int(input()))
