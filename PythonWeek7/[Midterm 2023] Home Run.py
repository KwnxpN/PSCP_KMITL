"""KKK"""

def homerun(field_amount, hit_distance):
    """https://open.spotify.com/track/47WfK6QKlLwIOxJaonJ3bA?si=7c89a2b6cfb1433c"""

    homerun_amount = 0
    for _ in range(field_amount):
        field_distance = float(input())
        if hit_distance > field_distance:
            homerun_amount += 1
    print(homerun_amount)
homerun(int(input()), float(input()))
