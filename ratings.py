import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    prodName = []

    prodAsin = []

    prodRatings = []

    keyword = input('Enter Keyword to Search: ')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for i in range(1, 21):

        time.sleep(10)

        driver.get('https://www.amazon.com/s?k=' + keyword + '&page=' + str(i))

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for el in soup.find_all("div", {"data-component-type": "s-search-result"}):
            print(el.find_next("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).span.text)

            prodName.append(el.find_next("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).span.text)

            print(el.find_next("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})[
                      "href"].rsplit('/')[3])

            prodAsin.append(el.find_next("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})[
                                "href"].rsplit('/')[3])

            print(el.find_next("span", {"class": "a-size-base s-underline-text"}).text)

            prodRatings.append(el.find_next("span", {"class": "a-size-base s-underline-text"}).text)

            print("\n")

    driver.quit()

    file = open("csv/ratings_" + keyword.replace(" ", "_") + ".csv", "w", encoding='utf-8')

    with file:
        w = csv.writer(file)
        w.writerows(zip(prodName, prodAsin, prodRatings))


main()
