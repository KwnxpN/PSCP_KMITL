"""KKK"""

def ticketfare():
    """https://open.spotify.com/track/50Y9OZ8R67SlGblz8m89A2?si=0014178e1d1c4a0c"""

    station_amount, first_sec_station, first_sec_price = int(input()), int(input()), int(input())
    second_sec_station, second_sec_price, third_sec_price = int(input()), int(input()), int(input())
    start_station, stop_station = int(input()), int(input())

    total_price = 0
    travel_distance = abs(start_station - stop_station)
    second_travel_distance = abs(travel_distance - first_sec_station)
    third_travel_distance = abs(travel_distance - (first_sec_station + second_sec_station))
    if travel_distance > station_amount or start_station > station_amount or \
        stop_station > station_amount:
        print("Error")
    elif travel_distance <= first_sec_station:
        total_price += first_sec_price
        print(total_price)
    elif travel_distance > first_sec_station and \
    travel_distance <= (first_sec_station+second_sec_station):
        second_total_price = second_travel_distance*second_sec_price
        total_price += (first_sec_price + (second_total_price))
        print(total_price)
    else:
        second_travel_distance -= third_travel_distance
        second_total_price = second_travel_distance*second_sec_price
        third_total_price = third_travel_distance*third_sec_price
        total_price += (first_sec_price+second_total_price+third_total_price)
        print(total_price)
ticketfare()
