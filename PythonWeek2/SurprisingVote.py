"""SurpriseVote"""

def suprisela(total, highest):
    """find diff"""
    middle = min(total - highest, highest)
    lowest = total - highest - middle
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
suprisela(float(input()), float(input()))
