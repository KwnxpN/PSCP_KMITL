"""Helloooo"""

def helloooo(word):
    "check if last alpha is vowels make it long 4"
    rev_word = word[::-1]
    rev_word_list = [char for char in rev_word]
    for i in rev_word_list:
        if i in "aeiou":
            found = rev_word.index(i)
            for _ in range(3):
                rev_word_list.insert(found, i)
            break
    print(*rev_word_list[::-1], sep="")
helloooo(str(input()))
