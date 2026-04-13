import requests
from bs4 import BeautifulSoup 

url = 'https://books.toscrape.com/'

def scrape_books(url):
    response = requests.get(url)
    print(response.status_code)
    if response.status_code != 200:
        return
    
    # set encoding explicity to handle special characters correctly
    response.encoding=response.apparent_encoding
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article",class_="product_pod")

    all_books=[]

    for book in books:
        title = book.h3.a['title']
        price_text = book.find('p',class_='price_color').text
        currency = price_text[0]
        price = float(price_text[1:])


        my_book = {
            'title':title,
            'price':price,
            'currency':currency
        }

        all_books.append(my_book)

    return all_books
books = scrape_books(url)

with open("books.json","w") as f:
    import json


    json.dump(books,f,indent=4,ensure_ascii=False)   # ensure_ascii=False because the currency was not being shown in GBP
        
        



scrape_books(url)

# now convert this to csv
import csv

books = scrape_books(url)  # already a list of dicts

with open("books.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price', 'currency'])
    
    writer.writeheader()
    writer.writerows(books)