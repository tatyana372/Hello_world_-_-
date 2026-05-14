N = int(input("Введите количество элементов (N): "))

A = []
print(f"Введите {N} чисел (каждое с новой строки):")
for _ in range(N):
    A.append(float(input()))

count = 0
i = 1

while i <= N:
    if A[i - 1] > 0:
        count = count + 1

    # i = i + 1
    i = i + 1

print("Количество положительных чисел:", count)