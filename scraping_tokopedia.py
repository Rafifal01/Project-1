from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = input("Masukkan url toko : ")

if url :
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    data = []
    for i in range(0, 30):
        soup = BeautifulSoup(driver.page_source, "html.parser")
        containers = soup.findAll('article', attrs = {'class':'css-ccpe8t'})

        for container in containers:
            try:
                produk = container.find('p', attrs = {'data-unify' : 'Typography'}).text
                nama = container.find('span', attrs = {'class' : 'name'}).text
                waktu = container.find('div', attrs={'class': 'css-1w6pe1p'}).text
                review = container.find('span', attrs={'data-testid': 'lblItemUlasan'}).text
                bintang = container.find('div', attrs={'data-testid': 'icnStarRating'})['aria-label']
                data.append((produk, nama, waktu, review, bintang))
                
            except AttributeError:
                continue

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
        time.sleep(3)
        
        
    print(data)
    df = pd.DataFrame(data, columns=[["Produk","Nama","Waktu","Review","Rating"]])
    df.to_csv("Tokopedia_JulClothing.csv", index=False)