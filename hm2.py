import csv

file_name = 'Corp_Summary.csv'


def make_team_structure(file_name: str) -> dict:
    """ Making a dict of teams structure in file

    Parameter:
    file_name (str): name of file, which contains information about workers

    Return value:
    dict: keys - names of departments, values - lists of department's teams
    """
    department_and_teams = {}
    with open(file_name) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            row = row[0].split(';')
            if row[1] not in department_and_teams:
                department_and_teams[row[1]] = []
            if row[2] not in department_and_teams[row[1]]:
                department_and_teams[row[1]].append(row[2])
    return department_and_teams


def make_report_about_departments(file_name: str) -> dict:
    """ Making a dict of statistics per each department

    Parameter:
    file_name (str): name of file, which contains information about workers

    Return value:
    dict: keys - names of departments, values - dicts of
        department's statistics (count of workers, max-min and mean of salary)

    """
    dep_stat = {}
    with open(file_name) as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            row = row[0].split(';')
            if row[1] not in dep_stat:
                dep_stat[row[1]] = {'Численность': 0,
                                    'Мин. ЗП': int(row[-1]),
                                    'Макс. ЗП': 0,
                                    'Ср. ЗП': 0.0}
            dep_stat[row[1]]['Численность'] += 1

            if int(row[5]) < dep_stat[row[1]]['Мин. ЗП']:
                dep_stat[row[1]]['Мин. ЗП'] = int(row[5])
            if int(row[5]) > dep_stat[row[1]]['Макс. ЗП']:
                dep_stat[row[1]]['Макс. ЗП'] = int(row[5])
            dep_stat[row[1]]['Ср. ЗП'] += int(row[5])
    for key, values in dep_stat.items():
        values['Ср. ЗП'] = round(values['Ср. ЗП'] / values['Численность'], 2)
        values['Мин-Макс ЗП'] = f'{values["Мин. ЗП"]} - {values["Макс. ЗП"]}'
        del values['Мин. ЗП']
        del values['Макс. ЗП']
    return dep_stat


def display_dep_stat(file_name: str):
    """ adequate data of departmetns statistics output

    uses function make_report_about_departments(file_name)

    Parametr:
    file_name (str): name of file, which contains information about workers
    """
    dict_dep_stat = make_report_about_departments(file_name)
    head = ['Департамент']
    head.extend(list(dict_dep_stat[list(dict_dep_stat.keys())[0]].keys()))
    for item in head:
        print('{:<15}'.format(item), end='')
    print()
    print('-'*100)
    for dep, values in dict_dep_stat.items():
        print('{:<15}'.format(dep), end='')
        for v in values.values():
            print('{:<15}'.format(str(v)), end='')
        print()
        print('-'*100)


def display_dep_structure(file_name: str):
    """ adequate data of departments structure output
    uses function make_team_structure(file_name)
    Parametr:
    file_name (str): name of file, which contains information about workers
    """
    dict_dep_teams = make_team_structure(file_name)
    max_key_length = max(len(key) for key in dict_dep_teams.keys())
    print("Департамент", end="\t\t")
    print('Подразделения')
    for key, values in dict_dep_teams.items():
        print('-'*100)
        print(f"{key:{max_key_length}}", end="\t\t")
        print(", ".join(values))
    print('-'*100)


def save_dep_stat(file_name: str):
    """ saves csv-file contains departments statistics

    uses function make_report_about_departments(file_name)

    Parametr:
    file_name (str): name of file, which contains information about workers
    """
    dict_dep_stat = make_report_about_departments(file_name)
    new_file_name = 'dep_stat.csv'
    with open(new_file_name, 'w') as new_file:
        writer = csv.writer(new_file)
        head = ['Департамент']
        head.extend(list(dict_dep_stat[list(dict_dep_stat.keys())[0]].keys()))
        writer.writerow(head)
        for dep, values in dict_dep_stat.items():
            row = [dep] + list(values.values())
            writer.writerow(row)


if __name__ == '__main__':

    print('Вам доступны три функции:')
    print('1) Иерархия команд.')
    print('2) Сводный отчет по департаментам.')
    print('3) Сохранить сводный отчет как отдельный csv-файл.')
    print('Напишите число - номер необходимой Вам функции.')

    choice = int(input())
    while choice not in [1, 2, 3]:
        print('Номер функции некорректный.'
              'Вам необходимо ввести число 1, 2 или 3.')
        choice = int(input())

    if choice == 1:
        display_dep_structure(file_name)
    elif choice == 2:
        display_dep_stat(file_name)
    elif choice == 3:
        save_dep_stat(file_name)
        print('Отчет сохранен в отдельном файле dep_stat.csv')
