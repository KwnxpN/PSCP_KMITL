"""KKK"""
import json

def cal(crew):
    """check who dead and alive and how many imposter left"""
    spaceship, death = {}, []
    while crew != "Start":
        spaceship.update(json.loads(crew))
        crew = str(input())
    death_crew = str(input())
    while death_crew != "End":
        death.append(death_crew)
        death_crew = str(input())
    return sorted(list(spaceship.items())), sorted(death)

def impostor(crew):
    """main"""
    spaceship, death = cal(crew)
    impostor_count = 0
    alive = ""
    dead = ""
    for i in spaceship:
        color = i[0]
        role = i[1]
        if color not in death:
            alive += "{} : {}\n".format(color, role)
            if role == "Impostor":
                impostor_count += 1
        else:
            dead += "{} : {}\n".format(color, role)
    res = "{} Impostor Remains\n".format(impostor_count) + "***Alive***\n" + alive +\
            "***Dead***\n" + dead
    print(res.strip())
impostor(str(input()))
