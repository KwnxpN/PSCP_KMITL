"""KKKK"""

def ping(line_1, line_2, line_3):
    """ping"""
    received = 0
    lost = 0
    for i in range(4):
        reply = input()
        if reply != "General failure." or reply != "Request timed out.":
            received += 1
        else:
            lost += 1
ping(input(), input(), input())
