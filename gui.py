import customtkinter
import tkinter
import tkinter.messagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class SoundPlayer(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sound Player")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.create_widgets()


    def create_widgets(self):

        self.playlist_frame = customtkinter.CTkFrame(self, width=100, height=300) 
        self.playlist_frame.grid(row=0, column=0, rowspan=2,sticky="nsew")
        self.title_label = customtkinter.CTkLabel(self.playlist_frame, text="Playlist", font=("Arial", 12))
        self.title_label.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")




app = SoundPlayer()
app.mainloop()


    
