import faker
import sqlite3
from random import randint

# Создание экземпляра Faker
generator = faker.Faker()

# Подключение к базе данных SQLite
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Создание таблицы, если её нет
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    age INTEGER CHECK (age >= 0),
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT UNIQUE NOT NULL,
    country TEXT,
    city TEXT,
    time_in_app INTEGER CHECK (time_in_app >= 0),
    favorite_genres TEXT
)
""")

# SQL-запрос для вставки данных
insert_query = """
INSERT INTO Users (first_name, last_name, middle_name, age, email, phone_number, country, city, time_in_app, favorite_genres)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Генерация и вставка 20000 пользователей
users = []
for _ in range(20000):
    users.append((
        generator.first_name(),
        generator.last_name(),
        generator.first_name(),
        generator.random_int(min=10, max=80),
        f'a{randint(1, 1000)}{generator.free_email()}',
        generator.phone_number(),
        generator.country(),
        generator.city(),
        generator.random_int(min=0, max=10000),
        ", ".join(generator.words(nb=3, ext_word_list=['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Fantasy', 'Mystery', 'Romance', 'Thriller']))
    ))

cursor.executemany(insert_query, users)
conn.commit()

# Закрытие соединения
cursor.close()
conn.close()
