import psycopg2
from psycopg2 import Error

def main():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            host="localhost",
            port=5435,
            dbname="student",
            user="postgres_task",
            password="student"
        )
        print("✅ Соединение с PostgreSQL успешно установлено")

        cursor = connection.cursor()

        sql_query = "SELECT id, name, category FROM products LIMIT 5;"
        cursor.execute(sql_query)

        records = cursor.fetchall()
        print("\n📊 Результаты запроса:")
        for row in records:
            print(f"ID: {row[0]} | Название: {row[1]} | Категория: {row[2]}")

    except Error as e:
        print(f"\n❌ Ошибка при работе с PostgreSQL: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("\n🔌 Соединение с базой данных закрыто.")

if __name__ == "__main__":
    main()