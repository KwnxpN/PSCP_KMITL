"""KKK"""

def fourdirect(command):
    """dude stop I hate this"""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    for i in command:
        if i == "U":
            line1 += "  *   "
            line2 += " ***  "
            line3 += "* * * "
            line4 += "  *   "
            line5 += "  *   "
        elif i == "D":
            line1 += "  *   "
            line2 += "  *   "
            line3 += "* * * "
            line4 += " ***  "
            line5 += "  *   "
        elif i == "R":
            line1 += "  *   "
            line2 += "   *  "
            line3 += "***** "
            line4 += "   *  "
            line5 += "  *   "
        elif i == "L":
            line1 += "  *   "
            line2 += " *    "
            line3 += "***** "
            line4 += " *    "
            line5 += "  *   "
    print(line1, line2, line3, line4, line5, sep='\n')
fourdirect(input())
