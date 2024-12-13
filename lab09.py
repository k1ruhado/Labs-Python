# Завдання 1: Переклад тексту за словником

import os

def translate_text():
    # Перевірка наявності файлів
    if not os.path.exists("dict.txt"):
        print("Помилка: файл 'dict.txt' не знайдено.")
        return

    if not os.path.exists("translate.txt"):
        print("Помилка: файл 'translate.txt' не знайдено.")
        return

    # Читання словника
    with open("dict.txt", "r", encoding="utf-8") as dict_file:
        dictionary = {}
        for line in dict_file:
            if '\t-\t' in line:  # Перевірка наявності роздільника
                eng, ukr = line.strip().split('\t-\t')
                dictionary[eng] = ukr

    # Читання тексту для перекладу
    with open("translate.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()

    # Переклад тексту
    words = text.split()
    translated_words = [dictionary.get(word, word) for word in words]

    # Запис результату у файл
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(" ".join(translated_words))

    print("Переклад завершено. Результат збережено у 'output.txt'.")

# Виклик функції для перекладу
translate_text()

# Завдання 2: Пошук країн за мовою

def find_countries_by_language():
    # Перевірка наявності файлу
    if not os.path.exists("input_countries.txt"):
        print("Помилка: файл 'input_countries.txt' не знайдено.")
        return

    # Читання файлу з країнами та мовами
    with open("input_countries.txt", "r", encoding="utf-8") as countries_file:
        country_language_map = {}
        for line in countries_file:
            if ' : ' in line:  # Перевірка наявності роздільника
                country, languages = line.strip().split(" : ")
                country_language_map[country] = languages.split()

    # Введення мови
    language = input("Введіть мову: ").strip()

    # Пошук країн
    countries = [country for country, languages in country_language_map.items() if language in languages]

    # Виведення результату
    if countries:
        print("Країни, де розмовляють цією мовою:", ", ".join(countries))
    else:
        print("Країн з цією мовою не знайдено.")

# Виклик функції для пошуку країн
find_countries_by_language()

# Завдання 3: Інформація про купе

def coupe_info():
    # Задана інформація про вагон
    wagon = [
        {1: "м", 2: None, 3: None, 4: "ж"},
        {1: None, 2: None, 3: None, 4: None},
        {1: "м", 2: "ж", 3: None, 4: None},
    ]

    # Список повністю вільних купе
    free_coupes = [index + 1 for index, coupe in enumerate(wagon) if all(place is None for place in coupe.values())]

    # Список всіх вільних місць
    free_places = [(index + 1, place) for index, coupe in enumerate(wagon) for place, occupant in coupe.items() if occupant is None]

    # Список вільних нижніх та верхніх місць
    free_lower_places = [(index + 1, place) for index, coupe in enumerate(wagon) for place, occupant in coupe.items() if occupant is None and place % 2 != 0]
    free_upper_places = [(index + 1, place) for index, coupe in enumerate(wagon) for place, occupant in coupe.items() if occupant is None and place % 2 == 0]

    # Список вільних місць з чоловічою або жіночою компанією
    free_in_male_company = [(index + 1, place) for index, coupe in enumerate(wagon) if all(occupant in [None, "м"] for occupant in coupe.values()) for place, occupant in coupe.items() if occupant is None]
    free_in_female_company = [(index + 1, place) for index, coupe in enumerate(wagon) if all(occupant in [None, "ж"] for occupant in coupe.values()) for place, occupant in coupe.items() if occupant is None]

    # Виведення результатів
    print("Повністю вільні купе:", free_coupes)
    print("Вільні місця:", free_places)
    print("Вільні нижні місця:", free_lower_places)
    print("Вільні верхні місця:", free_upper_places)
    print("Вільні місця з чоловічою компанією:", free_in_male_company)
    print("Вільні місця з жіночою компанією:", free_in_female_company)

# Виклик функції для інформації про купе
coupe_info()
