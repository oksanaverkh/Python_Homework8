import export_data as ed
import import_data as id
import input_check as ic
import logger as log


def user_choice():
    print('''Welcome to school directory!\n Choose an operation:
        1. Add
        2. Edit
        3. Delete
        4. Print to console
        5. Export
        6. View logging journal
        7. Exit''')
    choice = ic.check_input_1()
    while choice != '7':
        if choice == '1':
            print('''Choose an operation:
                1. Add a student
                2. Add a class''')
            add_choice = ic.check_input_2()
            if add_choice == '1':
                id.create_student()
            elif add_choice == '2':
                id.create_class()

        elif choice == '2':
            print('''Choose an operation:
                1. Edit a student info
                2. Change class''')
            add_choice = ic.check_input_2()
            if add_choice == '1':
                id.edit_student()
            elif add_choice == '2':
                id.change_class()

        elif choice == '3':
            id.delete_student()

        elif choice == '4':
            print(*ed.export_to_console())

        elif choice == '5':
            print('''Choose an operation:
                1. Export to .csv file
                2. Export to web-page''')
            add_choice = ic.check_input_2()
            if add_choice == '1':
                ed.export_to_csv()
            elif add_choice == '2':
                ed.export_to_html()

        elif choice == '6':
            print('''Choose an operation:
                1. Export to .csv file
                2. Print to console''')
            add_choice = ic.check_input_2()
            if add_choice == '1':
                log.log_output_journal_csv()
            elif add_choice == '2':
                log.log_output_journal()

        print('''Choose another operation:
        1. Add
        2. Edit
        3. Delete
        4. Print to console
        5. Export
        6. View logging journal
        7. Exit''')
        choice = ic.check_input_1()

    if choice == '7':
        return
