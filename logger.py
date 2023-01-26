from datetime import datetime as dt

def log_input_data(data):
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    with open('log.txt', 'a', encoding='utf=8') as file:
        file.write('{}:{}\n'
                .format(time, str(data)))


def log_output_journal():
    pass