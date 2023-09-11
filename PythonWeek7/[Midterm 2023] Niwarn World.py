"""KKK"""
import math
def niwarnworld(nnn, sss, kkk):
    """https://open.spotify.com/track/3vfwUrq22haMmIJyyyI7Hq?si=cac30ce7b1774630"""

    xxx_nnn = 2 +((math.log2(nnn**2)) / ((2*nnn)*(math.log2(nnn))))
    xxx_kkk = 2 +((math.log2(kkk**2)) / ((2*kkk)*(math.log2(kkk))))
    yyy_nnn_sss = ((math.sin(math.radians(30))) + (math.sqrt(2*sss))) / (xxx_nnn + 3)
    yyy_kkk = ((math.sin(math.radians(30))) + (math.sqrt(2*kkk))) / (xxx_kkk + 3)
    zzz_kkk = (yyy_kkk**2) + ((8456 * (xxx_kkk**4)) / (24*kkk))

    print("X: {}, Y: {}, Z: {}".format("%.1f"%xxx_nnn, "%.1f"%yyy_nnn_sss, "%.1f"%zzz_kkk))
niwarnworld(float(input()), float(input()), float(input()))
