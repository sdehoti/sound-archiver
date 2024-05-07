import customtkinter
import tkinter as tk
import tkinter.messagebox
from tools import Tools

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
        self.playlists = []

        self.create_widgets()


    def create_widgets(self):
        self.playlists_widget()
        self.features_widget()
        self.sounds_widget()
        self.player_controls_widget()



    def playlists_widget(self):
        self.playlist_frame = customtkinter.CTkScrollableFrame(self, label_text="Playlists")
        self.playlist_frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.playlist_frame.grid_columnconfigure(0, weight=1)

    def sounds_widget(self):
        self.sounds_frame = customtkinter.CTkFrame(self)
        self.sounds_frame.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.sounds_frame_label = customtkinter.CTkLabel(self.sounds_frame, text="Sounds", font= ("Arial", 16))
        self.sounds_frame_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.sounds_frame.grid_columnconfigure(0, weight=1)

        self.sounds_treeview = tk.ttk.Treeview(self.sounds_frame, columns=("name", "artist", "size", "date_created", "date_last_modified")) 
        self.sounds_treeview.heading("#0", text="ID")
        self.sounds_treeview.heading("name", text="Name")
        self.sounds_treeview.heading("artist", text="Artist")
        self.sounds_treeview.heading("size", text="Size")
        self.sounds_treeview.heading("date_created", text="Date Created")
        self.sounds_treeview.heading("date_last_modified", text="Date Last Modified")

        self.sounds_treeview.column("#0", width=50)
        self.sounds_treeview.column("name", width=200)
        self.sounds_treeview.column("artist", width=100)
        self.sounds_treeview.column("size", width=50)
        self.sounds_treeview.column("date_created", width=75)
        self.sounds_treeview.column("date_last_modified", width=75)



        self.sounds_treeview.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.sounds_frame.grid_rowconfigure(1, weight=1)

        # self.sounds_treeview.insert("", tkinter.END, values=("Song 1", "Artist 1", "3.5 MB"))
        # self.sounds_treeview.insert("", tkinter.END, values=("Song 2", "Artist 2", "4.2 MB"))
        # self.sounds_treeview.insert("", tkinter.END, values=("Song 3", "Artist 3", "2.1 MB"))

    def player_controls_widget(self):
        self.player_controls_frame = customtkinter.CTkFrame(self)
        self.player_controls_frame.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.player_controls_frame_label = customtkinter.CTkLabel(self.player_controls_frame, text="Player Controls", font= ("Arial", 16))
        self.player_controls_frame_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.player_controls_frame.grid_columnconfigure(0, weight=1)


        #Instead of using buttons for controls, use icons for play, stop, pause, and resume
       

    def features_widget(self):
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


    def create_playlist_button(self):
        self.create_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Create Playlist", command=lambda: gt.on_create_playlist(self))
        self.create_playlist_button.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
    
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

     
   
        

    

   

    def update_sounds(self, playlist):
        pass
        # self.sounds_treeview.delete(*self.sounds_treeview.get_children())
        # for i in range(10):




app = SoundPlayer()
app.mainloop()


    
