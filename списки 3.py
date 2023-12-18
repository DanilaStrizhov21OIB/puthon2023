def min_boats(m, n, weights):
    boats = 0
    weights.sort() 
    left = 0  
    right = n - 1 

    while left <= right:
        if weights[left] + weights[right] <= m:
            left += 1
            right -= 1
        else:
            boats += 1
    return boats
m = int(input())
n = int(input())
weights = []
for _ in range(n):
    weight = int(input())
    weights.append(weight)
result = min_boats(m, n, weights)
print(result)
