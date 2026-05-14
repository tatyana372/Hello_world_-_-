N = int(input("Введите количество чисел (N): "))

f = float(input("Введите первое число: "))

max_val = f

i = 2

while i <= N:
    x = float(input(f"Введите число {i}: "))

    if x > max_val:
        max_val = x

    i = i + 1

print(f"Максимальное число: {max_val}")