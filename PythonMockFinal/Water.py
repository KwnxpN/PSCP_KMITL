"""water"""

def water(month, price, limit, limit_change, no_need_pay):
    """check the water bill"""
    that_month, total = 0, 0
    for _ in range(month):
        water_used = float(input())
        if water_used > limit:
            that_month += price * (water_used - (water_used - limit))
            that_month += limit_change * (water_used - limit)
        else:
            that_month += price * water_used
        if that_month <= no_need_pay:
            that_month = 0
        total += that_month
        that_month = 0
    print("%.2f"%total)
water(int(input()), float(input()), float(input()), float(input()), float(input()))
