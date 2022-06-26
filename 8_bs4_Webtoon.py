from audioop import ratecv
from itertools import starmap
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=335885"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

#평점 가져오기(다른 테이블이므로 soup.find_all을 재정의함)
total_rates = 0
ratings = soup.find_all("div", attrs={"class":"rating_type"})
for rating in ratings:
    rate = rating.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("Gross stars: ", total_rates)
print("Average : ", total_rates / len(cartoons))


