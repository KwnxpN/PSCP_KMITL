"""KKKK"""

def calculate(price, size):
    """find worthy"""
    return size/price

def ruleofthree(snack):
    """compare snace and find which is worthy"""
    price = float(input())
    quantity = float(input())
    base_worthy = calculate(price, quantity)
    worthy_price = price
    worthy_size = quantity
    for _ in range(snack-1):
        price = float(input())
        quantity = float(input())
        average = calculate(price, quantity)
        if average > base_worthy:
            worthy_price = price
            worthy_size = quantity
            base_worthy = average
        elif average == base_worthy:
            if worthy_price >= price:
                worthy_price = price
                worthy_size = quantity
    print("%.2f"%worthy_price, "%.2f"%worthy_size)
ruleofthree(int(input()))
