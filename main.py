import sys
import os
from file_manager import FileManager
from menu import Menu
from sound_player import SoundPlayer
from share_file import ShareFiles
import sorting


def main():
    """
    Main function to run the sound archive project.
    """
    # Get the default path where the audio library should be located.
    default_path = os.getcwd()

    # Initialize necessary objects
    file_manager = FileManager()
    menu = Menu()
    sound_player = SoundPlayer()
    share_file = ShareFiles()

    # Main program loop
    while True:
        # Reset the working directory to the default path.
        os.chdir(default_path)

        # Display menu options and get user choice
        menu.clear_screen()
        menu.display()
        choice = menu.get_choice()

        # Perform actions based on user choice
        if choice == 'p':
            # Play files sequentially
            files = input("Enter the file path(s) separated by spaces:").split()
            sound_player.play_files(files)
        if choice == 'ps':
            # Play files simultaneously
            files = input("Enter the file path(s) separated by spaces:").split()
            sound_player.play_files_simultaneously(files)
        if choice == 'l':
            # List files in a selected folder
            folders = file_manager.list_folders()
            folder_choice = input("Enter the number of the folder: ")
            try:
                selected_folder = folders[int(folder_choice) - 1]
                file_manager.list_files(selected_folder)
            except IndexError:
                print("Invalid folder choice. Please try again.")

        if choice == 'add':
            # Add files to a folder
            folder_name = input("Enter the folder name: ")
            files = input("Enter the file path(s) separated by spaces:").split()
            file_manager.add_files_to_folder(folder_name, files)

        if choice == 'cr':
            # Create a new folder and copy files into it
            folder_name = input("Enter the folder name:")
            files = input("Enter the file path(s) separated by spaces:").split()
            file_manager.create_folder(folder_name, files)

        if choice == 'rm':
            # Remove a file from a folder
            folder_name = input("Enter the folder name:")
            file_name = input("Enter the file name:")
            file_manager.remove_file_from_folder(folder_name, file_name)

        if choice == 'rm dir':
            # Delete a folder
            folder_name = input("Enter the folder name:")
            file_manager.delete_folder(folder_name)

        if choice == 'rn':
            # Rename a file
            current_name = input("Enter the current file name:")
            new_name = input("Enter the new file name:")
            file_manager.rename_sound_file(current_name, new_name)

        if choice == 'rn dir':
            # Rename a folder
            current_name = input("Enter the current folder name:")
            new_name = input("Enter the new folder name:")
            file_manager.rename_folder(current_name, new_name)

        if choice == 'zip':
            # Zip files
            filenames = input(
                "Enter the Folder path to be zipped or seperate file path(s), separated by spaces, of the audios:")
            share_file.zip_files(filenames.split())

        if choice[0:4] == "sort":
            # Sort files in a folder
            path = input("Enter the path of the folder to sort:")
            sort = sorting.Sort(path)
            sort.sort_type(choice)

        if choice == 'pseg':
            # Play a segment of a sound file
            file_path = input("Enter the file path:")
            sound_player.play_sound_segment(file_path)

        if choice == 'pr':
            # Play a sound file in reverse
            file_path = input("Enter the file path:")
            sound_player.play_reverse(file_path)

        if choice == 'exit':
            # Exit the program
            print("Exiting...")
            sys.exit(0)
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
