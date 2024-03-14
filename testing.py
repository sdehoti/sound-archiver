import unittest
import time 
from share_file import play_sound, play_sounds_at_once

filename1 = 'sounds/coffee.wav'
filename2 = 'sounds/toaster.wav'

class testSound(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        play_sound(filename1)
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

class testMultipleSounds(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        play_sound([filename1,filename2])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
    
class testLayeredSounds(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        play_sounds_at_once([filename1,filename2])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)



if __name__ == "__main__":
    unittest.main()
