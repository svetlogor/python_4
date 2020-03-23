def employees_dict(list_full_names):
    """
    Convert list to dictionary.
    :param list_full_names: list
    :return: dict
    """
    dict_full_name = {}
    for i in range(len(list_full_names)):
        # Разбиваем ФИО
        full_name_split = list_full_names[i].split(' ')
        # Фамилия - индекс
        surname = full_name_split[0] + '-' + str(i)
        # Создаем кортеж
        try:
            full_name_tuple = (full_name_split[0], full_name_split[1], full_name_split[2])
        except IndexError:
            # Если у кого-то нет Отчества
            full_name_tuple = (full_name_split[0], full_name_split[1])
        # Собираем словарь
        dict_full_name.update({surname: full_name_tuple})
    return dict_full_name

# print(employees_dict(['Иванов Иван Иваныч', 'Петров Петр']))