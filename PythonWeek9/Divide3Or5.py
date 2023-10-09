"""KKK"""

def divide3or5(num):
    """เท่ ขอทำบ้าง"""
    return sum(filter(lambda x: x%3 == 0 or x%5 == 0, range(1, num+1)))
print(divide3or5(int(input())))
