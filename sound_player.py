from simpleaudio_test import play_sound, play_sounds_at_once

class SoundPlayer:
    def play_files(self, file_paths):
        for file in file_paths:
            play_sound(file)

    def play_files_simultaneously(self, file_paths):
        play_sounds_at_once(file_paths)
