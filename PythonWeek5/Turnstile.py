"""KKK"""

def turnstile():
    """the door need coin to push"""
    status = "locked"
    count = 0
    while True:
        action = input()
        if action != "END":
            if status == "locked":
                if action == "C":
                    status = "unlocked"
                else:
                    pass
            elif status == "unlocked":
                if action == "P":
                    count += 1
                    status = "locked"
                else:
                    pass
        else:
            break
    print(count)
turnstile()
