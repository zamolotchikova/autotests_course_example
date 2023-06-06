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
