"""KKKK"""

def main():
    """aaaa"""
    time = float(input())
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    day = int(day)
    hour = int(hour)
    minutes = int(minutes)
    seconds = int(seconds)
    if day > 9999:
        print("ERR_:__:__:__")
    elif day <= 9999:
        print("%04d:%02d:%02d:%02d" % (day, hour, minutes, seconds))
main()
