__author__ = 'IrinaPavlova'

import string, time


def make_udar_dic(udar):
    '''Создание словаря, содержащего информацию об ударениях в словоформе'''
    udar = open(udar, 'r')
    first = udar.readlines()
    global dictionary
    dictionary = {}
    for i in first:
        head, sep, tail = i.partition(',')
        i = head
        head, sep, tail = i.partition(' ')
        i = head
        if 'U' in i:
            dictionary[i.replace('U', '')] = i[i.index('U')-1]
    return dictionary


def opener(location):
    '''Открытие файла с удалением пунктуации для построения обратного индекса'''
    file = open(location+'.txt', 'r')
    file = file.readlines()
    file = [''.join(x for x in el if x not in string.punctuation) for el in file]
    return file


def number(g):
    '''Нумерация строк (начиная с 1)'''
    l = 1
    for k in g:
        yield l, k
        l += 1


def indext(t):
    '''Построение обратного индекса'''
    dic = {}
    numbered = number(t)
    for n, stroka in numbered:
        for w in stroka.split():
            if w not in dic:
                dic[w] = [n]
            else: dic[w].append(n)
    return dic


def snippet(canon, words, text):
    '''Поиск сниппета'''
    for i in words:
        for j in text[i]:
            if canon[j-2] != canon[-1]: yield(canon[j-2:j+1])
            else: yield(canon[j-1:j+1])


def last_word(words, text, text2):
    '''Поиск строки, в которой заданное слово последнее'''
    for i in words:
        for j in text[i]:
            splitted = text2[j-1].split()
            if splitted.index(i) == len(splitted)-1:
                yield (j-1, i)


def count_syll(w):
  '''Подсчет слогов'''
    count = 0
    vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'ё', 'я', 'и', 'ю']
    for l in w:
        if l in vowels: count += 1
    return count


def rhyme():
    '''Поиск рифмы'''
    arr=[]
    for i in last_word(request, text2, textwp):
        arrs = []
        for h in range(i[0]-2, i[0]+3):
            if count_syll(textwp[h].split()[-1])==count_syll(i[1]) or count_syll(textwp[h].split()[-1])==count_syll(i[1])-1\
                    or count_syll(textwp[h].split()[-1])==count_syll(i[1])+1:
                if dictionary[textwp[h].split()[-1]]==dictionary[i[1]]:
                    if textwp[h].split()[-1][-1]==i[1][-1]:
                        arrs.append(textwp[h].split()[-1])
        arr.append(arrs)
    return arr




text1 = open('long_poem.txt', 'r')  # открываем файл со стихами, из которого будем печатать сниппеты
text1 = text1.readlines()

request = open('words.txt', 'r').read().splitlines()  # открываем файл с запросом

text2 = opener('long_poem') # открываем файл без пунктуации
textwp = text2

text2 = indext(text2)  # строим обратный индекс текста со стихами

make_udar_dic('udar.txt')  # формируем словарь с ударениями из готового файла


j = 0
for k in range(10):
    tsn0 = time.clock()
    snippets = snippet(text1, request, text2)  # записываем результат поиска сниппетов
    j += time.clock()-tsn0
j = j/10
print('Average snippets search time is '+str(j))


m = 0
for k in range(10):
    tr0 = time.clock()
    rhymes = rhyme()  # записываем результат поиска рифм
    m += time.clock()-tr0
m = m/10
print('Average rhymes search time is '+str(m))



output_snippets = open('Snippets.txt', 'w')  # открываем файл для записи сниппетов
for elem in snippets:  # записываем сниппеты в файл
    for i in elem:
        output_snippets.write(i)
    output_snippets.write('\n')
output_snippets.close()


print(rhymes)

output_rhymes = open('Rhymes.txt', 'w') # открываем файл для записи рифмубщихся слов
for elem in rhymes:
    for i in elem:
        output_rhymes.write(i+'\n')  # записываем рифмы в файл
    output_rhymes.write('\n')
output_rhymes.close()


