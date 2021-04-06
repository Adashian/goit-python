import os


def file_dir(path):
    print(os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print(f'Спускаемся в папку {path}\\{i}')
            file_dir(path+'\\'+i)
            print(f'Возвращаемся в {path}')
        elif os.path.isfile(path+'\\'+i):
            print(f'----{i}')
            os.replace(path+'\\'+i,
                       path)


set_path = 'E:\\python\\goit-python\\module_4\\Хлам'
file_dir(set_path)
