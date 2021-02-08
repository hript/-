n = int(input())
l = []
p = []
t = [[-1, 0]]
start = 0
for i in range(n):
    current = int(input())
    if current == 0:
        l.append(p)
        p = []
        continue
    p.append(current)
l.append(p)
print(l)

max_mul = 1
for el in l:
    pos_first = 0
    pos_second = 0
    counter_neg = 0
    current_mul = 1
    negative_list = []
    for j, el_ in enumerate(el):
        if el_ < 0:
            negative_list.append(j)
        current_mul *= el_
    if len(negative_list) % 2 == 0:
        max_mul = max(max_mul, current_mul)
        continue
    if len(negative_list) >= 2:
        mul1 = 1
        for j in range(negative_list[-2] + 1):
            mul1 *= el[j]
        max_mul = max(max_mul, mul1)
        mul1 = 1
        for j in range(negative_list[0] + 2, len(el)):
            mul1 *= el[j]
        max_mul = max(max_mul, mul1)
        mul1 = 1
    else:
        mul1 = 1
        for j in range(negative_list[0] + 1):
            mul1 *= el[j]
        max_mul = max(max_mul, mul1)
        mul1 = 1
        for j in range(negative_list[0] + 2, len(el)):
            mul1 *= el[j]
        max_mul = max(max_mul, mul1)
        mul1 = 1

print(max_mul)



# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId=15
# Имеется набор данных, состоящий из целых чисел. Необходимо определить максимальное произведение подпоследовательности, состоящей из одного или более смежных элементов.
# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее по модулю 100.
