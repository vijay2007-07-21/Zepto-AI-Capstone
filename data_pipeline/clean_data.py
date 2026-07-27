import pandas as pd

# Load the scraped data
df = pd.read_csv("data_pipeline/books.csv")

# Remove the £ symbol and convert to float
df["price"] = df["price"].str.replace("£", "", regex=False).astype(float)

# Convert ratings to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

# Convert availability to boolean
df["availability"] = df["availability"] == "In stock"

# Add INR price
EXCHANGE_RATE = 105.50
df["price_inr"] = (df["price"] * EXCHANGE_RATE).round(2)

# Save cleaned data
df.to_csv("data_pipeline/clean_books.csv", index=False)

print("Data cleaned successfully!")
print(df.head())