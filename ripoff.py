import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from getFromDB import insertDocument
from getFromDB import getAllHrefs
from random import randint
from extractor_phone_email import extractor



def addDocument(driver,url):
    try:
        driver.get(url)
        sleep(randint(1,3))
    except:
        print("--URL not exists--")
        return
    print("New URL found : " + url)
    html = driver.find_element("xpath",'/html')
    text = html.text
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = text.lower()
    wordList = text.split()
    keywords = []
    counts = []
    #making keywords list and counting 
    for word in wordList:
        if word not in keywords:
            keywords.append(word)
            counts.append(str(wordList.count(word)))
    keywords = ','.join(keywords)
    counts = ','.join(counts)
    myExtractor = extractor.Extractor(text)
    result = myExtractor.get()
    phones = ','.join(result['phones'])
    emails = ','.join(result['emails'])
    insertDocument([{'link' : url,'keywords': keywords,'counts' : counts,'phones' : phones,'emails':emails ,'status' : 1}])
    return

def RipOffScraper(driver):
    page = 1
    print("--Scraping RipOffReport---")
    global hrefs
    hrefs = getAllHrefs()
    while(True):
        try:
            driver.get('https://www.ripoffreport.com/reports/specific_search/australia?&pg=' + str(page))
            sleep(randint(1,3))
        except:
            return
        new_hrefs = []
        report_panel = driver.find_element(By.ID,'resultList')
        result_itmes = report_panel.find_elements(By.CLASS_NAME,'resultItem')
        for item in result_itmes:
            report_link = item.find_element(By.CLASS_NAME,'report_link').get_attribute('href')
            if(report_link not in hrefs):
                new_hrefs.append(report_link)
                hrefs.append(report_link)
        for href in new_hrefs:
            addDocument(driver,href)
        page += 1
        