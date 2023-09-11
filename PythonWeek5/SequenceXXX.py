"""KKKK"""

def seqxxx(size, amount):
    """seqxxx"""
    text = ""
    for i in range(size):
        for _ in range(amount):
            count = 0
            for col in range(size):
                if i in (0, col, size - 1, size - col - 1) or count in (0, size - 1):
                    text += "*"
                else:
                    text += " "
                count += 1
            text += " "
        text += "\n"
    print(text)
seqxxx(int(input()), int(input()))
