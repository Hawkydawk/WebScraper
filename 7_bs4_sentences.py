import requests
from bs4 import BeautifulSoup

url = "https://sentencedict.com/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
sentenceList2 = soup.find_all("a", attrs={"class":"dotline"})
# for sentenceText in sentenceList2:
#     print(sentenceText.a.get_text())
print(sentenceList2)