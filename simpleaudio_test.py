'''
Created for CS-370 Lab Week 3
This is the most basic example of how to play a file using the simpleaudio package
'''

import sounds as sounds
from zipfile import ZipFile
import simpleaudio as sa
import os

# This is a test sound file
def play_sound(filename):
    # Tries 
    try:
        wave_obj = sa.WaveObject.from_wave_file(filename)
        print("I am now playing " + filename)
        print(wave_obj)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
    except:
        print('Invalid filepath')

# Play multiple audio files on top of each other
def play_sounds_at_once(filenames):
    waveObjects = []
    # Creates an array of Wave ojects from provided file paths
    for filename in filenames:
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

def rename_sound_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except FileExistsError:
        print(f"File '{new_name}' already exists.")

def zip_files(audio_files):
# audio_files: str list of audio file paths
    try:
        zip = ZipFile("./export/export.zip", "w")
        for file in audio_files:
            zip.write(file, arcname=file.split('/')[-1])
        zip.close()
    except:
        print("Cannot ZIP files")






