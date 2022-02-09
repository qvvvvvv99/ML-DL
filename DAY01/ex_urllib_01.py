# ---------------------------------------
# WEB 상에서 이미지 파일 다운로드 => 데이터 수집
# ---------------------------------------

import urllib.request as req
import os.path

url="http://uta.pw/shodou/img/28/214.png"
fileName="214.png"

# WEB에서 이미지 파일 업로드
req.urlretrieve(url, fileName)

# 다운로드 여부 확인
if os.path.exists(fileName):
    print(f'{fileName} 다운로드 성공')
else:
    print('다운로드 실패')