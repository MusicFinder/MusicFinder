# -*- coding: utf-8 -*-

with open('sim_result1.txt', encoding='utf-8') as f:
    lines1 = f.readlines()

with open('sim_result2.txt', encoding='utf-8') as f:
    lines2 = f.readlines()

song_res = {}
for lines in [lines1, lines2]:
    for line in lines:
        if line == '':
            continue
        #print ([line])
        song1, song2, sim = line.strip().split('\t')
        sim = float(sim)
        if song1 not in song_res:
            song_res[song1] = []
        song_res[song1].append((song2, sim))

with open('top3_sim_result.txt', 'w', encoding='utf-8') as f:
    pass
for song in song_res:
    #print(song, len(song_res[song]))
    sorted_sim_res = sorted(song_res[song], key=lambda item: item[1])
    #print (sorted_sim_res[0:5])
    top_songs = [item[0] for item in sorted_sim_res[0:3]]
    with open('top2_sim_result.txt', 'a', encoding='utf-8') as f:
        f.write(song + '\t' + '\t'.join(top_songs) + '\n')