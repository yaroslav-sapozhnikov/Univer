import numpy as np

matrix = np.array([[0, 0.04, 0.12, 0.13, 0.22, 0, 0.11, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
              [0.57, 0, 0, 0.37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 2
              [0.39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.47, 0, 0, 0, 0], # 3
              [0.09, 0.22, 0.26, 0, 0.14, 0, 0, 0, 0.02, 0.25, 0, 0, 0, 0, 0, 0], # 4
              [0, 0, 0, 0, 0, 0, 0, 0, 0.33, 0.17, 0.16, 0.07, 0, 0, 0, 0], # 5
              [0.37, 0.05, 0, 0, 0, 0, 0.21, 0, 0.06, 0, 0, 0.29, 0, 0, 0, 0], # 6
              [0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0.74, 0, 0, 0, 0, 0, 0], # 7
              [0, 0, 0, 0, 0, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
              [0, 0, 0, 0, 0, 0, 0.36, 0, 0, 0.27, 0, 0, 0, 0, 0.13, 0], # 9
              [0, 0, 0, 0, 0.27, 0, 0, 0, 0.27, 0, 0, 0, 0.15, 0, 0, 0.1], # 10
              [0, 0, 0, 0.27, 0, 0.22, 0, 0, 0, 0, 0, 0.18, 0, 0, 0.27, 0], # 11
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0.2, 0], # 12
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.74, 0, 0, 0, 0, 0, 0], # 13
              [0, 0, 0, 0, 0, 0, 0, 0.39, 0.26, 0, 0, 0.01, 0, 0, 0.29, 0], # 14
              [0, 0, 0, 0, 0, 0, 0, 0, 0.41, 0, 0, 0.19, 0, 0, 0, 0.21], # 15
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.29, 0, 0, 0.29, 0] # 16
              ])

# простая проверка
for i in range(len(matrix)):
    if matrix[i][i] != 0:
        print(f'Ошибка: {i+1}:{i+1} != 0')

# заполняем диагональ
for i in range(len(matrix)):
    s = 0
    for j in range(len(matrix)):
        s += matrix[i][j]
    matrix[i][i] = round(1 - s, 2)

# матрица вероятностей
print('matrix:\n', matrix)


print('---Задание 1---')
# 1) вероятность того, что за 6 шагов система перейдет из состояния 9 в состояние 11;

pk = np.linalg.matrix_power(matrix, 6) # возведение матрицы
print('1) вероятность того, что за 6 шагов система перейдет из состояния 9 в состояние 11 =', pk[8][10])


# 2) вероятности состояний системы спустя 10 шагов, если в начальный момент вероятность состояний были следующими
# A=(0,08;0,02;0,02;0,12;0,07;0,1;0,03;0,02;0,07;0,11;0,09;0,08;0,04;0,11;0,04;0);

A0 = np.matrix('0.08 0.02 0.02 0.12 0.07 0.1 0.03 0.02 0.07 0.11 0.09 0.08 0.04 0.11 0.04 0')
A = np.linalg.matrix_power(matrix, 10) # возведение матрицы
A = A0.dot(A) # перемножение матрицы на вектор
print('2) вероятности состояний системы спустя 10 шагов:\n', A)


# 3) вероятность первого перехода за 8 шагов из состояния 16 в состояние 10

def multiply(p1, p2): # функция перемножение матриц для первого перехода
    result = np.zeros((len(p2[0]), len(p1)))
    for i in range(len(p1)):
        for j in range(len(p2[0])):
            for k in range(len(p2)):
                if k != j: # пропуск перехода в это же состояние
                        result[i][j] += p1[i][k] * p2[k][j]
    return result


def first_trans(p, k): # функция нахождения вероятностей первого перехода за k шагов
    result = [[p[i][j] for j in range(len(p))] for i in range(len(p))]
    for i in range(k - 1):
        result = multiply(p, result)
    return result


f_t = first_trans(matrix, 8)
print('3) вероятность первого перехода за 8 шагов из состояния 16 в состояние 10 =', f_t[15][9])


# 4) вероятность перехода из состояния 7 в состояние 4 не позднее чем за 7 шагов

trans_p = [[matrix[i][j] for j in range(len(matrix))] for i in range(len(matrix))]
p4 = trans_p[6][3]
for i in range(7):
    trans_p = multiply(matrix, trans_p)
    p4 += trans_p[6][3]

print('4) вероятность перехода из состояния 7 в состояние 4 не позднее чем за 7 шагов =', p4)


# 5) среднее количество шагов для перехода из состояния 8 в состояние 2;

trans_p = [[matrix[i][j] for j in range(len(matrix))] for i in range(len(matrix))]
p5 = trans_p[7][1]
for t in range(2, 1000): # бесконечность заменяем большим числом
    trans_p = multiply(matrix, trans_p)
    p5 += t*trans_p[7][1]

print('5) среднее количество шагов для перехода из состояния 8 в состояние 2 =', p5)


# 6) вероятность первого возвращения в состояние 7 за 10 шагов;

def first_return(a, step, p_return=0):  # Функция, находящая первое возвращение в состояние

    # 0: вероятность первого возвращения в состояние, по умолчанию 0
    # 1: среднее время возвращения
    # 2: вероятность возвращения в состояние не позднее, чем за step шагов

    f = [[[a[i][j] for j in range(len(a))] for i in range(len(a))]]
    a_step = [[[a[i][j] for j in range(len(a))] for i in range(len(a))]]

    for k in range(1, step):
        a_step.append(multiply(a, a_step[-1]))
        f.append([[a_step[k][i][j] for j in range(len(a))] for i in range(len(a))])

        for m in range(k):
            for i in range(len(a)):
                for j in range(len(a)):
                    f[k][i][j] -= f[m][i][j] * a_step[k - m - 1][i][j]

    if p_return == 0:
        result = [f[-1][i][i] for i in range(len(a))]

    elif p_return == 1:
        result = [0 for i in range(len(a))]

        for k in f:
            for i in range(len(a)):
                result[i] += k[i][i]

    elif p_return == 2:
        result = [0 for i in range(len(a))]

        for j in range(len(f)):
            for i in range(len(a)):
                result[i] += (j + 1) * f[j][i][i]

    else:
        result = "Неверно введен параметр p_return"

    return result


print('6) вероятность первого возвращения в состояние 7 за 10 шагов =', first_return(matrix, 10)[6])


# 7) вероятность возвращения в состояние 7 не позднее чем за 7 шагов;

print('7) вероятность возвращения в состояние 2 не позднее чем за 9 шагов =', first_return(matrix, 9, 1)[2])

# 8) среднее время возвращения в состояние 15;

print('8) среднее время возвращения в состояние 15 =', first_return(matrix, 1000, 2)[14])


# 9) установившиеся вероятности.
def find_constant(p):
    D = matrix.T
    for i in range(0, len(p)):
        D[i][i] = p[i][i] - 1

    D[len(p) - 1] = 1
    B = np.zeros((len(D), 1))
    B[len(p) - 1] = 1
    X = np.linalg.matrix_power(D, -1).dot(B)
    return X


print("9) установившиеся вероятности:\n", find_constant(matrix))

print('---Задание 2---')

lu = 29  # интенсивность поступления
m = 5  # количество каналов обслуживания
mu = 8  # интенсивность обслуживания
n = 15  # максимальный размер очереди

# заполнение матрицы интенсивностей
L = np.zeros((m + n + 1, m + n + 1))
for i in range(0, n + m):  # заполнение диагонали интенсив. поступлений
    L[i][i + 1] = lu
for i in range(1, n + m + 1):  # заполнение диагонали интенсив. обслуживаний
    if i < m:
        L[i][i - 1] = i * mu
    else:
        L[i][i - 1] = m * mu

print("Матрица интенсивностей:\n", L)


# a) Составьте граф марковского процесса, запишите систему уравнений Колмогорова и найдите установившиеся вероятности состояний.
def probabilities(N, M, matrix):
    D = np.zeros((m + n + 1, m + n + 1))
    for i in range(m + n + 1):
        D[i][i] = L[i].sum()

    M_tr = L.T
    M = M_tr - D

    B = np.zeros((m + n + 1, 1))
    B[m + n][0] = 1

    M_ = M
    M_[-1, :] = 1
    M_obr = np.linalg.inv(M_)
    X = M_obr.dot(B)
    return X


p = probabilities(n, m, L)
print("a) установившиеся вероятности состояний:\n", p)


# b) Найдите вероятность отказа в обслуживании.

p_denial = p[m + n]
print("b) вероятность отказа в обслуживании =", p_denial)


# c) Найдите относительную и абсолютную интенсивность обслуживания.

q = 1 - p_denial
print("c) относительная интенсивность =", q)

A = q * lu
print("c) абсолютная интенсивность =",  A)


# d) Найдите среднюю длину в очереди.

av_len = 0
for i in range(1, n + 1):
    av_len += i * p[m + i]
print("d) средняя длина очереди =",  av_len)


# e) Найдите среднее время в очереди.

av_t = 0
for i in range(n):
    av_t += (i + 1) / (m * mu) * p[m + i]
print("e) среднее время в очереди =",  av_t)


# f) Найдите среднее число занятых каналов.

av_ch = 0
for i in range(1, m + 1):
    av_ch += i * p[i]
for i in range(m + 1, m + n + 1):
    av_ch += m * p[i]
print("f) среднее число занятых каналов =",  av_ch)


# g) Найдите вероятность того, что поступающая заявка не будет ждать в очереди.

no_wait = 0
for i in range(0, m):
    no_wait += p[i]
print("g) вероятность того, что поступающая заявка не будет ждать в очереди =",  no_wait)


# h) Найти среднее время простоя системы массового обслуживания.

downtime = 1 / lu
print("h) среднее время простоя системы массового обслуживания =", downtime)
