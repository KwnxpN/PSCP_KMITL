"""socks"""

def socks(unsort_socks):
    """count the couple of socks and sort them"""
    sock_list = []
    for sock in unsort_socks:
        if sock not in sock_list:
            sock_list.append(sock)
        else:
            pos = sock_list.index(sock)
            sock_list[pos] += sock
    want_to_remove = []
    for i in sock_list:
        if len(i) != 2:
            want_to_remove.append(i)
    for not_couple in want_to_remove:
        sock_list.remove(not_couple)
    sock_list.sort()
    if sock_list == []:
        print("None")
        print(0)
    else:
        print(*sock_list, sep=" ")
        print(len(sock_list))
socks(str(input()))
