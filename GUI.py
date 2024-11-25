
import functions

import FreeSimpleGUI
label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter To-do: ", key ='todo')
add_button = FreeSimpleGUI.Button("Add")

list_box = FreeSimpleGUI.Listbox(values=functions.get_todos(), key='todos'
                                 ,enable_events = True,size=[45,10])
edit_button = FreeSimpleGUI.Button('Edit')
complete_button = FreeSimpleGUI.Button('Complete')
exit_button=FreeSimpleGUI.Button('Exit')
window=FreeSimpleGUI.Window('My To-do App',
                            layout=[[label]
                                ,[input_box,add_button],
                                [list_box,edit_button,complete_button],
                                    [exit_button]],
                            font=('Helvetica',20))
#an instance of the Window type stored in the variable, window
#one single [] means one single row
#thAT'S WHY WE got type in a todo and the textbox in the same line
#if we placed them in a seperate sq bracket , then they would be in different rows
#window=FreeSimpleGUI.Window('My To-do App',layout=[[label],[input_box]])#an instance of the Window type stored in the variable, window
while True:
    event,values=window.read()
    print(event)#add
    print(values)#{'todo': hi} this is a dictionary , extract using values['todo']
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] +'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit =  values["todos"][0]
            todo_to_add = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index]=todo_to_add + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        #case 'todos':
        #window['todo'].update(value=values['todos'][0])
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            #number = todos.index(todo_to_complete)
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Exit":
            break

        case FreeSimpleGUI.WINDOW_CLOSED:
            break

window.close()