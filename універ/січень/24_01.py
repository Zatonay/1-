def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не знайдено!")
        return ""
#типо функця яка зчитує файл буук

# Фільтруємо текст, залишаючи тільки потрібні символи та слова (ето помог чат джипити)
def filter_text(text):
    allowed_symbols = {'.', ',', '!', '?'}
    filtered_text = ''.join(c if c.isalnum() or c.isspace() or c in allowed_symbols else ' ' for c in text)
    return filtered_text

def count_words(text):
    words = text.split()
    return len(words) #функция рахує слова



def count_characters(text):
    return len(text) # функція кількісті символів у тексті


if __name__ == "__main__":
    file_name = "book.txt"
    text = read_file(file_name)

    if text:
        filtered_text = filter_text(text)
        word_count = count_words(filtered_text)
        character_count = count_characters(filtered_text)

        print("Профільтрований текст:")
        print(filtered_text)
        print("\nКількість слів у тексті:", word_count)
        print("Кількість символів у тексті:", character_count)
    else:
        print("Не вдалося обробити текст.")