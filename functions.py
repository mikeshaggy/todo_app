import os
import getch

def get_todos(file_name="todos.txt"):
    """
    Function reads the text file and returns list of tasks to do
    """
    with open(file_name, "r") as f:
        result = f.readlines()
    return result


def update_todos(content, file_name="todos.txt"):
    """
    Function overwrites the text file with new list of tasks to do
    """
    with open(file_name, "w") as f:
        f.writelines(content)

def terminal_clearing():
    """
    Function asks the user for an input and then clears the terminal window
    """
    print("\nPress [Enter] to continue...")
    getch.getch()
    os.system("clear") # unix systems
    # os.system("cls") # windows system
