import random

# Генерація матриці 3x3
def generate_matrices():
    matrix = [[random.randint(10, 99) for _ in range(3)] for _ in range(3)]  # Матриця з двозначних чисел
    matrix_addend_1 = [[num // 10 for num in row] for row in matrix]  # Перша матриця
    matrix_addend_2 = [[num % 10 for num in row] for row in matrix]  # Друга матриця
    return matrix, matrix_addend_1, matrix_addend_2

# Використання
matrix, matrix_addend_1, matrix_addend_2 = generate_matrices()

print("Матриця з двозначними числами:")
for row in matrix:
    print(row)
print("\nПерша матриця (перші цифри):")
for row in matrix_addend_1:
    print(row)
print("\nДруга матриця (другі цифри):")
for row in matrix_addend_2:
    print(row)