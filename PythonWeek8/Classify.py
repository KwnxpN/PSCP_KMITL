"""KKK"""

def classify(students_id):
    """sort student id can count"""
    all_id = []
    non_dupe_id = []
    while students_id != "END":
        year = int(students_id[:2])
        major = int(students_id[2:4])
        all_id.append([year, major])
        if [year, major] not in non_dupe_id:
            non_dupe_id.append([year, major])
        students_id = str(input())
    all_id.sort()
    non_dupe_id.sort()
    prev_year = all_id[0][0] - 1
    for things in non_dupe_id:
        this_year = things[0]
        students_id = things[1]
        print(this_year if prev_year < this_year else "--", end=" ")
        prev_year = max(this_year, prev_year)
        print("{} {}".format(students_id, all_id.count(things)))
classify(str(input()))
