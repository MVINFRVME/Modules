# Задача 7. Матрицы
# Контекст
# Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам поручили разработать класс Matrix для обработки и
# анализа данных. Ваш класс должен предоставлять функциональность для выполнения основных операций с матрицами, таких
# как сложение, вычитание, умножение и транспонирование. Это будет полезно для обработки и структурирования больших
# объёмов данных, которые используются в обучении нейронных сетей.

# Задача
# 1. Создайте класс Matrix для работы с матрицами.
# Реализуйте методы:
#     -сложения,
#     -вычитания,
#     -умножения,
#     -транспонирования матрицы.
# 2. Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.


#     Советы
# Методы сложения/вычитания/умножения должны получать параметром другую матрицу (объект класса Matrix) и выполнять
# указанное действие над своей и этой другой матрицей. Например, метод сложения должен получить параметром новую матрицу
# и сложить её со своей текущей.
# Метод транспонирования не должен ничего получать, он должен работать исключительно со своей матрицей.
# Транспонирование — это алгоритм, при котором строки матрицы меняются местами с её столбцами:

# Алгоритм транспонирования матрицы можно расписать следующим образом:
# 1. Создать новую матрицу result с размерами, обратными размерам исходной матрицы. Количество строк новой матрицы равно
# количеству столбцов исходной, а количество столбцов новой матрицы равно количеству строк исходной.
# 2. Пройтись по каждому элементу исходной матрицы. Для каждого элемента с индексами (i, j):
#     1. Поместить значение этого элемента (i, j) в ячейку с индексами (j, i) новой матрицы. То есть транспонирование
#     происходит с помощью обмена индексов местами.
#     2. После завершения цикла новая матрица result будет содержать транспонированную матрицу, которую можно вернуть.

# Пример:
# # Создание экземпляров класса Matrix
# m1 = Matrix(2, 3)
# m1.data = [[1, 2, 3], [4, 5, 6]]

# m2 = Matrix(2, 3)
# m2.data = [[7, 8, 9], [10, 11, 12]]

# # Тестирование операций
# print("Матрица 1:")
# print(m1)

# print("Матрица 2:")
# print(m2)

# print("Сложение матриц:")
# print(m1.add(m2))

# print("Вычитание матриц:")
# print(m1.subtract(m2))

# m3 = Matrix(3, 2)
# m3.data = [[1, 2], [3, 4], [5, 6]]

# print("Умножение матриц:")
# print(m1.multiply(m3))

# print("Транспонирование матрицы 1:")
# print(m1.transpose())

# Вывод
# Матрица 1:
# 1  2  3
# 4  5  6

# Матрица 2:
# 7   8   9
# 10  11  12

# Сложение матриц:
# 8   10  12
# 14  16  18

# Вычитание матриц:
# -6  -6  -6
# -6  -6  -6

# Умножение матриц:
# 22  28
# 49  64

# Транспонирование матрицы 1:
# 1  4
# 2  5
# 3  6

class Matrix:
    def __init__(self, row, column):
        # todo можно передавать только data, а row и column вычислять
        self.row = row
        self.column = column
        self.data = None

    def __str__(self):
        matrix_str = ''
        for i_row in self.data:
            for elem in i_row:
                matrix_str += str(elem) + '\t'
            matrix_str += '\n'
        return matrix_str

    def add(self, other):
        result = []
        for i in range(self.row):
            local = []
            for j in range(self.column):
                local.append(self.data[i][j] + other.data[i][j])
            result.append(local)

        res_m = Matrix(self.row, self.column)
        res_m.data = result

        return res_m

    def subtract(self, other):
        result = []
        for i in range(self.row):
            local = []
            for j in range(self.column):
                local.append(self.data[i][j] - other.data[i][j])
            result.append(local)

        res_m = Matrix(self.row, self.column)
        res_m.data = result

        return res_m

    def multiply(self, other):
        result = []
        for i in range(self.row):
            local = []
            for j in range(other.column):
                summ = 0
                for k in range(self.column):
                    summ += self.data[i][k] * other.data[k][j]
                local.append(summ)
            result.append(local)

        res_m = Matrix(self.row, self.column)
        res_m.data = result

        return res_m

    def transpose(self):
        result = []
        for i in range(self.column):
            local = []
            for j in range(self.row):
                local.append(self.data[j][i])
            result.append(local)

        res_m = Matrix(self.row, self.column)
        res_m.data = result

        return res_m



m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2)) # todo посмотри что будет, если метод add назвать __add__, а здесь заменить на m1 + m2

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
