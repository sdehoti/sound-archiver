import sys
import os
import shutil
from simpleaudio_test import play_sound, play_sounds_at_once, rename_sound_file

def create_folder(folder_name, file_paths):
    try:
        os.mkdir(folder_name)
        for file_path in file_paths:
            shutil.move(file_path, os.path.join(folder_name, os.path.basename(file_path)))
        print(f"Folder '{folder_name}' created successfully and files moved.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def delete_folder(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"Folder '{folder_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def delete_file(folder_name, file_name):
    file_path = os.path.join(folder_name, file_name)
    try:
        os.remove(file_path)
        print(f"File '{file_name}' deleted successfully from folder '{folder_name}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found in folder '{folder_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

argvlen = len(sys.argv)

if argvlen <= 1 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print("usage:", sys.argv[0], '--help')
    print('-h     : print this help message and exit (also --help)')
    print('-p     : plays one or more .wav files (also --play)')
    print('-ls    : plays one or more .wav files simultaneously (also --layersounds)')
    print('-a     : lists all the available files in the sounds directory (also --all)')
    print('-r     : renames the sound (also --rename)')
    print('-cf    : create a folder and move .wav files into it')
    print('-df    : delete a folder')
    print('-rm    : remove a specific file from a folder')

    sys.exit(0)

if sys.argv[1] == '-c' or sys.argv[1] == '--count':
    print("counted ", argvlen-2, " argument"+"s" if argvlen-2 > 1 else "")
    sys.exit(0)

if (sys.argv[1] == '-p' or sys.argv[1] == '--play') and argvlen >= 3:
    play_sound(sys.argv[2])
    sys.exit(0)

if (sys.argv[1] == '-ls' or sys.argv[1] == '--layersounds') and argvlen >= 3:
    play_sounds_at_once(sys.argv[2:])
    sys.exit(0)

if (sys.argv[1] == '-a' or sys.argv[1] == '--all'):
    directory = "sounds"
    files = os.listdir(directory)
    for file in files:
        print(file)
    sys.exit(0)

if (sys.argv[1] == '-r' or sys.argv[1] == '--rename'):
    rename_sound_file(sys.argv[2], sys.argv[3])
    sys.exit(0)

if (sys.argv[1] == '-cf' or sys.argv[1] == '--createfolder') and argvlen >= 4:
    folder_name = sys.argv[2]
    file_paths = sys.argv[3:]
    create_folder(folder_name, file_paths)
    sys.exit(0)

if (sys.argv[1] == '-df' or sys.argv[1] == '--deletefolder') and argvlen >= 3:
    folder_name = sys.argv[2]
    delete_folder(folder_name)
    sys.exit(0)

if (sys.argv[1] == '-rm' or sys.argv[1] == '--removefile') and argvlen >= 4:
    folder_name = sys.argv[2]
    file_name = sys.argv[3]
    delete_file(folder_name, file_name)
    sys.exit(0)

print(sys.argv[0], "error, unexpected arguments ", sys.argv[1:], file=sys.stderr)
sys.exit(1)
