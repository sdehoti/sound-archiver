import simpleaudio as sa
import wave
import audioop
import random
import sqlite3


class SoundPlayer:
    def __init__(self, db_file):
        self.db_file = db_file
        # Connect to the database
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def play_files(self, folder_name):
        try:
            self.cursor.execute("SELECT path FROM AudioFiles WHERE path = ?", (folder_name,))
            files = self.cursor.fetchall()
            if files:
                for file in files:
                    filename = file[0]
                    wave_obj = sa.WaveObject.from_wave_file(filename)
                    print("I am now playing " + filename)
                    print(wave_obj)
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                    input("Press Enter to continue...")
            else:
                print(f"No files found in '{folder_name}' folder.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def play_files_simultaneously(self, folder_name):
        try:
            self.cursor.execute("SELECT path FROM AudioFiles WHERE path = ?", (folder_name,))
            files = self.cursor.fetchall()
            if files:
                waveObjects = []
                for file in files:
                    filename = file[0]
                    waveObjects.append(sa.WaveObject.from_wave_file(filename))
                playObjects = []
                for wave in waveObjects:
                    playObjects.append(wave.play())
                for play in playObjects:
                    play.wait_done()
            else:
                print(f"No files found in '{folder_name}' folder.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def play_reverse(self, file_path):
        try:
            with wave.open(file_path, 'rb') as wav_file:
                sample_width = wav_file.getsampwidth()
                num_channels = wav_file.getnchannels()
                frame_rate = wav_file.getframerate()
                num_frames = wav_file.getnframes()
                audio_data = wav_file.readframes(num_frames)
                reversed_audio_data = audioop.reverse(audio_data, sample_width)
            wave_obj = sa.WaveObject(reversed_audio_data, num_channels, sample_width, frame_rate)
            print("I am now playing " + file_path)
            print(wave_obj)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            input("Press Enter to continue...")
        except:
            print('Invalid filepath')

    def play_sound_segment(self, file_path):
        try:
            with wave.open(file_path, 'rb') as wav_file:
                sample_width = wav_file.getsampwidth()
                num_channels = wav_file.getnchannels()
                frame_rate = wav_file.getframerate()
                num_frames = wav_file.getnframes()
                start_frame = random.randint(0, num_frames // 2)
                wav_file.setpos(start_frame)
                audio_data = wav_file.readframes(num_frames // 2)
            wave_obj = sa.WaveObject(audio_data, num_channels, sample_width, frame_rate)
            print("I am now playing " + file_path)
            print(wave_obj)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            input("Press Enter to continue...")
        except:
            print('Invalid filepath')

    def __del__(self):
        self.cursor.close()  # Close cursor before closing connection
        self.conn.close()