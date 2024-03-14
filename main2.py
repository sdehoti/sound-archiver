import sys
from file_manager import FileManager
from menu import Menu
from sound_player import SoundPlayer

def main():
    file_manager = FileManager()
    menu = Menu()
    sound_player = SoundPlayer()

    while True:
        menu.clear_screen()
        menu.display()
        choice = menu.get_choice()

        if choice == '1':
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            sound_player.play_files(files)
        elif choice == '2':
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            sound_player.play_files_simultaneously(files)
        elif choice == '3':
            folders = file_manager.list_folders()
            folder_choice = input("Enter the number of the folder: ")
            try:
                selected_folder = folders[int(folder_choice) - 1]
                file_manager.list_files(selected_folder)
            except IndexError:
                print("Invalid folder choice. Please try again.")
        elif choice == '4':
            print("Enter the folder name:")
            folder_name = input()
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            file_manager.create_folder(folder_name, files)
        elif choice == '5':
            print("Enter the folder name:")
            folder_name = input()
            file_manager.delete_folder(folder_name)
        elif choice == '6':
            print("Enter the folder name:")
            folder_name = input()
            print("Enter the file name:")
            file_name = input()
            file_manager.remove_file_from_folder(folder_name, file_name)
        elif choice == '7':
            print("Enter the current folder name:")
            current_name = input()
            print("Enter the new folder name:")
            new_name = input()
            file_manager.rename_folder(current_name, new_name)
        elif choice == '8':
            folder_name = input("Enter the folder name: ")
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            file_manager.add_files_to_folder(folder_name, files)
        elif choice == '9':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

