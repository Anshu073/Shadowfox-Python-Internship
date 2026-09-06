# Web Scraper

import requests
from bs4 import BeautifulSoup

url = "https://www.shadowfox.org.in"

try:
    response = requests.get(url)
    print("Status code:", response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.text
    print("Title of page:", title)

    headings = soup.find_all(['h1', 'h2', 'h3'])
    print("\nTotal headings found:", len(headings))

    for h in headings:
        print(h.text)

    links = soup.find_all('a')
    print("\nTotal links found:", len(links))

    file = open("scraped_data.txt", "w", encoding="utf-8")
    file.write("Title: " + title + "\n\n")
    file.write("Headings:\n")
    for h in headings:
        file.write(h.text + "\n")
    file.write("\nTotal links: " + str(len(links)))
    file.close()

    print("\nData saved in scraped_data.txt file")

except Exception as e:
    print("Something went wrong:", e)