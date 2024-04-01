import unittest
import time 
from sound_player import SoundPlayer

filename1 = 'sounds/coffee.wav'
filename2 = 'sounds/toaster-2.wav'

class testSound(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        SoundPlayer.play_files(SoundPlayer, [filename1])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

class testMultipleSounds(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        SoundPlayer.play_files(SoundPlayer, [filename1, filename2])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
    
class testLayeredSounds(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        SoundPlayer.play_files_simultaneously(SoundPlayer, [filename1,filename2])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

class testReversedSound(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        SoundPlayer.play_reverse(SoundPlayer, filename1)
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

class testSegmentSound(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        SoundPlayer.play_sound_segment(SoundPlayer, filename1)
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)


if __name__ == "__main__":
    unittest.main()
