"""KKK"""
import math
def heron(aaa, bbb, ccc):
    """find area of triangle"""
    sss = (aaa + bbb + ccc) / 2
    area = math.sqrt(sss*(sss-aaa)*(sss-bbb)*(sss-ccc))
    print("%.3f"%area)
heron(float(input()), float(input()), float(input()))
