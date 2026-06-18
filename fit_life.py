# Проект FitLife - MVP версия 1.1

# Задаем константы
WATER_PER_KG = 30
MLITER_PER_LITER = 1000

MIN_AGE = 5
MAX_AGE = 99

MIN_WEIGHT = 10
MAX_WEIGHT = 500

MIN_HEIGHT = 0.5
MAX_HEIGHT = 2.60

ROUND_DEPTH = 1

ERROR_MESSAGE = "Ошибка: Введено неверное значение."

# Запрос имени пользователя и его проверка
user_name = input("Привет! Как я могу к тебе обращаться? ")
while not user_name:
    print(ERROR_MESSAGE)
    user_name = input("Пожалуйста, представьтесь: ")

# Запрос возраста и его проверка
while True:
    try:
        user_age = int(input(
            "Укажи, пожалуйста, свой возраст "
            f"(от {MIN_AGE} до {MAX_AGE} лет): "))
        if (MIN_AGE <= user_age <= MAX_AGE):
            break
        print(ERROR_MESSAGE)
    except ValueError:
        print(ERROR_MESSAGE)

# Запрос веса в кг.
while True:
    try:
        user_weight = float(input(
            "Укажи, пожалуйста, свой вес в килограммах, "
            "используя точку (например 75.6): "))
        if (MIN_WEIGHT <= user_weight <= MAX_WEIGHT):
            break
        print(ERROR_MESSAGE)
    except ValueError:
        print(ERROR_MESSAGE)

# Запрос роста в метрах
while True:
    try:
        user_height = float(input(
            "Укажи, пожалуйста, свой рост в метрах, "
            "используя точку (например 1.80): "))
        if (MIN_HEIGHT <= user_height <= MAX_HEIGHT):
            break
        print(ERROR_MESSAGE)
    except ValueError:
        print(ERROR_MESSAGE)

# Расчет индекса массы тела
user_bmi = round((user_weight / (user_height ** 2)), ROUND_DEPTH)

# Расчет нормы воды
water_mliter = (user_weight * WATER_PER_KG)
water_liter = round((water_mliter / MLITER_PER_LITER), ROUND_DEPTH)

# Вывод резуьтата
print(f"""
Отчет для пользователя: {user_name} ({user_age} г.)
Твой Индекс Массы Тела: {user_bmi}
Рекомендуемая норма воды: {water_liter} л. в день

Расчет окончен. Будьте здоровы!""")
