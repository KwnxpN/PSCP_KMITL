"""KKK"""

def day2011(day, month):
    """blyad suka python"""
    month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30}
    day_dict = {0:"Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday",
                4: "Wednesday", 5: "Thursday", 6: "Friday"}
    res = sum(month_dict.get(i) for i in range(1, month)) + day - 1
    print(day_dict.get(res%7))
day2011(int(input()), int(input()))
