"""
FileName : numpy_02.py
Numpy Array 속성
"""
# 모듈로딩 -----------------------------------
import numpy as np

# numpy 객체 생성 -----------------------------
#nparr=np.array([[1,2], [11,22], [111,222]])
#nparr=np.array([[1,2,3], [11,22,33], [111,222,333]])
nparr=np.array([[[1,2], [11,22], [111,222]], [[1,2], [11,22], [111,222]]])
print('type(nparr) =', type(nparr))
print(nparr)

print("=== Numpy Array 속성 ====")
print('nparr.ndim =>', nparr.ndim)
print('nparr.shape =>', nparr.shape)
print('nparr.size =>', nparr.size)
print('nparr.dtype =>', nparr.dtype)
print('nparr.itemsize =>', nparr.itemsize)
print('nparr.DATA =>', nparr.data)

print("\n=== Numpy Array 메소드 ====")
print('nparr.max() =>', nparr.max())
print('nparr.min() =>', nparr.min())
print('nparr.sum() =>', nparr.sum())               # 원소 합계
print('nparr.sum(axis=0) =>', nparr.sum(axis=0))   # 열(col)방향 합
print('nparr.sum(axis=1) =>', nparr.sum(axis=1))   # 행(row)방향 합
print('nparr.mean() =>', nparr.mean())             # 원소값 평균