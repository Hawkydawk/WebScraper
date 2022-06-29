from tkinter import N
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import re
from argparse import FileType
from gettext import find


for i in range(689):
    urlParts = ("https://sentencedict.com/word/list_%d.html" %(i+1))
    
    url = urlParts
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml") #가져온 text를 lxml을 써서 BeautifulSoup 객체로 만들었음. 즉, soup에 모든 정보가 들어있음.

    sentList = soup.find_all("li", attrs={"class":"dotline"})
    #len(sentList)
    j = 1
    for sent in sentList:
        flagN = ("@%d@" %j)
        sentLine = flagN + sent.a.get_text()
        # if " in a sentence" in sentLine:
        #     sentLine = sentLine.strip(" in a sentence")
        # else:
        #     continue
        link = 'https://sentencedict.com'+sent.a["href"]
        f=open("sentenceEx_1.txt", 'a', encoding='UTF-8')
        f.write(sentLine + '\t' + link + '\n')
        j += 1
        
        #URL을 link로 바꿔서 전체를 새 파일(파일명= sentLine)에 저장 (url, res, soup, sent, sentLine, f)
        
        urlLink = link
        resLink = requests.get(urlLink)
        resLink.raise_for_status()

        soupLink = BeautifulSoup(resLink.text, 'lxml')

        titleDiv = soupLink.find("div", attrs={"class":"title"})
        titleText = titleDiv.h2.get_text()
        fileT = open("sentenceIn_1.txt", 'a', encoding='UTF-8')
        fileT.write("@"+titleText+"@"+'\n')
        fileT.close()
        
        sentenceBlock = soupLink.find("div", attrs={"id":"all"})
        for sentLink in sentenceBlock:
            sentLineLink = sentLink.get_text()
            fLink = open("sentenceIn_1.txt", "a", encoding='UTF-8')
            fLink.write(sentLineLink+"\n")
            fLink.close()

    f.close()


