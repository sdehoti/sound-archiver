import os
import sys
import shutil
from simpleaudio_test import play_sound, play_sounds_at_once, rename_sound_file

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def display_menu():
    clear_screen()
    print("Welcome to the Sound Archive Management System\n")
    print("1. Play one or more .wav files")
    print("2. Play multiple .wav files simultaneously")
    print("3. List all available files in the directory")
    print("4. Create a folder and move .wav files into it")
    print("5. Delete a folder")
    print("6. Remove a specific file from a folder")
    print("7. Rename a sound folder")
    print("8. Add files to existing folder")
    print("9. Exit\n")

def play_files(file_paths):
    for file in file_paths:
        play_sound(file)

def play_files_simultaneously(file_paths):
    play_sounds_at_once(file_paths)

def list_available_files(folder_name):
    print(f"Available files in the '{folder_name}' folder:")
    directory = folder_name  # Assuming folder_name is the path to the user-created folder
    files = os.listdir(directory)
    for file in files:
        print(file)  # Print each file individually

    input("Press Enter to continue...")

def list_available_folders():
    print("Available folders:")
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
    for i, folder in enumerate(folders, 1):
        print(f"{i}. {folder}")
    return folders


def create_folder(folder_name, file_paths):
    try:
        os.mkdir(folder_name)
        for file_path in file_paths:
            shutil.copy(file_path, os.path.join(folder_name, os.path.basename(file_path)))
        print(f"Folder '{folder_name}' created successfully and files copied.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def add_files_to_folder(folder_name, file_paths):
    try:
        for file_path in file_paths:
            shutil.copy(file_path, os.path.join(folder_name, os.path.basename(file_path)))
        print(f"Files duplicated into folder '{folder_name}' successfully.")
    except FileNotFoundError:
        print(f"Folder '{folder_name}' not found.")
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

def remove_file_from_folder(folder_name, file_name):
    file_path = os.path.join(folder_name, file_name)
    try:
        os.remove(file_path)
        print(f"File '{file_name}' deleted successfully from folder '{folder_name}'.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found in folder '{folder_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def rename_sound(current_name, new_name):
    try:
        os.rename(current_name, new_name)
        print(f"File '{current_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{current_name}' not found.")
    except FileExistsError:
        print(f"File '{new_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            play_files(files)
        elif choice == '2':
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            play_files_simultaneously(files)
        elif choice == '3':
            folders = list_available_folders()
            folder_choice = input("Enter the number of the folder: ")
            try:
                selected_folder = folders[int(folder_choice) - 1]
                list_available_files(selected_folder)
            except IndexError:
                print("Invalid folder choice. Please try again.")
        elif choice == '4':
            print("Enter the folder name:")
            folder_name = input()
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            create_folder(folder_name, files)
        elif choice == '5':
            print("Enter the folder name:")
            folder_name = input()
            delete_folder(folder_name)
        elif choice == '6':
            print("Enter the folder name:")
            folder_name = input()
            print("Enter the file name:")
            file_name = input()
            remove_file_from_folder(folder_name, file_name)
        elif choice == '7':
            print("Enter the current folder name:")
            current_name = input()
            print("Enter the new folder name:")
            new_name = input()
            rename_sound(current_name, new_name)
        elif choice == '8':
            folder_name = input("Enter the folder name: ")
            print("Enter the file path(s) separated by spaces:")
            files = input().split()
            add_files_to_folder(folder_name, files)
        elif choice == '9':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
