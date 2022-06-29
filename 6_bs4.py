from tkinter import N
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

for i in range(688):
    urlParts = ("https://sentencedict.com/word/list_%d.html" %(i+1))
    
    url = urlParts
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml") #가져온 text를 lxml을 써서 BeautifulSoup 객체로 만들었음. 즉, soup에 모든 정보가 들어있음.
    #print(soup.title.get_text())
    #print(soup.a)  #soup 객체에서 첫 a element 반환
    #print(soup.a.attrs)  # a element의 속성정보를 Dictionary로 반환
    #print(soup.a["href"])  # Dictionary 키에 해당하는 값 반환
    #print(soup.style.attrs) 
    # list1 = soup.find("li", attrs={"class":"dotline"}) #<li> 리스트 태그 블록 반환
    #print(listW.a)  #리스트 블록 안 a 태그 블록 반환
    # print(list1.a.get_text())  #태그에 쌓인 글자부분만 반환
    #print(list1.next_sibling)  #계행 등의 이유가 있으면 목록의 다음 항목이 나타나지 않을 수 있음. 그러면 next_sibling을 한 번 더 써주면 됨.
    # list2 = list1.next_sibling.next_sibling #목록의 다음 항목을 불러옴.
    # print(list2.a.get_text()) 
    # list3 = list2.next_sibling.next_sibling
    # print(list3.a.get_text())
    # print(list1.parent)  #list1의 부모(ul 태그)로 쌓인 모든 리스트 항목을 다 불러옴.
    # list4=list3.find_next_sibling("li")
    # print(list4.a.get_text())
    # print(list1.find_next_siblings("li"))
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
        f=open("sentenceEx_1.txt", 'a')
        f.write(sentLine + '\t' + link + '\n')

        #URL을 link로 바꿔서 전체를 새 파일(파일명= sentLine)에 저장
        
        j += 1

    f.close()


