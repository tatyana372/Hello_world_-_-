volume_input = input("Введите необходимый объем раствора (в мл): ")
volume = float(volume_input)

salt_mass = volume * 0.009

water_volume = volume

print("\n--- Результаты расчета ---")
print(f"Общий объем: {volume:.2f} мл")
print(f"Масса соли:  {salt_mass:.3f} г")
print(f"Объем воды:  {water_volume:.2f} мл")
print("-" * 26)

file = open('recipe.txt', 'w', encoding='utf-8')
file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
file.write("-" * 23 + "\n")
file.write(f"Общий объем: {volume:.2f} мл\n")
file.write(f"Масса соли:  {salt_mass:.3f} г\n")
file.write(f"Объем воды:  {water_volume:.2f} мл\n")
file.close()
