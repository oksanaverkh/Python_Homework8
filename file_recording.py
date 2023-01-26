import logger as log
from datetime import datetime as dt


def record_to_file(data):
    with open('School_database.txt', 'a') as file:
        time = dt.now().strftime('%d/%m/%Y %H:%M')
        file.write(str(time)+' ')
        file.write(str(data))
        file.write('\n')
    log.log_input_data('Database updated in .txt file')


def clear_file(filename):
    file = open(filename, 'w')
    file.close()
