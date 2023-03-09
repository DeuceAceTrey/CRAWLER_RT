import undetected_chromedriver.v2 as uc
from time import sleep
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from getFromDB import insertDocument
from getFromDB import getAllHrefs
from random import randint
from extractor_phone_email import extractor
from twocaptcha import TwoCaptcha
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

API_KEY = '3b54a25d825f40884ccfd9c707913033'
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

def RateMDsScraper(driver):
    driver.get('https://www.ratemds.com/best-doctors/qld/')
    sleep(randint(3,5))
    while(True):
        try:
            turnstile_src = driver.find_element(By.ID,'turnstile-wrapper').find_element(By.TAG_NAME,'iframe').get_attribute('src')
            break
        except:
            sleep(3)
            continue
    solver = TwoCaptcha(API_KEY)
    st = turnstile_src.index('/0x')
    ed = turnstile_src.index('/',st+1)
    sitekey = turnstile_src[st+1:ed]
    result = solver.turnstile(sitekey=sitekey, url='https://www.ratemds.com/best-doctors/qld/')
    tries = 0
    while(tries < 5):
        while(True):
            try:
                iframe = driver.find_element(By.XPATH, "//iframe[@title='Widget containing a Cloudflare security challenge']")
                driver.switch_to.frame(iframe)
                checkbox = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="cf-stage"]//label[@class="ctp-checkbox-label"]/input',
                )

                if checkbox:
                    checkbox.click()
                    tries += 1

            except Exception as e:
                print(e)
                sleep(randint(3,5))
    
    try:
        doctor_cards = driver.find_element(By.CLASS_NAME,'doctor-card-container').find_elements(By.CLASS_NAME,'doctor-profile-card')
    except:
        return        
    
    # while(True):
    #     iframe = driver.find_element()
    
    
if(__name__ == "__main__"):
    driver = init_UC(None)
    RateMDsScraper(driver)
    