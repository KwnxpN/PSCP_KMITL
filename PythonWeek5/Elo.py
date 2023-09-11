'''elo'''
def main():
    '''equation'''
    ra_val = int(input())
    rb_val = int(input())
    winner = str(input())
    cala = 1/(1+10**((rb_val-ra_val)/400))
    calb = 1/(1+10**((ra_val-rb_val)/400))
    if winner == "A":
        print("%.2f" % cala)
    else:
        print("%.2f" % calb)
main()
