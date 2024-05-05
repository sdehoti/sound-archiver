import os

class Menu:
    """
    A class to display a menu and handle user choices for the Sound Archive Management System.
    """

    def display(self):
        """
        Display the main menu options.
        """
        print("Welcome to the Sound Archive Management System\n.Your current working directory is: ", os.getcwd())
        print("-p : Play one or more .wav files")
        print("-ps : Play multiple .wav files simultaneously")
        print("-pr : Play a .wav file in reverse")
        print("-pseg : Play a randomly chosen segment of a .wav file")
        print("-l : List all available files in the directory")
        print("-add : Add files to existing folder")
        print("-cr : Create a folder and move .wav files into it")
        print("-rm : Remove a specific file from a folder")
        print("-rm dir : Delete a folder")
        print("-rn : Rename a sound file")
        print("-rn dir :  Rename a sound folder")
        print("-zip : Compress selected sounds files into a .zip file")
        print("-sortz : Sort files by size")
        print("-sorta : Sort files alphabetically")
        print("-sortc : Sort files by date created")
        print("-sortm : Sort files by date modified")
        print("-exit : Exit\n")

    def get_choice(self):
        """
        Get user choice from the menu.

        Returns:
            str: User's choice.
        """
        return input("Choose one of the listed options: ")

    def clear_screen(self):
        """
        Clear the terminal screen.
        """
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')
