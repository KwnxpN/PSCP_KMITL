"""KKK"""

def calculator(number):
    """make a calculator"""
    count = 0
    if number == 1:
        print("1")
    else:
        for i in range(1, number+1):
            i = str(i)
            length = len(i)
            count += length
        result = count + number
        print(result)
calculator(int(input()))
