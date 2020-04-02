# Задачи на циклы и оператор условия
# Test-selector included
test_task = int(input("Enter a number of task to check"))
if test_task == 1:
    '''
    Задача 1
    Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
    '''
    str0 = '000000'
    for i in range(5):
        print(i + 1, '-', str0)

elif test_task == 2:
    '''
    Задача 2
    Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.
    '''
    h = 0
    for j in range(10):
        while True:
            input_phrase = "Write " + str(j + 1) + "-th single number\n"
            num = int(input(input_phrase))
            if num >= 0 and num <= 9:
                if num == 5:
                    h += 1
                break
            else:
                print('That was not a single number. ', end='')
    print(h)

elif test_task == 3:
    '''
    Задача 3
    Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
    '''
    sum1 = int(0)
    for k in range(1, 101, 1):
        sum1 += k
    print(sum1)

elif test_task == 4:
    '''
    Задача 4
    Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
    '''
    mpl1 = int(1)
    for l in range(2, 11, 1):
        mpl1 = mpl1 * l
    print(mpl1)

elif test_task == 5:
    '''
    Задача 5
    Вывести цифры числа на каждой строчке.
    '''
    source_int1 = int(input("Enter a number"))
    while source_int1 > 0:
        print(source_int1 % 10)
        source_int1 = source_int1 // 10

elif test_task == 6:
    '''
    Задача 6
    Найти сумму цифр числа.
    '''
    int_sum1 = int(0)
    source_int2 = int(input("Enter a number"))
    while source_int2 > 0:
        int_sum1 = int_sum1 + source_int2 % 10
        source_int2 = source_int2 // 10
    print(int_sum1)

elif test_task == 7:
    '''
    Задача 7
    Найти произведение цифр числа.
    '''
    int_mpl1 = int(1)
    source_int2 = int(input("Enter a number"))
    while source_int2 > 0:
        int_mpl1 = int_mpl1 * source_int2 % 10
        source_int2 = source_int2 // 10
    else:
        print("Nothing to multiply, base value is ", end="")
    print(int_mpl1)

elif test_task == 8:
    '''
    Задача 8
    Дать ответ на вопрос: есть ли среди цифр числа 5?
    '''
    source_int3 = int(input("Enter a number"))
    while source_int3 > 0:
        if source_int3 % 10 == 5:
            print("There is a '5' number")
            break
        source_int3 = source_int3 // 10
    else:
        print("nothing to do here. ", end="")
    print("No number '5' found")

elif test_task == 9:
    '''
    Задача 9
    Найти максимальную цифру в числе
    '''
    max_int1 = int(0)
    source_int4 = int(input("Enter a number"))
    while source_int4 > 0:
        if max_int1 < source_int4 % 10
            max_int1 = source_int4 % 10
        source_int4 = source_int4 // 10
    else:
        print("nothing to do here. ", end="")
    print(max_int1)

elif test_task == 10:
    '''
    Задача 10
    Найти количество цифр 5 в числе
    '''
    int_count1 = int(0)
    source_int5 = int(input("Enter a number"))
    while source_int5 > 0:
        if source_int5 % 10 == 5:
            int_count1 += 1
        source_int5 = source_int5 // 10
    else:
        print("nothing to do here. ", end="")
    print(source_int5)

else:
    print("No such task number. Please relaunch.")