N = int(input("Введите количество элементов (N): "))

A = []
print(f"Введите {N} целых чисел (каждое с новой строки):")
for _ in range(N):
    A.append(int(input()))

i = 1
sum_val = 0

while i <= N:
    if A[i - 1] % 2 != 0:
        sum_val = sum_val + A[i - 1]

    i = i + 1

print("Сумма нечетных элементов:", sum_val)