

a = input("Введите число : ")

try:
    if  float(a)< 0:
        print('Отрицательное')
    elif float(a) == 0:
        print('Нуль')
    else:
         print('Положительное')
except:
    print('Введите число!')

