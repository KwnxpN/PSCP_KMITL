"""KKK"""

def lamer_ruk_ter_jing_jing(shark):
    """who create this"""
    zone_dict = {
        "THE SHALLOW ZONE": ["BULL SHARK"],
        "THE TWILIGHT ZONE": ["CHAIN CATSHARK", "GREAT WHITE SHARK", "GUMMY SHARK", "BLUE SHARK", \
                              "MAKO SHARK"],
        "THE MIDNIGHT ZONE": ["FRILLED SHARK", "GOBLIN SHARK", "SIXGILL SHARK", "GREENLAND SHARK", \
                              "COOKIECUTTER SHARK"],
        "THE ABYSSAL ZONE" : ["MEGAMOUTH SHARK"]
    }
    if "SHARK" not in shark:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
    else:
        for zone in zone_dict:
            for sharktype in zone_dict.get(zone):
                if sharktype == shark:
                    print(zone)
                    break
lamer_ruk_ter_jing_jing(str(input()))
