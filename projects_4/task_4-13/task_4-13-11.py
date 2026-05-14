N = int(input("Введите количество элементов (N): "))
A = []
print(f"Введите {N} чисел (каждое с новой строки):")
for _ in range(N):
    A.append(float(input()))

sum_val = 0
count = 0
i = 1

while i <= N:
    if i % 2 == 0:
        sum_val = sum_val + A[i - 1]
        count = count + 1

    i = i + 1

if count > 0:
    aver = sum_val / count
else:
    aver = 0

print("Среднее арифметическое элементов с четными индексами:", aver)