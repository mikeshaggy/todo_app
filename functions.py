import os
import getch

FILE_PATH = "todos.txt"

def get_todos(file_path=FILE_PATH):
    """
    Function reads the text file and returns list of tasks to do
    """
    with open(file_path, "r") as f:
        result = f.readlines()
    return result


def update_todos(content, file_path=FILE_PATH):
    """
    Function overwrites the text file with new list of tasks to do
    """
    with open(file_path, "w") as f:
        f.writelines(content)

def terminal_clearing():
    """
    Function asks the user for an input and then clears the terminal window
    """
    print("\nPress [Enter] to continue...")
    getch.getch()
    os.system("clear") # unix systems
    # os.system("cls") # windows system
