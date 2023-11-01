N = int(input())

numbers = list(map(int, input().split()))

reversed_numbers = numbers[::-1]

for number in reversed_numbers:
    print(number, end=" ")
