# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
# и использование модуля time для корректного отображения времени.
# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.

import os, time

directory = "."

for root, dirs, files in os.walk(directory):
    for file in files:
        # Формирование полного пути к файлу
        filepath = os.path.join(root, file)
        # Время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # Размер файла
        filesize = os.path.getsize(filepath)
        # Родительская директория
        parent_dir = os.path.dirname(os.path.abspath(file))

        print(f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, "
              f"Время изменения: {formatted_time}, Родительская директория: {parent_dir}")
