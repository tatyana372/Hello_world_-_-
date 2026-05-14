N = int(input("Введите число N: "))

Sum = 0
i = 1

while i <= N:
    Sum = Sum + i ** 2

    i = i + 1

print(f"Сумма квадратов первых {N} чисел: {Sum}")