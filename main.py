from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import os
import urllib

service = ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

driver = webdriver.Chrome(service=service)

SAVE_PATH = "images"

link = "" # shutterstock search link
pages = 10

start_from = 1
image = 1
for i in range(start_from, start_from + pages + 1):
    url = f"{link}&page={i}" if "?" in link else f"{link}?page={i}"
    driver.get(url)
    print(f"Page {i} loaded")

    # wait for site to load
    driver.implicitly_wait(5)

    thumbnails = driver.find_elements(by=By.XPATH, value="//*[contains(@class, 'mui-') and contains(@class, '-thumbnail')]")

    for i in thumbnails:
        img_link = i.get_property("src")
        print(f"Downloading image {img_link}")
        os.makedirs(SAVE_PATH, exist_ok=True)
        urllib.request.urlretrieve(img_link, os.path.join(SAVE_PATH, f"{image}.jpg"))
        image += 1
