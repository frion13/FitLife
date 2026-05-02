WATER_PER_KG = 30
print("Здравствуйте!")
user_name = input("Введите имя: ")
user_age = int(input("Введите количество полных лет: "))
user_weight = float(input("Введите ваш вес в кг, например, 50.6: "))
user_height = float(input("Введите ваш рост в метрах, например, 1.7: "))

# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / 1000, 1)

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print('Расчет окончен. Будьте здоровы!')
