# Local Heardle
Guess the song game from a local directory of mp3 files.

## Requirements
Python, pygame, mutagen

`pip install -r requirements.txt`

## Usage
First edit config.py and point to the directory that is filled with you mp3 files.  Note that the program only looks in the root directory and not and subdirectories.  You can also edit the segment times.  Then run the program:

`python main.py`

The program will prompt you to press enter to play a song.  The program will then choose a random song in the directory you provided and a random part in the song.  The song will them play for a little bit and then you can guess what song it is.  Enter the filename of the song (without the .mp3) to make your guess.  If you want to replay the segment you can type nothing and just press enter.  If you got it wrong, the program will keep playing more and more of the song and you can continue making guesses.  Once you finally get it right, the program will tell you that you got it right and continue playing the song from that point until you stop it.  The program keeps looping so you can continue playing.  Type `!quit` in the song guessing part to quit the game.

Unfortunately with this program you cannot tab to complete the file name.  Just have the your music folder open and copy the file name to guess.
