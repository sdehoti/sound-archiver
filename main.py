import sys
from file_manager import FileManager
from menu import Menu
from sound_player import SoundPlayer
from share_file import ShareFiles

def main():
    file_manager = FileManager()
    menu = Menu()
    sound_player = SoundPlayer()
    share_file = ShareFiles()

    while True:
        menu.clear_screen()
        menu.display()
        choice = menu.get_choice()

        if choice == 'p':
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            sound_player.play_files(files)
        if choice == 'ps':
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            sound_player.play_files_simultaneously(files)
        if choice == 'l':
            folders = file_manager.list_folders()
            folder_choice = input("Enter the number of the folder: ")
            try:
                selected_folder = folders[int(folder_choice) - 1]
                file_manager.list_files(selected_folder)
            except IndexError:
                print("Invalid folder choice. Please try again.")
        if choice == 'add':
            folder_name = input("Enter the folder name: ")
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            file_manager.add_files_to_folder(folder_name, files)
        if choice == 'cr':
            print("Enter the folder name:")
            folder_name = input()
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            file_manager.create_folder(folder_name, files)
        if choice == 'rm':
            print("Enter the folder name:")
            folder_name = input()
            print("Enter the file name:")
            file_name = input()
            file_manager.remove_file_from_folder(folder_name, file_name)
        if choice == 'rm dir':
            print("Enter the folder name:")
            folder_name = input()
            file_manager.delete_folder(folder_name)
        if choice == 'rn':
            print("Enter the current file name:")
            current_name = input()
            print("Enter the new file name:")
            new_name = input()
            file_manager.rename_sound_file(current_name, new_name)
        if choice == 'rn dir':
            print("Enter the current folder name:")
            current_name = input()
            print("Enter the new folder name:")
            new_name = input()
            file_manager.rename_folder(current_name, new_name)
        if choice == 'zip':
            print("Enter the sound file names:")
            filenames = input()
            share_file.zip_files(filenames)
        if choice == 'exit':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

