__author__ = 'Кирьянов Евгений Александрович'

import os

# Переход в папку
def gotodir(dir_path):
    os.chdir(dir_path)
    print('Текущая папку : ' + os.getcwd())

# создаем папку
def newdir(dir_path):
    try:
        os.mkdir(dir_path)
        print('Создана папка ' + dir_path)
    except FileExistsError:
        print("Такая директория уже существует")

# удаляем дирректорию
def deldir(dir_path):
    del_d = input('Точно удалить? да/нет')
    if del_d  == 'да':
        os.rmdir(dir_path)
        print(dir_path + " удалена")
    else:
        print("ну и правильно")
