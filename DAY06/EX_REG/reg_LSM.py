import matplotlib.pyplot as plt
import numpy as np

# 지도학습 - 회귀(Regression)

# (1) 데이터 준비 및 확인 -------------------------------
x=[2, 4, 6, 8]
y=[81, 93, 91, 97]

# (2) 데이터 지나는 직석 긋기 ----------------------------
# 일차 함수 기울기 => 기울기 = (x-x평균)(y-y평균) 합 | (x-x평균) 합
# x와 y의 평균값
mx=np.mean(x)
my=np.mean(y)
print(f'x의 평균값 : {mx}, y의 평균값 : {my}')

# 기울기 공식의 분모
divisor=sum([(mx-i)**2 for i in x])

# 기울기 공식의 분자
def top(x, mx, y, my):
    d=0
    for i in range(len(x)):
        d+=(x[i]-mx)*(y[i]-my)
    return d

dividend=top(x, mx, y, my)
print(f'분모 : {divisor} - 분자 : {dividend}')

# 기울기와 y 절편 구하기
a=dividend/divisor
b=my-(mx*a)

print(f'기울기 a = {a} - y 절편 b = {b}')

y2=[a*i+b for i in x]
plt.plot(x, y, 'ro')
plt.plot(x, y2)
plt.show()