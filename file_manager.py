import os
import shutil

class FileManager:
    def list_files(self, folder_name):
        print(f"Available files in the '{folder_name}' folder:")
        files = os.listdir(folder_name)
        for file in files:
            print(file)  # Print each file individually
        input("Press Enter to continue...")

    def list_folders(self):
        print("Available folders:")
        folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
        for i, folder in enumerate(folders, 1):
            print(f"{i}. {folder}")
        return folders
    
    def add_files_to_folder(self, folder_name, file_paths):
        try:
            for file_path in file_paths:
                shutil.copy(file_path, os.path.join(folder_name, os.path.basename(file_path)))
            print(f"Files duplicated into folder '{folder_name}' successfully.")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def create_folder(self, folder_name, file_paths):
        try:
            os.mkdir(folder_name)
            for file_path in file_paths:
                shutil.copy(file_path, os.path.join(folder_name, os.path.basename(file_path)))
            print(f"Folder '{folder_name}' created successfully and files copied.")
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def remove_file_from_folder(self, folder_name, file_name):
        file_path = os.path.join(folder_name, file_name)
        try:
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully from folder '{folder_name}'.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found in folder '{folder_name}'.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def delete_folder(self, folder_name):
        try:
            shutil.rmtree(folder_name)
            print(f"Folder '{folder_name}' deleted successfully.")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def rename_sound_file(current_name, new_name):
        try:
            os.rename(current_name, new_name)
            print(f"File '{current_name}' renamed to '{new_name}' successfully.")
        except FileNotFoundError:
            print(f"File '{current_name}' not found.")
        except FileExistsError:
            print(f"File '{new_name}' already exists.")

    def rename_folder(self, current_name, new_name):
        try:
            os.rename(current_name, new_name)
            print(f"Folder '{current_name}' renamed to '{new_name}' successfully.")
        except FileNotFoundError:
            print(f"Folder '{current_name}' not found.")
        except FileExistsError:
            print(f"Folder '{new_name}' already exists.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
