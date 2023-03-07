import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# import pandas as pd
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager
from getFromDB import insertDocument
from getFromDB import getAllHrefs
from getFromDB import insertDocument
from getFromDB import getAllTargets
import threading
import pytz
from datetime import datetime
# from pyvirtualdisplay import Display
from extractor_phone_email import extractor

DEPTH = 20
STARTING_TIME = '19:00:00'
ENDING_TIME = '06:00:00'
urls = []
new_hrefs= []
hrefs = []
inserted_hrefs = []
DELAY_TIME = 300

def getAllUrls(driver,url,d):
    global urls,new_hrefs,inserted_hrefs
    if(d == DEPTH):
        return
    if('http' not in url):
        move_url = 'https://' + url
    else:
        move_url = url    
    print(move_url)
    driver.get(move_url)
    sleep(30)
    if(move_url not in hrefs and move_url not in inserted_hrefs):
        print("New URL found : " + move_url)
        inserted_hrefs.append(move_url)
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
        urls.append({'link' : move_url,'keywords': keywords,'counts' : counts,'phones' : phones,'emails':emails })
        insertDocument([{'link' : move_url,'keywords': keywords,'counts' : counts,'phones' : phones,'emails':emails }])
    a_tags = driver.find_elements(By.TAG_NAME,'a')
    need_hrefs = []
    for a_tag in a_tags:
        while(True):
            try:
                href = a_tag.get_attribute('href')
                break
            except:
                continue
        if(href != None):
            domain = get_domain_from_url(url)
            if(domain in href and href not in new_hrefs and href not in need_hrefs):
                new_hrefs.append(href)
                need_hrefs.append(href)
            
    for href in need_hrefs:
        getAllUrls(driver,href,d+1)
    return 

def check_time():
    #return True
    dt = datetime.now()
    aus_dt = dt.astimezone(pytz.timezone('Australia/Sydney'))
    start_time = datetime.strptime(STARTING_TIME, '%H:%M:%S').time()
    end_time = datetime.strptime(ENDING_TIME, '%H:%M:%S').time()
    time_now = aus_dt.time()
    print('NOW : ' + str(time_now))
    #return True
    return (time_now > start_time or time_now < end_time)

def search(st,en,df,driver):
    
    for i in range(st,en):
        row = df[i]
        # url = row[0]
        url = df[i]
        getAllUrls(driver,url,0)

def get_domain_from_url(url):
    
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    try:
        filename = parsed_url.netloc
    except:
        # Si falla es porque la implementación de parsed_url no reconoce los atributos como "path"
        if len(parsed_url)>=4:
            filename = parsed_url[1]
        else:
            filename = ""

    return filename

def init_UC(headers):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    # chrome_options.add_argument('--disable-setuid-sandbox')
    headers = {
    'authority': 'accounts.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"108.0.5359.125"',
    'sec-ch-ua-full-version-list': '"Not?A_Brand";v="8.0.0.0", "Chromium";v="108.0.5359.125", "Google Chrome";v="108.0.5359.125"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"8.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=91c169ab-71ab-4040-933c-d2bca9ab8f98,signin_mode=all_accounts,signout_mode=show_confirmation',
    'x-client-data': 'CLL5ygE=',
}
    driver = uc.Chrome(service=Service(chromedriver_autoinstaller.install()),options = chrome_options,headers=headers)
    return driver

def main():
    if(__name__ == '__main__'):
        # with Display():
            chrome_options = uc.ChromeOptions()
            #chrome_options.add_argument('--disable-gpu')
            # chrome_options.add_argument('--headless')
            #chrome_options.add_argument('--window-size=1920,1080')
            #chrome_options.add_argument('--no-sandbox')
            #chrome_options.add_argument('--start-maximized')
            #chrome_options.add_argument('--disable-setuid-sandbox')
            #prefs = {"profile.managed_default_content_settings.images": 2}
            #chrome_options.add_experimental_option("prefs", prefs)
            # chrome_options.add_argument('--log-level 3') 
            # chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,ar;q=0.8,zh-CN;q=0.7,zh;q=0.6,ko;q=0.5',
                'cache-control': 'max-age=0',
                'referer': 'https://www.ratemds.com/best-doctors/qld/?__cf_chl_tk=BqZuqnT6ucDY5U7LNR5IjS0Wr0.tCwBNrmhpa69pXbg-1678171935-0-gaNycGzNCuU',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Windows",
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
                }
            print("Starting first chrome driver")
            driver_1 = init_UC(None)
    
            # driver_1.delete_all_cookies()
            # driver_1.maximize_window()
            # print("Starting second chrome driver")
            # driver_2 = webdriver.Chrome(service=Service(ChromeDriverManager.install))
    
            # driver_2.delete_all_cookies()
            # driver_2.maximize_window()
            # file_path = input("Please insert search url file path : ")
            target_urls = getAllTargets()
            # domains = []
            # for target_url in target_urls:
            #     domains.append(get_domain_from_url(target_url))
            
            
            #half = int(length/2)
            print("----Running Crawler---")
            while(True):
                if(True):
                    
                    global hrefs
                    hrefs = getAllHrefs()
                    target_urls = getAllTargets()
                    print(target_urls)
                    length = len(target_urls)
                    print("Starting Thread 1")
                    search(0,length,target_urls,driver_1)
                    #thread_1 = threading.Thread(target=search,args=(0,half,target_urls,driver_1,))
                    print("Starting Thread 2")
                    #thread_2 = threading.Thread(target=search,args=(half,length,target_urls,driver_2,))
                    # thread_1.start()
                    # thread_2.start()
                    # thread_1.join()
                    # thread_2.join()
                    # insertDocument(urls)
                    sleep(DELAY_TIME)



        

main()