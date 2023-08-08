"""KKKK"""

def align(width, placement, text):
    """align text"""
    if placement == "left":
        print(text.ljust(width))
    elif placement == "right":
        print(text.rjust(width))
    elif placement == "center" and len(text)%2 != 0:
        print(" "+text.center(width-1))
    elif placement == "center":
        print(text.center(width))
align(int(input()), input(), input())
