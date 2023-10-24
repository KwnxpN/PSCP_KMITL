"""PH"""

def ph_checker(liqiud):
    """check the liquid that is acidic or akaline or neutral"""
    if liqiud < 0 or liqiud > 14:
        print("error")
    elif liqiud < 7:
        print("acidic")
    elif liqiud == 7:
        print("neutral")
    else:
        print("akaline")
ph_checker(float(input()))
