




































''' Задача 1
import math

def get_input():
    return input("Введите число: ")

def check_int(num):
    if not str(num).isdigit():
        print("Ошибка: введите целое число")
        return None

    return int(num)

def calculate_square(num):
    return num ** 2

def calculate_cube(num):
    return num ** 3

def calculate_sqrt(num):
    return math.sqrt(num)

def calculate_sin(num):
    return math.sin(num)

def calculate_cos(num):
    return math.cos(num)

def calculate_tan(num):
    return math.tan(num)

def calculate_factorial(num):
    return math.factorial(num)

def print_result(result):
    print("Результат:", result)

def main():
    num = None
    while num is None:
        num = check_int(get_input())
    square = calculate_square(num)
    cube = calculate_cube(num)
    sqrt = calculate_sqrt(num)
    sin = calculate_sin(num)
    cos = calculate_cos(num)
    tan = calculate_tan(num)
    factorial = calculate_factorial(num)
    print_result(square)
    print_result(cube)
    print_result(sqrt)
    print_result(sin)
    print_result(cos)
    print_result(tan)
    print_result(factorial)
main()
'''






















''' Задача 2.1
s = input("Введите строку: ")
unique = sorted(set(s))
print("Уникальные символы в строке:", *unique)
'''











''' Задача 2.2
my_list = [1, 3, 5, 7, 9, 11, 13]
if any(x % 2 == 0 for x in my_list):
    print("Список содержит хотя бы одно четное число")
else:
    print("Список не содержит четных чисел")
if all(x % 2 == 1 for x in my_list):
    print("Все числа в списке являются нечетными")
else:
    print("Список содержит хотя бы одно четное число")
'''










''' Задача 2.3
def rotate(matrix):
    return [list(row) for row in zip(*reversed(matrix))]

my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated = rotate(my_matrix)
print(rotated)
'''















''' Задача 2.4
def backpack(weights, values, max_weight):
    n = len(weights)
    bp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if weights[i-1] > j:
                bp[i][j] = bp[i-1][j]
            else:
                bp[i][j] = max(bp[i-1][j], bp[i-1][j-weights[i-1]] + values[i-1])
    return bp[n][max_weight]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_weight = 8

max_value = backpack(weights, values, max_weight)
print(f"Максимальная стоимость, которую можно унести в рюкзаке: {max_value}")
'''



















''' Задача 2.5
def matrix_operation(matrix1, matrix2, operation):
    result = []
    if operation == "+":
        for i, row in enumerate(matrix1):
            result.append([x + y for x, y in zip(row, matrix2[i])])
    elif operation == "-":
        for i, row in enumerate(matrix1):
            result.append([x - y for x, y in zip(row, matrix2[i])])
    elif operation == "*":
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                sum = 0
                for k in range(len(matrix2)):
                    sum += matrix1[i][k] * matrix2[k][j]
                row.append(sum)
            result.append(row)
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(matrix_operation(matrix1, matrix2, "+"))
print(matrix_operation(matrix1, matrix2, "-"))
print(matrix_operation(matrix1, matrix2, "*"))
'''