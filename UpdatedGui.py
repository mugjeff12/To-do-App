import functions
import FreeSimpleGUI
import time
import os

# Ensure todos.txt exists
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

# Set theme and GUI layout
FreeSimpleGUI.theme("DarkBlack1")
clock = FreeSimpleGUI.Text(key='clock')
label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter To-do: ", key='todo')
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                                 enable_events=True, size=[45, 10])
edit_button = FreeSimpleGUI.Button('Edit')
complete_button = FreeSimpleGUI.Button('Complete')
exit_button = FreeSimpleGUI.Button('Exit')

window = FreeSimpleGUI.Window('My To-do App',
                              layout=[[clock], [label],
                                      [input_box, add_button],
                                      [list_box, edit_button, complete_button],
                                      [exit_button]],
                              font=('Helvetica', 20))

# Event loop
while True:
    event, values = window.read(timeout=200)

    # Handle window close or exit
    if event in (FreeSimpleGUI.WINDOW_CLOSED, "Exit"):
        break

    # Update the clock
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    print(event)  # Debugging: Print the event
    print(values)  # Debugging: Print the values dictionary

    # Handle events
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]  # Selected item in the listbox
                todo_to_add = values["todo"]  # New text from the input box
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = todo_to_add + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                FreeSimpleGUI.popup("Please select an item first.", font=('TimesNewRoman', '20'))

        case "todos":
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                FreeSimpleGUI.popup("No item selected in the list.", font=('TimesNewRoman', '20'))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                FreeSimpleGUI.popup("Please select an item to mark as complete.", font=('TimesNewRoman', '20'))

# Close the window
window.close()
