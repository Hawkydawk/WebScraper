from argparse import FileType
from gettext import find
import requests
from bs4 import BeautifulSoup
import re

#URL은 link에서 받아올 것
urlLink = "https://sentencedict.com/memory%20dump.html"

res = requests.get(urlLink)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

#제목 받기 (title, setenceLine이 없으면 continue)
titleDiv = soup.find("div", attrs={"class":"title"})
titleText = titleDiv.h2.get_text()
fileT = open("sentenceIn_1.txt", 'w')
fileT.write("@@"+titleText+"@@"+'\n')
fileT.close()

#본문 받기 (id가 ad_로 시작하면 continue로 넘길 것)
sentenceBlock = soup.find_all("div", attrs={"id":"all"})
for sent in sentenceBlock:
    sentLine = sent.find("div").get_text()
    print(sentLine)
#     #광고 제외
#     # adDiv = sent.find("div", attrs={"id":"ad_marginbottom_0"})
#     # if adDiv:
#     #     continue
#       sentLine = sent.div.get_text()
# #    link = "https://sentencedict.com"+sent.a["href"]
#     f=open("sentenceIn_1.txt", "a")
#     f.write(sentLine+'\n')
#     f.close()

# 강의 영상 2:30:00