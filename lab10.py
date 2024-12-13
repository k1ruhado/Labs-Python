# Завдання 1: Підрахунок повторень елемента в кортежі
def count_occurrences(data, num):
    return data.count(num)

tuple_data = (1, 2, 3, 2, 4, 2, 5)
number_to_check = 2  # Замінити на потрібне число для перевірки
count = count_occurrences(tuple_data, number_to_check)
print(f"Число {number_to_check} повторюється {count} раз(ів) у кортежі.")

# Завдання 2: Знайти індекс елемента в кортежі
def find_index(data, num):
    if num in data:
        return data.index(num)
    return -1

number_to_find = 3  # Замінити на потрібне число для пошуку
index = find_index(tuple_data, number_to_find)
if index != -1:
    print(f"Число {number_to_find} знаходиться на індексі {index}.")
else:
    print(f"Число {number_to_find} не знайдено в кортежі.")

# Завдання 3: Новий кортеж з першого та останнього елемента
def create_new_tuple(data):
    return (data[0], data[-1])

new_tuple = create_new_tuple(tuple_data)
print(f"Новий кортеж: {new_tuple}")

# Завдання 4: Перевірка, чи всі елементи однакові
def are_elements_equal(data):
    return len(set(data)) == 1

if are_elements_equal(tuple_data):
    print("Усі елементи кортежу однакові.")
else:
    print("Елементи кортежу різні.")

# Завдання 5: Сума числових елементів
def sum_numeric_elements(data):
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, str) and item.isdigit():
            total += int(item)
    return total

mixed_tuple = (10, 20, "a", "30", "bcd")
total_sum = sum_numeric_elements(mixed_tuple)
print(f"Сума елементів дорівнює {total_sum}")

# Завдання 6: Зміна останньої цифри в кортежах списку
def replace_last_element(lst, new_value):
    return [tuple(item[:-1] + (new_value,)) for item in lst]

list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100  # Замінити на потрібне значення
new_list = replace_last_element(list1, new_value)
print(f"Результат: {new_list}")

# Завдання 7: Рахуємо час із файлу
def count_times_from_file(filename):
    time_counts = {}
    try:
        with open(filename, 'r') as handle:
            for line in handle:
                if line.startswith("From "):
                    time = line.split()[5].split(":")[0]
                    time_counts[time] = time_counts.get(time, 0) + 1
    except FileNotFoundError:
        print("Файл не знайдено.")
    return sorted(time_counts.items())

filename = "mbox-short.txt"  # Замінити на ім'я файлу
sorted_times = count_times_from_file(filename)
for time, count in sorted_times:
    print(time, count)

# Завдання 8*: Обчислення відстані для дрона
def calculate_total_distance(points, path):
    total_distance = 0
    for i in range(len(path) - 1):
        start, end = sorted((path[i], path[i + 1]))
        total_distance += points.get((start, end), 0)
    return total_distance

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
path = [0, 1, 3, 2, 0]
total_distance = calculate_total_distance(points, path)
print(f"Загальна відстань: {total_distance}")
