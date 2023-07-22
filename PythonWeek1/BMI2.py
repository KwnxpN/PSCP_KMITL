"""KKKK"""

def main():
    """llll"""
    def get_info1():
        """aaaa"""
        name_1 = str(input())
        kg_1 = float(input())
        cm_1 = float(input())
        return name_1 + "'s BMI =", kg_1 / ((cm_1* 0.01) **2)
    def get_info2():
        name_2 = str(input())
        kg_2 = float(input())
        cm_2 = float(input())
        return name_2 + "'s BMI =",kg_2 / ((cm_2*0.01)**2)
    def get_info3():
        name_3 = str(input())
        kg_3 = float(input())
        cm_3 = float(input())
        return name_3 + "'s BMI =",kg_3 / ((cm_3*0.01)**2)
    def get_info4():
        name_4 = str(input())
        kg_4 = float(input())
        cm_4 = float(input())
        return name_4 + "'s BMI =",kg_4 / ((cm_4*0.01)**2)
    def get_info5():
        name_5 = str(input())
        kg_5 = float(input())
        cm_5 = float(input())
        return name_5 + "'s BMI =",kg_5 / ((cm_5*0.01)**2)
        
    print(get_info1(),get_info2(),get_info3(),get_info4(),get_info5(),sep='\n'())
main()
