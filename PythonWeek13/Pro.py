"""KKK"""

def pro(come, pay, price, people):
    """promotion shabu shabu yay"""
    if people >= come:
        if people%come == 0:
            print(int(((people/come)*pay)*price))
        else:
            print(int((((people//come)*pay)+people%come)*price))
    else:
        print(people*price)
pro(int(input()), int(input()), int(input()), int(input()))
