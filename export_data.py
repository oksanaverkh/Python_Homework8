import logger as log
import import_data as id


def export_to_console():
    log.log_input_data('School database preview requested by user')
    with open('School_database.txt', 'r') as data:
        data = data.readlines()
    log.log_input_data('School database unloaded in terminal')
    return data


def export_to_csv():
    log.log_input_data(
        'School database preview in csv-format requested by user')
    with open('School_database.csv', 'w') as file:
        file.write(str(id.final_vers_all_classes())+'\n')
        students_all = id.final_vers_all_students()
        for key, val in students_all.items():
            file.write('{}:{}\n'.format(key, val))
    log.log_input_data('File .csv unloaded')


def export_to_html():
    log.log_input_data(
        'School database preview in html-format requested by user')
    style1 = 'style="font-size:42px;"'
    style2 = 'style="font-size:32px;"'
    style3 = 'style="font-size:28px;"'

    html = '<html>\n <head>    <p {}>{}</p></head>\n <body>\n'\
        .format(style1, 'School database')

    html += '<head>    <p {}>{}</p></head>\n'\
        .format(style2, 'Classes and students identificators list:')
    classes_all = id.final_vers_all_classes()
    for key, val in classes_all.items():
        data = ('{}:{}\n'.format(key, val))
        html += '    <p {}>{}</p>\n'\
            .format(style3, data)

    html += '<head>    <p {}>{}</p></head>\n'\
        .format(style2, 'Information about students:')
    students_all = id.final_vers_all_students()
    for key, val in students_all.items():
        data = ('{}:{}\n'.format(key, val))
        html += '    <p {}>{}</p>\n'\
            .format(style3, data)

    html += '   </body>\n</html'

    with open('index.html', 'w') as page:
        page.write(html)
    log.log_input_data('File .html unloaded')
    return html
