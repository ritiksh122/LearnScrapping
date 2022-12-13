from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import pandas as pd
from bs4 import BeautifulSoup as bs



s=Service('C:\Program Files (x86)\chromedriver.exe')

driver=webdriver.Chrome(service=s)

website='https://medium.com/tag/politics'
driver.maximize_window()
driver.get(website)
r=driver.page_source
soup=bs(r,'html.parser')



articles=soup.find_all('article',class_='meteredContent')

names=[]
headings=[]
Links=[]

temp='https://medium.com'

for i in articles:
    texts=i.p.strings
    heading=i.h2.strings
    link=i.h2.parent.parent.parent
    for j in texts:
         names.append(j)
    for y in heading:
        headings.append(y)
    for z in link:
        Links.append(temp+z.get('href'))



Content=[]

for k in Links:
    driver.get(k)
    result=driver.page_source
    soup2=bs(result,'html.parser')
    l=(soup2.section.find_all('div'))
    emp=''
    for i in l:
    
        emp=emp + i.get_text()
        

        
    
    Content+=[emp]    
    

df=pd.DataFrame({'Names':names,'Headings':headings,'Links':Links,'MainContent':Content})
df.to_csv('mediumData.csv',index=False)





    
    
    
        


    
    




        
    
    
    
    
    

