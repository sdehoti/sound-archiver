import unittest
import time 
from sound_player import SoundPlayer

filename1 = 'sounds/coffee.wav'
filename2 = 'sounds/toaster-2.wav'

class testSound(unittest.TestCase):
    """
    Test case for playing a single sound file.
    """
    def test_play_time(self):
        """
        Tests the time taken to play a single sound file.
        """
        start_time = time.time()
        SoundPlayer.play_files(SoundPlayer, [filename1])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

class testMultipleSounds(unittest.TestCase):
    """
    Test case for playing multiple sound files sequentially.
    """
    def test_play_time(self):
        """
        Tests the time taken to play multiple sound files sequentially.
        """
        start_time = time.time()
        SoundPlayer.play_files(SoundPlayer, [filename1, filename2])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
    
class testLayeredSounds(unittest.TestCase):
    """
    Test case for playing multiple sound files simultaneously.
    """
    def test_play_time(self):
        """
        Tests the time taken to play multiple sound files simultaneously.
        """
        start_time = time.time()
        SoundPlayer.play_files_simultaneously(SoundPlayer, [filename1,filename2])
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

class testReversedSound(unittest.TestCase):
    """
    Test case for playing a sound file in reverse.
    """
    def test_play_time(self):
        """
        Tests the time taken to play a sound file in reverse.
        """
        start_time = time.time()
        SoundPlayer.play_reverse(SoundPlayer, filename1)
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

class testSegmentSound(unittest.TestCase):
    """
    Test case for playing a random segment of a sound file.
    """
    def test_play_time(self):
        """
        Tests the time taken to play a random segment of a sound file.
        """
        start_time = time.time()
        SoundPlayer.play_sound_segment(SoundPlayer, filename1)
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(elapsed_time)




if __name__ == "__main__":
    unittest.main()
