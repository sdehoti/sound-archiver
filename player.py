import customtkinter
from sound_player import SoundPlayer
from PIL import Image
import tkinter

class Player:
    """
    Player Class
    """
    def __init__(self, master):
        """
        Initializes a new instance of the Player class.

        Parameters:
            master: The tkinter master widget to which the player interface will be attached.
        """
        self.sound = ['No sound selected']
        self.pointer = 0
        self.frame = customtkinter.CTkFrame(master)
        self.frame.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.frame_label = customtkinter.CTkLabel(self.frame, text="Player Controls", font= ("Arial", 16))
        self.frame_label.grid(row=0, column=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.play_options = tkinter.StringVar(master=self.frame, value="default")
        self.radiobuttons()
        self.render_buttons()
        self.render_wave_icon()
        self.render_sound_name()
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(4, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)

    def update(self, sound):
        """
        Updates the player with a new list of sound files.

        Parameters:
            sound: A list of sound file paths to update the player with.
        """
        self.sound = sound
        self.pointer = 0
        self.sound_name.configure(text=self.sound[self.pointer].split('/')[-1])

    def render_wave_icon(self):
        """
        Renders a wave icon using a custom tkinter label widget.
        """
        self.wave_icon = customtkinter.CTkImage(light_image=Image.open('default-cover-art.png'), dark_image=Image.open('default-cover-art.png'), size=(180,180))
        self.label = customtkinter.CTkLabel(self.frame, text="", image=self.wave_icon)
        self.label.grid(row=1, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")

    def render_sound_name(self):
        """
        Renders the name of the currently selected sound file using a custom tkinter label widget.
        """
        self.sound_name = customtkinter.CTkLabel(master=self.frame, text=self.sound[self.pointer].split('/')[-1])
        self.sound_name.grid(row=2, column=2, sticky="ew")

    def render_buttons(self):
         """
        Renders control buttons for playback using custom tkinter button widgets.
        """
         self.prev_button = customtkinter.CTkButton(master=self.frame, text="⏮", command=lambda: self.prev_sound(), font= ("Arial", 20))
         self.prev_button.grid(row=3, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
         self.play_button = customtkinter.CTkButton(master=self.frame, text="⏵", command=lambda: self.play(), font= ("Arial", 20))
         self.play_button.grid(row=3, column=2, padx=(5, 5), pady=(5, 5), sticky="ew")
         self.next_button = customtkinter.CTkButton(master=self.frame, text="⏭", command=lambda: self.next_sound(), font= ("Arial", 20))
         self.next_button.grid(row=3, column=3, padx=(5, 5), pady=(5, 5), sticky="ew")

    def play(self):
        """
        Handles the playback of sound files based on the selected playback option.
        """
        if self.play_options.get() == "reverse":
            SoundPlayer.play_reverse(SoundPlayer, self.sound[self.pointer])
        elif self.play_options.get() == "random":
            SoundPlayer.play_sound_segment(SoundPlayer, self.sound[self.pointer])
        elif self.play_options.get() == "layered":
            SoundPlayer.play_files_simultaneously(SoundPlayer, self.sound)
            self.play_options.set("default")
            return
        elif self.play_options.get() == "default":
            SoundPlayer.play_files(SoundPlayer, [self.sound[self.pointer]])
        
        self.play_options.set("default")
        self.next_sound()

    def next_sound(self):
        """
        Moves to the next sound file in the list and updates the player interface accordingly.
        """
        if self.pointer + 1 < len(self.sound):
            self.pointer += 1
            self.sound_name.configure(text=self.sound[self.pointer].split('/')[-1])
        else:
            self.pointer = 0
            self.sound_name.configure(text=self.sound[self.pointer].split('/')[-1])
    
    def prev_sound(self):
        """
        Moves to the previous sound file in the list and updates the player interface accordingly.
        """
        if self.pointer - 1 > -1:
            self.pointer -= 1
            self.sound_name.configure(text=self.sound[self.pointer].split('/')[-1])
        else:
            self.pointer = len(self.sound) - 1
            self.sound_name.configure(text=self.sound[self.pointer].split('/')[-1])
     
    def radiobuttons(self):
        """
        Renders radio buttons for selecting different playback options using custom tkinter radio button widgets.
        """
        self.radiobuttons_frame = customtkinter.CTkFrame(master=self.frame)
        self.radiobuttons_frame.grid(row=1, column=0,padx=(20, 20), pady=(20, 20), )
        self.radiobuttons_frame.grid_columnconfigure(0, weight=1)
        self.radiobuttons_frame.grid_columnconfigure(2, weight=1)
        self.radiobuttons_label = customtkinter.CTkLabel(self.radiobuttons_frame, text="Play Options")
        self.radiobuttons_label.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
        self.default_button = customtkinter.CTkRadioButton(master=self.radiobuttons_frame, text="None", variable=self.play_options, value="default")
        self.default_button.grid(row=1, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
        self.reverse_button = customtkinter.CTkRadioButton(master=self.radiobuttons_frame, text="Reverse", variable=self.play_options, value="reverse")
        self.reverse_button.grid(row=2, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
        self.random_button = customtkinter.CTkRadioButton(master=self.radiobuttons_frame, text="Random", variable=self.play_options, value="random")
        self.random_button.grid(row=3, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")
        self.layered_button = customtkinter.CTkRadioButton(master=self.radiobuttons_frame, text="Layered", variable=self.play_options, value="layered")
        self.layered_button.grid(row=4, column=1, padx=(5, 5), pady=(5, 5), sticky="ew")