a = int(input("Введите число, и нажмите Enter "))
if ((a%2) != 0) and ((a/2)>0):
    print ("положительное нечетное число")
if (a%2 == 0) and ((a/2)>0):
    print("положительное четное число")
elif (a%2 == 0) and ((a/2)<0):
    print("отрицательное четное число")
elif (a%2 != 0) and ((a/2)<0):
    print("отрицательное нечетное число")
elif (a/2 == 0):
    print("нулевое число")
