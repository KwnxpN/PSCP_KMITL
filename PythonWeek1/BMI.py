"""KKKK"""
NAME_1 = str(input())
KG_1 = float(input())
CM_1 = float(input())
NAME_2 = str(input())
KG_2 = float(input())
CM_2 = float(input())
NAME_3 = str(input())
KG_3 = float(input())
CM_3 = float(input())
NAME_4 = str(input())
KG_4 = float(input())
CM_4 = float(input())
NAME_5 = str(input())
KG_5 = float(input())
CM_5 = float(input())

def main():
    """llll"""
    def calbmi_1():
        """aaaa"""
        return KG_1 / ((CM_1* 0.01) **2)
    def calbmi_2():
        """aaaa"""
        return KG_2 / ((CM_2*0.01)**2)
    def calbmi_3():
        """aaaa"""
        return KG_3 / ((CM_3*0.01)**2)
    def calbmi_4():
        """aaaa"""
        return KG_4 / ((CM_4*0.01)**2)
    def calbmi_5():
        """aaaa"""
        return KG_5 / ((CM_5*0.01)**2)
    print(NAME_1 + "'s  BMI = %.2f" %calbmi_1())
    print(NAME_2 + "'s  BMI = %.2f" %calbmi_2())
    print(NAME_3 + "'s  BMI = %.2f" %calbmi_3())
    print(NAME_4 + "'s  BMI = %.2f" %calbmi_4())
    print(NAME_5 + "'s  BMI = %.2f" %calbmi_5())
main()
