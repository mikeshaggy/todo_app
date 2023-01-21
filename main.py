import functions as f

def main():
    while True:
        user_choice = input("Type add, show, edit, complete or exit: ").strip().lower()
        
        if user_choice.startswith("add"): # adding a new task to the list
            todo = user_choice[4:]
            todos = f.get_todos()
            todos.append(todo.capitalize() + "\n")
            f.update_todos(todos)
            print(f"\nTask [{todo}] has been succesfully added\n")
            f.terminal_clearing()
        elif user_choice.startswith("show"): # displaying the list of tasks
            todos = f.get_todos()
            if not todos:
                print("\nThe list is empty!\n")
            else:
                for index, item in enumerate(todos):
                    print(f"{index + 1}. {item}", end="")
            f.terminal_clearing()
        elif user_choice.startswith("edit"): # editting specific task
            try:
                number = int(user_choice[5:]) - 1
                new_todo = input("Enter the new tasks: ")
                todos = f.get_todos()
                todos[number] = new_todo.capitalize() + "\n"
                f.update_todos(todos)
                print(f"\nTask #{number} has been succesfully edited\n")
                f.terminal_clearing()
            except ValueError:
                print("\nERROR: [edit] command needs to be followed with the number of item to edit\n")
            except IndexError:
                print("\nERROR: There is no item with that number\n")
        elif user_choice.startswith("complete"): # completing a task
            try:
                number = int(user_choice[9:]) - 1
                todos = f.get_todos()
                todos.pop(number)
                f.update_todos(todos)
                print(f"\nTask #{number + 1} has been completed\n")
                f.terminal_clearing()
            except ValueError:
                print("\nERROR: [complete] command needs to be followed with the number of item to edit\n")
            except IndexError:
                print("\nERROR: There is no item with that number\n")
        elif user_choice.startswith("exit"): # quitting the program
            break
        else:
            print("ERROR: Command not found")
    print("Quitting the program...")

if __name__ == "__main__":
    main()