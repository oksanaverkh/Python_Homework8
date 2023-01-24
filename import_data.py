all_classes = {}
all_students = {}
id_student = 1

def create_class(cl_name=False):
    if not cl_name:
        cl_name = input('Enter a class number: ')
    all_classes[cl_name] = []

def create_student():
    surname = input("Enter student's surname: ")
    name = input("Enter student's name: ")
    patronymic = input("Enter student's patronymic: ")
    birthdate = input("Enter student's birthdate: ")
    phone = input("Enter student's telephone: ")
    address = input("Enter student's address: ")
    class_name = input("Enter student's class: ")

    if class_name not in all_classes:
        create_class(class_name)
    
    all_classes[class_name].append(id_student)

    students_data = [surname, name, patronymic, birthdate, phone, address, class_name]
    
    global all_students
    all_students[id_student] = students_data
    global id_student
    id_student+=1

def edit_student():
    student_id = input("Enter student's id: ")
    surname = input("Enter student's new surname: ")
    name = input("Enter student's new name: ")
    patronymic = input("Enter student's new patronymic: ")
    birthdate = input("Enter student's new birthdate: ")
    phone = input("Enter student's new telephone: ")
    address = input("Enter student's new address: ")
    class_name = all_students[student_id][-1]
    new_students_data = [surname, name, patronymic, birthdate, phone, address, class_name]
    all_students[student_id] = new_students_data

def delete_student():
    student_id = input("Enter student's id: ")
    global all_classes
    global all_students
    all_classes[all_students[student_id][-1]].remove(student_id)
    del all_students[student_id]

def change_class():
    student_id = input("Enter student's id: ")
    old_class_number = all_students[student_id][-1]
    new_class_number = input('Enter new class number')
    global all_classes
    global all_students
    all_classes[old_class_number].remove(student_id)
    all_classes[new_class_number].append(student_id)