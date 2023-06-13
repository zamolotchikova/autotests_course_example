# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
purchases = []
file = open(r'test_file\task_3.txt', mode='r', encoding='utf-8')
purchase = 0
for i in file:
    if i == '\n':
        purchases.append(purchase)
        purchase = 0
    else:
        purchase += int(i)

purchases = sorted(purchases, reverse=True)
print(purchases)
three_most_expensive_purchases = sum(purchases[:3])
print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
