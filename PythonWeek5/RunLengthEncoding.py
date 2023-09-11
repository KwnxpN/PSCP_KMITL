"""KKKK"""

def runlenencode(word_get):
    """count alpha"""
    alpha_count = 0
    for i in range(0, len(word_get)-1, 1):
        if word_get[i] == word_get[i+1]:
            alpha_count += 1
        elif word_get[i] != word_get[i+1]:
            alpha_count += 1
            print(str(alpha_count)+word_get[i], end='')
            alpha_count = 0
        else:
            break
    print(str(alpha_count+1)+word_get[-1], end='')
runlenencode(input())
