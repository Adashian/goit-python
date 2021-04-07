import os
import pathlib
from shutil import move


def check_dir(path):
    types = (
             ['.svg', '.jpeg', '.png', '.jpg'],
             ['.avi', '.mp4', '.mov', '.mkv'],
             ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
             ['.mp3', '.ogg', '.wav', '.amr'],
             ['.zip', '.gz', '.tar']
            )
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            print(f'Спускаемся в {path}/{i}')
            check_dir(path + '/' + i)
            print(f'Возвращаемся в {path}')
        elif os.path.isfile(path+'/'+i):
            x = pathlib.Path(i)
            x = x.suffix
            print(f'Найден файл {i} с расширением {x}')
            if x.lower() in types[0]:
                try:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Pictures')
                except:
                    print(f'Такой файл уже существует ')
                    continue
            elif x.lower() in types[1]:
                try:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Video')
                except:
                    print(f'Такой файл уже существует ')
                    continue
            elif x.lower() in types[2]:
                try:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Documents')
                except:
                    print(f'Такой файл уже существует ')
                    continue
            elif x.lower() in types[3]:
                try:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Music')
                except:
                    print(f'Такой файл уже существует ')
                    continue
            elif x.lower() in types[4]:
                try:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Archives')
                except:
                    print(f'Такой файл уже существует ')
                    continue
            else:
                try:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Other')
                except:
                    print(f'Такой файл уже существует ')
                    continue


def move_file(path, destination):
    move(path, destination)


set_path = '/home/yaroslav/PycharmProjects/goit-python/test_dir'
check_dir(set_path)
