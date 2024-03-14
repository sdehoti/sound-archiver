import simpleaudio as sa

class SoundPlayer:
    def play_files(self, file_paths):
        for filename in file_paths:
            try:
                wave_obj = sa.WaveObject.from_wave_file(filename)
                print("I am now playing " + filename)
                print(wave_obj)
                play_obj = wave_obj.play()
                play_obj.wait_done()
            except:
                print('Invalid filepath')

    def play_files_simultaneously(self, file_paths):
        waveObjects = []
        # Creates an array of Wave ojects from provided file paths
        for filename in file_paths:
            try:
                waveObjects.append(sa.WaveObject.from_wave_file(filename))
            except:
                continue
        playObjects = []
        # Creates an array of played Wave objects and plays them
        for wave in waveObjects:
            try:
                playObjects.append(wave.play())
            except:
                continue
        # The function waits until all sounds have been played
        for play in playObjects:
            try:
                play.wait_done()
            except:
                continue
