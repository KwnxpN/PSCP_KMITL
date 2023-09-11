"""KKK"""

def oneforall(times):
    """bruh"""
    result = ""
    for i in range(1, times+1):
        name = input()
        if i == times:
            result += (name+"_"+str(times))
        elif i%2 != 0 and i != times+1:
            result += name+("*"*i)
        else:
            result += name+("-"*i)
    print(result)
oneforall(int(input()))
