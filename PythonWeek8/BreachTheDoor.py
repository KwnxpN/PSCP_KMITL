"""KKK"""

def breachthedoor(sentence):
    """why do we need to hack eJudge when we
    not even understand anything in eJudge"""
    sentence_list = sentence.split()
    result_list = []
    for word in sentence_list:
        for char in word:
            if not char.isalpha() or char.isdigit():
                word = word.replace(char, '')
        length = len(word)
        if length > 6:
            result_list.append(word)
    print(" ".join(result_list))
breachthedoor(str(input()))
