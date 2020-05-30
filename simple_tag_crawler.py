# 심플 인스타그램 태그 크롤러.
# 키워드를 바탕으로 해당 키워드와 연관된 태그를 수집

from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os
import urllib
import time
import urllib.request

SLEEP_TIME = 5

#headless option
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

search = input("for search keyword : ")
search = urllib.parse.quote(search)
url = 'https://www.instagram.com/explore/tags/'+str(search)+'/'

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(SLEEP_TIME) #페이지 로드 타임 wait

count = 0

def get_post_link() :
    links = []

    while True:
        pageString = driver.page_source
        soup = BeautifulSoup(pageString, 'lxml')
        target = soup.find_all(name="div", attrs={"class" : "Nnq7C weEfm"})
        
        for link in target:
            for i in range(0,3):
                title = link.select('a')[i]
                url = title.attrs['href']
                links.append(url)
            print(links)
            last_heigt = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SLEEP_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_heigt:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SLEEP_TIME)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_heigt:
                    break
                else:
                    last_heigt = new_height
                    continue
    return links


def get_hashtag(links):
    data = {}
    data["hashtags"] = []

    for i in range(0, len(links)):
        url = 'https://www.instagram.com'+links[i]
        webpage = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(webpage, "lxml", from_encoding='utf-8')
        target = soup.find_all("meta", attrs = {"property":"instapp:hashtags"})

        for tag in target:
            tag = tag['content']
            data["hashtags"].append(tag)
    return data   


def make_json_file(data):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, 'hashtags.json'), 'w+') as json_file:
        json.dump(data, json_file)

links = get_post_link()
data = get_hashtag(links)
make_json_file(data)
