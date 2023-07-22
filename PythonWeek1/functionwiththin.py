"""25"""
def fff(xxx):
    """l"""
    return 2*xxx

def ggg(xxx):
    """l"""
    return (3 * xxx **4) - (xxx ** 3) + (2 * xxx **2) + 10

def hhh(xxx, yyy, zzz):
    """l"""
    return (zzz + xxx)**2 - xxx*yyy + yyy**2

def iii(xxx, yyy, zzz, qqq):
    """l"""
    return (xxx**2 + yyy**2 - zzz**2) / (qqq**2 - (2 * xxx * qqq) + (2 * xxx))

def main():
    """k"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    print(fff(fff(aaa)))
    print(ggg(fff(aaa - bbb)))
    print(hhh(fff(aaa+bbb), fff(aaa+ccc), ggg(fff(ddd**2))))
    print(iii(hhh(fff(aaa+bbb), fff(aaa-ccc), ggg(fff(ddd**2))), ggg(fff(aaa-bbb)),\
        fff(fff(fff(fff(fff(ccc))))), ddd**8))
main()
