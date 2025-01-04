# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название
# файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell()
# перед записью.

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    str_num = 0
    str_start_byte = file.seek(0)  # байт начала первой строки
    for info_ in strings:
        file.write(info_ + '\n')
        str_num += 1
        key = (str_num, str_start_byte)  # задаём ключи словаря, кортеж (номер строки+байт начала строки)
        strings_positions[key] = info_  # добавляем значения в словарь, для этого ключа присваиваем значение
        str_start_byte = file.tell()
    file.close()
    return strings_positions


file_name = "test.txt"
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write("test.txt", info)
for elem in result.items():
    # "elem" будет проходить по каждому элементу в этом массиве и присваивать
    # значение текущего элемента elem, чтоб вывести через команду print.
    # items() - это метод словарей в Python. Он возвращает итерируемый объект, позволяющий получить
    # пары "ключ-значение" словаря.
    print(elem)
