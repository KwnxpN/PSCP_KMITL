"""century"""
import math
def century(times):
    """calculate century"""
    for _ in range(times):
        years = input()
        years_get = ""
        years_type = ""
        for i in years:
            if i.isalpha():
                years_type = years_type + i
            if i.isdigit():
                years_get = years_get + i
        years_get = int(years_get)
        if years_type == "BE":
            if years_get < 544:
                print("ERROR")
            else:
                years_get -= 543
                result = math.ceil(years_get*0.01)
                print(result)
        elif years_type == "AD":
            result = math.ceil(years_get*0.01)
            print(result)
        else:
            print("ERROR")
century(int(input()))
