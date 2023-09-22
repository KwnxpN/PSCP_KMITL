"""KKK"""

def almostmean(amount):
    """my friend next to me crying to netflix ejudge"""
    top_score = 0
    top_list, mylist, summary = [], [], 0
    for _ in range(amount):
        student = input().split()
        mylist.append(student)
    for i in mylist:
        summary += float(i[1])
    summary = summary/amount
    for i in mylist:
        if top_score < float(i[1]) < summary:
            top_score = float(i[1])
            top_list = i
    print("{}\t{}".format(top_list[0], top_list[1]))
almostmean(int(input()))
