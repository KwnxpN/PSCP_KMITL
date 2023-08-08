"""KKKK"""
def table(noodle_amounts):
    """noodle 15 baht need to multi any num"""
    for i in range(1, noodle_amounts+1):
        print("15 x {0} = {1}".format(i, i*15))
table(int(input()))
