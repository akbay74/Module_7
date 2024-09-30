import os
import time

for dirpath, directory, files in os.walk('D:\Temp'):
    for file in files:
        filepath = os.path.join(dirpath, file)
        filetime = os.path.getmtime(filepath)
        date_time = time.strftime("%d-%m-%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file},\n'
              f' Путь: {filepath},\n'
              f' Размер: {filesize} байт,\n'
              f' Время изменения: {date_time},\n'
              f' Родительская директория: {parent_dir}')
