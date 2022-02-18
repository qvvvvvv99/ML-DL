"""
FileName : numpy_03.py
Numpy Array 배열 생성
"""
# 모듈로딩 -----------------------------------
import numpy as np

# ndarray 배열 생성 및 초기화 --------------------------
a = np.zeros(5, dtype='i')
print(f'a.shape={a.shape}\t a.dtype={a.dtype}')
print(f'a={a}\n')

a = np.zeros((2,3), dtype='i')
print(f'a.shape={a.shape}\t a.dtype={a.dtype}')
print(f'a={a}\n')

b = np.ones((2,3), dtype='i8')
print(f'b.shape={b.shape}\t b.dtype={b.dtype}')
print(f'b={b}\n')

# 다른 배열과 같은 크기로 생성하고 싶은 경우 -------------
c = np.ones_like(b, dtype='f')
print(f'c.shape={c.shape}\t c.dtype={c.dtype}')
print(f'c={c}\n')

d = np.zeros_like(b, dtype='f')
print(f'd.shape={d.shape}\t d.dtype={d.dtype}')
print(f'd={d}\n')


# 초기화 하지 않고 생성하고 싶은 경우 -------------
e = np.empty((4,3))
print(f'e.shape={e.shape}')
print(f'e={e}\t e.dtype={e.dtype}\n')