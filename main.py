import sys
from file_manager import FileManager
from menu import Menu
from sound_player import SoundPlayer
from share_file import ShareFiles
import sorting
import os


def main():
    default_path = os.getcwd()  # the audio library should be in the same directory as the main.py file
    file_manager = FileManager("sound_archive.db")
    menu = Menu()
    sound_player = SoundPlayer("sound_archive.db")  # Pass the db_file argument here
    share_file = ShareFiles()

    while True:
        os.chdir(default_path)  # Reset the working directory to the default path.
        menu.clear_screen()
        menu.display()
        choice = menu.get_choice()

        if choice == 'p':
            files = file_manager.get_audio_files()
            file_paths = [file[2] for file in files]  # Extract file paths from database records
            sound_player.play_files(file_paths)
        if choice == 'ps':
            files = file_manager.get_audio_files()
            sound_player.play_files_simultaneously([file[2] for file in files])
        if choice == 'l':
            folders = file_manager.list_folders()
            folder_choice = input("Enter the number of the folder: ")
            try:
                selected_folder = folders[int(folder_choice) - 1]
                files = file_manager.get_audio_files(folder=selected_folder)
                for file in files:
                    print(file[1])  # Print each file name
            except IndexError:
                print("Invalid folder choice. Please try again.")

        if choice == 'add':
            folder_name = input("Enter the folder name: ")
            files = input("Enter the file path(s) separated by spaces:").split()
            file_manager.add_files_to_folder(folder_name, files)

        if choice == 'cr':
            folder_name = input("Enter the folder name:")
            files = input("Enter the file path(s) separated by spaces:").split()
            file_manager.create_folder(folder_name, files)

        if choice == 'rm':
            folder_name = input("Enter the folder name:")
            file_name = input("Enter the file name:")
            file_manager.remove_file_from_folder(folder_name, file_name)

        if choice == 'rm dir':
            folder_name = input("Enter the folder name:")
            file_manager.delete_folder(folder_name)

        if choice == 'rn':
            current_name = input("Enter the current file name:")
            new_name = input("Enter the new file name:")
            file_manager.rename_sound_file(current_name, new_name)

        if choice == 'rn dir':
            current_name = input("Enter the current folder name:")
            new_name = input("Enter the new folder name:")
            file_manager.rename_folder(current_name, new_name)

        if choice == 'zip':
            filenames = input(
                "Enter the Folder path to be zipped or seperate file path(s), separated by spaces, of the audios:")
            share_file.zip_files(filenames.split())

        if choice[0:4] == "sort":
            path = input("Enter the path of the folder to sort:")
            sort = sorting.Sort(path)
            sort.sort_type(choice)

        if choice == 'pseg':
            file_path = input("Enter the file path:")
            sound_player.play_sound_segment(file_path)

        if choice == 'pr':
            file_path = input("Enter the file path:")
            sound_player.play_reverse(file_path)

        if choice == 'exit':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


