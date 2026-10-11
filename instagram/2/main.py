import os
import re

# Конфигурация файлов и приоритетов
files = ["admin.txt", "people.txt", "people_all.txt", "people_dont_know.txt"]
priorities = {"admin.txt": 1, "people.txt": 2, "people_all.txt": 3, "people_dont_know.txt": 4}


def read_names(file_name):
    """Чтение имен из файла с фильтрацией по символу @ и обработкой нескольких ников на строке."""
    if not os.path.exists(file_name):
        print(f"Файл {file_name} не найден.")
        return set()

    names_set = set()
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            # Извлекаем все ники, начинающиеся с @, и добавляем их в множество
            names = re.findall(r"@[\w\d_]+", line.strip())
            names_set.update(names)
    return names_set


def collect_and_sort_names():
    """Сбор и сортировка данных с приоритетом файлов."""
    data = {}
    duplicate_tracker = {}
    group_counts = {file: 0 for file in files}

    # Чтение данных и отслеживание дубликатов
    for file in files:
        names = read_names(file)
        group_counts[file] = len(names)
        for name in names:
            if name in data:
                duplicate_tracker[name] = duplicate_tracker.get(name, []) + [file]
            else:
                data[name] = file

    sorted_data = sorted(data.items(), key=lambda x: (priorities[x[1]], x[0]))
    return sorted_data, duplicate_tracker, group_counts


def format_output(sorted_data, format_type):
    """Форматирование списка по выбранному типу."""
    output = []
    section_counters = {file: 1 for file in files}
    combined_counter = 1

    if format_type == "1":
        for name, file in sorted_data:
            num_prefix = ")" * priorities[file]
            output.append(f"{combined_counter}{num_prefix} {name}")
            combined_counter += 1
    else:
        for name, file in sorted_data:
            num_prefix = ")" * priorities[file]
            output.append(f"{section_counters[file]}{num_prefix} {name}")
            section_counters[file] += 1

    return output


def main():
    """Основная логика программы."""
    sorted_data, duplicate_tracker, group_counts = collect_and_sort_names()

    # Запрос формата списка у пользователя
    while True:
        print("\nВыберите формат списка:")
        print("1 - Все ники в одном списке с преимуществом по папкам")
        print("2 - Сохранение структуры списка с разделением по секциям")
        user_choice = input("Введите номер выбора (1 или 2): ").strip()
        if user_choice in {"1", "2"}:
            break
        print("Неверный выбор. Пожалуйста, введите 1 или 2.")

    output = format_output(sorted_data, user_choice)

    # Вывод на экран
    print("\nРезультирующий список пользователей:")
    print("\n".join(output))

    # Вывод информации о дубликатах
    if duplicate_tracker:
        print("\nДубликаты (внимательно проверьте данные):")
        for name, locations in duplicate_tracker.items():
            print(f"{name}: найдено в файлах {', '.join(locations)}")

    # Вывод информации о количестве участников
    total_participants = sum(group_counts.values())
    print(f"\nВсего участников: {total_participants}")
    print("Количество участников по группам:")
    for file, count in group_counts.items():
        print(f"{file}: {count} участников")


if __name__ == "__main__":
    main()
