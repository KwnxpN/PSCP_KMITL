"""KKKK"""

def main():
    """llll"""

    time_sec = float(input())
    days = time_sec // (24 * 3600)
    time_sec = time_sec % (24 * 3600)
    hours = time_sec // 3600
    time_sec %= 3600
    minutes = time_sec // 60
    time_sec %= 60
    seconds = time_sec
    days = int(days)
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    print(days, hours, minutes, seconds)
main()
