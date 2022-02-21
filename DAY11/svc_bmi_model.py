# ----------------------------------------------------------------
# 목표 : BMI 지수에 따른 체형 분류 모델 생성
# 데이터 : CSV파일, 키-몸무게-BMI 형식 => 데이터 + 라벨
# 학습 : 지도학습 => 분류(Classification) : SVC
# ----------------------------------------------------------------

# 모듈 로딩 --------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# 데이터 관련 변수 선언 ---------------------------------------------
fileName='../Data/BMI/bmi.csv'

# (1) 데이터 준비
bmiDF=pd.read_csv(fileName)

# (2) 데이터 전처리
# (2-1) 수치 데이터 0 ~ 1 사이로 정규화
h=bmiDF['height']/200
w=bmiDF['weight']/80

# (2-2) 데이터 - 라벨 분리
data=pd.concat([h,w], axis=1)   # 열(column) 방향 합치기
print(data.head())

label=bmiDF['bmi']

# (3) 학습을 위한 데이터 준비
# Trainnig 용 데이터, 라벨 / Test 용 데이터, 라벨
# train_test_split() -> default - 75% : 25%
train_data, test_data, train_label, test_label=train_test_split(data, label)

# (4) 학습
# (4 - 1) 학습 모델 객체 생성
bmiModel=SVC()

# (4 - 2) 학습하기 => fit()
bmiModel.fit(train_data, train_label)

# (5) 검증
pre_label=bmiModel.predict(test_data)
ac_score_test=accuracy_score(test_label, pre_label)
print(f'ac_score_test : {ac_score_test}')

report=classification_report(test_label, pre_label)
print(f'classification REPORT\n{report}')