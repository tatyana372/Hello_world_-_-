N = int(input("Введите количество элементов (N): "))

A = []
print(f"Введите {N} чисел (каждое с новой строки):")
for _ in range(N):
    A.append(float(input()))

Sum = 0
i = 1

while i <= N:
    Sum = Sum + A[i - 1]
    i = i + 1

if N > 0:
    average = Sum / N
else:
    average = 0

print("Среднее арифметическое:", average)