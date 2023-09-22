"""KKK"""

def day2011(day, month):
    """bylad"""
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    res = sum(month_list[:month-1]) + day
    print(days_list[(res - 3)%7])
day2011(int(input()), int(input()))
