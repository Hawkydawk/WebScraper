import re
p = re.compile("ca.e")
# . (ca.s): 문자 하나 > care, cafe, case...
# ^ (^de): 문자열의 시작 > desk, destinatin, default...
# $ (se$): 문자열의 끝 > case, base...

def print_match(m):
    if m:
        print(m.group()) #일치하는 문자열 반환
        print(m.string)  #입력받은 문자열. string은 변수이므로 괄호X
        print(m.start()) #일치하는 문자열 시작 인덱스 
        print(m.end()) #일치하는 문자열 끝 인덱스
        print(m.span()) #일치하는 문자열 시작/끝 인덱스
    else:
        print("매치 안 됨")

mt = p.match("careless")  #care, 
print_match(mt)

# m = p.search('good care')  #care
# print_match(m)

# lst = p.findall("good care cafe")
# print(lst)