"""KKK"""

def calculatorv2(num):
    """blyad"""
    if num != 1:
        num_digit = len(str(num))
        count = 0
        digit_now = 1
        lek_gao = 0
        multi_oper = 2
        while len(str(digit_now)) < num_digit:
            count += multi_oper * (digit_now * 9)
            lek_gao += digit_now * 9
            digit_now = digit_now * 10
            multi_oper += 1
        count += multi_oper * (num - lek_gao)
        print(count)
    else:
        print(1)
calculatorv2(int(input()))
