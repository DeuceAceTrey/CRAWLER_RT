import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from getFromDB import insertDocument
from getFromDB import getAllHrefs
from extractor_phone_email import extractor

API_KEY = '315a6718e3755af1ea7e8f06558143382cb715cc'
response = requests.get("https://api.zenrows.com/v1/?apikey=" + API_KEY + "&url=https%3A%2F%2Fwww.ratemds.com%2Fbest-doctors%2Fqld%2F&js_render=true&premium_proxy=true")
from urllib import urlencode

def getHTML(url):
    url = urlencode(url)
    request_url = "https://api.zenrows.com/v1/?apikey=" + API_KEY + "&url=" + url + "&js_render=true&premium_proxy=true"
    r = requests.get(request_url)
    html = r.text    
    return html

def RateMds():
    page = 0
    hrefs = getAllHrefs()
    while(True):
        try:
            url = urlencode('https://www.ratemds.com/best-doctors/qld/?page=' + str(page))
            html = getHTML(url)
        except:
            return
        
        soup = BeautifulSoup(html,features='html.parser')
        card_container = soup.find('div',attrs={'class':'doctor-card-container'})
        doctor_cards = card_container.find_all('div',attrs={'class':'doctor-profile-card'})
        need_hrefs = []
        for card in doctor_cards:
            href = card.find_('a',attrs={'class' : 'search-item-doctor-name'})
            if(href in hrefs):
                need_hrefs.append(href)
                hrefs.append(href)
        for href in need_hrefs:
            html = getHTML(href)
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
        page += 1
            
        
    
    
            