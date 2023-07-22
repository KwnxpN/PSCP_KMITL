"""KKKK"""
 
def day():
    """lll"""
    yrs = int(input())
    if yrs % 400 == 0 and yrs % 100 == 0:
        print("Yes")
    elif yrs % 4 == 0 and yrs % 100 != 0:
        print("Yes")
    else:
        print("No")
day()