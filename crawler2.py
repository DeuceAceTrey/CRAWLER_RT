import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from getFromDB import insertDocument
from getFromDB import getAllHrefs
from getFromDB import getAllTargets
from random import randint
from extractor_phone_email import extractor
from ripoff import RipOffScraper
from ratemds import RateMDsScraper

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
    driver = uc.Chrome(version_main = 110,options = chrome_options,headers=headers)
    return driver


if(__name__ == "__main__"):
    target_urls = getAllTargets()
    driver = init_UC(None)
    for target_url in target_urls:
        if('ripoffreport'  in target_url):
            RipOffScraper(driver)
        elif('ratemds' in target_url):
            RateMDsScraper(driver)
        else:
            print("--No Scraper Found--")
        