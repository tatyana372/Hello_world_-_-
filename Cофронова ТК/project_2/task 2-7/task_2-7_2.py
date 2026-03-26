sequences = ["ATATACGCGTA", "CTTCGGNGGA"]
for seq in sequences:
    print(f"Последовательность: {seq}")  
    for letter in seq:
        print(letter)
    print("-" * 20) 
print("Цикл выполнен")