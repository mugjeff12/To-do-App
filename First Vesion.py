#user_text = input('To Do List: ')
#print(user_text)
from multiprocessing.spawn import set_executable
text = 'show'
#print(text[1:]) # should be bcde
#print(text[1:2])#should be b
#underlying logic :  right number is inclusive , left number is exclusive , everything in between
#fdsfs
while True:
    #ardit wanted to introduce list slicing
    #so he wanted the user action to be add Fix the computer
    #but i feel like thats not really intuitive
    #but here is the code
    user_prompt = input("Type Add or Show or Edit or Complete or Exit: ")
    user_prompt = user_prompt.strip()
    #print(todo.capitalize())
    #print(todo.title())

    if 'Add' in user_prompt:
        #todo = input("Please enter your task: ") +"\n"
        todo = user_prompt[4:]
        todo = todo.title()
            #file = open('todos.txt','r')
            #todos = file.readlines()
            #file.close()
            #This closes the file
        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo+'\n')
        with open('todos.txt','w') as file:
            file.writelines(todos)


            #file = open('todos.txt','w') #w overwrites the file
            #file.writelines(todos)
            #file.close()

            #newtodos =[item.strip('\n') for item in todos])
    elif 'Show' in user_prompt:
        # | = bitwise OR operator
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        result = user_prompt[5:]

        if result == '':
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                # if u want python to ignore special characters do this
                # in case of /t , /a
                # file = open(r"D:\Books which i must give a read\Books.txt",'r')
                print(row)
        else:
            print("The result is not an empty string:", result)
            row = f"{result}-{todos[int(result)-1]}"

            print(row,end='')

            #for i in range(len(todos)):
                #print(todos[i])
    elif "Edit" in user_prompt:
        number = int(user_prompt[5:])
        number = number -1 #index starts from 0
        todo = input("Please enter your task: ")
        todo = todo.title()
        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos[number] = todo+ "\n"
        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif "Complete" in user_prompt:
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        number =int(int(user_prompt[9:]))
        complete_item = todos[number-1].strip('\n')
        #we have two options here , pop or remove
        row1=f"{complete_item} is completed. The entry at {number} will be removed."
        print(row1)
        todos.pop(number-1)
        with open('todos.txt','w') as file:
            file.writelines(todos)


    elif 'Exit' in user_prompt:
        break
    else:
        print("Incorrect command")
print("Have a nice day!")

#useful stuff to sort a list in ascending order you can use list.sort()
#in order to reverse the order ie descending use list.sort(reverse=True)


    #todos is a variable which is an object called a list , you can carry out methods on objects which are like
    #functions
#todo2 = input(user_prompt)
#todos = [todo1 , todo2]
#print(todos)
#print(type(user_prompt))
#print(type(todos))

#for index , item in todos:
#print(index, item)# this basically also gives the index and the item
