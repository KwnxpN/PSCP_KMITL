"""Restaurant"""

def calcu(before_order, after_order, discount, promotion):
    """Discount everything"""
    bf_discount, af_discount = 0, 0
    if before_order >= promotion:
        bf_discount = before_order - (before_order * discount)
    if after_order >= promotion:
        af_discount = after_order - (after_order * discount)
    return bf_discount, af_discount

def restaurant_trick(price, promotion, discount, offer):
    """Trick of the trade"""
    if price != promotion:
        pay_price = price + offer
        if pay_price >= promotion:
            get_discount = pay_price * (discount / 100)
        else:
            get_discount = 0
        if get_discount > offer:
            text = "Yes {:.3f}".format(get_discount - offer)
        elif get_discount < offer:
            text = "No {:.3f}".format(offer - get_discount)
        else:
            text = "Yes"
    else:
        discount = discount / 100
        before_order = price
        after_order = price + offer
        bf_discount, af_discount = calcu(before_order, after_order, discount, promotion)
        if bf_discount < af_discount:
            text = "No {:.3f}".format(af_discount - bf_discount)
        elif bf_discount > af_discount:
            text = "Yes {:.3f}".format(bf_discount - af_discount)
        else:
            text = "Yes"
    return text

print(restaurant_trick(float(input()), float(input()), float(input()), float(input())))
