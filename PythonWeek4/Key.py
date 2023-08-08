"""KKK"""

def sum_of_id(num):
    """cal sum digit from citizen ID num"""
    sum_id = 0
    for digit in str(num):
        sum_id += int(digit)
    return sum_id

def key(id_13_digits):
    """cal to find keynum"""
    digit_result = sum_of_id(id_13_digits)
    last3digits = (id_13_digits%1000)*10
    result = (digit_result + last3digits)
    if result >= 1000:
        result = str(result)[-4:]
        print(result)
    else:
        print(result+1000)
key(int(input()))
