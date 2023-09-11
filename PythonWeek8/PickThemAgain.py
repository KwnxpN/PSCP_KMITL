"""KKK"""

def pickthemagain(number_group):
    """pick them but input are str and
    mod 3 and 5 and reverse"""

    my_number_list = number_group.split()
    my_number_list.reverse()
    result_list = []
    for num in my_number_list:
        if int(num)%3 == 0 or int(num)%5 == 0:
            result_list.append(num)
    if result_list == []:
        print("Nope")
    for num in result_list:
        print(num)
pickthemagain(str(input()))
