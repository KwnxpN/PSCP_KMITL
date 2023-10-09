"""KKK"""

def removetag(html):
    """get out <>"""
    mylist = []
    if "<" in html or ">" in html:
        for _ in range(html.count("<")):
            html = html[html.find(">") + 1:]
            mylist.append(html[:html.find("<")].strip())
            html = html[html.find("<") + 1:]
    else:
        mylist = html.split()
    print(" ".join(mylist).split())
removetag(str(input()))
