# 모듈로딩 -----------------------------------
import numpy as np

print(f' np.ndarray =>{np.ndarray}')

# numpy 객체 생성 -----------------------------
nparray01=np.array([1,2,3,4,5])
print('type(nparray01) =', type(nparray01))
print('nparray01 =', nparray01)
print('nparray01.shape =', nparray01.shape)
print('nparray01.size =', nparray01.size)
print('nparray01.dtype =', nparray01.dtype)
print(nparray01,'\n')


nparray01=np.array(['a','b','c'])
print('type(nparray01) =', type(nparray01))
print('nparray01 =', nparray01)
print('nparray01.shape =', nparray01.shape)
print('nparray01.size =', nparray01.size)
print('nparray01.dtype =', nparray01.dtype)
print(nparray01,'\n')

nparray01=np.array(['a',1,True])
print('type(nparray01) =', type(nparray01))
print('nparray01 =', nparray01)
print('nparray01.shape =', nparray01.shape)
print('nparray01.size =', nparray01.size)
print('nparray01.dtype =정수형+문자형 <U11', nparray01.dtype)
print(nparray01,'\n')

nparray02=np.array([[1,2,3], [11,22,33]], dtype=object)
print('type(nparray02) =', type(nparray02))
print('nparray02.shape =', nparray02.shape)
print('nparray02.size =', nparray02.size)
print('nparray02.dtype =', nparray02.dtype)
print('nparray02 =>', nparray02)
print('nparray02[0] =>', nparray02[0])
print('nparray02[1] =>', nparray02[1])
print()

nparray03=np.array([[[1,2,3], [11,22,33]], [[4,5,6],[44,55,66]]], dtype=object)
print('type(nparray03) =', type(nparray03))
print('nparray03.shape(깊이,행,열) =', nparray03.shape)
print('nparray03.size =', nparray03.size)
print('nparray03.dtype =', nparray03.dtype)
print('nparray03 =>', nparray03)
print('nparray03[0] =>', nparray03[0])
print('nparray03[1] =>', nparray03[1])