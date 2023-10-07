"""KKK"""


def phasmo():
    """get the evidience then check what ghost we found"""
    ghost_dict = {
        "EMF Level 5": ["Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"],
        "Ghost Writing": ["Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"],
        "Fingerprints": ["Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"],
        "Spirit Box": ["Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"],
        "Freezing Temperatures": ["Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"],
        "Ghost Orb": ["Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"],
        "No evidence": ["Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom", "Poltergeist",
                        "Revenant", "Shade", "Spirit", "Wraith", "Yurei"]
    }
    evidence_list, ghost_get = [], []
    for _ in range(3):
        evidence_list.append(str(input()))
    for things in evidence_list:
        ghost_get.append(set(ghost_dict.get(things)))
    remain = set.intersection(*ghost_get)
    result = sorted(remain)
    if result:
        print(*result, sep="\n")
    else:
        print("Not yet discovered")


phasmo()
