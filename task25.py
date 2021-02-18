from math import sqrt
counter = 2
current_counter = 0
first, second = 0, 0

for i in range(11275, 16329):
    l = []
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            current_counter += 1
            if current_counter == 1:
                first = i // j
            if current_counter == 2:
                second = i // j
            if i // j > sqrt(i):
                counter += 2
            if i // j == sqrt(i):
                counter += 1
            if counter > 5:
                break
    if counter == 5:
        print(first, second)
    counter = 2
    current_counter = 0


#Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [11275; 16328], числа, имеющие ровно 5 различных делителей. 
#В ответе для каждого найденного числа запишите два его наибольших делителя, не равных самому числу, в порядке возрастания.
