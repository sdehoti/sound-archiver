import simpleaudio as sa
import wave
import audioop
import random
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

class SoundPlayer:
    """
    SoundPlayer class provides methods to play audio files, reverse audio, and play random segments of audio files.
    """
    def generate_sound_image(self, file_path):
            """
            Generates an image of the sound wave from a Wave object and saves it as a PNG file.

            Parameters:
                wave_obj (Wave): Wave object of the audio file.
                output_path (str): File path to save the PNG image.

            Returns:
                None

            Raises:
                None
            """
            wave_obj = wave.open(file_path, 'rb')
            # Get the audio data from the Wave object
            audio_data = wave_obj.readframes(-1)

            # Print the audio data for debugging
            print(audio_data)

            # Convert the audio data to a numpy array
            audio_array = np.frombuffer(audio_data, dtype=np.int16)

            # Create the time axis for the sound wave
            time = np.arange(0, len(audio_array)) / wave_obj._framerate

            # Plot the sound wave
            plt.plot(time, audio_array)
            plt.grid(True)

            # Save the plot as a PNG image

            plt.savefig('./data/sound_wave.png')
            plt.close()

    def play_files(self, file_paths):
        """
        Plays audio files sequentially.

        Parameters:
            file_paths (list): List of file paths to audio files.

        Returns:
            None

        Raises:
            None
        """
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
        """
        Plays audio files simultaneously.

        Parameters:
            file_paths (list): List of file paths to audio files.

        Returns:
            None

        Raises:
            None
        """
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
        """
        Plays the reversed version of an audio file.

        Parameters:
            file_path (str): File path to the audio file.

        Returns:
            None

        Raises:
            None
        """
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
        """
        Plays a random segment of an audio file.

        Parameters:
            file_path (str): File path to the audio file.

        Returns:
            None

        Raises:
            None
        """
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

if __name__ == "__main__":
    SoundPlayer.generate_sound_image(SoundPlayer, './sounds/coffee.wav')