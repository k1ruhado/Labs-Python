# Лабораторна робота 6
# Робота з файлами в Python

# Завдання 1: Записати своє ім'я та прізвище у файл
with open('name.txt', 'w') as file:
    file.write('Kirill Demyanenko')
print("Ім'я та прізвище записані у файл name.txt")

# Завдання 2: Записати дані від користувача до файлу
lines = ["Привіт, це перший рядок!", "Це другий рядок!"]  # Симуляція введення
with open('user_input.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')

with open('user_input.txt', 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    num_chars = sum(len(line) for line in lines)

print(f"Кількість рядків: {num_lines}, Кількість символів: {num_chars}")

# Завдання 3: Аналіз файлу poetry.txt
try:
    with open('poetry.txt', 'r') as file:
        lines = file.readlines()
        not_start_t = 0
        end_with_d = 0
        capital_words = 0
        for line in lines:
            if not line.startswith('T'):
                not_start_t += 1
            if line.rstrip().endswith('d'):
                end_with_d += 1
            for word in line.split():
                if word.istitle():
                    capital_words += 1

    print(f"Рядків, що не починаються на 'T': {not_start_t}")
    print(f"Рядків, що закінчуються на 'd': {end_with_d}")
    print(f"Слів, що починаються з великої літери: {capital_words}")
except FileNotFoundError:
    print("Файл poetry.txt не знайдено.")

# Завдання 4: Підрахунок символів та найдовше слово в mbox-short.txt
try:
    with open('mbox-short.txt', 'r') as file:
        longest_word = ''
        for line in file:
            print(f"Кількість символів у рядку: {len(line.strip())}")
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    print(f"Найдовше слово: {longest_word}")
except FileNotFoundError:
    print("Файл mbox-short.txt не знайдено.")

# Завдання 5: Вивести вміст файлу у верхньому регістрі
try:
    with open('mbox-short.txt', 'r') as file:
        for line in file:
            print(line.strip().upper())
except FileNotFoundError:
    print("Файл mbox-short.txt не знайдено.")

# Завдання 6: Рядки з '@' та їх кількість
try:
    with open('mbox-short.txt', 'r') as file:
        count = 0
        for line in file:
            if '@' in line:
                print(line.strip())
                count += 1
    print(f"Кількість рядків зі знаком '@': {count}")
except FileNotFoundError:
    print("Файл mbox-short.txt не знайдено.")

# Завдання 7*: Робота з відгуками
try:
    with open('feedback.txt', 'r') as file:
        positive = []
        negative = []
        for line in file:
            if line.startswith('Positive:'):
                positive.append(line)
            elif line.startswith('Negative:'):
                negative.append(line)

    with open('positive.txt', 'w') as pos_file:
        pos_file.writelines(positive)

    with open('negative.txt', 'w') as neg_file:
        neg_file.writelines(negative)

    with open('feedback_analysis.txt', 'w') as analysis:
        analysis.write(f"Total feedbacks: {len(positive) + len(negative)}\n")
        analysis.write(f"Count of positive feedbacks: {len(positive)}\n")
        analysis.write(f"Count of negative feedbacks: {len(negative)}\n")

    print("Відгуки розділено на позитивні та негативні. Результати збережено у файлі feedback_analysis.txt.")
except FileNotFoundError:
    print("Файл feedback.txt не знайдено.")
