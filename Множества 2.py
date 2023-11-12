
print("Введите числа первого списка, каждое число на отдельной строке:")
list1 = set()
while True:
    num = input()
    if not num:
        break
    list1.add(int(num))

print("Введите числа второго списка, каждое число на отдельной строке:")
list2 = set()
while True:
    num = input()
    if not num:
        break
    list2.add(int(num))

intersection = list1 & list2

print("Количество чисел, содержащихся в обоих списках:", len(intersection))
