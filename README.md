# GlobalUnited
CS370 Final Project for team Global United
## Team Members
- Fabian: Contributed to sound_player, testing and share_file module.
- Shahrom: Contributed to testing files, refactoring and adding features the sounds files and folders manipulations
- Terence: Contributed to sound_player, testing and sorting modules.
- Zurain: Contributed to adding functionalities regarding organizing folders and making the UI for the archive

## How To Use
Our program uses a graphical user interface built using the tkinter and customtkinter libraries. To run the application all the source files need to be in the same directory as the sounds folder, which will work as the main audio library. Once everything is in the same directory run the following commands: 

``
pip install -r requirements.txt
``
``
python3 gui.py
``
<img width="1312" alt="IMG_4622" src="https://github.com/WhitmanCS370/GlobalUnited/assets/128567935/26e309ce-73c6-4dbc-bd6b-6d89275c15e3">




## Testing
For testing, we have written unit tests for methods of SoundPlayer from sound_player.py in the testing.py file. To implement these unit tests we have used the unittest library. We have decided to manually test our archive's grouping, sorting, and export functionality, as it requires us to see if these features are executed correctly.

## Challenges
One of the biggest challenges we have overcome was implementing the play_files_simultaneously method from SoundPlayer. After reading the official documentation of the simpleaudio library, we have used the conversion function to convert the individual audio files into Wave objects played one by one in a very short amount of time so that they layer on top of each other.
