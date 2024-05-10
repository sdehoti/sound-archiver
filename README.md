# GlobalUnited
CS370 Final Project for team Global United
## Team Members
- Fabian: In Epoch 2, I worked on the export sound feature using priamrily the zipfile and os modules. This way the users are able to export a group of sounds into a single zip file which can later be shared with other users. I also contributed to the refactoring and enhancement of the sound_player file and implemented error handling for the functions used in the backend to manipulate with the sound. In Epoch 3, I primarily worked on the GUI Player object in player.py and built a connection between Player and the backend. I have also implemented the sorting feature of the imported sounds in the Sounds section.

- Shahrom: Contributed to testing files, refactoring and adding features the sounds files and folders manipulations
  
- Terence: Contributed to gui.py and tools.py.
  
- Zurain: For Epoch 2 I developed the grouping sounds feature. That feature allows users to select which sounds in a library they want to group together and then add to a new folder which they can rename. These folders are basically playlists with names that can be edited. I also contributed to developing a simple UI that runs in the terminal. For Epoch 3, I developed the record audio feature which allows users to record audio files, and when they click on stop audio, the gui.py converts the audio file to .wav format and then saves the file in the sounds folder. I also contributed to the internal documentation for some of the files of the project.

## How To Use
Our program uses a graphical user interface built using the tkinter and customtkinter libraries. To run the application all the source files need to be in the same directory as the sounds folder, which will work as the main audio library. Once everything is in the same directory run the following commands: 

``
pip install -r requirements.txt
``
``
python3 gui.py
``
<img width="1312" alt="IMG_4622" src="https://github.com/WhitmanCS370/GlobalUnited/assets/128567935/26e309ce-73c6-4dbc-bd6b-6d89275c15e3">






