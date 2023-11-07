"""KKK"""

def onetime_pass(otp_num):
    """check otp"""
    count, count3 = 0, 0
    while otp_num != "0":
        length = len(otp_num)
        num_list = list(set(list(otp_num)))
        for num in num_list:
            if otp_num.count(num) == 3:
                count3 += 1
            elif otp_num.count(num) == 2:
                count += 1
        if length == 4 and (count == 1):
            print("Valid")
        elif length == 6 and (count == 2 or count3 == 1):
            print("Valid")
        elif length == 8 and (count == 3 or count3 == 2):
            print("Valid")
        else:
            print("Invalid")
        count, count3 = 0, 0
        num_list = []
        otp_num = str(input())
onetime_pass(str(input()))
