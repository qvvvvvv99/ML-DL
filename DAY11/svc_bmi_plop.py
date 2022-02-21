# ----------------------------------------------------------------
# 데이터 분포 확인
# ----------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

fileName='../Data/BMI/bmi.csv'

# (1) 데이터 읽기 --------------------------------------------------
# read_csv() => DataFrame 형태 변환
bmiDF=pd.read_csv(fileName)
bmiDF.info()
# .head() : 상위 다섯개 데이터
print(f'bmiDF.head()------------\n{bmiDF.head()}')
print(f'bmiDF.index : {bmiDF.index}')
print(f'bmiDF.columns : {bmiDF.columns}')

# 인덱스 변경 : bmi 컬럼을 인덱스 설정
bmiDF.set_index("bmi", inplace=True)
print(f'bmiDF.index : {bmiDF.index}')
print(f'bmiDF.columns : {bmiDF.columns}')

# print(bmiDF.loc['fat'])

# BMI 지수 라벨별로 데이터 추출하여 하나의 그래프에 그리기
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

# 행 인덱스 => 'fat'
ax.scatter(bmiDF.loc['fat', 'weight'], bmiDF.loc['fat', 'height'], c='red', label='Fat')
# 행 인덱스 => 'normal'
ax.scatter(bmiDF.loc['normal', 'weight'], bmiDF.loc['normal', 'height'], c='blue', label='Normal')
# 행인덱스 => 'thin'
ax.scatter(bmiDF.loc['thin', 'weight'], bmiDF.loc['thin', 'height'], c='yellow', label='Thin')

# 범례 추가
plt.legend()

plt.show()