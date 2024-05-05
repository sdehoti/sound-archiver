import os 
from datetime import datetime

class Sort:
    """
    Sort class provides methods to sort files in a directory based on different criteria.
    """
    def __init__(self, path):
        """
        Initializes the Sort object with the specified directory path.

        Parameters:
            path (str): The path of the directory to sort.

        Returns:
            None

        Raises:
            None
        """
        self.path = path
        try:
            os.chdir(path)
        except FileNotFoundError:
            print("The specified path does not exist.")

    def sort_size(self):
        """
        Sorts the files in the current directory based on their sizes.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        files = os.listdir()
        files.sort(key = os.path.getsize)
        for file in files:
            print(file)
        input("Press enter to continue...")

    def sort_name(self):
        """
        Sorts the files in the current directory alphabetically by name.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        files = os.listdir()
        files.sort()
        for file in files:
            print(file)
        input("Press enter to continue...")
    
    def sort_date_created(self):
        """
        Sorts the files in the current directory based on their creation time.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
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

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        files = os.listdir()
        files.sort(key = os.path.getmtime)
        for file in files:
            timestamp = os.path.getmtime(file)
            print(f"{file} : {datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
        input("Press enter to continue...")

    def sort_type(self, choice):
        """
        Sorts the files in the current directory based on the specified criteria.

        Parameters:
            choice (str): The sorting criteria. 
                          'sortz' for sorting by size,
                          'sortc' for sorting by creation date,
                          'sortm' for sorting by modification date,
                          'sorta' for sorting alphabetically by name.

        Returns:
            None

        Raises:
            KeyError: If an invalid sorting choice is provided.
        """
        methods = {
            'sortz': self.sort_size,
            'sortc': self.sort_date_created,
            'sortm': self.sort_date_modified,
            'sorta': self.sort_name}
        return methods[choice]()