"""KKK"""

def badkeyboard(wrong_word):
    """https://open.spotify.com/track/3jTXU9nqIkYcTNuzXt6nsP?si=1d5d590ca0d74d94"""

    new_word = ""
    for i in wrong_word:
        if i == "i":
            new_word += i.replace("i", "o")
        elif i == "o":
            new_word += i.replace("o", "i")
        elif i == "I":
            new_word += i.replace("I", "O")
        elif i == "O":
            new_word += i.replace("O", "I")
        else:
            new_word += i
    print(new_word)
badkeyboard(input())
