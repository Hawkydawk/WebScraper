import requests
import re
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%ED%9C%B4%EB%8C%80%ED%8F%B0%20%EA%B3%B5%EA%B8%B0%EA%B3%84&pagingIndex=1&pagingSize=40&productSet=total&query=%ED%9C%B4%EB%8C%80%ED%8F%B0%20%EA%B3%B5%EA%B8%B0%EA%B3%84&sort=rel&timestamp=&viewType=list"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
res=requests.get(url, headers=headers)
res.raise_for_status()
soup= BeautifulSoup(res.text, 'lxml')

items = soup.find_all("li", attrs={"class":re.compile("^basicList_item")})
#print(items[0].find("a", attrs={"class":re.compile("^basicList")}).get_text())
for item in items:
    titleIntro = item.find("a", attrs={"class":re.compile("^basicList_link")}).get_text()
    price = item.find("span", attrs={"class":re.compile("^price_num")}).get_text()
    rating = item.find("em", attrs={"class":re.compile("^basicList_num")}).get_text()
    webLink = item.a["href"]
    print((titleIntro, price, rating, webLink))
    
