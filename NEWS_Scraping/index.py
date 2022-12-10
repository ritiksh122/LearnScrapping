from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import pandas as pd

s=Service('C:\Program Files (x86)\chromedriver.exe')

driver=webdriver.Chrome(service=s)
website='https://www.bbc.com/news/business'
driver.get(website)

titles=driver.find_elements(By.XPATH,"//div[@id='lx-stream']/div/ol/li/article/header/div/h3/a/span")
article_links=driver.find_elements(By.XPATH,"//div[@id='lx-stream']/div/ol/li/article/header/div/h3/a")
img_links=driver.find_elements(By.XPATH,"//div[@id='lx-stream']/div/ol/li/article/div/div/div/a/div/img")
date_time=driver.find_elements(By.XPATH,"//div[@id='lx-stream']/div/ol/li/article/div/div/time/span[2]")

Titles=[]
Article_links=[]
Img_links=[]
Date_time=[]
Article_content=[]

for i in range(len(titles)):
    Titles.append(titles[i].text)
    Article_links.append(article_links[i].get_attribute('href'))
    Img_links.append(img_links[i].get_attribute('src'))
    Date_time.append(date_time[i].text)

for x in Article_links:
    driver.get(x)
    main_content=driver.find_elements(By.XPATH,'//div[@data-component="text-block"]/div/p')
    temp=''
    for y in range(len(main_content)):
       temp=temp+ main_content[y].text
    Article_content.append(temp)


driver.close()

df1=pd.DataFrame({'Titles':Titles,'Date&Time':Date_time,'Images_URL':Img_links,'Article_links':Article_links,'Article_conetent':Article_content})
df1.to_csv('News_Data1.csv',index=False)



    