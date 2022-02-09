import urllib.request as req
import urllib.parse as parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stdId': '108'
}
params = parse.urlencode(values)

url = API + "?" + params
print("url=", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")


filename="forecast.txt"
with open(filename, mode='w', encoding='utf-8') as file:
    file.write(text)


# 기상청 문자열 출력하기
with open('forecast.txt', mode='r', encoding='utf-8') as file:
    while True:
        line=file.readline()
        if not line: break
        idx=line.find("기상청")
        if idx >= 0:
            print(f'{line} - {line[idx:idx+3]}')