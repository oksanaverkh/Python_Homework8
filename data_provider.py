from random import randint

all_classes = {}
all_students = {}
id_student = 1
# data = ''
all_classes[] = []


def create_database():
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
    address = ["Znamenka str", "Lubyanka str", "Maroseyka str", "Ilyinka str"]
    address = f"Moscow, {address[randint(0,3)]}, {randint(1,100)}, {randint(1,100)}"
    class_name = ['5a', '5b', '4a', '4b']
    class_name = class_name[randint(0, 3)]

    # all_classes[class_name] = []

    all_classes[class_name]+=str(id_student)

    students_data = [surname, name, patronymic,
                     birthdate, phone, address, class_name]

    all_students[id_student] = students_data
    id_student += 1
    return id_student

create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()
create_database()




print(all_classes)
# print(all_students)
# for key, val in all_students.items():
#     print(key, val)
for key in all_students[2:]:
    print(key, all_students[key])
