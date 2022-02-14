"""
FileName : numpy_03.py
Numpy Array 배열 생성
"""
# 모듈로딩 -----------------------------------
import numpy as np

# numpy 배열 생성 및 초기화 --------------------------
a = np.arange(10)           # 0 ~ (10-1)
print(f'a.shape={a.shape}')
print(f'a={a}\n')

a = np.linspace(0, 100, 3)  # 시작, 끝(포함), 갯수
print(f'a.shape={a.shape}')
print(f'a={a}\n')

a = np.linspace(0, 100, 3, endpoint=False)  # 시작, 끝(포함), 갯수
print(f'a.shape={a.shape}')
print(f'a={a}\n')

a, step = np.linspace(0, 100, 13, endpoint=False, retstep=True)  # 시작, 끝(포함), 갯수
print(f'a.shape={a.shape}')
print(f'a={a}\nstpe={step}')


