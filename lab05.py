# Завдання 1. Вивести на екран послідовність чисел від 1 до 20.
print("Завдання 1:")
for i in range(1, 21):
    print(i, " ")
print()

# Завдання 2. Вивести всі числа від A до B включно, в порядку зростання або спадання.
print("Завдання 2:")
A, B = 1, 10  
if A < B:
    for i in range(A, B + 1):
        print(i, " ")
else:
    for i in range(A, B - 1, -1):
        print(i, " ")
print()

# Завдання 3. Добуток 10 чисел, що вводить користувач.
print("Завдання 3:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
product = 1
for num in numbers:
    product *= num
print("Добуток:", product)

# Завдання 4. Вивести парні числа серед 10 чисел, що вводить користувач.
print("Завдання 4:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
even_numbers = [num for num in numbers if num % 2 == 0]
print("Парні числа:", even_numbers)

# Завдання 5. Вивести найбільше з 10 чисел, що вводить користувач.
print("Завдання 5:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
print("Найбільше число:", max(numbers))

# Завдання 6. Вивести символи з парними індексами рядка.
print("Завдання 6:")
user_string = "abcdef"  
even_index_chars = user_string[::2]
print("Символи з парними індексами:", even_index_chars)

# Завдання 7. Побудова шаблону зірочок.
print("Завдання 7:")
n = 5
for i in range(1, n + 1):
    print("* " * i)
for i in range(n - 1, 0, -1):
    print("* " * i)
