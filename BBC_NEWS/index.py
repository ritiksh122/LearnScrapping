from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd



PATH="C:\Program Files (x86)"

driver=webdriver.Chrome()

driver.get("https://www.bbc.com")

travel=driver.find_element(By.CSS_SELECTOR,"li.orb-nav-newsdotcom a")
travel.click()

Titles=[]
Links=[]



element=driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[4]/div[11]/div/div/div[2]/ol")
titles=element.find_elements(By.CSS_SELECTOR,"span.gs-c-promo-heading__title")
links=element.find_elements(By.CSS_SELECTOR,"a.gs-c-promo-heading")



for i in range(len(titles)):
    Titles.append(titles[i].text)
    Links.append(links[i].get_attribute('href'))



driver.quit()

df=pd.DataFrame({'Titles':Titles,'Links':Links})
df.to_csv('data.csv',index=False)
print(df)










