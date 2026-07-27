from turtle import title

import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"


def get_soup(url):
    """Download a webpage and return BeautifulSoup object."""

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to open {url}")
        return None
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")




def extract_book_data(book):

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    rating = book.p["class"][1]

    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    # Get book detail page URL
    relative_link = book.h3.a["href"]

# Build the correct absolute URL
    book_url = urljoin(BASE_URL, relative_link)

    # Visit book page
    detail_soup = get_soup(book_url)
    print(book_url)

    if detail_soup is None:
      print("Failed to open:", book_url)

    if detail_soup:
      breadcrumb = detail_soup.find("ul", class_="breadcrumb")

      if breadcrumb:
        category = breadcrumb.find_all("li")[2].text.strip()
      else:
        category = "Unknown"
    else:
      category = "Unknown"
    
    return {
        "title":title,
        "price": price,
        "rating": rating,
        "availability": availability,
        "category": category
    }
def scrape_multiple_pages(num_pages=5):

    all_books = []

    for page in range(1, num_pages + 1):

        if page == 1:
            url = BASE_URL
        else:
            url = BASE_URL + f"catalogue/page-{page}.html"

        print(f"Scraping Page {page}...")

        soup = get_soup(url)

        if soup is None:
            continue

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            book_data = extract_book_data(book)
            all_books.append(book_data)

    return all_books
def save_to_csv(book_list):

    with open(
        "data_pipeline/books.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "title",
            "price",
            "rating",
            "availability",
            "category"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(book_list)

    print("\nbooks.csv saved successfully!")

def main():

    all_books = scrape_multiple_pages(5)

    print(f"\nTotal Books Collected: {len(all_books)}")

    save_to_csv(all_books)


if __name__ == "__main__":
    main()