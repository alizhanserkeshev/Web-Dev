# Считываем количество элементов в массиве
N = int(input())

# Считываем элементы массива и разделяем их по пробелу
array = list(map(int, input().split()))

# Инициализируем два указателя: один на начало массива, другой на его конец
left = 0
right = N - 1

# Переставляем элементы массива в обратном порядке, пока указатели не пересекутся
while left < right:
    # Меняем местами элементы, на которые указывают указатели
    array[left], array[right] = array[right], array[left]
    # Сдвигаем указатели
    left += 1
    right -= 1

# Выводим массив после перестановки элементов
for num in array:
    print(num, end=' ')
