n = int(input("Введите количество строк:\n"))
m = int(input("Введите количество столбцов:\n"))
matrix = []

try:
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input(f"Введите элемент [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
except ValueError:
    print("Ошибка: Введен некорректный элемент матрицы. Пожалуйста, введите целое число.")

print("Матрица:")
for row in matrix:
    print(row)

print("Функция заполнит матрицу символами % и & в шахматном порядке. В левом верхнем углу будет стоять точка.")
sim1 = "%"
sim2 = "&"

def matr(row, n, m, matrix):
    print("Обработанная матрица:")
    for i in range(n):
        for j in range(m):
            if i == j:
                matrix[i][j] = sim1
            elif (i + j) % 2 == 0:
                matrix[i][j] = sim1
            if (i + j) % 2 != 0:
                matrix[i][j] = sim2
    for row in matrix:
        print(row)
    tochka = "."
    matrix[0][0] = tochka
    print("Конечная матрица:")
    for row in matrix:
        print(row)

matr(matrix, n, m, matrix)
