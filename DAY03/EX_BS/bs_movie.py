from bs4 import BeautifulSoup
import urllib.request as req

url="https://movie.naver.com/movie/sdb/rank/rmovie.naver"
res=req.urlopen(url)

soup=BeautifulSoup(res, "html.parser")

# 1위
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# 10위
#old_content > table > tbody > tr:nth-child(11) > td.title > div > a
# 원하는 데이터 추출
# 1개만 추출
movie=soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
print("movie = ", movie.attrs['title'])
print("movie = ", movie.string)

# 여러개 추출
#movies=soup.select("#old_content > table > tbody > tr > td.title > div > a")
