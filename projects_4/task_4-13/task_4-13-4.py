N = int(input("Введите число N: "))

Sum = 0
i = 1

while i <= N:
    Sum = Sum + i
    i = i + 1

print(f"Сумма первых {N} чисел: {Sum}")