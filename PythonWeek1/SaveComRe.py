"""KKKK"""
def main():
    """LLLL"""
    start_here = 492137954293754252786
    milli = start_here
    sec = milli//1000
    milli %= 1000
    minutes = sec//60
    sec %= 60
    hours = minutes//60
    minutes %= 60
    days = hours//24
    hours %= 24
    print(days, hours, minutes, sec, milli)
main()
