import os
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
            file_name = os.path.basename(i)
            file_type = os.path.splitext(file_name)[1]
            print(f'Найден файл {i} с расширением {file_type}')
            try:
                if file_type.lower() in types[0]:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Pictures')
                elif file_type.lower() in types[1]:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Video')
                elif file_type.lower() in types[2]:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Documents')
                elif file_type.lower() in types[3]:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Music')
                elif file_type.lower() in types[4]:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Archives')
                else:
                    move_file(path + '/' + i, '/home/yaroslav/PycharmProjects/goit-python/test/Other')
            except:
                print(f'Такой файл уже существует ')
                continue


def move_file(path, destination):
    move(path, destination)


set_path = '/home/yaroslav/PycharmProjects/goit-python/test_dir'
check_dir(set_path)