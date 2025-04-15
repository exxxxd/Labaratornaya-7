import random

list = [random.randint(1, 10) for _ in range(20)]

dubli = {}

for item in list:
    if item in dubli:
        dubli[item] += 1
    else:
        dubli[item] = 1

print("Список чисел:", list)

hasdubli = False
print("Повторяющиеся элементы в списке:")
for item, count in dubli.items():
    if count > 1:
        print(f"- {item} (встречается {count} раз)")
        hasdubli = True

if not hasdubli:
    print("Повторяющихся чисел нет.")
