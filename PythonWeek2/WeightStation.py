"""ช่างน้ำหนักทำไม"""

def find_missing(avg, ww1, ww2, ww3):
    """ลำบากฉันเนี่ย"""
    missing = avg*4 - (ww1 + ww2 + ww3)
    return missing

def weight():
    """เสียทำไมไม่ซ่อมเอง"""
    average, weight1 = float(input()), float(input())
    weight2, weight3 = float(input()), float(input())
    result = find_missing(average, weight1, weight2, weight3)
    if weight1 + weight2 + weight3 + result > 15000:
        print("Overweight")
    elif abs(average - weight1) > average/2 or abs(average - weight2) > average/2\
        or abs(average - weight3) > average/2 or abs(average - result) > average/2:
        print("Unbalance")
    else:
        print("Pass", "%.2f" %result)
weight()
