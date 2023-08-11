"""KKKK"""
def nearer(alice, bob, icecream):
    """find nearest person"""
    if abs(icecream - alice) > abs(icecream - bob):
        print("Bob", abs(icecream-bob))
    elif abs(icecream - bob) > abs(icecream - alice):
        print("Alice", abs(icecream-alice))
    elif abs(icecream - bob) == abs(icecream - alice):
        print("Sundaes", abs(icecream - alice))
nearer(int(input()), int(input()), int(input()))
