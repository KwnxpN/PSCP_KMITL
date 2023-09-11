"""KKK"""

def seccon(sec_get, sec_set, min_set, hours_set):
    """aaaa"""
    minutes = sec_get//sec_set
    second = sec_get%sec_set
    hours = minutes//min_set
    minutes = minutes%min_set
    hours = hours%hours_set
    print("%d:%d:%d"%(hours, minutes, second))
seccon(int(input()), int(input()), int(input()), int(input()))
