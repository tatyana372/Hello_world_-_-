print("=== Анализ последовательности ДНК ===\n")
dna = input("Введите последовательность ДНК: ")
dna = dna.upper()
print(f"\nПоследовательность в верхнем регистре: {dna}\n")
print("Подсчёт нуклеотидов:")

count_a = dna.count("A")
count_t = dna.count("T")
count_g = dna.count("G")
count_c = dna.count("C")

print(f"A: {count_a}")
print(f"T: {count_t}")
print(f"G: {count_g}")
print(f"C: {count_c}")

total_length = len(dna)
print(f"\nОбщая длина: {total_length} нуклеотидов")

print("\nПроцентное содержание:")

if total_length > 0:
    percent_a = (count_a / total_length) * 100
    percent_t = (count_t / total_length) * 100
    percent_g = (count_g / total_length) * 100
    percent_c = (count_c / total_length) * 100

    print(f"A: {percent_a:.2f}%")
    print(f"T: {percent_t:.2f}%")
    print(f"G: {percent_g:.2f}%")
    print(f"C: {percent_c:.2f}%")
else:
    print("Последовательность пустая, процентное содержание не может быть вычислено.")
