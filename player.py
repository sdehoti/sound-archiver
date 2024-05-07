import customtkinter
from sound_player import SoundPlayer

class Player:
    def __init__(self, master):
        self.frame = customtkinter.CTkFrame(master)
        self.frame.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.frame_label = customtkinter.CTkLabel(self.frame, text="Player Controls", font= ("Arial", 16))
        self.frame_label.grid(row=0, column=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        #self.frame.grid_columnconfigure(0, weight=0)
        self.render_buttons()
        self.render_wave_icon()
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(4, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.sound = None

    def update(self, sound):
        # a string list of sound file paths
        self.sound = sound

    def render_wave_icon(self):
        self.wave_icon = customtkinter.CTkImage(file='data/sound_wave.png')
        self.wave_icon.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")

    def render_buttons(self):
         self.prev_button = customtkinter.CTkButton(master=self.frame, text="⏮", command=lambda: SoundPlayer.play_files(SoundPlayer, self.sound), font= ("Arial", 20))
         self.prev_button.grid(row=3, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
         self.play_button = customtkinter.CTkButton(master=self.frame, text="⏵", command=lambda: SoundPlayer.play_files(SoundPlayer, self.sound), font= ("Arial", 20))
         self.play_button.grid(row=3, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")
         self.next_button = customtkinter.CTkButton(master=self.frame, text="⏭", command=lambda: SoundPlayer.play_files(SoundPlayer, self.sound), font= ("Arial", 20))
         self.next_button.grid(row=3, column=3, padx=(5, 5), pady=(5, 5), sticky="ew")

        