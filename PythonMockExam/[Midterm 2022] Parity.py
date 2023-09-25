"""KKK"""

def parity(bits, choice):
    """add number evn or odd"""
    count = 0
    for number in bits:
        if number == "1":
            count += 1
        else:
            pass
    if choice == "Even":
        if count%2 == 0:
            bits += "0"
        else:
            bits += "1"
    elif choice == "Odd":
        if count%2 == 0:
            bits += "1"
        else:
            bits += "0"
    print(bits)
parity(str(input()), input())
