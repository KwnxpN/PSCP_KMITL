"""KKK"""

def dataspike():
    """lll"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    num6 = float(input())
    num7 = float(input())
    num8 = float(input())
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5 and num1 >= num6 and\
        num1 >= num7 and num1 >= num8:
        largest_num = num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5 and num2 >= num6 and\
        num2 >= num7 and num2 >= num8:
        largest_num = num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5 and num3 >= num6 and\
        num3 >= num7 and num3 >= num8:
        largest_num = num3
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5 and num4 >= num6 and\
        num4 >= num7 and num4 >= num8:
        largest_num = num4
    elif num5 >= num2 and num5 >= num3 and num5 >= num4 and num5 >= num1 and num5 >= num6 and\
        num5 >= num7 and num5 >= num8:
        largest_num = num5
    elif num6 >= num2 and num6 >= num3 and num6 >= num4 and num6 >= num5 and num6 >= num1 and\
        num6 >= num7 and num6 >= num8:
        largest_num = num6
    elif num7 >= num2 and num7 >= num3 and num7 >= num4 and num7 >= num5 and num7 >= num6 and\
        num7 >= num1 and num7 >= num8:
        largest_num = num7
    elif num8 >= num2 and num8 >= num3 and num8 >= num4 and num8 >= num5 and num8 >= num6 and\
        num8 >= num7 and num8 >= num1:
        largest_num = num8
    print(int(largest_num))
dataspike()
