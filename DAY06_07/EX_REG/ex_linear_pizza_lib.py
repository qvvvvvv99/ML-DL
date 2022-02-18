# ---------------------------------------------------------------
# 목표 : 피자 사이즈에 따른 가격 예측
# 단계 1 : 데이터 수집, 데이터 분포 분석
# 단계 2 : 데이터 분포 확인 후 학습 방법 선정
#       => 선형 데이터 분포 => Linear Regression
# 단계 3 : ML 오픈 라이브러리 활용하여 구현
#       => scikit-learn LIB
# ---------------------------------------------------------------

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 데이터 ---------------------------------------------------------
# 인치 x, 가격 y
x=np.array([6,8,10,15,18])
y=np.array([7,9,13,17.5,19.3])

# ML에서 사용가능하도록 데이터 변환
x=x.reshape(-1,1)   # 2차원으로 변경

# (1) 모델 객체 생성
model=LinearRegression()

# (2) 학습
model.fit(x,y)
print(f'W => {model.coef_}\nb => {model.intercept_}')

# (3) 확인
pre_y=model.predict(x)
print(f'y => {y}\npre_y => {pre_y}')

# (4) 검사 => 현재 생성된 w, b에 대한 정확도
result=model.score(x, pre_y)
print(f'result => {result}')