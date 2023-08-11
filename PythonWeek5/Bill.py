"""KKK"""

def bill(price):
    """price + service charge + VAT"""
    service = price*0.10
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    price += service
    vat = price*0.07
    price += vat
    print("%.2f" % price)
bill(int(input()))
