import export_data as ed
import import_data as id

def user_choice():
    print('''Welcome to school directory!\n Choose an operation:
        1. Add
        2. Edit
        3. Delete
        4. Print to console
        5. Export
        6. Exit''')
    choice = input('Enter an operation number: ')
    if choice =='1':
        print('''Choose an operation:
            1. Add a student
            2. Add a class''')
        add_choice = input()
        if add_choice =='1':
            id.create_student()
        elif add_choice =='2':
            id.create_class()
    
    elif choice=='2':
        print('''Choose an operation:
            1. Edit a student info
            2. Change class''')
        add_choice = input()
        if add_choice =='1':
            id.edit_student()
        elif add_choice =='2':
            id.change_class()
        
    elif choice=='3':
        id.delete_student()
    
    elif choice=='4':
        ed.export_to_console()
    
    elif choice=='5':
        ed.export_to_csv()
    
    elif choice=='6':
        return
    
    else:
        print('Incorrect value, try again')
        choice = input()
