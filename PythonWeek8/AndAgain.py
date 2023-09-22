"""KKK"""

def andagin(sentence):
    """vowels and sort by dictionary standard"""
    count = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result_list = []
    sentence = sentence.replace(".", " ")
    word_list = sentence.split()
    for word in word_list:
        for char in word:
            if char in vowels_list:
                count += 1
        if count >= 2:
            result_list.append(word)
        count = 0
    result_list = sorted(result_list)
    if result_list == []:
        print("Nope")
    for i in result_list:
        print(i)
andagin(str(input()))
