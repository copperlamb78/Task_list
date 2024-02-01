import os

def listing(tasks):
    if not tasks:
        clear_screen()
        print('Nothing to listing!')
        return
    clear_screen()
    print('TASKS')
    print('')
    for list in tasks:
        print(list)
    print('')

def undo(tasks, undo_tasks):
    if not tasks:
        clear_screen()
        print('Nothing to undo!')
        return 
    undo_task = tasks.pop()
    undo_tasks.append(undo_task)
    listing(list_of_task)   

def redo(tasks, undo_tasks):
    if not undo_tasks:
        clear_screen()
        print('Nothing to redo!')
        return
    redo_task = undo_tasks.pop()
    tasks.append(redo_task)
    listing(list_of_task)

def clear_screen():
    os.system('clear')

def add_task(tasks, task):
    clear_screen()
    tasks.append(task)
    listing(list_of_task)



list_of_task = []
undo_task_list = []

with open('list_task.json', 'r') as file:
    tasks = json.load(file)
    list_of_task = tasks

while True:
    print('Comands: list, undo, redo, quit')
    task = input('Digit a task or comand: ').capitalize()

    commands = {
    'List': lambda: listing(list_of_task),
    'Undo': lambda: undo(list_of_task, undo_task_list),
    'Redo': lambda: redo(list_of_task, undo_task_list),
    'add': lambda: add_task(list_of_task, task),
    }   

    if task == 'Quit':
        print('Finalizando sistema...')
        break

    command = commands.get(task) if commands.get(task) is not None else \
        commands['add']
    command()
    
    with open('list_task.json', 'w') as file:
        json.dump(
            list_of_task,
            file,
            indent= 2
        )
    
