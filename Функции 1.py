def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_list(num):
    result = [factorial(num)]
    while num > 1:
        num -= 1
        result.append(result[-1] // num)
    return result

number = 4
result_list = factorial_list(number)
print(result_list)
