from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

driver=webdriver.Chrome()
driver.maximize_window()


website='https://www.business-standard.com/topic/credit-card'
driver.get(website)

time.sleep(2)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)



page=driver.page_source
soup = bs(page, 'html.parser')

main=soup.select("ul.listing li div.listing-txt")
Dates=[]
Headings=[]
Links=[]
temp="https://www.business-standard.com/"

for i in main:
    date=i.find('p')
    Dates.append(date.text)
    
    heading=i.find('h2')
    Headings.append(heading.text)

    links=i.find('h2').find('a')
    Links.append(temp+links['href'])

Main_content=[]
for j in range(len(Links)):
    driver.get(Links[j])
    soup1=bs(driver.page_source,"html.parser")
    main_content=soup1.select_one('span.p-content :nth-child(2)').get_text()
    Main_content.append(main_content)




df=pd.DataFrame({"Dates":Dates,"Headings":Headings,"Links":Links,"Description":Main_content})
df.to_csv("data.csv",index=False)






    
   









