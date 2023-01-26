import logger as log
from random import randint
from file_recording import record_to_file

all_classes = {}
all_students = {}
id_student = 1


def create_database_classes(nameclass=False):   # Initial filling of database
    if not nameclass:
        nameclass = input('Enter a class number: ')
    all_classes[nameclass] = []


def create_database_students():     # Initial filling of database
    for _ in range(randint(10, 15)):
        global id_student
        global all_students
        global all_classes

        surname = ['Van Dejk', 'Kjaer', 'Larsson', 'Kim', 'Tyan', 'Fox',
                   'Wolf', 'Noyer', 'Kulibali', 'Kim', 'Lim', 'Petrovskiy']
        surname = surname[randint(0, 11)]
        name = ['Kalidu', 'Pak', 'Igor', 'Artemiy', 'Andrey', 'Gwan',
                'Ir', 'Virgil', 'Simon', 'Sebastian', 'Manuel', 'Killian']
        name = name[randint(0, 11)]
        patronymic = ['Nikolaevich', 'Mikhailovich', 'Olegovich', 'Petrovich', 'Ilnurovich',
                      'Chon', 'Tze', 'Matveevich', 'An', 'Albertovich', 'Markovich', 'Cher']
        patronymic = patronymic[randint(0, 11)]
        day = randint(1, 31)
        if day < 10:
            day = str(f'0{day}')
        month = randint(1, 12)
        if month < 10:
            month = str(f'0{month}')
        birthdate = f"{day}.{month}.{randint(2011,2014)}"
        phone = f"8-{randint(901,999)}-{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}"
        address = ["Znamenka str", "Lubyanka str",
                   "Maroseyka str", "Ilyinka str"]
        address = f"Moscow, {address[randint(0,3)]}, {randint(1,100)}, {randint(1,100)}"
        class_name = ['5a', '5b', '4a', '4b']
        class_name = class_name[randint(0, 3)]

        if class_name not in all_classes:
            create_database_classes(class_name)

        all_classes[class_name].append(id_student)

        students_data = [surname, name, patronymic,
                         birthdate, phone, address, class_name]

        all_students[id_student] = students_data
        id_student += 1
    id_student -= 1
    log.log_input_data('Initial database formed')
    return id_student


def recording():
    record_to_file(all_classes)
    for key in all_students:
        data = f'{key}: {all_students[key]}'
        record_to_file(data)


def create_class(cl_name=False):
    log.log_input_data('Creation of a new class requested by user')
    if not cl_name:
        cl_name = input('Enter a class number: ')
    all_classes[cl_name] = []
    log.log_input_data('New class created')
    record_to_file(all_classes)
    print(all_classes)


def create_student():
    log.log_input_data('Addition of a new student requested by user')
    global id_student
    global all_students
    global all_classes
    id_student += 1
    surname = input("Enter student's surname: ")
    name = input("Enter student's name: ")
    patronymic = input("Enter student's patronymic: ")
    birthdate = input(f"Enter student's birthdate: ")
    phone = input(f"Enter student's telephone: ")
    address = input(f"Enter student's address: ")
    class_name = input("Enter student's class: ")

    if class_name not in all_classes:
        create_class(class_name)

    all_classes[class_name].append(id_student)

    students_data = [surname, name, patronymic,
                     birthdate, phone, address, class_name]

    all_students[id_student] = students_data
    record_to_file(all_classes)
    for key in all_students:
        data = f'{key}: {all_students[key]}'
        record_to_file(data)
    
    log.log_input_data('New student added to database')
    print(all_classes)
    print(all_students[id_student])
    


def edit_student():
    log.log_input_data('Update of info about a student requested by user')
    student_id = int(input("Enter student's id: "))
    surname = input("Enter student's new surname: ")
    name = input("Enter student's new name: ")
    patronymic = input("Enter student's new patronymic: ")
    birthdate = input("Enter student's new birthdate: ")
    phone = input("Enter student's new telephone: ")
    address = input("Enter student's new address: ")
    class_name = all_students[student_id][-1]
    new_students_data = [surname, name, patronymic,
                         birthdate, phone, address, class_name]
    all_students[student_id] = new_students_data
    record_to_file(all_classes)
    for key in all_students:
        data = f'{key}: {all_students[key]}'
        record_to_file(data)
    log.log_input_data('Info about student updated')
    print(all_students[id_student])

def delete_student():
    log.log_input_data('Deletion info about a student requested by user')
    student_id = int(input("Enter student's id: "))
    global all_classes
    global all_students
    all_classes[all_students[student_id][-1]].remove(student_id)
    del all_students[student_id]
    record_to_file(all_classes)
    for key in all_students:
        data = f'{key}: {all_students[key]}'
        record_to_file(data)
    log.log_input_data('Info about student deleted')
    print(all_classes)
    print(all_students)

def change_class():
    log.log_input_data("Change of a student's class requested by user")
    global all_classes
    global all_students
    student_id = int(input("Enter student's id: "))
    old_class_number = all_students[student_id][-1]
    new_class_number = input('Enter new class number: ')

    all_classes[old_class_number].remove(student_id)
    all_classes[new_class_number].append(student_id)
    all_students[student_id][-1] = new_class_number

    record_to_file(all_classes)
    for key in all_students:
        data = f'{key}: {all_students[key]}'
        record_to_file(data)
    log.log_input_data("Student's class changed")
    print(all_classes)
    print(all_students[id_student])

def final_vers_all_classes():
    return all_classes

def final_vers_all_students():
    return all_students