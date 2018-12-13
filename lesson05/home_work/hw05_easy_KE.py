__author__ = 'Кирьянов Евгений Александрович'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('Задача 1')

import os
import shutil
# создаем дирректории 1-9
print('создаем папки')
for i in range(1, 10):
    try:
        os.mkdir('dir_' + str(i))
        print('Создана папка dir_' + str(i))
    except FileExistsError:
        print('Такая  директория (dir_' + str(i) + ") уже существует")
# удаляем дирректории 1-9
print('теперь удаляем')
del_d = input('Точно удалить? да/нет')
if del_d  == 'да':
    for i in range(1, 10):
        os.rmdir('dir_' + str(i))
        print("dir_" + str(i) + " больше нет(")
else:
    print("ну и правильно")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print()
print('Задача 2')

print('список фалов и папок в текущей папке')
for i in os.listdir():

    print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print()
print('задача 3')
os.path.realpath(__file__)
name = str(__file__)
print('оригинальный файл : ', name)
n_f_name = (name + '.copy')
new_f = shutil.copy(__file__, n_f_name)
print('копия : ', new_f)