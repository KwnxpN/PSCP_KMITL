"""KKK"""

def temperature(tempe, unit, con_unit):
    """convert tempe"""
    mydict = {
        "CF": tempe * (9/5) + 32,
        "CK": tempe + 273.15,
        "CR": (tempe + 273.15) * (9/5),
        "FC": (tempe - 32) / (9/5),
        "FK": (tempe + 459.67) * (5/9),
        "FR": (tempe - 32) + 491.67,
        "KC": tempe - 273.15,
        "KF": (tempe - 273.15) * 1.80 + 32,
        "KR": (tempe - 273.15) * (9/5) + 491.67,
        "RC": (tempe - 491.67) * (5/9),
        "RF": tempe - 459.67,
        "RK": tempe * (5/9)
    }
    if unit == con_unit:
        print("{:.2f}".format(tempe))
    else:
        res = mydict.get(unit + con_unit)
        print("{:.2f}".format(res))
temperature(float(input()), str(input()), str(input()))
