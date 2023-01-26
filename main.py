import user_interface as ui
import file_recording as fr
import import_data as id

def main():
    fr.clear_file('School_database.txt')
    id.create_database_students()
    id.recording()
    ui.user_choice()

if __name__ == '__main__':
    main()