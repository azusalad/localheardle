import pygame
import os
import random
import math
import time
from mutagen.mp3 import MP3

from config import *

finish = False
while True:
    # initialize a song and random length within the song to start playback
    win = False
    os.chdir(music_dir)
    songs = [x for x in os.listdir() if ".mp3" in x]
    song = random.choice(songs)
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    song_length = MP3(song).info.length
    play_pos = random.randint(0,math.floor(song_length - 15))
    pygame.mixer.music.set_volume(volume)
    turn = 1

    # actual game part
    input('Press enter to start\n>')
    while not win:
        replay = True
        print('Turn counter: ' + str(turn))

        while replay:
            pygame.mixer.music.rewind() # i am not sure if this is needed
            pygame.mixer.music.play(loops=0, start=play_pos)
            time.sleep(timings[turn]) # only play for a certain amount of time
            pygame.mixer.music.stop()
            guess = input('Guess a song name or type nothing to replay the segment\n>')
            if guess == "!quit":
                finish = True
                break
            elif guess != "":
                replay = False


        if finish:
            break # too lazy
        if song.split(".mp3")[0] == guess:
            win = True
        else:
            print('wrong')
        turn +=1
        if turn == 7:
            break


    if finish:
        break
    if win:
        print('you win the song was ' + str(song))
        pygame.mixer.music.play(loops=0, start=play_pos)
    else:
        print('you lose the song was ' + str(song))
    pygame.mixer.music.play(loops=0, start=play_pos)
    input('press enter to stop the playback\n>')
    pygame.mixer.music.stop()

print('the song was ' + str(song))
