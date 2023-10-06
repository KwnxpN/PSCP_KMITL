"""KKK"""

def ipad_air(color, ram, network):
    """iPad air from china Ching Chong"""
    color_list = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    dict_64 = {"Wi-Fi": 19900, "Wi-Fi + Cellular": 24400}
    dict_256 = {"Wi-Fi": 24900, "Wi-Fi + Cellular": 29400}
    if color not in color_list or (ram != 64 and ram != 256)\
        or (network != "Wi-Fi" and network != "Wi-Fi + Cellular"):
        print("Not Available")
    elif ram == 64:
        print(dict_64.get(network))
    elif ram == 256:
        print(dict_256.get(network))
ipad_air(str(input()), int(input()), str(input()))
