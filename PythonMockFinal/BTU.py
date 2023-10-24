"""BTU"""

def btu(room_area, room_height, people, hot_room, facing):
    """recommend that what air conditioner btu should be"""
    btu_dict = {
        tuple([i for i in range(100, 151)]) : 5000,
        tuple([i for i in range(151, 251)]) : 6000,
        tuple([i for i in range(251, 301)]) : 7000,
        tuple([i for i in range(301, 351)]) : 8000,
        tuple([i for i in range(351, 401)]) : 9000,
        tuple([i for i in range(401, 451)]) : 10000,
        tuple([i for i in range(451, 551)]) : 12000,
        tuple([i for i in range(551, 701)]) : 14000,
        tuple([i for i in range(701, 1001)]) : 18000,
        tuple([i for i in range(1001, 1201)]) : 21000,
        tuple([i for i in range(1201, 1401)]) : 23000,
        tuple([i for i in range(1401, 1501)]) : 24000,
        tuple([i for i in range(1501, 2001)]) : 30000,
        tuple([i for i in range(2001, 2501)]) : 34000,
    }
    for groupnum in btu_dict:
        for num in groupnum:
            if room_area == num:
                total_btu = btu_dict.get(groupnum)
    if room_height > 8:
        heightchange = room_height - 8
        total_btu += (1000 * heightchange)
    if people > 2:
        peoplechange = people - 2
        total_btu += (600 * peoplechange)
    if hot_room == "kitchen":
        total_btu += 4000
    if facing == "facing the sun":
        total_btu += (total_btu * 0.1)
    if facing == "shaded":
        total_btu -= (total_btu * 0.1)
    print(int(total_btu))
btu(int(input()), int(input()), int(input()), str(input()), str(input()))
