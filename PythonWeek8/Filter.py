"""KKK"""

import json as blyad
def sort(get_list):
    """sort here"""
    return get_list[0]

def filter_blyad(students_score, score_filter):
    """blyad python"""
    mylist = []
    score_dict = blyad.loads(students_score)
    student_id = list(score_dict.keys())
    student_score = list(score_dict.values())
    for i in range(len(student_score)):
        if student_score[i] >= score_filter:
            mylist.append([student_id[i], "%.2f"%student_score[i]])
    mylist.sort(key=sort)
    if mylist == []:
        print("Nope")
    for student in mylist:
        print("{}\t{}".format(student[0], student[1]))
filter_blyad(str(input()), float(input()))
