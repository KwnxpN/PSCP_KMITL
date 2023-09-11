"""KKK"""

def bonus(salary, years, month):
    """https://open.spotify.com/track/1uJbdRLz38VTAXxhyXRC85?si=df12d2aba3204b54"""

    if month >= 10:
        years += 1
    if years > 20:
        years = 20
    bonus_get = salary*years
    if bonus_get > 1000000:
        bonus_get = 1000000
    elif bonus_get < 5000:
        bonus_get = 5000
    print(bonus_get)
bonus(int(input()), int(input()), int(input()))
