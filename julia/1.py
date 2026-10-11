import math

def kvadrat(a, b, c):
    """Розв'язує квадратне рівняння ax^2 + bx + c = 0."""
    if a == 0:
        return None  # Не є квадратним рівнянням
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,  )
    else:
        return None

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено.")
        return

    results = []
    for line in lines:
        try:
            # Перевіряємо, чи рядок містить три числа
            coefficients = list(map(float, line.split()))
            if len(coefficients) != 3:
                raise ValueError("Рядок не містить рівно три числа.")
            a, b, c = coefficients
            roots = solve_quadratic(a, b, c)
            results.append((a, b, c, roots))
        except ValueError:
            # Пропускаємо некоректні рядки
            continue

    # Сортуємо результати: спершу два корені, потім один, потім без коренів
    results.sort(key=lambda x: (len(x[3]) if x[3] else 0, x[3] is None))

    # Записуємо результати у вихідний файл
    with open(output_file, 'w') as outfile:
        for a, b, c, roots in results:
            if roots is None:
                outfile.write(f"{a:.2f} {b:.2f} {c:.2f} None\n")
            elif len(roots) == 1:
                outfile.write(f"{a:.2f} {b:.2f} {c:.2f} {roots[0]:.2f}\n")
            else:
                outfile.write(f"{a:.2f} {b:.2f} {c:.2f} {roots[0]:.2f} {roots[1]:.2f}\n")

# Викликаємо функцію для обробки файлу
process_file("input.txt", "output.txt")
