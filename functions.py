FILE_PATH='todos.txt'

def get_todos(filepath = FILE_PATH): # when i set filepath to todos.txt i make it a default parameter
    """Reads a text file
    and returns the items in the list
    """
    with open(filepath, 'r') as file:

        todos=file.readlines()
    return todos

def write_todos(todos_arg,filepath = FILE_PATH):
    """Write the todo items list in the text file"""
    #always make sure non default parameter is before default parameter
    # i wont use it but the function definition will look like
    #def write_todos(tools_arg,filepath='todos.txt')
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
print(__name__)
if __name__ =="__main__":
    print('e')