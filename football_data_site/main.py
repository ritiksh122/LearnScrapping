from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 
import pandas as pd



s=Service('C:\Program Files (x86)\chromedriver.exe')
website='https://www.adamchoi.co.uk/teamgoals/detailed'
driver=webdriver.Chrome(service=s)
driver.get(website)



all_matches_button=driver.find_element(By.XPATH,"//label[@analytics-event='All matches']")
all_matches_button.click()

matches=driver.find_elements(By.TAG_NAME,'tr')

date=[]
home_team=[]
score=[]
away_team=[]


for match in matches:
    date.append(match.find_element(By.XPATH,"./td[1]").text)
    home_team.append(match.find_element(By.XPATH,"./td[2]").text)
    score.append(match.find_element(By.XPATH,"./td[3]").text)
    away_team.append(match.find_element(By.XPATH,"./td[4]").text)

time.sleep(10)
driver.quit()


    # converting into csv file 

df=pd.DataFrame({'Date':date,'Home_team':home_team,'Score':score,'Away_team':away_team})
df.to_csv('football_data.csv',index=False)
print(df)    



