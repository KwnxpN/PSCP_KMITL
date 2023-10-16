"""KKK"""

def hamming(word1, word2):
    """ham ham ham ham ham ham yay"""
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    print(count)
hamming(str(input()), str(input()))
