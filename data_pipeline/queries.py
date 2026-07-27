import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("data_pipeline/books.db")

queries = {
    "1. All books with rating 5":
    """
    SELECT title, rating
    FROM books
    WHERE rating = 5;
    """,

    "2. Books costing more than £50":
    """
    SELECT title, price
    FROM books
    WHERE price > 50;
    """,

    "3. Number of books in each category":
    """
    SELECT c.name AS category,
           COUNT(*) AS total_books
    FROM books b
    JOIN categories c
        ON b.category_id = c.id
    GROUP BY c.name
    ORDER BY total_books DESC;
    """,

    "4. Average price by category":
    """
    SELECT c.name AS category,
           ROUND(AVG(price), 2) AS avg_price
    FROM books b
    JOIN categories c
        ON b.category_id = c.id
    GROUP BY c.name
    ORDER BY avg_price DESC;
    """,

    "5. Top 10 most expensive books":
    """
    SELECT title, price
    FROM books
    ORDER BY price DESC
    LIMIT 10;
    """
}

for title, sql in queries.items():
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    df = pd.read_sql(sql, conn)
    print(df)




books_df = pd.read_sql("SELECT * FROM books", conn)
categories_df = pd.read_sql("SELECT * FROM categories", conn)

merged_df = pd.merge(
    books_df,
    categories_df,
    left_on="category_id",
    right_on="id",
    suffixes=("_book", "_category")
)

print(merged_df.head())

conn.close()