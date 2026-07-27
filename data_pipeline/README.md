# 📚 Book Data Pipeline

## Project Overview

This project scrapes book information from https://books.toscrape.com, cleans the data, converts prices from GBP to INR, stores the data in a normalized SQLite database, and performs SQL analysis using Python and Pandas.

---

## Features

- Web scraping using Requests and BeautifulSoup
- Data cleaning using Pandas
- Price conversion (GBP → INR)
- SQLite normalized database
- SQL queries
- Pandas `read_sql()`
- Pandas `merge()`

---

## Folder Structure

```
data_pipeline/
│
├── scrape_books.py
├── clean_data.py
├── database.py
├── queries.py
├── books.csv
├── clean_books.csv
├── books.db
└── README.md
```

---

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- pandas
- lxml

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1: Scrape Books

```bash
python scrape_books.py
```

### Step 2: Clean Data

```bash
python clean_data.py
```

### Step 3: Create Database

```bash
python database.py
```

### Step 4: Execute SQL Queries

```bash
python queries.py
```

---

## Database Design

### Categories Table

- id
- name

### Books Table

- id
- title
- price
- rating
- availability
- category_id
- price_inr

The database uses a foreign key relationship between the `books` and `categories` tables.

---

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite