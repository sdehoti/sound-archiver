import os

class Menu:
    def display(self):
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

    def get_choice(self):
        return input("Enter your choice: ")

    def clear_screen(self):
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')