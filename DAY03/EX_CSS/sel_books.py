from bs4 import BeautifulSoup

HTML_FILE = 'books.html'
with open(HTML_FILE, encoding='utf-8') as f:
    soup = BeautifulSoup(f, "html.parser")

# CSS 선택자 방식 검색
sel = lambda q : print(soup.select_one(q).string)

sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("#bible #nu")
sel("#bible > #nu")
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)