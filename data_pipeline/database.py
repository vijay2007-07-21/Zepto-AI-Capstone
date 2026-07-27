import sqlite3
import pandas as pd

# Load cleaned data
df = pd.read_csv("data_pipeline/clean_books.csv")

# Connect to SQLite database
conn = sqlite3.connect("data_pipeline/books.db")
cursor = conn.cursor()

# Create categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    rating INTEGER,
    availability BOOLEAN,
    category_id INTEGER,
    price_inr REAL,
    FOREIGN KEY(category_id) REFERENCES categories(id)
)
""")

# Insert unique categories
categories = df["category"].unique()

for category in categories:
    cursor.execute(
        "INSERT OR IGNORE INTO categories(name) VALUES (?)",
        (category,)
    )

# Insert books
for _, row in df.iterrows():

    cursor.execute(
        "SELECT id FROM categories WHERE name=?",
        (row["category"],)
    )

    category_id = cursor.fetchone()[0]

    cursor.execute("""
    INSERT INTO books
    (title, price, rating, availability, category_id, price_inr)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        row["title"],
        row["price"],
        int(row["rating"]),
        bool(row["availability"]),
        category_id,
        row["price_inr"]
    ))

conn.commit()
conn.close()

print("Database created successfully!")