"""KKK"""

def blooddonation(ages, weight, blood_donate_times):
    """Welcome to the hospital"""
    status = "No"
    if ages == 17 or (60 <= ages <= 70):
        consent = str(input())
        if consent == "False":
            status = "No"
    if (17 <= ages <= 70) and (weight >= 45):
        if blood_donate_times == 0 and ages <= 55:
            status = "Yes"
        elif blood_donate_times > 0:
            status = "Yes"
    if ages == 17 or (60 <= ages <= 70):
        if status == "Yes" and consent == "True":
            print("Yes")
        else:
            print("No")
    elif status == "Yes":
        print("Yes")
    else:
        print("No")
blooddonation(int(input()), int(input()), int(input()))
