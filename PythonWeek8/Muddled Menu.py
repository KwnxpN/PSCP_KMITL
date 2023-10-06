"""KKK"""

def muddlemenu():
    """check the menu from autism chef and sort them"""
    menu_list = []
    while True:
        order = str(input())
        if order == "DONE":
            break
        elif order == "SOMETHING'S WRONG":
            menu_list.clear()
        elif order == "CLOSED":
            menu_list.clear()
            break
        else:
            pos = order.find("#")
            if order[pos + 1:].isdigit():
                menu_list.insert(int(order[pos + 1:])-1, order[:pos - 1])
            elif "Can't do:" in order:
                rev_pos = order.find(":") + 2
                menu_list.remove(order[rev_pos:])
            else:
                menu_list.append(order[:pos - 1])
    print("Full Course:", menu_list, "Reversed:", list(reversed(menu_list)))
muddlemenu()
