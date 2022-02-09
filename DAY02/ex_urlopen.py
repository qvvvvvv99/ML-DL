# 이미지 파일 다운로드하기
import urllib.request as req

# URL과 저장 경로 지정
url="http://uta.pw/shodou/img/28/214.png"
savename="img_date.png"
debug = True

# HTTP Response 객체 변환 -> byte 데이터
resObj = req.urlopen(url)
header = resObj.getheaders()
data = resObj.read()

if debug:
    print(f'type(resObj)    => {type(resObj)}')
    print(f'resObj.header() => \n{header}')
    print(f'resObj.read()    => \n{data}')

# 바이너리 모드로 파일 저장
with open(savename, mode="wb") as file:
    file.write(data)
    print("저장되었습니다...!")