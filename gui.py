import customtkinter
import tkinter as tk
import tkinter.messagebox
from tools import Tools
import os
import shutil
from tkinter import filedialog
from datetime import datetime

from player import Player


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

gt = Tools()


class SoundPlayer(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sound Player")
        self.geometry("1200x580")

        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure((0,2), weight=0)
    

        self.number_of_playlists = 0
        self.playlists = {}
        self.current_playlist = []

        
        self.playlists["All_Sounds"] = os.listdir("sounds")
     
        

        self.create_widgets()


    def create_widgets(self):
        # Create the main widgets for the application
        self.playlists_widget()
        self.features_widget()
        self.sounds_widget()
        self.player_controls_widget()



    def playlists_widget(self):
        # Create the playlists frame and the default "All Sounds" button
        self.playlist_frame = customtkinter.CTkScrollableFrame(self, label_text="Playlists")
        self.playlist_frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.playlist_frame.grid_columnconfigure(0, weight=1)
        
        self.all_sounds_button = customtkinter.CTkButton(master=self.playlist_frame, text="All Sounds", command=lambda: self.update_sounds("All_Sounds"))
        self.all_sounds_button.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

        available_playlists = os.listdir("sounds")
        for playlist in available_playlists:
            if os.path.isdir(f"sounds/{playlist}"):
                button = customtkinter.CTkButton(master=self.playlist_frame, text=playlist, command=lambda playlist=playlist: self.update_sounds(playlist))
                button.grid(row=self.playlist_frame.grid_size()[1], column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
                self.number_of_playlists += 1


    def sounds_widget(self):
        self.sounds_frame = customtkinter.CTkFrame(self)
        self.sounds_frame.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.sounds_frame_label = customtkinter.CTkLabel(self.sounds_frame, text="Sounds", font= ("Arial", 16))
        self.sounds_frame_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.sounds_frame.grid_columnconfigure(0, weight=1)

        self.sounds_treeview = tk.ttk.Treeview(self.sounds_frame, columns=("name", "artist", "size", "date_created", "date_last_modified")) 
        self.sounds_treeview.heading("#0", text="ID", anchor="w")
        self.sounds_treeview.heading("name", text="Name", anchor="center")
        self.sounds_treeview.heading("artist", text="Artist", anchor="center")
        self.sounds_treeview.heading("size", text="Size", anchor="center")
        self.sounds_treeview.heading("date_created", text="Date Created", anchor="w")
        self.sounds_treeview.heading("date_last_modified", text="Date Last Modified")

        self.sounds_treeview.column("#0", width=20, anchor="w")
        self.sounds_treeview.column("name", width=70, anchor="w")
        self.sounds_treeview.column("artist", width=70, anchor="w")
        self.sounds_treeview.column("size", width=50,   anchor="w")
        self.sounds_treeview.column("date_created", width=50, anchor="w")
        self.sounds_treeview.column("date_last_modified", width=50, anchor="w")

       

        self.sounds_treeview.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.sounds_frame.grid_rowconfigure(1, weight=1)
        

        if self.current_playlist:
            self.update_sounds("Current_Playlist")
        else:
            self.update_sounds("All_Sounds") 

        # Bind the Treeview widget to the update_current_playlist method when a sound is selected in the list
        self.sounds_treeview.bind("<<TreeviewSelect>>", self.update_current_playlist) 

      
        
    def update_current_playlist(self, event):
        # Update the current playlist with the selected sounds
        self.current_playlist = []  

        selected_items = self.sounds_treeview.selection()
        for item in selected_items:
            sound_name = self.sounds_treeview.item(item, "values")[0]
            self.current_playlist.append(sound_name)
        self.playlists["Current_Playlist"] = self.current_playlist 

        
   
        # self.sounds_treeview.insert("", tkinter.END, values=("Song 1", "Artist 1", "3.5 MB"))
        # self.sounds_treeview.insert("", tkinter.END, values=("Song 2", "Artist 2", "4.2 MB"))
        # self.sounds_treeview.insert("", tkinter.END, values=("Song 3", "Artist 3", "2.1 MB"))

    def player_controls_widget(self):
        player = Player(self)

        #Instead of using buttons for controls, use icons for play, stop, pause, and resume
       

    def features_widget(self):
        # Create the features frame and its widgets
        self.features_frame = customtkinter.CTkFrame(self)
        self.features_frame.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.features_frame_label = customtkinter.CTkLabel(self.features_frame, text="Tools", font= ("Arial", 16))
        self.features_frame_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.features_frame.grid_columnconfigure(0, weight=1)


        self.create_playlist_button()
        self.sort_playlist_button()
        self.edit_sound_button()
        self.record_sound_button()
        self.delete_playlist_button()
        self.add_sound_to_playlist()


    def create_playlist_button(self):
        self.create_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Create Playlist", command=lambda: gt.on_create_playlist(self))
        self.create_playlist_button.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def add_sound_to_playlist(self):
        self.add_sound_to_playlist = customtkinter.CTkButton(master=self.features_frame, text="Add Sound to Playlist", command=lambda: gt.on_add_sound_to_playlist(self))
        self.add_sound_to_playlist.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")   
        
    def sort_playlist_button(self):
        self.sort_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Sort Playlist", command=lambda: gt.on_sort_playlis(self))
        self.sort_playlist_button.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def edit_sound_button(self):
        self.edit_sound_button = customtkinter.CTkButton(master=self.features_frame, text="Edit Sound File", command=lambda: gt.on_edit_sound(self))
        self.edit_sound_button.grid(row=3, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def record_sound_button(self):
        self.record_sound_button = customtkinter.CTkButton(master=self.features_frame, text="Record Sound", command=lambda: gt.on_record_sound(self))
        self.record_sound_button.grid(row=4, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def delete_playlist_button(self):
        self.delete_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Delete Playlist", command= lambda: gt.on_delete_playlist(self))
        self.delete_playlist_button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

     
   

   

    def update_sounds(self, playlist_name):
        
        # Update the sounds list based on the selected playlist
        if playlist_name in self.playlists:
            self.sounds = self.playlists[playlist_name]

        self.sounds_treeview.delete(*self.sounds_treeview.get_children())
        for i, sound in enumerate(self.sounds, 1):
            sound_stats = os.stat(f"sounds/{sound}")
            sound_size = sound_stats.st_size
            sound_date_created = datetime.fromtimestamp(sound_stats.st_ctime).strftime("%Y-%m-%d %H:%M:%S")
            sound_date_last_modified = datetime.fromtimestamp(sound_stats.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

            self.sounds_treeview.insert("", tk.END, values=(i, sound, "Unknown", f"{sound_size / 1024:.2f} KB", sound_date_created, sound_date_last_modified))
        
        self.sounds_treeview.bind("<Double-1>", lambda event: gt.on_play_sound(self))
            #self.sounds_treeview.bind("<Double-1>", lambda event: gt.on_play_sound(self))
       
        




app = SoundPlayer()
app.mainloop()


    
