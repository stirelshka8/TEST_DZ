import os
import time
from art import tprint

# Код ниже не нужен от слова совсем) Но так как я учусь, то пусть будет
start_id = 0

if start_id == 1:
    os.system("clear")
    print("\033[31m{}\033[0m".format("[+] start subproces ..."))
    time.sleep(3)
    print("\033[31m{}\033[0m".format("[+] initialization AI ..."))
    time.sleep(3)
    print("\033[31m{}\033[0m".format("[+] welcome to the club ..."))
    time.sleep(3)
    print("\033[31m{}\033[0m".format("[+] promramm is starting ..."))
    time.sleep(3)
    os.system("clear")
    tprint("FP by Python")
    time.sleep(3)
    os.system("clear")

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


# ---------------------------------------------------------------------------------------------------------------
# Функция поиска человека по номеру документа
def document_search(param, search_location=None):
    # Просим пользователя ввести номер документа
    # param = input("Введите номер документа >>> ")
    # Переменная отвечающая за вывод данных, при отсутствии данных будет иметь параметр False
    if search_location is None:
        search_location = documents
    output_data = False
    # Проходимся циклом по словарю и вычленяем все словари
    for document in search_location:
        # В том случае если в одном из словарей по ключу name будет найдены введенные данный
        if param == document["number"]:
            # Они запишутся в переменную output_data
            output_data = document["name"]
            # Выводим полученные данные
            return f"Документ с № {param} принадлежит {output_data}"
            # В случае отсутствия искомых данных переменная будет иметь параметр False
    if not output_data:
        # Выводим о неудаче
        return f"Документ с номером {param} в базе не найден!"
    return


# Функция определения номера полки где находится документ
def document_location(params, search_location=None):
    # Просим пользователя ввести номер документа
    # parameter = input("Введите номер документа >>> ")
    # Переменная отвечающая за вывод данных, при отсутствии данных будет иметь параметр False
    if search_location is None:
        search_location = documents
    output_data = False
    # Проходимся циклом по словарю и распределяем ключи и значения в свои переменные
    for rack, val_ in search_location.items():
        # Функция проверяет введенный параметр с значением из словаря и в том случае если такое значение есть
        if params in val_:
            # Переменной присваивается значение ключа словаря
            output_data = rack
            # Выводим полученные данные
            return f"Документ с номером {params} лежит на полке № {output_data}"
            # В случае отсутствия искомых данных переменная будет иметь параметр False
    if not output_data:
        # Выводим о неудаче
        return f"Документ с номером {params} в базе не найден!"
    return


# Функция определения номера полки где находится документ
def whole_dictionary(search_location):
    # Переменная шага для вывода списка
    i = 0
    # Создаем пустой список куда будем записывать данные
    wh_dict = []
    # Проходим циклом по всему списку вычленяя словари
    for docos in search_location:
        # Из получившихся словарей вытаскиваем все значени
        for val_ in docos.values():
            # Записываем в список
            wh_dict.append(val_)
        # Прибавляем к переменной 3 для того что бы вывести следующие значения
        i += 3
        # Выводим данные
        return wh_dict[i], wh_dict[i + 1], wh_dict[i + 2]
    return


# Функция добавления данных как на полку так и в словарь
def adding_document(search_location_documents, search_location_directories):
    # Переменная для вывода существующих полок
    place_dir = []
    # Функция которая вычленяет все полки для последующего вывода
    for sdl_ in search_location_directories:
        place_dir.append(sdl_)
    # Методом join собираем все полки в строку и разделяем запятой
    place = ', '.join(place_dir)
    # Просим пользователя ввести необходимые данные
    new_docos_number = input("Введите номер нового документа >>> ")
    new_docos_type = input("Введите тип нового документа >>> ")
    new_docos_name = input("Введите владельца нового документа (Имя Отчество) >>> ")
    new_docos_place = input(f"Введите № полки нового документа (есть полки с ID № {place}) >>> ")
    # Функция которая "смотрит" есть ли введенная пользователем полка
    if new_docos_place in search_location_directories:
        # Если полка есть то на указанную полку добавляем данные
        search_location_directories[new_docos_place].append(new_docos_number)
        # Так же собираем новый словарь из введенных данных
        new_data_package = {"type": new_docos_type, "number": new_docos_number, "name": new_docos_name}
        # И добавляем в корень
        search_location_documents.append(new_data_package)
        return f"Данные нового документа ({new_docos_type} {new_docos_number} {new_docos_name}) занесены!"
    else:
        # Выводим данный текст в случае если указанной полки не существуеит
        return (f"""Добавить данные на указанную Вами полку невозможно, полки не существует.
Попробуйте выбрать из имеющихся полок (есть полки с ID № {place}) или добавите новую.""")


# Функция удаления документа
def deleting_document(search_location_documents, search_location_directories):
    del_docos_number = input("Введите номер документа который необходимо удалить >>> ")
    # Делаем пверхностную копию для дальнейшей работы
    copy_location_documents = search_location_documents.copy()
    copy_location_directories = search_location_directories.copy()
    # Переменная которая которая в случае обнаружения искомого принимет значение True
    # с ее помощью скажем пользователю что искомого объекта нет
    output_data = False
    # Проходимся функцией по скопированным документам и вычленяем все словари
    for docos in copy_location_documents:
        # Если номер в словаре совпадаетс введенным
        if del_docos_number == docos["number"]:
            # то удаляем уже не из скопированного а из корня
            search_location_documents.remove(docos)
            # выводим результат
            return f"Документ с № {del_docos_number} удален из каталога."
        # Этой функцией проходимся по полкам и так же как и в функции выше ищем, сверяем и удаляем
    for keys_, val_ in copy_location_directories.items():
        if del_docos_number in val_:
            search_location_directories[keys_].remove(del_docos_number)
            return f"Данные документа с № {del_docos_number} удален с полки № {keys_}"
    # В случае отсутствия искомогообъекта выводим текст
    if not output_data:
        return f"Данные документа с № {del_docos_number} не найден(ы)."
    return


# Функция перемещения документа
def moving_document(search_location_directories):
    mov_docos_number = input("Введите номер документа который необходимо переместить >>> ")
    copy_location_directories = search_location_directories.copy()

    # Переменная для вывода существующих полок
    place_dir = []
    # Функция которая вычленяет все полки для последующего вывода
    for sdl_ in search_location_directories:
        place_dir.append(sdl_)
    # Методом join собираем все полки в строку и разделяем запятой
    place = ', '.join(place_dir)

    # Проходимся функцией по скопированному и вычленяем все данные которые распределяем в переменные
    for keys_former, val_ in copy_location_directories.items():
        # Если введенное есть в словаре выполняем код ниже
        if mov_docos_number in val_:
            print(f"На какую полку будем перемещать. Есть полки с № {place}")
            new_place = input("Номер новой полки >>> ")
            # Функция проверяет есть ли введенная полка и если есть то из старого славаря удаляем, а в новый добавляем
            if new_place in copy_location_directories:
                search_location_directories[keys_former].remove(mov_docos_number)
                search_location_directories[new_place].append(mov_docos_number)
                return f"Документ с № {mov_docos_number} перемещен с полки № {keys_former} на полку № {new_place}. "
            else:
                return f"Полки с № {new_place} не существует."
    else:
        return f"Данные документа с № {mov_docos_number} не найден(ы)."


# Функция добавления новой полки
def add_place(search_location_directories):
    add_place_number = input("Введите номер новой полки >>> ")
    # Проверяем есть ли полка с таким же номером
    if add_place_number in search_location_directories:
        return f"Полка с № {add_place_number} уже существует."
    # Если нет то создаем
    else:
        search_location_directories[add_place_number] = []
        return f"Полка с № {add_place_number} создана."


# ---------------------------------------------------------------------------------------------------------------
# Родительская функция которая служит для вывода текста и запуска других функций
def user_input():
    # Этой командой отправляем в команду напрямую в командную строку которая очищает консоль
    while True:
        print("\033[31m{}\033[0m".format("""
        ***********************************************************************************************************
        Команды:
        p  –  команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
        s  –  команда, которая спросит номер документа и выведет номер полки, на которой он находится;
        l  –  команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
        a  –  команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя 
              владельца и номер полки, на котором он будет храниться;
        d  –  команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
        m  –  команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
        as –  команда, которая спросит номер новой полки и добавит ее в перечень.
        ***********************************************************************************************************"""))
        print()
        print()
        launch_command = input("\033[34m{}\033[0m".format("Введите команду >>> "))
        print()
        if launch_command == 'p':
            print("\033[32m\033[42m{}\033[0m".format("Выбран параметр поиска человека по номеру документа"))
            print()
            document_search()
            print()
            print()
        elif launch_command == 's':
            print("\033[32m\033[42m{}\033[0m".format(
                "Выбран параметр поиска полки на которой хранятся документы по номеру документа"))
            print()
            document_location()
            print()
            print()
        elif launch_command == 'l':
            print("\033[32m\033[42m{}\033[0m".format("Выбран параметр вывода всего словаря"))
            print()
            whole_dictionary(search_location=documents)
            print()
            print()
        elif launch_command == 'a':
            print("\033[32m\033[42m{}\033[0m".format("Выбран параметр добавления документа"))
            print()
            adding_document(search_location_documents=documents, search_location_directories=directories)
            print()
            print()
        elif launch_command == 'd':
            print("\033[32m\033[42m{}\033[0m".format("Выбран параметр удаления документа"))
            print()
            deleting_document(search_location_documents=documents, search_location_directories=directories)
            print()
            print()
        elif launch_command == 'm':
            print("\033[32m\033[42m{}\033[0m".format("Выбран параметр перемещения документа"))
            print()
            moving_document(search_location_directories=directories)
            print()
            print()
        elif launch_command == 'as':
            print("\033[32m\033[42m{}\033[0m".format("Выбран параметр добавления новой полки"))
            print()
            add_place(search_location_directories=directories)
            print()
            print()
        elif launch_command == 'q':
            print("\033[3m\033[33m\033[41m{}\033[0m".format("Работа программы завершена!"))
            break
        else:
            print("\033[3m\033[33m\033[41m{}\033[0m".format("Введена неверная команда! Повторите запрос."))


# Вызываем родительскую функцию
# user_input()

if __name__ == '__main__':
    user_input()
