"""frame but so weird"""

def bigframe(word1, word2, word3, word4, word5):
    """im braindead fr"""
    word1, word2, word3, word4, word5 = word1.strip(), word2.strip(), word3.strip(),\
        word4.strip(), word5.strip()
    len1 = len(word1)
    len2 = len(word2)
    len3 = len(word3)
    len4 = len(word4)
    len5 = len(word5)
    length = max(len1, len2, len3, len4, len5)
    print("*"*(length+4))
    print("*", word1+(' '*(length-len1)), "*")
    print("*", word2+(' '*(length-len2)), "*")
    print("*", word3+(' '*(length-len3)), "*")
    print("*", word4+(' '*(length-len4)), "*")
    print("*", word5+(' '*(length-len5)), "*")
    print("*"*(length+4))
bigframe(str(input()), str(input()), str(input()), str(input()), str(input()))
