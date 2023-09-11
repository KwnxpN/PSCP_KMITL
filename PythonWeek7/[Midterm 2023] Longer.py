"""KKK"""
from math import pi

def longer(rrr, aaa, bbb):
    """https://open.spotify.com/track/42TLIkJ2kFSY0WlCBjqzhB?si=44ee3518aff64f72"""

    circle_circum = 2*pi*rrr
    rectangle_circum = (aaa*2)+(bbb*2)
    circum_diff = abs(circle_circum - rectangle_circum)
    if circle_circum > rectangle_circum:
        print("Circle is longer")
        print("%.5f"%circum_diff)
    elif rectangle_circum > circle_circum:
        print("Rectangle is longer")
        print("%.5f"%circum_diff)
    else:
        print("Equal")
        print("%.5f"%circum_diff)
longer(float(input()), float(input()), float(input()))
