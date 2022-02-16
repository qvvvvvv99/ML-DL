# --------------------------------------------------------------------
# 목표 : iris 품종 분류
# 데이터 : 3가지 품종별 꽃잎 길이, 너비, 꽃받침 길이, 너비
# 라벨 : setosa, versicolor, verginca
# 학습 : 데이터 + 라벨 => 지도 학습 - 분류 => SVC
# --------------------------------------------------------------------
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import urllib.request as req
import os, pandas as pd

# (1) 데이터 준비 ------------------------------------------------------
fileName= "../Data/iris2.csv"
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# req.urlretrieve(url, fileName)
# if os.path.exists(fileName): print(f'{fileName} download OK')
# else: print(f'{fileName} download FAIL')

# 데이터 로딩
irisData=pd.read_csv(fileName, header=None)
# 데이터 확인
irisData.info()    # 데이터에 대한 기본 정보 확인
print(irisData.head())
print(f'irisData.columns => {irisData.columns}')

# (2) 데이터 가공 ----------------------------------------------------------
# 학습을 위한 데이터와 바렐로 분리
data=irisData.iloc[:,:4]    # 모든 행의 0~3번 column
label=irisData.iloc[:,4]    # 모든 행의 4번 column
print(f'data => \n{data}\nlabel => \n{label}')

# 학습 데이터 : 테스트 데이터 = 75% : 25%
train_data, test_data, train_label, test_label=train_test_split(data, label)

# (3) 모델 생성
irisModel=SVC()
irisModel.fit(train_data, train_label)
pre=irisModel.predict(test_data)

ac_score=metrics.accuracy_score(test_label, pre)
print("정답률 = ", ac_score)