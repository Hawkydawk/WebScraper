from bs4 import BeautifulSoup
import requests
import re

url = "http://a4esl.org/a/g3.html"
req = requests.get(url)
req.raise_for_status()

bs = BeautifulSoup(req.text, "lxml")

li_tag=bs.find_all('li')

int1 = 0
for list in li_tag:
    ttText = list.tt.get_text()
    aText = list.a.get_text()
    li_URL = list.a["href"]
    # print(li_URL)
    
    int1 += 1

    if "Flash" in ttText:
        continue
    elif "HTML" in ttText:
        li_req = requests.get(li_URL)
        li_req.raise_for_status()
        li_bs = BeautifulSoup(li_req.text, 'lxml')
        li_sentList = li_bs.find_all("li")

        fileName = str(int1)+"_"+aText+".txt"
        fileName = fileName.replace("'", "_")
        fileName = fileName.replace("?","+")
        fileName = fileName.replace('"', '_')
        fileNew = open(fileName, 'w', encoding='UTF-8')
        fileNew.write('@@'+ttText+'\t'+li_URL+'\n')
        fileNew.close()

        for sent in li_sentList:
            sentLine = sent.get_text()
            f=open(fileName, 'a', encoding='UTF-8')
            f.write(sentLine+'\n')
        f.close()
    
    elif "JavaScript" in ttText:
        li_req = requests.get(li_URL)
        li_req.raise_for_status()
        li_bs = BeautifulSoup(li_req.text, 'lxml')
        li_sentList = li_bs.find_all("script")

        fileName = str(int1)+"_"+aText+".txt"
        fileName = fileName.replace("'", "_")
        fileName = fileName.replace("?","+")
        fileName = fileName.replace('"', '_')
        fileNew = open(fileName, 'w', encoding='UTF-8')
        fileNew.write('@@'+ttText+'\t'+li_URL+'\n')
        fileNew.close()

        for sent in li_sentList:
            sentLine = sent.get_text()
            f=open(fileName, 'a', encoding='UTF-8')
            f.write(sentLine+'\n')
        f.close()

# 아래 or(|)에 오류 있음.
    # elif "Flash"|"HTML"|"JavaScript" in ttText:
    #     li_req = requests.get(li_URL)
    #     li_req.raise_for_status()
    #     li_bs = BeautifulSoup(li_req.text, 'lxml')
    #     li_sentList = li_bs.find_all("script")

    #     fileName = str(int1)+"@@"+aText+".txt"
    #     fileName = fileName.replace("'", "_")
    #     fileName = fileName.replace("?","+")
    #     fileName = fileName.replace('"', '_')
    #     fileNew = open(fileName, 'w', encoding='UTF-8')
    #     fileNew.write('@@'+ttText+'\t'+li_URL+'\n')
    #     fileNew.close()

        
    
    






# file1 = open("any_2.txt", 'w')
# file1.write(body_tag)
# file1.close()
