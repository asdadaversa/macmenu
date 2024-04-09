from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


url = "https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"


def parse_all_menu_links(url: str):

    options = Options()
    service = Service()
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    linki = soup.find_all("a")
    with open("../mac_product_test.txt", "w+") as file:
        for link in linki:
            href = link.get("href")
            if href and "/ua/uk-ua/product" in href:
                file.write(f"https://www.mcdonalds.com{href}\n")

    driver.quit()


parse_all_menu_links(url)
