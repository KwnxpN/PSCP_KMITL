"""KKK"""

def word_per_minutes(ages, wpm):
    """grading the typing"""
    grade_dict = {
        "Kids" : ["Very Slow" * (wpm < 11), "Slow" * (11 <= wpm <= 20), "Average" * \
                  (21 <= wpm <= 30), "Fast" * (31 <= wpm <= 40), "Very Fast" * (wpm > 40)],
        "Adults" : ["Very Slow" * (wpm < 26), "Slow/Beginner" * (26 <= wpm <= 35), \
                    "Intermediate/Average" * (36 <= wpm <= 45), "Fast/Advanced" * \
                    (46 <= wpm <= 65), "Very Fast" * (66 <= wpm <= 80), "Insane" * \
                    (wpm > 80)]
    }
    print("".join(grade_dict.get(ages)))
word_per_minutes(str(input()), int(input()))
