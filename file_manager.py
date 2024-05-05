import os
import shutil


class FileManager:
    """
    A class to manage file and folder operations within a sound archive project.
    """

    def list_files(self, folder_name):
        """
        Lists all files in the specified folder.

        Args:
            folder_name (str): The name of the folder to list files from.
        """
        print(f"Available files in the '{folder_name}' folder:")
        files = os.listdir(folder_name)
        for file in files:
            print(file)  # Print each file individually
        input("Press Enter to continue...")

    def list_folders(self):
        """
        Lists all available folders in the current directory.
        """
        print("Available folders:")
        folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
        for i, folder in enumerate(folders, 1):
            print(f"{i}. {folder}")
        return folders

    def add_files_to_folder(self, folder_name, file_paths):
        """
        Adds files to a specified folder by copying them from their current locations.

        Args:
            folder_name (str): The name of the folder to add files to.
            file_paths (list): List of file paths to be added to the folder.
        """
        try:
            for file_path in file_paths:
                shutil.copy(file_path, os.path.join(folder_name, os.path.basename(file_path)))
            print(f"Files duplicated into folder '{folder_name}' successfully.")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def create_folder(self, folder_name, file_paths):
        """
        Creates a new folder and copies files into it.

        Args:
            folder_name (str): The name of the new folder to be created.
            file_paths (list): List of file paths to be copied into the new folder.
        """
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
        """
        Removes a specific file from a folder.

        Args:
            folder_name (str): The name of the folder containing the file.
            file_name (str): The name of the file to be removed.
        """
        file_path = os.path.join(folder_name, file_name)
        try:
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully from folder '{folder_name}'.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found in folder '{folder_name}'.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def delete_folder(self, folder_name):
        """
        Deletes a specified folder and all its contents.

        Args:
            folder_name (str): The name of the folder to be deleted.
        """
        try:
            shutil.rmtree(folder_name)
            print(f"Folder '{folder_name}' deleted successfully.")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def rename_sound_file(current_name, new_name):
        """
        Renames a sound file.

        Args:
            current_name (str): The current name of the file.
            new_name (str): The new name for the file.
        """
        try:
            os.rename(current_name, new_name)
            print(f"File '{current_name}' renamed to '{new_name}' successfully.")
        except FileNotFoundError:
            print(f"File '{current_name}' not found.")
        except FileExistsError:
            print(f"File '{new_name}' already exists.")

    def rename_folder(self, current_name, new_name):
        """
        Renames a folder.

        Args:
            current_name (str): The current name of the folder.
            new_name (str): The new name for the folder.
        """
        try:
            os.rename(current_name, new_name)
            print(f"Folder '{current_name}' renamed to '{new_name}' successfully.")
        except FileNotFoundError:
            print(f"Folder '{current_name}' not found.")
        except FileExistsError:
            print(f"Folder '{new_name}' already exists.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

