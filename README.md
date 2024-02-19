# GlobalUnited
CS370 Final Project for team Global United
## Team Members
- Fabian: Contributed to the play_sound and play_sounds_at_once functions in simpleaudio_test.py.
- Shahrom
- Terence
- Zurain
## How To Use
Our program uses a command line interface. To access the CLI features, the user has to navigate to the code directory where the cli_example.py file is located. The user can then run the following prompt in the command line to view all of the possible commands in the sound archive.
```
python cli_example.py -h
```
or
```
python3 cli_example.py -h
```
For commands that require an additional argument, it can be included at the end of the prompt.
For example this prompt will play the toaster.wav audio file:
```
python cli_example.py -p ./sounds/toaster.wav
```
The argument can also be passed as a list of different WAV audio files
```
python cli_example.py -p ./sounds/*.wav
```
## Testing

## Challenges
One of the biggest challenges we have overcome was the implementation of the play_sounds_at_once function. After reading the official documentation of the simpleaudio library, we have used the conversion function to conver the individual audio files into Wave objects that are played one by one in a very short amount of time so that they layer on top of each other.