# GlobalUnited
CS370 Final Project for team Global United
## Team Members
- Fabian: Contributed to sound_player, testing and share_file module.
- Shahrom: Contributed to testing files, refactoring and adding features the sounds files and folders manipulations
- Terence: Contributed to sound_player, testing and sorting modules.
- Zurain: Contributed to adding functionalities regarding organizing folders and making the UI for the archive

## How To Use
Our program uses a command line interface; to use it, the source files need to be in the same directory as the 
audio library. To make use of the program; 

- run python main.py
```
    Welcome to the Sound Archive Management System.
    Your current working directory is:  /Users/path/GlobalUnited/
    -p : Play one or more .wav files
    -ps : Play multiple .wav files simultaneously
    -pr : Play a .wav file in reverse
    -l : List all available files in the directory
    -add : Add files to existing folder
    -cr : Create a folder and move .wav files into it
    -rm : Remove a specific file from a folder
    -rm dir : Delete a folder
    -rn : Rename a sound file
    -rn dir :  Rename a sound folder
    -zip : Compress selected sounds files into a .zip file
    -sortz : Sort files by size
    -sorta : Sort files alphabetically
    -sortc : Sort files by date created
    -sortm : Sort files by date modified
    -exit : Exit

    Choose one of the listed options: 
```
- choose an option from the menu by responding with the corresponding command, for example, to play a sound, you respond with "p". Thereafter, you will enter the path of the sound(s) you want to play which can be "./sounds/*.wav" or "sounds/*.wav sounds/**.wav". 

## Testing
For testing, we have written unit tests for methods of SoundPlayer from sound_player.py in the testing.py file. To implement these unit tests we have used the unittest library. We have decided to manually test our archive's grouping, sorting, and export functionality, as it requires us to see if these features are executed correctly.

## Challenges
One of the biggest challenges we have overcome was implementing the play_files_simultaneously method from SoundPlayer. After reading the official documentation of the simpleaudio library, we have used the conversion function to convert the individual audio files into Wave objects played one by one in a very short amount of time so that they layer on top of each other.
