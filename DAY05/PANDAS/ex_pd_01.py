# ------------------------------------------------------------------------
# 다양한 형태의 데이터를 DataFrame 형태로 처리하는 Pandas
# .xml .csv .yaml 등 다양한 형태의 데이터를 하나의 테이블로 만든다
# ------------------------------------------------------------------------

import pandas as pd

# (1) 시리즈(Series = 행(Row)) 데이터 생성하기
sr=pd.Series(10)
print(f'sr TYPE : {type(sr)}\n {sr}')
print(f'sr.index : {sr.index}\nsr.value : {sr.values}')

sr2=pd.Series(20)
print(f'sr2 TYPE : {type(sr2)}\n {sr2}')
print(f'sr2.index : {sr2.index}\nsr2.value : {sr2.values}')

sr3=pd.Series([1, 3, 5, 7, 9])
print(f'sr3 TYPE : {type(sr3)}\n {sr3}')
print(f'sr3.index : {sr3.index}\nsr3.value : \n{sr3.values}')

# (2) 데이터프레임(DataFrame) 데이터 생성하기
df=pd.DataFrame([sr, sr2])
print(f'df TYPE : {type(df)}\n {df}')
print(f'df.index : {df.index}\ndf.columns : \n{df.values}')