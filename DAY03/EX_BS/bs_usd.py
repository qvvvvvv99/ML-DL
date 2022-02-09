from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup=BeautifulSoup(res, "html.parser")

# coy selector 해서 원하는 데이터 가져오기
#exchangeList > li.on > a.head.usd > div > span.value
# li.on 일때만 가능 -> li:nth-child(1) 바꿔주면 가능
price = soup.select_one("#exchangeList > li:nth-child(1) > a.head.usd > div > span.value").string
print("usd/krw =", price)
