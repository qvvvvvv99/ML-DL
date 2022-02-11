# -------------------------------------------------------------------
# DataFrame, Series 데이터 가져오기
# -------------------------------------------------------------------
import pandas as pd

# (1) Series 에서 데이터 가져오기 --------------------------------------
sr=pd.Series([13,5,7,10])

# Series 에서 1개 데이터 가져오기 [인덱스번호]
print(f'sr[0] => {sr[0]}')
print(f'sr[3] => {sr[3]}')

# 2개 이상 데이터 가져오기 [[인덱스, 인덱스]]
print(f'sr[[0,2]] => {sr[[0,2]]}')

# from ~ to 데이터 가져오기 [시작인덱스:끝인덱스+1]
print(f'sr[1:3] => {sr[1:3]}')
print(f'sr[1:] => {sr[1:]}')

# (2) DataFrame 에서 데이터 가져오기 ----------------------------------
df=pd.DataFrame([[1,2,3],[11,22,33],[111,222,333],[10,20,30]])
print(f'df => \n{df}')
print(f'df.shape : {df.shape}, df.ndim : {df.ndim}')

# 행라벨 & 컬럼명 설정 ------------------------------------------------
df.index=['r0', 'r1', 'r2', 'r3']
df.columns=['c0', 'c1', 'c2']

# 열(column) 1개 가져오기 => [컬럼인덱스]
one=df[0]
print(f'one => type : {type(one)}\n{one}')

# 열(column) 여러개 가져오기 => [[컬럼인덱스],[컬럼인덱스]]
two=df[[0,2]]
print(f'two => type : {type(two)}\n{two}')

# 열(column) 슬라이싱 X => [시작인덱스:끝인덱스+1] => 행(row) 슬라이싱
sdata=df[0:2]
print(f'sdata => type : {type(sdata)}\n{sdata}')

# 행(row) 1개 가져오기 => df변수명.iloc[행인덱스]
rone=df.iloc[0]
print(f'rone => type : {type(rone)}\n{rone}')

# 행(row) 여러개 가져오기 => df변수명.iloc[[행인덱스][행인덱스]]
rtwo=df.iloc[[0,2]]
print(f'rtwo => type : {type(rtwo)}\n{rtwo}')

# 행(row) 슬라이싱 => df변수명.iloc[시작인덱스:끝인덱스+1]
rdata=df.iloc[0:2]
print(f'rdata => type : {type(rdata)}\n{rdata}')

rdata=df[0:2]
print(f'rdata => type : {type(rdata)}\n{rdata}')