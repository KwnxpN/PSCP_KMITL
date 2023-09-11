"""KKK"""

def lift(people_amount, weight_limit):
    """https://open.spotify.com/track/5n3UhHQI7SHKkhI69u69Yq?si=9b8b1598b9344417"""

    age_status = "No adult"
    total_weight = 0
    if people_amount == 0:
        print("Safe")
    else:
        for _ in range(people_amount):
            age = int(input())
            weight = float(input())
            total_weight += weight
            if age >= 12 and age_status == "No adult":
                age_status = "Have adult"
        if age_status == "Have adult" and total_weight <= weight_limit:
            print("Safe")
        else:
            print("Not Safe")
lift(int(input()), float(input()))
