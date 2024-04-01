import simpleaudio as sa
import wave
import audioop
import random

class SoundPlayer:
    def play_files(self, file_paths):
        for filename in file_paths:
            try:
                wave_obj = sa.WaveObject.from_wave_file(filename)
                print("I am now playing " + filename)
                print(wave_obj)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                input("Press Enter to continue...")
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
        
    def play_reverse(self, file_path):
        try:
            # Open the WAV file
            with wave.open(file_path, 'rb') as wav_file:
                # Extract audio data
                sample_width = wav_file.getsampwidth()
                num_channels = wav_file.getnchannels()
                frame_rate = wav_file.getframerate()
                num_frames = wav_file.getnframes()
                audio_data = wav_file.readframes(num_frames)
                
                # Reverse audio data
                reversed_audio_data = audioop.reverse(audio_data, sample_width)

        
            wave_obj = sa.WaveObject(reversed_audio_data, num_channels,sample_width, frame_rate)
            print("I am now playing " + file_path)
            print(wave_obj)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            input("Press Enter to continue...")

        except:
             print('Invalid filepath')
        
    def play_sound_segment(self, file_path):
        try:
            # Open the WAV file
            with wave.open(file_path, 'rb') as wav_file:
                # Extract audio data
                sample_width = wav_file.getsampwidth()
                num_channels = wav_file.getnchannels()
                frame_rate = wav_file.getframerate()
                num_frames = wav_file.getnframes()

                # Randomly select a segment of the sound
                start_frame = random.randint(0,num_frames // 2)
                wav_file.setpos(start_frame)
                audio_data = wav_file.readframes(num_frames // 2)

    
            wave_obj = sa.WaveObject(audio_data, num_channels,sample_width, frame_rate)
            print("I am now playing " + file_path)
            print(wave_obj)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            input("Press Enter to continue...")
        except:
            print('Invalid filepath')

SoundPlayer.play_sound_segment(SoundPlayer,'./sounds/coffee.wav')