from functions import get_todos,write_todos
#or u could use import functions and then use functions.get_todos()
import time
row = f"Today is {time.strftime("%b %d, %Y.")}The time now is {time.strftime("%H:%M:%S")}"
print(row)
while True:
    #you could use a multiline string here
    #like this
    text = """
    hi 
    hello
    bye 
    """
    user_prompt = input("Type Add or Show or Edit or Complete or Exit: ").strip()
    command = user_prompt.split()[0].lower()  # Extract command and convert to lowercase

    if (user_prompt.startswith('add')) or (user_prompt.startswith('Add')):
        todo = user_prompt[4:].strip()
        if todo:
            todo = todo.title()
            todos=get_todos() #functions.get_todos()

            todos.append(todo + '\n')  # Always add with newline
            write_todos('todos.txt',todos)
        else:
            print("No task provided. Please try again.")

    elif command == 'show':
        todos = get_todos()

        todos = [todo.strip('\n') for todo in todos if todo.strip()]  # Clean up tasks
        if todos:
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        else:
            print("No tasks found.")

    elif command == 'edit':
        try:
            number = int(user_prompt.split()[1])
            todos = get_todos()

            if 1 <= number <= len(todos):  # Validate range
                todo = input("Please enter your task: ").strip().title()
                if todo:
                    todos[number - 1] = todo + '\n'
                    write_todos('todos.txt', todos)

                    print(f"Task {number} updated successfully.")
                else:
                    print("Invalid task. Please try again.")
            else:
                print(f"Task number {number} is out of range.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")
            continue

    elif command == 'complete':
        try:
            number = int(user_prompt.split()[1])  # Extract task number
            todos = get_todos()

            # Validate range
            if 1 <= number <= len(todos):
                complete_item = todos.pop(number - 1).strip('\n')  # Remove the task
                print(f"'{complete_item}' is completed. The entry at {number} has been removed.")

                # Write updated list back to file
                write_todos('todos.txt', todos)


            else:
                print(f"Task number {number} is out of range.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")
            continue

    elif command == 'exit':
        break
    else:
        print("Incorrect command.")
