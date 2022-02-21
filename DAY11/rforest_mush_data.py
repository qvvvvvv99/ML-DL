# ----------------------------------------------------------------
# 식용 & 독버섯 데이터 수집
# ----------------------------------------------------------------

import urllib.request as req
import os.path

# 데이터 관련 변수
url='https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'
dirPath='../Data/MUSH/'
fileName=f'{dirPath}mush.csv'

# 데이터 다운로드
# (1) 데이터 저장 경로 체크
if not os.path.exists(dirPath): os.mkdir(dirPath)
if os.path.exists(dirPath): print(f'{dirPath} 존재합니다.')

# (2) 데이터 파일 다운로드
req.urlretrieve(url, fileName)
if os.path.exists(fileName): print(f'{fileName} 다운로드 성공')
else: print('다운로드 실패')