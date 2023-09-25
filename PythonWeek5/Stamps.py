"""KKK"""

def stamper(that_money, every_that_money, get_stamp, stamp):
    """get stamp mark"""
    stamp += (that_money // every_that_money) * get_stamp
    return stamp

def discounter(payment, that_stamp, every_stamp, discount_by):
    """discount"""
    discounted = 0
    if that_stamp > 0:
        while discounted < payment and that_stamp >= every_stamp:
            discounted += discount_by
            that_stamp -= every_stamp
    return discounted, that_stamp

def calculator():
    """Calculate"""
    dine_in_times = int(input())
    every_that_money = int(input())
    get_stamp = int(input())
    every_stamp = int(input())
    discount_by = int(input())
    sum_pay = 0
    stamp = 0
    for _ in range(dine_in_times):
        payment = int(input())
        discounted, stamp = discounter(payment, stamp, every_stamp, discount_by)
        if payment - discounted >= 0:
            payment = payment - discounted
        else:
            payment = 0
        stamp = stamper(payment, every_that_money, get_stamp, stamp)
        sum_pay += payment
    print(sum_pay)
    print(stamp)
calculator()
