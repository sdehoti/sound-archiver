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

    def on_create_playlist(self, playlist):

        dialog = customtkinter.CTkInputDialog(text="Enter the name of the playlist: ", title="Create Playlist")
        playlist_name = dialog.get_input()

        if playlist_name:
            button = customtkinter.CTkButton(master=playlist.playlist_frame, 
                                            text=playlist_name,
                                            command=playlist.update_sounds(playlist_name))
            button.grid(row=playlist.playlist_frame.grid_size()[1], column=0, padx=5, pady=5)


        

    def update_sounds(self, playlist):
        pass

    def on_delete_playlist(self):
        pass

    def on_delete_sounds(self):
        pass
