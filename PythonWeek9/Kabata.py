"""KKK"""

def check_kabata(kabata_word):
    """kakababtakatabakkakatababakka"""
    if kabata_word.find("baka") != -1:
        return 'no'
    kaba_list = ['bakka', 'ka', 'ba', 'ta']
    for word in kaba_list:
        kabata_word = kabata_word.replace(word, '')
    return 'no' if kabata_word else 'yes'

def kabata():
    "katababatatakabakkatabataka"
    for _ in range(int(input())):
        print(check_kabata(input()))
kabata()
