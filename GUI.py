import functions

import FreeSimpleGUI
label = FreeSimpleGUI.Text("Type in a to-do")
input_box = FreeSimpleGUI.InputText(tooltip="Enter To-do: ")
add_button = FreeSimpleGUI.Button("Add")
window=FreeSimpleGUI.Window('My To-do App',layout=[[label],[input_box,add_button]])#an instance of the Window type stored in the variable, window
#one single [] means one single row
#thAT'S WHY WE got type in a todo and the textbox in the same line
#if we placed them in a seperate sq bracket , then they would be in different rows
#window=FreeSimpleGUI.Window('My To-do App',layout=[[label],[input_box]])#an instance of the Window type stored in the variable, window

window.read()

window.close()