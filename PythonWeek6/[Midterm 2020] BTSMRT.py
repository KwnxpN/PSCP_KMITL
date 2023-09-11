"""btsmrt"""

def btsandmrt(days, age, height):
    """check if child or old can get free ticket"""
    if days == "Children Day" and age < 14 and height <= 140:
        print("FREE")
    elif days == "Senior Day" and age >= 60:
        print("FREE")
    elif age < 14 and height < 90:
        print("FREE")
    else:
        print("PAY")
btsandmrt(input(), float(input()), float(input()))
