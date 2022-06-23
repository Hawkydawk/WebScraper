import requests
res = requests.get("https://sentencedict.com/")
#res = requests.get("http://nodocoding.tistory.com")
res.raise_for_status()
#print("응답코드: ", res.status_code) #200이면 정상
# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else: 
#     print("문제 발생. [에러코드: ", res.status_code, "]")

print(len(res.text))

with open("mySentence.html", 'w', encoding="utf8") as f:
    f.write(res.text)