"""KKK"""

def wordseq2(word1, word2):
    """jung"""
    length = max(len(word1), len(word2))
    for i in range(length+1):
        print(word2[0:i]+word1[i:])
wordseq2(str(input()), str(input()))
