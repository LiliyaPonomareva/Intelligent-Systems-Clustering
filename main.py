from find_distance import *

#все полученные ядра классов
core = [core1, core2, core3, core4]
for a in range(4):
    if (a == 0):
        print('Ядро класса square:')
    elif (a == 1):
        print('Ядро класса triangle:')
    elif (a == 2):
        print('Ядро класса circle:')
    elif (a == 3):
        print('Ядро класса S:')
    print(core[a])

#Объекты и их параметры
obj = [obj13, obj14, obj15, obj16]
for ind in range(4):
    print('Объект', ind+1)
    print(numpy.array(obj[ind]))
    D1 = pow(abs(distance(obj[ind], core1, matrix1)), 0.5)
    D2 = pow(abs(distance(obj[ind], core2, matrix2)), 0.5)
    D3 = pow(abs(distance(obj[ind], core3, matrix3)), 0.5)
    D4 = pow(abs(distance(obj[ind], core4, matrix4)), 0.5)
    list = [D1, D2, D3, D4]
    print('Расстояние до класса square:', D1)
    print('Расстояние до класса triangle:', D2)
    print('Расстояние до класса circle:', D3)
    print('Расстояние до класса S:', D4)
    if(D1 == min(list)):
        print('Вывод: Класс square')
        print()
    elif(D2 == min(list)):
        print('Вывод: Класс triangle')
        print()
    elif(D3 == min(list)):
        print('Вывод:Класс circle')
        print()
    elif(D4 == min(list)):
        print('Вывод:Класс S')
        print()
