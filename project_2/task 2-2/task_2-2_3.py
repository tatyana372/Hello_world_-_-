equipment_name = "Микроскоп оптический"
inventory_number = "INV-2024-001"
is_functional = True
quantity = 3
functional_status = "Исправен" if is_functional else "Неисправен"

print("Оборудование\t\tИнвентарный номер\tСостояние\tКоличество")
print(f"{equipment_name}\t\t{inventory_number}\t\t{functional_status}\t\t{quantity}")