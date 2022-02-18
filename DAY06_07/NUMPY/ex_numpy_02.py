import numpy as np

a=np.zeros(5, dtype='i')
print(f'a.shape={a.shape}\t a.dtype={a.dtype}')
print(f'a={a}\n')

a=np.zeros((2,3), dtype='i')
print(f'a.shape={a.shape}\t a.dtype={a.dtype}')
print(f'a={a}\n')

a=np.ones(5, dtype='i')
print(f'a.shape={a.shape}\t a.dtype={a.dtype}')
print(f'a={a}\n')

# numpy 배열 생성 및 초기화 -------------------------------
a=np.arange(10)     # 0 ~ (10 - 1)
print(f'a.shape={a.shape}')
print(f'a={a}\n')

a=np.linspace(0,100,12)                 # 시작, 끝(포함), 갯수
print(f'a.shape={a.shape}')
print(f'a={a}\n')

a=np.linspace(0,100,3, endpoint=False)     # 시작, 끝(미포함), 갯수
print(f'a.shape={a.shape}')
print(f'a={a}\n')

a,step=np.linspace(0, 100, 13, retstep=True)    # 시작, 끝(포함), 갯수
print(f'a.shape={a.shape}')
print(f'a={a}\nstep={step}')