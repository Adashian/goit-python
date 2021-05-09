def read_info(file):
    new_file = open('E:\\students.txt', 'w')
    count_1, count_2, count_3 = 0, 0, 0
    for i in range(len(s1)):
        s2 = file[i].split(';')
        x = str((int(s2[1]) + int(s2[2]) + int(s2[3])) / 3)
        new_file.write(x + '\n')
        count_1 += int(s2[1])
        count_2 += int(s2[2])
        count_3 += int(s2[3])
    count_1 = str(count_1 / len(file))
    count_2 = str(count_2 / len(file))
    count_3 = str(count_3 / len(file))
    x2 = f'{count_1} {count_2} {count_3}'
    new_file.write(x2)
    new_file.close()


inf = open('E:\\dataset_3363_4.txt', 'r')
s1 = inf.readlines()
inf.close()


read_info(s1)
