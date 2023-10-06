"""KKK"""

def pongya(num):
    """make dicision what I'm gonna say"""
    if num%3 == 0 or str(num)[-1] == "3":
        print("PONG")
    else:
        print(num)
pongya(int(input()))
