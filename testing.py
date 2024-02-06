import unittest
import time 
from simpleaudio_test import play_sound

filename = 'sounds/coffee.wav'

class testSound(unittest.TestCase):
    def test_play_time(self):
        start_time = time.time()
        play_sound(filename)
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

if __name__ == "__main__":
    unittest.main()
