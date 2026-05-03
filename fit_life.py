WATER_PER_KG = 30
WATER_ML = 1000
print('Здравствуйте!')

user_name = input("Введите имя: ")
while True:
    if not user_name.strip() or user_name.isspace():
        user_name = input("Введите имя: ")
    break

user_age = int(input('Введите количество полных лет: '))
while True:
    if user_age <= 0:
        user_age = input('Введите количество полных лет: ')
    break

user_weight = float(input('Введите ваш вес в кг, например, 50.6: '))
while True:
    if user_weight <= 0:
        user_weight = float(input('Введите ваш вес в кг, например, 50.6: '))
    break

user_height = float(input('Введите ваш рост в метрах, например, 1.7: '))
while True:
    if user_height <= 0:
        user_height = float(input(
            'Введите ваш рост в метрах, например, 1.7: '))
    break

# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)
water_l = round(user_weight * WATER_PER_KG / WATER_ML, 1)

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print('Расчет окончен. Будьте здоровы!')
