from tkinter import N
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import re


url = "http://a4esl.org/q/j/ni/fb-prepositions.html"
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
sentList = soup.find_all("script")
# len(sentList)
# print(sentList)
fileName = 'grammar21.txt'
fileTitle = soup.script.get_text()
fileNew = open(fileName, 'w')
fileNew.write(fileTitle+'\t'+url+'\n')
fileNew.close()

for sent in sentList:
    sentLine = sent.get_text()
    f=open(fileName, 'a')
    f.write(sentLine+'\n')

f.close()
