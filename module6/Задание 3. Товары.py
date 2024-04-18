# # Задание 3. Товары
# Что нужно сделать
# В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды товаров,
# второй — за списки количества разнообразных товаров на складе:

goods = {
    "Лампа": "12345",
    "Стол": "23456",
    "Диван": "34567",
    "Стул": "45678",
}

store = {
    "12345": [{"quantity": 27, "price": 42}],
    "23456": [{"quantity": 22, "price": 510},
              {"quantity": 32, "price": 520}],
    "34567": [{"quantity": 2, "price": 1200},
              {"quantity": 1, "price": 1150}],
    "45678": [{"quantity": 50, "price": 100},
              {"quantity": 12, "price": 95},
              {"quantity": 43, "price": 97},],
}

# Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров. Цена указана за одну штуку.
# Напишите программу, которая рассчитывает общую стоимость позиций для каждого товара на складе и выводит эту
# информацию на экран.
#
# Результат работы программы:
# Лампа — 27 штук, стоимость 1134 рубля.
# Стол — 54 штуки, стоимость 27 860 рублей.
# Диван — 3 штуки, стоимость 3550 рублей.
# Стул — 105 штук, стоимость 10 311 рублей.

# for i_key in goods.keys():
#     total_quantity = 0
#     total_price = 0
#     for i_list in range(len(store[goods[i_key]])):
#         total_quantity += store[goods[i_key]][i_list]['quantity']
#         total_price += store[goods[i_key]][i_list]['quantity'] * store[goods[i_key]][i_list]['price']
#     print(f'{i_key} - {total_quantity} шт, стоимость {total_price} рубля')

# или

for name, article in goods.items():
    total_quantity = 0
    total_price = 0
    for i_good in store[article]:: # todo для чего ты используешь range(len(...)), цикл for умеет доставать объекты из коллекции
        total_quantity += i_good['quantity']
        total_price += i_good['quantity'] * i_good['price']
    print(f'{name} - {total_quantity} шт, стоимость {total_price} рубля')
