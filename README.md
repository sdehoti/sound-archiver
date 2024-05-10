# GlobalUnited
CS370 Final Project for team Global United
## Team Members
  
- Shahrom: Contributed to refactoring of code, adding features such as exporting in share_file.py and several file manager features. On top of that, I contributed to gui.py and player.py modules by adding features such as play options, export sounds and also have made changes to the design of the Player Controls component to ensure it renders correctly and integrates well with the overall design of the rest of the components.

- Fabian: In Epoch 2, I worked on the export sound feature using priamrily the zipfile and os modules. This way the users are able to export a group of sounds into a single zip file which can later be shared with other users. I also contributed to the refactoring and enhancement of the sound_player file and implemented error handling for the functions used in the backend to manipulate with the sound. In Epoch 3, I primarily worked on the GUI Player object in player.py and built a connection between Player and the backend. I have also implemented the sorting feature of the imported sounds in the Sounds section.
  
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


## Reflection 

**Challenges: ** Our biggest challenge in this project was implementing the GUI. We had difficulties getting accustomed to the Tkinter interface and because we wanted better customization over the GUI we decided also to use the customtkinter library. This proved to be difficult however we read the documentation and looked at the examples provided in the customtkinter GitHub repo to get a better feel of how everything interacts. We then slowly built our GUI frame by frame and got it to work, barely though. Our application right now is very slow because we did not implement threading hence all operations, including the expensive ones, are running on one main thread which significantly reduces the time it takes to render the UI after getting user input. Therefore sometimes the buttons take a couple of seconds to respond. In the future, we would like to resolve this problem and optimize our code better. 





