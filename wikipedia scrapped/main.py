import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup as bs
# from narrate import narrate

async def main(keyword):
   
    browser=await launch()

    page=await browser.newPage()

    await page.goto("https://www.wikipedia.org/")

    

    await page.type(' [id=searchInput] ', keyword)

    await page.screenshot({'path':'result1.png'})

    # await page.screenshot({'path':'main_page.png'})
    await page.keyboard.press('Enter')
    await page.waitForNavigation()

    

   


    data=await page.evaluate('''
        () => {
            const contents=document.querySelectorAll('.mw-parser-output p')
            const d=Array.from(contents).map(para=>para.innerHTML)
            return d
        }

    ''')
    
    allData =''.join(data)

    print(allData)
    await page.screenshot({'path':'result2.png'})
    soup=bs(allData)
    text=soup.get_text().strip()
    print(text)

    


    
    await browser.close()

while True:
    try:
        keyword=input('? ')
        asyncio.get_event_loop().run_until_complete(main(keyword))
    except EOFError:
        print('bye')
        break


    