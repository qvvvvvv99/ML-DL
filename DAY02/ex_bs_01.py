from bs4 import BeautifulSoup

with open('01.html', mode='r', encoding='utf-8') as f:
    htmlData = f.read()

# HTML 객체 생성하기
soup=BeautifulSoup(htmlData, 'html.parser')

# print(f'soup type : { type(soup) }\n{soup}')

h1 = soup.html.body.h1  # <h1>스크레핑이란</h1>
p1 = soup.html.body.p   # <p>웹 페이지를 분석하는 것</p>
p2 = p1.next_sibling.next_sibling   # <p>원하는 부분을 추출하는 것</p>

# obj.string : 태그 사이의 문자열
print("h1 = " + h1.string)  # h1.string : 스크레핑이란
print("p = " + p1.string)
print("p = " + p2.string)