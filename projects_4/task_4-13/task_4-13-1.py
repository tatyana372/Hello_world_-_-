A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
C = float(input("Введите число C: "))
D = float(input("Введите число D: "))

min_val = A

if B < min_val:
    min_val = B

if C < min_val:
    min_val = C

if D < min_val:
    min_val = D

print("Минимальное число:", min_val)