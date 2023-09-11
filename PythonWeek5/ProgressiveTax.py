"""KKK"""

def protax(price):
    """give me your tax primate"""
    if 0 <= price <= 150000:
        tax = 0
    elif 150000 < price <= 300000:
        diff = price - 150000
        price -= diff
        tax = diff * 0.05
    elif 300000 < price <= 500000:
        diff = price - 300000
        price -= diff
        tax = diff * 0.1
    elif 500000 < price <= 750000:
        diff = price - 500000
        price -= diff
        tax = diff * 0.15
    elif 750000 < price <= 1000000:
        diff = price - 750000
        price -= diff
        tax = diff * 0.2
    elif 1000000 < price <= 2000000:
        diff = price - 1000000
        price -= diff
        tax = diff * 0.25
    elif 2000000 < price <= 4000000:
        diff = price - 2000000
        price -= diff
        tax = diff * 0.3
    elif price > 4000000:
        diff = price - 4000000
        price -= diff
        tax = diff * 0.35
    else:
        tax = 0
    return tax, price

def caltax(price):
    """calculate"""
    tax = 0
    while price > 150000:
        sum_tax, price = protax(price)
        tax += sum_tax
    return int(tax)

print(caltax(float(input())))
