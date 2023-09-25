"""KKK"""

def meteorite(weight, sliced, limit):
    """protect the world"""
    ammo = 0
    meteor = 1
    while weight >= limit:
        ammo += meteor * 1
        shoot = meteor * 1
        weight /= sliced
        meteor = sliced*shoot
    return ammo
print(meteorite(float(input()), int(input()), float(input())))
