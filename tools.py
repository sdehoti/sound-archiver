import customtkinter
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import shutil
import os
import wavio 
import sounddevice as sd


class Tools:
    def __init__(self):
        pass
    
    def on_sort_playlist(self, object):
        pass

    def on_edit_sound(self, object):
        pass

    def on_record_sound(self, object):
        pass

    def toggle_record_sound(self,soundplayer):
        print("working")
        if not soundplayer.recording_in_progress:
            self.start_recording(soundplayer)
            soundplayer.recording_in_progress = True  # Update flag
        else:
            self.stop_recording(soundplayer)
            soundplayer.recording_in_progress = False  # Update flag

    def start_recording(self,soundplayer):
        # Define the recording parameters
        self.duration = 10  # Recording duration in seconds
        self.sample_rate = 44100  # Sample rate (samples per second)
        self.channels = 1  # Number of audio channels (1 for mono, 2 for stereo)

        # Start recording
        self.recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate,
                                channels=self.channels, dtype='float64')
        soundplayer.record_sound_button.configure(text="Stop Recording")

    def stop_recording(self,soundplayer):
        # Stop recording
        sd.wait()

        # Save the recorded audio to a WAV file in the "sounds" folder
        filename = tk.simpledialog.askstring("New Sound", "Enter a name for your new recording:") + ".wav"
        filepath = os.path.join("sounds", filename)
        wavio.write(filepath, self.recording, self.sample_rate, sampwidth=3)

        # Display a message box confirming the recording is saved
        tkinter.messagebox.showinfo("Recording Saved",
                                    f"The recording has been saved as {filename} in the 'sounds' folder.")

        # Reset the button text
        soundplayer.record_sound_button.configure(text="Record Sound")
        #soundplayer.update_sounds("All_Sounds")

    def on_add_sound_to_playlist(self, playlist_path,playlist_name, soundplayer):
        sound_files = filedialog.askopenfilenames(
        title="Add Sounds to Playlist",
        initialdir="sounds",  # Optionally start in the sounds folder
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")]  # Add more audio filetypes as needed
        )

        if sound_files: 
            for file in sound_files:
                try: 
                    shutil.copy(file, playlist_path)
                    soundplayer.playlists[playlist_name].append(file)
                    # Add the filename to your playlist data structure if needed  
                except shutil.Error as err:
                    tkinter.messagebox.showerror("Error", f"Failed to copy {file}: {err}") 

    def create_playlist_folder(self, soundplayer):

        playlist_name = tk.simpledialog.askstring("Create Playlist", "Enter a name for your playlist:")
        #need to keep track of the playlists created. 
        
        if playlist_name:  # Check if a name was provided
            soundplayer.playlists[playlist_name] = []
            button = customtkinter.CTkButton(master=soundplayer.playlist_frame, 
                                            text=playlist_name,
                                            command= lambda: soundplayer.update_sounds(playlist_name))
            button.grid(row=soundplayer.playlist_frame.grid_size()[1], column=0, padx=5, pady=5)
            
            playlist_path = os.path.join("sounds", playlist_name)

            try:
                os.mkdir(playlist_path)
                return playlist_path, playlist_name
            except FileExistsError:
                tkinter.messagebox.showerror("Error", f"Playlist '{playlist_name}' already exists.")
                button.destroy()

        return None 

    def on_create_playlist(self, soundplayer):
        playlist_path, playlist_name = self.create_playlist_folder(soundplayer)
        if playlist_path:
            self.on_add_sound_to_playlist(playlist_path, playlist_name ,soundplayer)

    def update_sounds(self, soundplayer, playlist):
        pass

    def on_delete_playlist(self, soundplayer):
        dialog = customtkinter.CTkInputDialog(text="Enter the name of the playlist to delete: ", title="Delete Playlist")
        playlist_name = dialog.get_input()
        if playlist_name in soundplayer.playlists:
            shutil.rmtree(os.path.join("sounds", playlist_name))
            del soundplayer.playlists[playlist_name]
            for widget in soundplayer.playlist_frame.winfo_children():
                if widget.cget("text") == playlist_name:
                    widget.destroy()
        else:
            tkinter.messagebox.showerror("Error", f"Playlist '{playlist_name}' not found.")
 
    def on_delete_sounds(self):
        pass
