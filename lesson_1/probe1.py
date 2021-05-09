from pprint import pprint

with open('E:/dataset_3363_3.txt', 'r') as doc:
    my_list = []
    for line in doc:
        line = line.strip()
        my_list.append(line)
    my_lower_list = [my_lower_list.lower() for my_lower_list in my_list]
    print(my_lower_list)

    # max = 0
    #
    # for i in my_lower_list:
    #     counter = 0
    #     for j in my_lower_list:
    #         if i == j:
    #             print(i, j, sep='!!!!')

    # for i in my_list:
    #     counter = my_lower_list.count(i)
    #     print(i)

    # http: // reposit.uni - sport.edu.ua /
    # http: // nbuv.gov.ua / node / 2116
    # http: // nbuv.gov.ua / node / 2116
    # https: // www.dissercat.com /
    # https: // cyberleninka.ru / search?q = % D0 % B2 % D0 % B5 % D0 % BB % D0 % BE % D1 % 81 % D0 % B8 % D0 % BF % D0 % B5 % D0 % B4 % D0 % BD % D0 % B8 % D0 % B9 % 20 % D1 % 81 % D0 % BF % D0 % BE % D1 % 80 % D1 % 82 & page = 1
    # https: // uni - sport.edu.ua / sites / default / files / vseDocumenti / styl_vankuver._metodychka_nufvsu.pdf
