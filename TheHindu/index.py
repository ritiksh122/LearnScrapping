from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

from selenium import webdriver

url="https://www.thehindu.com/news/international/"

driver=webdriver.Chrome()
driver.maximize_window
driver.get(url)

Links=[]
Headings=[]
Authors=[]

main_contents=[]

result=driver.page_source

soup=BeautifulSoup(result,'html.parser')

all_div=soup.select('div.element.row-element')

for i in all_div:
    a_tag=i.find('a').get('href')
    Links.append(a_tag)

    head=i.find('h3')
    Headings.append(head.get_text())

    authors=i.select_one('div.author-name')
    Authors.append(authors.get_text())


for i in range(len(Links)):
    
    time.sleep(1)
    driver.get(Links[i])
    r=driver.page_source
    soup2=BeautifulSoup(r,'html.parser')

    main_content=soup2.find('div',attrs={"itemprop":"articleBody"})
    main_contents.append(main_content.get_text())
        

     

df=pd.DataFrame({"Authors":Authors,"Headings":Headings,"Links":Links,"Description":main_contents})
df.to_csv('theHinduData.csv',index=False)
    




    



  





