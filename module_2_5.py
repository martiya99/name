#по вводным данным получается другой вывод на консоль
def get_matrix(m, n, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

#скорректировала, чтобы матрицы выводились согласно заданию
def get_matrix(m, n, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(5, 3, 42)
result3 = get_matrix(2, 4, 13)
print(result1)
print(result2)
print(result3)
