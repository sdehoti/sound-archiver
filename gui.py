import customtkinter
import tkinter
import tkinter.messagebox
from tools import Tools

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

gt = Tools()

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
        self.playlists_widget()
        self.features_widget()



    def playlists_widget(self):
        self.playlist_frame = customtkinter.CTkScrollableFrame(self, label_text="Playlists")
        self.playlist_frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.playlist_frame.grid_columnconfigure(0, weight=1)

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


    def create_playlist_button(self):
        self.create_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Create Playlist", command=lambda: gt.on_create_playlist(self))
        self.create_playlist_button.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
    
    def sort_playlist_button(self):
        self.sort_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Sort Playlist", command=lambda: gt.on_sort_playlis(self))
        self.sort_playlist_button.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def edit_sound_button(self):
        self.edit_sound_button = customtkinter.CTkButton(master=self.features_frame, text="Edit Sound File", command=gt.on_edit_sound)
        self.edit_sound_button.grid(row=3, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def record_sound_button(self):
        self.record_sound_button = customtkinter.CTkButton(master=self.features_frame, text="Record Sound", command=gt.on_record_sound)
        self.record_sound_button.grid(row=4, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def delete_playlist_button(self):
        self.delete_playlist_button = customtkinter.CTkButton(master=self.features_frame, text="Delete Playlist", command=gt.on_delete_playlist)
        self.delete_playlist_button.grid(row=5, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

     
   
        

    

   

    def update_sounds(self, playlist):
        pass
        # self.sounds_treeview.delete(*self.sounds_treeview.get_children())
        # for i in range(10):




app = SoundPlayer()
app.mainloop()


    
