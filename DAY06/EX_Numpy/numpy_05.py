"""
FileName : numpy_05.py
Numpy Array 배열 생성
"""
# 모듈로딩 -----------------------------------
import numpy as np

# numpy 배열 행 & 열 반전-------------------------
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f'a.shape={a.shape}')
print(f'a={a}\n')

a= a.T      # transpose로 전치
print(f'a.shape={a.shape}')
print(f'a={a}\n')


# numpy 배열 크기 변경-------------------------
a = np.arange(12)
print(f'a.shape={a.shape}')
print(f'a={a}\n')

b=a.reshape(3,4)
print(f'b.shape={b.shape}')
print(f'b={b}\n')

b=a.reshape(2,-1)    # 원소 갯수 고정으로 갯수만틈 3행 생성 가능
print(f'b.shape={b.shape}')
print(f'b={b}\n')

b=a.reshape(2, 2,-1)    # 원소 갯수 고정으로 갯수만틈 3행 생성 가능
print(f'b.shape={b.shape}')
print(f'b={b}\n')

b=a.reshape(2, -1, 2)    # 원소 갯수 고정으로 갯수만틈 3행 생성 가능
print(f'b.shape={b.shape}')
print(f'b={b}\n')


# 다차원 배열 ==> 1차원 배열로 펼치기
a = np.arange(12)
print(f'a.shape={b.shape}')
print(f'a.flatten()={a.flatten()}')
print(f'a.ravel()={a.ravel()}')
print(f'a.reshape(-1)={a.reshape(-1)}\n')

aa=np.array([1,2,3,4,5])
print(f'aa.shape={aa.shape}')
print(f'aa={aa}\n')

bb=aa.reshape(1,5)
print(f'bb.shape={bb.shape}')
print(f'bb={bb}\n')

cc=aa.reshape(5,1)
print(f'cc.shape={cc.shape}')
print(f'cc={cc}\n')