# import time
# from playwright.sync_api import sync_playwright

# #scraping data from google doc
# def AutoFill(client_data):
#     #dummy data
#     country = client_data[1]
#     full_name = client_data[2]
#     companyname = client_data[3]
#     representedrightsholder = client_data[4]
#     contact_email_noprefill = client_data[5]
#     url_box3 = client_data[6].split(',') #Allegedly infringing URLs 
#     print(url_box3)
#     is_geo_ugc_imagery = client_data[7]  # if yes check is_geo_ugc_imagery--yes else check is_geo_ugc_imagery--no
#     legalother_explain = client_data[8]
#     legalother_quote = client_data[9]
#     subject_of_image = client_data[10]
#     signature = client_data[11]

#     #Getting the page link
#     link = "https://support.google.com/legal/contact/lr_legalother?product=googlemybusiness"

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         #page.set_default_timeout = 300000
#         #page.set_default_navigation_timeout = 300000
#         page.goto(link,timeout=0,wait_until='domcontentloaded')
#         #select country

#         #input text
#         time.sleep(2)
#         page.click('span:has-text("Select one")')
        
#         time.sleep(2)
#         page.locator('text=' + country + ' >> nth = 1').click()
        
#         time.sleep(2)
#         page.fill('#full_name',full_name)
        
#         time.sleep(2)
#         page.fill('#companyname',companyname)
        
#         time.sleep(2)
#         page.fill('#representedrightsholder',representedrightsholder)
        
#         time.sleep(2)
#         page.fill('#contact_email_noprefill',contact_email_noprefill)
        
#         for i in range(0,len(url_box3)):
#             time.sleep(2)
#             if(i == 0):
#                 page.fill('#url_box3',url_box3[i])
#             else:
#                 page.locator('a:has-text("Add additional")').click()
#                 page.locator(".default-textbox >> nth = " + str(i)).fill(url_box3[i])
        
#         time.sleep(2)
#         if(int(is_geo_ugc_imagery) > 0):
#             page.locator('span:has-text("Yes") >> nth = 0').click()
#         else:
#             page.locator('span:has-text("No") >> nth = 0').click()
        
#         time.sleep(2)
#         page.fill('#legalother_explain',legalother_explain)
        
#         time.sleep(2)
#         page.fill('#legalother_quote',legalother_quote)
        
#         time.sleep(2)
#         if(int(subject_of_image) > 0):
#             page.locator('span:has-text("Please check to confirm")').click()
        
#         time.sleep(2)
#         page.fill('#signature',signature)

#         #submit form
#         time.sleep(2)
#         page.locator('button:has-text("Submit")').click()

#         time.sleep(5)#wait for form to complete submit
#         context.close()
#         browser.close()

import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def AutoFill(client_data):

    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-setuid-sandbox')
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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=91c169ab-71ab-4040-933c-d2bca9ab8f98,signin_mode=all_accounts,signout_mode=show_confirmation',
    'x-client-data': 'CLL5ygE=',
}
    driver = uc.Chrome(options = chrome_options,headers=headers)
    driver.delete_all_cookies()
    username = 'aarontapi3@gmail.com'
    password = 'Tapi20220601*#'
    print("--Logging Into Google Account--")

    driver.get('https://accounts.google.com/ServiceLogin')
    sleep(.5)

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))).click()
    driver.find_element("xpath",'//input[@type="email"]').send_keys(username)
    driver.find_element("xpath",'//*[@id="identifierNext"]').click()

    sleep(10)
    driver.get_screenshot_as_file('screenshot_password.png')
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).click()
    driver.find_element("xpath",'//input[@type="password"]').send_keys(password)
    driver.find_element("xpath",'//*[@id="passwordNext"]').click()
    sleep(5)
    driver.get_screenshot_as_file('screenshot_logged.png')

    print("--Successfully Logged In--")
    #dummy data
    # country = client_data[1]
    # full_name = client_data[2]
    # companyname = client_data[3]
    # representedrightsholder = client_data[4]
    # contact_email_noprefill = client_data[5]
    # url_box3 = client_data[6].split(',') #Allegedly infringing URLs 
    # print(url_box3)
    # is_geo_ugc_imagery = client_data[7]  # if yes check is_geo_ugc_imagery--yes else check is_geo_ugc_imagery--no
    # legalother_explain = client_data[8]
    # legalother_quote = client_data[9]
    # subject_of_image = client_data[10]
    # signature = client_data[11]

    # #Getting the page link
    # link = "https://support.google.com/legal/contact/lr_legalother?product=googlemybusiness"
    # driver.get(link)
    
    # driver.find_element('xpath','//*[@id="lr_legalother"]/div[5]/div[1]').click()
    # sleep(randint(2,3))
    # country_ul = driver.find_element('xpath','//*[@id="lr_legalother"]/div[5]/div[1]/ol')
    # selector = "//li[contains(text(), '" + country + "')]"
    # country_ul.find_element('xpath',selector).click()
    
    # sleep(randint(1,2))
    
    # driver.find_element('xpath','//*[@id="full_name"]').send_keys(full_name)

    # sleep(randint(1,2))
    # driver.find_element('xpath','//*[@id="companyname"]').send_keys(companyname)
    
    # sleep(randint(1,2))
    # driver.find_element('xpath','//*[@id="representedrightsholder"]').send_keys(representedrightsholder)
    
    # sleep(randint(1,2))
    # driver.find_element('xpath','//*[@id="contact_email_noprefill"]').send_keys(contact_email_noprefill)

    # for i in range(0,len(url_box3)):
    #     sleep(randint(1,2))
    #     if(i == 0):
            
    #         driver.find_element('xpath','//*[@id="url_box3"]').send_keys(url_box3[i])
    #     else:
    #         driver.find_element('xpath','//*[@id="lr_legalother"]/div[25]/a').click()
    #         sleep(randint(1,2))
    #         div_textbox = driver.find_elements(By.CLASS_NAME,'additional-textbox')[i-1]
    #         div_textbox.find_element(By.TAG_NAME,'input').send_keys(url_box3[i])
            
    # sleep(randint(1,2))
    # if(int(is_geo_ugc_imagery) > 0):
    #     driver.find_element('xpath','//*[@id="lr_legalother"]/div[29]/fieldset/div[1]/div/label/span').click()
    # else:
    #     driver.find_element('xpath','//*[@id="lr_legalother"]/div[29]/fieldset/div[2]/div/label/span').click()
    
    # sleep(randint(1,2))
    # driver.find_element('xpath','//*[@id="legalother_explain"]').click()
    # driver.find_element('xpath','//*[@id="legalother_explain"]').send_keys(legalother_explain)
    
    # sleep(randint(1,2))
    # driver.find_element('xpath','//*[@id="legalother_quote"]').click()
    # driver.find_element('xpath','//*[@id="legalother_quote"]').send_keys(legalother_quote)
    
    # sleep(randint(1,2))
    # if(int(subject_of_image) > 0):
    #     try:
    #         driver.find_element('xpath',"//*[contains(text(), 'Please check to confirm')]").click()
    #     except:
    #         driver.find_element('xpath',"//*[contains(text(), 'Please tick to confirm')]").click()
        
    # sleep(randint(1,2))
    # driver.find_element('xpath','//*[@id="signature"]').click()
    # driver.find_element('xpath','//*[@id="signature"]').send_keys(signature)
    
    # #submit form
    # sleep(randint(1,2))
    # driver.find_element('xpath','//button[contains(text(), "Submit")]').click()
    # time.sleep(65)
    # driver.close()

    country = client_data[1]
    full_name = client_data[2]
    companyname = client_data[3]
    representedrightsholder = client_data[4]
    contact_email_noprefill = client_data[5]
    url_box3 = client_data[6].split(',') #Allegedly infringing URLs 
    print(url_box3)
    is_geo_ugc_imagery = client_data[7]  # if yes check is_geo_ugc_imagery--yes else check is_geo_ugc_imagery--no
    legalother_explain = client_data[8]
    legalother_quote = client_data[9]
    subject_of_image = client_data[10]
    signature = client_data[11]

    #Getting the page link
    link = "https://support.google.com/legal/contact/lr_legalother?product=googlemybusiness"
    print("Moving to " + link)
    driver.get(link)
    print("--Inputing Data---")
    
    driver.find_element('xpath','//*[@id="lr_legalother"]/div[5]/div[1]').click()
    
    sleep(randint(2,3))
    
    country_ul = driver.find_element('xpath','//*[@id="lr_legalother"]/div[5]/div[1]/ol')
    selector = "//li[contains(text(), '" + country + "')]"
    country_ul.find_element('xpath',selector).click()
    
    sleep(randint(1,2))
    
    driver.find_element('xpath','//*[@id="full_name"]').send_keys(full_name)

    sleep(randint(1,2))
    
    driver.find_element('xpath','//*[@id="companyname"]').send_keys(companyname)
    
    sleep(randint(1,2))
    
    driver.find_element('xpath','//*[@id="representedrightsholder"]').send_keys(representedrightsholder)
    
    sleep(randint(1,2))
    
    driver.find_element('xpath','//*[@id="contact_email_noprefill"]').click()
    driver.find_element('xpath','//*[@id="contact_email_noprefill"]').send_keys(Keys.CONTROL + 'a')
    driver.find_element('xpath','//*[@id="contact_email_noprefill"]').send_keys(Keys.DELETE)
    sleep(.5)
    driver.find_element('xpath','//*[@id="contact_email_noprefill"]').send_keys(contact_email_noprefill)

    for i in range(0,len(url_box3)):
        sleep(randint(1,2))
        if(i == 0):
            
            driver.find_element('xpath','//*[@id="url_box3"]').send_keys(url_box3[i])
        else:
            driver.find_element('xpath','//*[@id="lr_legalother"]/div[25]/a').click()
            sleep(randint(1,2))
            div_textbox = driver.find_elements(By.CLASS_NAME,'additional-textbox')[i-1]
            div_textbox.find_element(By.TAG_NAME,'input').send_keys(url_box3[i])
            
    sleep(randint(1,2))
    
    if(int(is_geo_ugc_imagery) > 0):
        driver.find_element('xpath','//*[@id="lr_legalother"]/div[29]/fieldset/div[1]/div/label/span').click()
    else:
        driver.find_element('xpath','//*[@id="lr_legalother"]/div[29]/fieldset/div[2]/div/label/span').click()
    
    sleep(randint(1,2))
    
    driver.find_element('xpath','//*[@id="legalother_explain"]').click()
    driver.find_element('xpath','//*[@id="legalother_explain"]').send_keys(legalother_explain)
    
    sleep(randint(1,2))
    
    driver.find_element('xpath','//*[@id="legalother_quote"]').click()
    JS_ADD_TEXT_TO_INPUT = """
    var elm = arguments[0], txt = arguments[1];
    elm.value += txt;
    elm.dispatchEvent(new Event('change'));
    """
    
    elem = driver.find_element('xpath','//*[@id="legalother_quote"]')

    driver.execute_script(JS_ADD_TEXT_TO_INPUT,elem,legalother_quote)
    
    try:
        driver.find_element('xpath',"//*[contains(text(), 'Please check to confirm')]").click()
    except:
        driver.find_element('xpath',"//*[contains(text(), 'Please tick to confirm')]").click()
    

    sleep(randint(1,2))
    
    # if(int(subject_of_image) > 0):
    #     driver.find_element('xpath','//*[@id="lr_legalother"]/div[34]/fieldset/div/label/label/span[2]').click()
    driver.get_screenshot_as_file('screenshot_check.png')
    sleep(randint(1,2))
    
    driver.find_element('xpath','//*[@id="signature"]').click()
    driver.find_element('xpath','//*[@id="signature"]').send_keys(signature)
    
    #submit form
    print("--Submit Report--")
    sleep(randint(1,2))
    driver.find_element('xpath','//button[contains(text(), "Submit")]').click()
    time.sleep(5)
    driver.get_screenshot_as_file('screenshot_submit.png')
    print("Screenshot Saved")
    context = driver.find_element(By.TAG_NAME,'body').text
    # print(context)
    if('Your email has been sent' in context):
        print("---Successfully reported---")
    else:
        print("---Report Failed. Please Check report data---")