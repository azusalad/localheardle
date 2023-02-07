# how long to play a segment depending on how many tries you have done
# turn:time song plays for (seconds)
# So for example right now the 1st turn plays for 0.5 seconds and the 2nd for 1 second.
timings = {
1:0.5,
2:1,
3:2,
4:4,
5:6,
6:9
}

# the folder that contains all of your music
# in windows make sure to do escape the backslashes.  Example: "users\\myname\\downloads"
# Or you can put an r in front of the string.  Example: r"users\myname\downloads"
# on unix systems you do not have to worry
music_dir = "your/music/directory"

# volume
volume = 0.2
