"""KKKK"""

def virus(virus_body):
    """check if o is lower case count
    if O is upper do nothing"""
    count = 0
    for i in virus_body:
        if (i.islower()) == True:
            count += 1
        else:
            pass
    print(count)
virus(str(input()))
