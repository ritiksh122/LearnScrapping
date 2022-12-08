from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH="C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome()

driver.get("https://www.nytimes.com/section/technology")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "stream-panel"))
    )
    contents = driver.find_elements(By.CSS_SELECTOR,'li.css-112uytv')
    for content in contents:
        writers=content.find_element(By.CSS_SELECTOR,'div span')
        Authors=writers.text
        print(writers.text)
        news=content.find_element(By.CSS_SELECTOR,'a p.css-1pga48a')
        print(news.text)
        date=content.find_element(By.CSS_SELECTOR,'div.css-e0xall')
        print(date.text)
        heading=content.find_element(By.CSS_SELECTOR,'h2.css-1kv6qi')
        print(heading.text)
        link=content.find_element(By.TAG_NAME, 'a')
        print(link.get_attribute("href"))
       

          


   





    
finally:
    driver.quit()