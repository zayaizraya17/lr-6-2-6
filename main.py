import random
num = [[random.randint(-10, 10) for i in range(4)] for j in range(20)]
print(num)
new = set()
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        for k in range(4):
            for l in range(4):
                new.add((num[i][k], num[j][l]))
print("Список уникальных пар:", list(new))
x = int(input("Введите целое число: "))
count = 0
for i in new:
    if sum(i) < x:
        count += 1
print(f"Количество пар с суммой меньше {x}: {count}")