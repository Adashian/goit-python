from collections import defaultdict


inf = open('E:\\dataset_3363_4.txt', 'r')
s1 = inf.readlines()
inf.close()


def count_word_in_file(file):

    answer = None
    result = 0
    for i in range(len(file)):
        s2 = file[i].split()
        word_count = defaultdict(int)
        for j in s2:
            word_count[j] += 1
            if word_count[j] >= result:
                result = word_count[j]
                answer = j
    return answer, result


x = finally_answer = count_word_in_file(s1)
print(x)
