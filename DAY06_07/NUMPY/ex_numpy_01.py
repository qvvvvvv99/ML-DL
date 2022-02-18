# 모듈 로딩 ----------------------------------------------
import  numpy as np

# ndarray 객체 생성
#ndarray01=np.array([1,2,3,4,5])
ndarray01=np.array([[1,2,3,4,5],[11,22,33,44,55]])

# ndarray 객체 속성
print(f'type(ndarray01) => {type(ndarray01)}')
print(f'ndarray01.shape => {ndarray01.shape}')
print(f'ndarray01.ndim => {ndarray01.ndim}')
print(f'ndarray01.dtype => {ndarray01.dtype}')
print(f'ndarray01.data => {ndarray01.data}')

# ndarray 객체 메서드
print("\n=== EX_Numpy Array 메소드===")
print('ndarray01.max() => ', ndarray01.max())
print('ndarray01.min() => ', ndarray01.min())
print('ndarray01.sum() => ', ndarray01.sum())

print('ndarray01.sum(axis=0) => ', ndarray01.sum(axis=0))   # 열(col) 방향 합
print('ndarray01.sum(axis=1) => ', ndarray01.sum(axis=1))   # 행(row) 방향 합
print('ndarray01.nean() => ', ndarray01.mean())             # 원소값 평균

