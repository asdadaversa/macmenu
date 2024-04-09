import time
import os
import django

from unidecode import unidecode
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'macmenu.settings')
django.setup()

from products.models import Products


def get_links(file_address: str):
    with open(file_address, "r+") as file:
        all_links = [row.strip() for row in file]

    return all_links


def parse_menu(all_links: list[str]):

    for link in all_links:

        options = Options()
        service = Service()
        options.headless = True
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(link)
        html = driver.page_source
        time.sleep(10)
        soup = BeautifulSoup(html, "html.parser")

        try:
            name = soup.find("title").get_text().strip()
            description = soup.find("div", class_="cmp-text").get_text().strip()
            latinos_name = unidecode(soup.find("title").get_text().strip()).replace(" ", "").lower()

            all_nutrition = soup.find_all("span", class_="sr-only sr-only-pd")
            calories = all_nutrition[2].text.replace('\n', '').strip().replace("  ", "")
            fats = all_nutrition[5].text.replace('\n', '').strip().replace("  ", "")
            carbs = all_nutrition[8].text.replace('\n', '').strip().replace("  ", "")
            proteins = all_nutrition[11].text.replace('\n', '').strip().replace("  ", "")

            all_metric2 = soup.find_all("span", class_="value")
            unsaturated_fats = all_metric2[4].text.replace('\n', '').strip().replace("  ", "").split("(")[0]
            sugar = all_metric2[5].text.replace('\n', '').strip().replace("  ", "").split("(")[0]
            salt = all_metric2[6].text.replace('\n', '').strip().replace("  ", "").split("(")[0]
            portion = all_metric2[7].text.replace('\n', '').strip().replace("  ", "").split("(")[0]


            print(f"name: {name}")
            print(link)
            print(latinos_name)
            print(f"description: {description}")
            print(f"calories: {calories}")
            print(f"fats: {fats}")
            print(f"carbs: {carbs}")
            print(f"proteins: {proteins}")
            print(f"unsaturated_fats: {unsaturated_fats}")
            print(f"sugar: {sugar}")
            print(f"salt: {salt}")
            print(f"portinon: {portion}")

            product = Products.objects.create(
                latinos_name=latinos_name,
                name=name,
                description=description,
                calories=calories,
                fats=fats,
                carbs=carbs,
                proteins=proteins,
                unsaturated_fats=unsaturated_fats,
                sugar=sugar,
                salt=salt,
                portion=portion
            )
        except Exception as e:
            print(f"Error saving product: {e}")
            continue
        driver.quit()


all_links = get_links("../mac_product_test.txt")
parse_menu(all_links)
