
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

result = [coord for coord in coordinates if sum(coord) != n]

print(result)
