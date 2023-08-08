"""KKKK"""

def sequence9(rows):
    """pyramid"""
    num = 0
    count_1 = 0
    count_2 = 0
    for i in range(1, rows+1):
        for _ in range(1, (rows-i)+1):
            print("  ", end=" ")
            count_1 += 1
        while num != ((2*i)-1):
            if count_1 <= rows-1:
                print("%02d"%(1+num), end=" ")
                count_1 += 1
            else:
                count_2 += 1
                print("%02d"%(1+num-(2*count_2)), end=" ")
            num += 1
        count_2 = count_1 = num = 0
        print()
sequence9(int(input()))
