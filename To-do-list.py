

print('Welcome to TODO-6X by 6X Company')
tasks=[]
done=[]

while True:
    for i in range(len(tasks)):
        if tasks[i]  in done:
            print(i+1,'.', tasks[i], '(Done)')
        else:
            print(i+1,'.', tasks[i], '(Not Done Yet)')
    operation=input('"+":Add a Task\n"*"edit a Task\n"quit":Quit the app\nYour Operation here:')
    while operation=='*' and tasks==[]:
        if operation=='*':
            operation=input('Your Tasks list is Empty, Please ADD Tasks first\n"+":Add a Task\n"*"edit a Task\nYour Operation here:')
    if operation=='+':
        tasks.append(input('Add a Task To Do:'))
    elif operation=='*':
        index= int(input('please choose your Task Index'))
        edit=input('"-":Delete a Task\n"c"Complete a Task\nYour Operation here:')
        if edit=='-':
            del tasks[index-1]
            print('Your Operation is Done')
        if edit=='c':
            done.append(tasks[i-1])
            print('Your Operation is Done')
    elif operation=='quit':
        print('Good bye, From 6X Company')
        break
        
