import tkinter as tk
from tkinter import ttk
#import sqlite3  # Assuming you're using SQLite for the database
import unittest.mock as mock  # Using mock library for database simulation

class Sound:
    def __init__(self, sound_id, filename, title="", artist="", date_created=""):
        self.sound_id = sound_id
        self.filename = filename
        self.title = title
        self.artist = artist
        self.date_created = date_created

class Playlist:
    def __init__(self, playlist_id, name):
        self.playlist_id = playlist_id
        self.name = name
        self.songs = [] 


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sound Player")
        self.window.geometry("900x700")

        self.sound_list = []  # List to store Sound objects
        self.current_sound = None  # Currently playing sound
        self.queue = []  # Queue to store upcoming sounds
        self.playlists = []  # List to store Playlist objects
        self.selected_playlist = None  # Currently selected playlist

        self.create_widgets()
        self.mock_database()  # Simulate database interaction
        #self.connect_to_database()  # Uncomment this line to connect to a real database



    def mock_database(self):
           # Create mock objects to simulate database behavior
        self.conn = mock.Mock()
        cursor = mock.Mock()
        self.conn.cursor.return_value = cursor

        # Mock cursor behavior to return predefined playlist and sound data
        cursor.fetchall.return_value = [
            # Playlist data
            (1, "Playlist 1"),
            (2, "Playlist 2"),

            # Sound data (assign them to playlists)
            (1, "sound1.mp3", "Song 1", "Artist 1", "date_created 1", 1),  # Playlist 1
            (2, "sound2.mp3", "Song 2", "Artist 2", "date_created 2", 1),  # Playlist 1
            (3, "sound3.mp3", "Song 3", "Artist 3", "date_created 3", 2),  # Playlist 2
        ]

        # Populate playlist list with mock data
        for row in cursor.fetchall():
            if len(row) == 2:  # Playlist data
                playlist = Playlist(*row)
                self.playlists.append(playlist)
            else:  # Sound data
                sound = Sound(*row[:-1])  # Unpack sound data
                playlist_id = row[-1]
                for playlist in self.playlists:
                    if playlist.playlist_id == playlist_id:
                        playlist.songs.append(sound)
                        break

        # Update playlist listbox
        self.update_playlist_listbox()
      

    def on_playlist_select(self, event):
        print("Entering on_playlist_select method")
        selected_playlist_name = self.playlist_listbox.selection()[0]  # Get name from selected item

        for playlist in self.playlists:
            if playlist.name == selected_playlist_name:
                self.selected_playlist = playlist
                break

        # Clear the sound_listbox and update with the selected playlist's songs 
        self.sound_list.clear()
        if self.selected_playlist:
            self.sound_list = self.selected_playlist.songs  
            self.update_listbox() 


    def update_playlist_listbox(self):
        self.playlist_listbox.delete(*self.playlist_listbox.get_children())  # Clear existing items
        for playlist in self.playlists:
            self.playlist_listbox.insert('', tk.END, values=playlist.name) 




    def create_widgets(self):

        # Create a frame to contain the listboxes, for layout control
        listboxes_frame = tk.Frame(self.window)
        listboxes_frame.pack(fill=tk.BOTH, expand=True)  

        # Playlist listbox
        self.playlist_listbox = ttk.Treeview(listboxes_frame, columns=("Playlists"), show="headings")
        self.playlist_listbox.heading("Playlists", text="Playlists")
        self.playlist_listbox.grid(row=0, column=0, sticky="nsew") 
        self.playlist_listbox.bind("<<TreeviewSelect>>", self.on_playlist_select)

        # Listbox to display sounds and metadata
        self.sound_listbox = ttk.Treeview(listboxes_frame, columns=("ID", "filename", "title", "artist", "date_created"), show="headings")
        self.sound_listbox.heading("ID", text="ID")
        self.sound_listbox.heading("filename", text="Filename")
        self.sound_listbox.heading("title", text="Title")
        self.sound_listbox.heading("artist", text="Artist")
        self.sound_listbox.heading("date_created", text="date_created")

         # Set column widths (adjust as needed)
        self.sound_listbox.column("ID", width=1, anchor= "w")  
        self.sound_listbox.column("filename", width=100, anchor="center")
        self.sound_listbox.column("title", width=50, anchor="center")
        self.sound_listbox.column("artist", width=50, anchor="center")
        self.sound_listbox.column("date_created", width=50, anchor="center")

        self.sound_listbox.grid(row=0, column=1, sticky="nsew") 

        # Configure weights for the rows and columns within the frame
        listboxes_frame.grid_rowconfigure(0, weight=1)  
        listboxes_frame.grid_columnconfigure(0, weight=2)  
        listboxes_frame.grid_columnconfigure(1, weight=8)  

        # Button to select a sound from the list
        self.select_button = tk.Button(self.window, text="Play", command=self.play_selected)
        self.select_button.pack(padx=10, pady=10)

        # Playback controls 
        self.pause_button = tk.Button(self.window, text="Pause", command=self.pause)
        self.pause_button.pack(padx=5, pady=10, side=tk.RIGHT)
        self.skip_button = tk.Button(self.window, text="Skip", command=self.skip)
        self.skip_button.pack(padx=10, pady=10, side=tk.LEFT)



    def update_listbox(self):
        self.sound_listbox.delete(*self.sound_listbox.get_children())  # Clear listbox
        for sound in self.sound_list:
            self.sound_listbox.insert("", tk.END, values=(sound.sound_id, sound.filename, sound.title, sound.artist, sound.date_created))

    def play_selected(self):
        selected_item = self.sound_listbox.selection_get()
        if selected_item:
            sound_id = self.sound_listbox.item(selected_item, "values")[0]  # Get sound ID from filename
            for sound in self.sound_list:
                if sound.sound_id == sound_id:
                    self.current_sound = sound
                    # Implement playback functionality using a library like playsound or pygame
                    print(f"Playing: {sound.title}")
                    break  # Exit loop after finding the selected sound

        # Add selected sound to the queue (optional)
        if self.current_sound:
            self.queue.append(self.current_sound)
            self.update_queue_listbox()



    def pause(self):
        # Implement pause functionality for the current sound (placeholder)
        print("Pause button pressed")

    def skip(self):
        if self.queue:
            self.current_sound = self.queue.pop(0)  # Play next sound in the queue
            # Implement playback functionality for the new


    def start(self):
        self.window.mainloop()


gui = GUI()
gui.start()