import customtkinter
import tkinter
import tkinter.messagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class SoundPlayer(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sound Player")
        self.geometry("1100x580")

        self.grid_columnconfigure((1), weight=1)
        self.grid_columnconfigure((0,2), weight=0)

        self.number_of_playlists = 0
        
       


        self.create_widgets()


    def create_widgets(self):
        self.playlists()
        self.features()




    def features(self):
        self.features_frame = customtkinter.CTkFrame(self)
        self.features_frame.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.features_frame_label = customtkinter.CTkLabel(self.features_frame, text="Tools", font= ("Arial", 16))
        self.features_frame_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.features_frame.grid_columnconfigure(0, weight=1)


        self.create_playlist_button()
        # self.sort_playlist_button()
        # self.edit_sound_button()
        # self.record_sound_button()

    def create_playlist_button(self):
        self.create_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Create Playlist", command=self.on_create_playlist)
        self.create_playlist_button.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
    

        
    def playlists(self):
        self.playlist_frame = customtkinter.CTkScrollableFrame(self, label_text="Playlists")
        self.playlist_frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.playlist_frame.grid_columnconfigure(0, weight=1)

        for i in range(10):  # Adjust this for the number of playlists you need
            button = customtkinter.CTkButton(master=self.playlist_frame, 
                                            text=f"Playlist {i + 1}",
                                            command=self.update_sounds(f"Playlist {i + 1}"))
            button.grid(row=i, column=0, padx=10, pady=10) # Adjust padx and pady as needed


    def on_create_playlist(self):
        tkinter.messagebox.showinfo("Create Playlist", "Create Playlist button clicked")

    def update_sounds(self, playlist):
        pass
        # self.sounds_treeview.delete(*self.sounds_treeview.get_children())
        # for i in range(10):




app = SoundPlayer()
app.mainloop()


    
