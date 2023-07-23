"""KKKK"""

def distance(xx1, yy1, xx2, yy2):
    """lll"""
    return ((xx2 - xx1) ** 2 + (yy2 - yy1) ** 2) ** 0.5

def circles_overlap(circle1_x, circle1_y, circle2_x, circle2_y):
    """lll"""
    dist_centers = distance(circle1_x, circle1_y, circle2_x, circle2_y)
    return dist_centers
def rad_circle(circle1_radius, circle2_radius):
    """lll"""
    sum_radii = circle1_radius + circle2_radius
    return sum_radii

def total():
    """lll"""
    circle1_x, circle1_y, circle1_radius = float(input()), float(input()), float(input())
    circle2_x, circle2_y, circle2_radius = float(input()), float(input()), float(input())

    overlap = circles_overlap(circle1_x, circle1_y, circle2_x, circle2_y)
    radi_dis = rad_circle(circle1_radius, circle2_radius)
    if overlap < radi_dis:
        print("Yes")
    else:
        print("No")
total()
