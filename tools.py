import customtkinter


class Tools:
    def __init__(self):
        pass
    
    def on_play_sound(self, object):
        pass

    def on_stop_sound(self, object):
        pass

    def on_pause_sound(self, object):
        pass

    def on_resume_sound(self, object):
        pass

    def on_sort_playlist(self, object):
        pass

    def on_edit_sound(self, object):
        pass

    def on_record_sound(self, object):
        pass

    def on_create_playlist(self, soundplayer):

    



        dialog = customtkinter.CTkInputDialog(text="Enter the name of the playlist: ", title="Create Playlist")
        playlist_name = dialog.get_input()

        if playlist_name:
            button = customtkinter.CTkButton(master=soundplayer.playlist_frame, 
                                            text=playlist_name,
                                            command=soundplayer.update_sounds(playlist_name))
            button.grid(row=soundplayer.playlist_frame.grid_size()[1], column=0, padx=5, pady=5)
            soundplayer.playlists[playlist_name] = soundplayer.current_playlist
            soundplayer.current_playlist = []

      

        
        
        

    def update_sounds(self, soundplayer, playlist):


        pass

    def on_delete_playlist(self, soundplayer):
        dialog = customtkinter.CTkInputDialog(text="Enter the name of the playlist to delete: ", title="Delete Playlist")
        playlist_name = dialog.get_input()
        if playlist_name in soundplayer.playlists:
            soundplayer.playlists.remove(playlist_name)
            for widget in soundplayer.playlist_frame.winfo_children():
                if widget.cget("text") == playlist_name:
                    widget.destroy()


        

    def on_delete_sounds(self):
        pass
