from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

PATH="C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome()

driver.get("https://www.nytimes.com/section/technology")

titles=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/h2")
descs=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/p")
links=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a")
dates=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/span")
authors=driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/div/p/span")
Titles=[]
Descs=[]
Links=[]
Dates=[]
Authors=[]
for i in range(len(titles)):
    Titles.append(titles[i].text)
    Descs.append(descs[i].text)
    Links.append(links[i].get_attribute('href'))
    Dates.append(dates[i].text)
    Authors.append(authors[i].text)

driver.quit()


df=pd.DataFrame({'Titles':Titles,'Descriptions':Descs,'Links':Links,'Dates':Dates,'Authors':Authors})
df.to_csv('data.csv',index=False)
print(df)