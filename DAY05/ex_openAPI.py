# -----------------------------------------------------
# OpenAPI 활용 데이터 수집
# OpenweatherMap
# KEY - 2f217cd56b92f630927cf55476a9172f
# -----------------------------------------------------

import  json, requests as req

# 변수 -------------------------------------------------
# OpenAPI KEY
apiKey="2f217cd56b92f630927cf55476a9172f"

# OpenAPI 접근 URL
# http:// 추가 까먹지 말기!!
apiURL="http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

# 조사할 도시 데이터
cities=["Daegu, KR", "Seoul, KR", "Busan, KR"]

DEBUG = False

# WEB OpenAPI 활용 데이터 수집 --------------------------
for city in cities:
    # URL 생성
    if DEBUG : print(f'city => {city}')
    url=apiURL.format(city=city, key=apiKey)
    if DEBUG : print(f'url => {url}')

    # 데이터 가져오기
    data=req.get(url)
    if DEBUG : print(f'data => {data.text}')

    # 데이터 분석하기 쉬운 형태로 변환 str => json
    data=json.loads(data.text)
    # 도시명, 날씨, 최저기온, 최고기온, 습도, 기압, 풍향, 풍속
    if DEBUG :  print(f'data => type : {type(data)}')
    if DEBUG:
        for k, v in data.items():
            print(f'{k}- {v}')

    print(f'----{data["name"]}----')
    print(f'| 날씨 : {data["weather"][0]["description"]}')
    print(f'| 기온 : {data["main"]["temp_min"]} ~ {data["main"]["temp_max"]} Kelvin')
    print(f'| 기압 : {data["main"]["humidity"]}%')
    print(f'| 기압 : {data["main"]["pressure"]}hPa')