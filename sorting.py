import os 
from datetime import datetime

class Sort:
   
    def __init__(self, path):
        self.path = path
        try:
            os.chdir(path)
        except FileNotFoundError:
            print("The specified path does not exist.")

    def sort_size(self):
        files = os.listdir()
        files.sort(key = os.path.getsize)
        for file in files:
            print(file)
        input("Press enter to continue...")

    def sort_name(self):
        files = os.listdir()
        files.sort()
        for file in files:
            print(file)
        input("Press enter to continue...")
    
    def sort_date_created(self):
        """
        Sorts the files in the current directory based on their creation time.
        """
        files = os.listdir()
        files.sort(key = os.path.getctime)
        for file in files:
            timestamp = os.path.getctime(file)
            print(f"{file} : {datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
        input("Press enter to continue...")

    def sort_date_modified(self):
        """
        Sorts the files in the current directory based on their modification time.
        """
        files = os.listdir()
        files.sort(key = os.path.getmtime)
        for file in files:
            timestamp = os.path.getmtime(file)
            print(f"{file} : {datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
        input("Press enter to continue...")


