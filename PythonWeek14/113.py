"""KKK"""

def oneonethree(num):
    """I don't like 113"""
    while "113" in num:
        num = num.replace("113", "")
    print(num)
oneonethree(str(input()))
