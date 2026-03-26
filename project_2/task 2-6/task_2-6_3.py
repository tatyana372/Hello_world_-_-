donor = input("Группа крови донора (0, A, B, AB): ").upper()
recipient = input("Группа крови пациента (0, A, B, AB): ").upper()
if donor == '0':
    print("Переливание возможно (универсальный донор)")
elif donor == recipient:
    print("Переливание возможно (группы совпадают)")
else:
    print("Переливание невозможно")