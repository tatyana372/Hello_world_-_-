N = int(input("Введите количество элементов (N): "))

A = []
print(f"Введите {N} чисел (каждое с новой строки):")
for _ in range(N):
    A.append(float(input()))

i = 1
sum_val = 0

while i <= N:
    if i % 2 != 0:
        sum_val = sum_val + A[i - 1]

    i = i + 1

print("Сумма элементов с нечетными индексами:", sum_val)