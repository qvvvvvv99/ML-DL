from bs4 import BeautifulSoup
import urllib.request as req

url="https://www.korea.kr/rss/dept_kma.xml"
res=req.urlopen(url)

soup=BeautifulSoup(res, "html.parser")