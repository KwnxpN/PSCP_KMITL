"""KKK"""

def colors_mix(color_1, color_2):
    """mix the color and tell what color we get"""
    color_dict = {
        ("Blue", "Red") : "Violet",
        ("Blue", "Yellow") : "Green",
        ("Red", "Yellow") : "Orange"
    }
    color_get = tuple(sorted([color_1.strip(), color_2.strip()]))
    res = color_dict.get(color_get)
    if res:
        print(res)
    elif color_1 == color_2 and color_1 in "RedBlueYellow":
        print(color_1)
    else:
        print("Error")
colors_mix(str(input()), str(input()))
