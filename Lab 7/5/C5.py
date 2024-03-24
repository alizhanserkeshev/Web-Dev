def xor(x, y):
    return int((x or y) and not (x and y))

x = int(input())
y = int(input())

result = xor(x, y)

print(result)
