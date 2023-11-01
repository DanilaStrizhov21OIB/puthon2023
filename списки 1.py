N = int(input("Введите число N: "))
numbers = []
for i in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)
reversed_numbers = list(reversed(numbers))

print("Перевернутый массив чисел:")
for number in reversed_numbers:
    print(number)