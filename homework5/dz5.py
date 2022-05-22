
#b= lambda x: print("чётное") if x %2==0 and x!= 0 else print('нечётное')
#print(b(int(input('Введите число'))))



a=int(input("Введите ка число  : "))
print(str(lambda x: print("чётное") if x %2==0 and x!= 0 else print('нечётное',a)))