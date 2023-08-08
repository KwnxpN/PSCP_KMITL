"""KKKK"""
import math
def grade3(subject_amount):
    """find average grade with input
    amounts of grade and any score"""
    sum_grade = 0
    for _ in range(1, subject_amount+1):
        score = float(input())
        if score <= 100 and score >= 95:
            sum_grade += 4
        elif score <= 95 and score >= 90:
            sum_grade += 3.5
        elif score <= 90 and score >= 85:
            sum_grade += 3
        elif score <= 85 and score >= 80:
            sum_grade += 2.5
        elif score <= 80 and score >= 75:
            sum_grade += 2
        elif score <= 75 and score >= 70:
            sum_grade += 1.5
        elif score <= 70 and score >= 65:
            sum_grade += 1
        elif score <= 65 and score >= 60:
            sum_grade += 0.5
        else:
            sum_grade += 0

    result = sum_grade / subject_amount
    print("%.2f"%(math.floor(result*100)/100.0))
grade3(int(input()))
