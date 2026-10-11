import re

def process_nicks(take, give):
    with open(take, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Парсимо ніки та вміст у дужках, ігноруючи номери перед ніками
    nicks = []
    for line in lines:
        # Видаляємо можливий номер у рядку на початку
        line = re.sub(r"^\d+\)\s*", "", line).strip()
        match = re.match(r"@\S+", line)  # Знаходимо нік
        if match:
            nick = match.group(0)
            comment_match = re.search(r"\((.*?)\)", line)  # Знаходимо текст у дужках
            comment = comment_match.group(1) if comment_match else ""
            nicks.append((nick, comment))

    # Сортуємо:
    # 1. За кількістю символів у дужках (рядки без дужок мають кількість 0)
    # 2. По алфавіту повного рядка (нік і дужки)
    nicks_sorted = sorted(nicks, key=lambda x: (len(x[1]), f"{x[0]} ({x[1]})" if x[1] else x[0]))

    # Формуємо фінальний список із нумерацією
    result = [f"{i + 1}) {nick} ({comment})" if comment else f"{i + 1}) {nick}"
              for i, (nick, comment) in enumerate(nicks_sorted)]

    # Записуємо результат у файл
    with open(give, 'w', encoding='utf-8') as f:
        f.write("\n".join(result))

# Виклик функції
process_nicks('take.txt', 'give.txt')
