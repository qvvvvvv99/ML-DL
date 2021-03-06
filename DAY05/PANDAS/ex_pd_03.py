# -------------------------------------------------------------------
# DataFrame, Series 데이터 가져오기
# -------------------------------------------------------------------
import pandas as pd

# 데이터 생성 ---------------------------------------------------------
df=pd.DataFrame({
    '몸무게'  :[10.0, 70.4, 45.7, 35.2],
    '키'      :[190, 187, 165, 145],
    '타입'    :['L', 'F', 'N', 'N']
})

print(f'df => \n{df}')
print(f'df.index => {df.index}')
print(f'df.columns => {df.columns}')

# 행이름(라벨 설정)
df.index=['김', '이', '박', '최']
print(f'df => \n{df}')

# 데이터 가져오기
print(df['몸무게'])
print(df.몸무게)

print(df.loc['이'])