"""KKK"""

def inverter(twobits):
    """not gate"""
    newbits = ""
    for num in twobits:
        if num == "1":
            newbits += num.replace("1", "0")
        else:
            newbits += num.replace("0", "1")
    if int(newbits) == 0:
        print(" ")
    else:
        print(int(newbits))
inverter(str(input()))
