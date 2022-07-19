import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    prodName = []

    prodAsin = []

    keyword = input('Enter Keyword to Search: ')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for i in range(1, 8):

        time.sleep(10)

        driver.get('https://www.amazon.in/s?k=' + keyword + '&rh=p_n_availability%3A1318485031&page=' + str(i))

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for el in soup.find_all("span", {"aria-label": "Only 1 left in stock."}):

            print(el.find_previous("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).span.text)

            prodName.append(el.find_previous("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).span.text)

            print(el.find_previous("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})["href"].rsplit('/')[3])

            prodAsin.append(el.find_previous("a", {
                "class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})["href"].rsplit('/')[3])


    driver.quit()

    file = open("csv/1" + keyword.replace(" ", "_") + ".csv", "w", encoding='utf-8')

    with file:
        w = csv.writer(file)
        w.writerows(zip(prodName, prodAsin))

main()
