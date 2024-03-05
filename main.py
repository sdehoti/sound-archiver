'''
>> python main.py --dostuff arguments
'''

import sys
import os
import simpleaudio as sa
from simpleaudio_test import play_sound, play_sounds_at_once, rename_sound_file
argvlen = len(sys.argv)

'''
This is a debugging statement that prints out the list of command line arguments that were included when you 
invoked this program from the command line.
'''
print("sys.argv: ", sys.argv)

'''
# HELP: This is a command line argument that is invoked by typing --help or -h
>> python main.py --help
>> python main.py --h
'''

# This if statement checks to see what argument comes right after the program name
# Note that it also runs if you have no arguments after the program name
if argvlen<=1 or sys.argv[1]=='--help' or sys.argv[1]=='-h':

    # This prints out a sample of how you might use this command
    print("usage:",sys.argv[0], '--help')
    print('-h     : print this help message and exit (also --help)')
    print('-p     : plays one or more .wav files (also --play)')
    print('-ls    : plays one or more .wav files simultaneously (also --layersounds)')
    print('-a     : lists all the available files in the sounds directory (also --all)')
    print('-r     : renames the sound (also --rename)' )

    # Note that it is proper hygiene to have this at the end of each
    sys.exit(0);

'''
# HELP: This is another command line argument, invoked by typing --count or -c.
For example:
>> python cli_example.py --count
>> python cli_example.py -c *
>> python3 cli_example.py -c ../sounds/*.wav
    we use this command to count the number of wav files in sounds dir
'''
# Count is pretty basic: It just counts the command line arguments that come after it
if sys.argv[1] == '-c' or sys.argv[1] == '--count' :
    print("counted ", argvlen-2, " argument"+"s" if argvlen-2>1 else "")
    sys.exit(0)

'''
To add additional command line arguments, that have more capabilities, you need create more if statements.
For example, if we want to play a file, we should construct a new if statement to parse the following that you might 
enter into the command line:
>> python cli_example.py --play sounds/toaster.wav
>> python cli_example.py -p sounds/coffee.wav

You can use count as a template/example.
For now, it doesn't have to actually play a file, but it should take in a filepath as an additional argument
that comes after play (see the examples above).

For now, just have it print out the statement:
"I am now playing <filepath>."

(You'll add in the ability to actually play in the next step.)
'''

# ADD YOUR CODE FOR PLAY HERE
if (sys.argv[1] == '-p' or sys.argv[1] == '--play') and argvlen >= 3:
    play_sound(sys.argv[2])
    sys.exit(0)

#  Playing multiple sounds simultaneously 
if (sys.argv[1] == '-ls' or sys.argv[1] == '--layersounds') and argvlen >= 3:
    play_sounds_at_once(sys.argv[2:])
    sys.exit(0)

# Listing all available sounds with the command "-all"
if (sys.argv[1] == '-a' or sys.argv[1] == '--all'):
    directory = "sounds"
    files = os.listdir(directory)
    for file in files:
        print(file) 
    sys.exit(0)

# Renaming sounds 
if (sys.argv[1] == '-r' or sys.argv[1] == '--rename'):
    rename_sound_file(sys.argv[2], sys.argv[3])
    sys.exit(0)

'''
This goes at the end of all of your if statements and it lets you know if you have 
unknown or unaddressed command line arguments.
'''
print(sys.argv[0], "error, unexpected arguments ", sys.argv[1:],file=sys.stderr)

sys.exit(1)
