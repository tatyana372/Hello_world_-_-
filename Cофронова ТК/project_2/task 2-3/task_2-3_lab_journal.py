researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_title = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод по эксперименту: ")

with open("journal.txt", "w", encoding="utf-8") as file:
  file.write("+--------------------------------------------------+\n")
  file.write("| Электронный лабораторный журнал                  |\n")
  file.write("+--------------------------------------------------+\n")
  file.write(f"| ФИО исследователя : {researcher_name:<40}|\n")
  file.write(f"| Дата             : {experiment_date:<40}|\n")
  file.write(f"| Эксперимент      : {experiment_title:<40}|\n")
  file.write("+--------------------------------------------------+\n")
  file.write("| Вывод:                                           |\n")
  file.write("+--------------------------------------------------+\n")
  
print("Данные успешно записаны в файл journal.txt")
