import os
import shutil
import sqlite3

class FileManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_audio_files_table()

    def create_audio_files_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS AudioFiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                path TEXT
            )
        """)
        self.conn.commit()

    def list_files(self, folder_name):
        try:
            self.cursor.execute("SELECT name FROM AudioFiles WHERE path = ?", (folder_name,))
            files = self.cursor.fetchall()
            if files:
                print(f"Available files in the '{folder_name}' folder:")
                for file in files:
                    print(file[0])  # Print each file individually
            else:
                print(f"No files found in '{folder_name}' folder.")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def list_folders(self):
        try:
            self.cursor.execute("SELECT DISTINCT path FROM AudioFiles WHERE path != ''")
            folders = self.cursor.fetchall()
            if folders:
                print("Available folders:")
                for i, folder in enumerate(folders, 1):
                    print(f"{i}. {folder[0]}")
                return [folder[0] for folder in folders]
            else:
                print("No folders found.")
                return []
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def add_files_to_folder(self, folder_name, file_paths):
        try:
            for file_path in file_paths:
                # Insert file information into the database
                self.cursor.execute("INSERT INTO AudioFiles (name, path) VALUES (?, ?)", (os.path.basename(file_path), folder_name))
            self.conn.commit()
            print(f"Files added to folder '{folder_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def create_folder(self, folder_name, file_paths):
        try:
            # Create folder in the database
            self.cursor.execute("INSERT INTO AudioFiles (name, path) VALUES (?, '')", (folder_name,))
            self.conn.commit()
            print(f"Folder '{folder_name}' created successfully.")
            # Add files to the folder in the database
            self.add_files_to_folder(folder_name, file_paths)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def remove_file_from_folder(self, folder_name, file_name):
        try:
            self.cursor.execute("DELETE FROM AudioFiles WHERE name = ? AND path = ?", (file_name, folder_name))
            self.conn.commit()
            print(f"File '{file_name}' deleted successfully from folder '{folder_name}'.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def delete_folder(self, folder_name):
        try:
            self.cursor.execute("DELETE FROM AudioFiles WHERE path = ?", (folder_name,))
            self.conn.commit()
            print(f"Folder '{folder_name}' deleted successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def rename_sound_file(self, folder_name, current_name, new_name):
        try:
            self.cursor.execute("UPDATE AudioFiles SET name = ? WHERE name = ? AND path = ?",
                                (new_name, current_name, folder_name))
            self.conn.commit()
            print(f"File '{current_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def rename_folder(self, current_name, new_name):
        try:
            self.cursor.execute("UPDATE AudioFiles SET path = ? WHERE path = ?", (new_name, current_name))
            self.conn.commit()
            print(f"Folder '{current_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_audio_files(self, folder=None):
        try:
            if folder:
                self.cursor.execute("SELECT * FROM AudioFiles WHERE path = ?", (folder,))
            else:
                self.cursor.execute("SELECT * FROM AudioFiles")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def __del__(self):
        self.conn.close()

