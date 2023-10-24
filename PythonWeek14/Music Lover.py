"""KKK"""

def music_lover(amount):
    """sort the musician and them's music"""
    music_list = []
    music_dict = {}
    for _ in range(amount):
        band_n_music = tuple(str(input()).split("-"))
        music_list.append(band_n_music)
    for i in range(len(music_list)):
        key = music_list[i][0]
        if key not in music_dict:
            music_dict.update({music_list[i][0] : [music_list[i][1]]})
        else:
            music_dict[key].append(music_list[i][1])
    for band in music_dict:
        print(band, *music_dict.get(band), sep="\n")
music_lover(int(input()))
