import numpy as np
import matplotlib.pyplot as plt

# (1) 데이터 준비 -------------------------------------------------------------
# 공부시간 X - 합격여부 Y => 0:불합격, 1:합격
data=[[2,0],[4,0],[6,0],[8,1],[10,1],[12,1],[14,1]]

# 데이터와 라벨 분리
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

# (2) 최적화 => 기울기와 절편 찾기 ------------------------------------------------
a=b=0
lr=0.05

# 시그모이드 함수 정의
def sigmoid(x):
    return 1 / (1+np.e**(-x))

# 경사하강법 실행
for i in range(2001):
    for x_data, y_data in data:
        # a, b에 대한 경사하강법에 따른 값 찾기
        a_diff=x_data*(sigmoid(a*x_data+b)-y_data)
        b_diff=sigmoid(a*x_data+b)-y_data

        # a, b값 업데이트
        a=a-lr*a_diff
        b=b-lr*b_diff

        if i % 100 == 0:
            print(f'epoch={i}, 기울기={a}, 절편={b}')

# (3) 시각화 - 미완료
plt.scatter(x_data, y_data, c='red')
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)
x_range=(np.arange(0,15,0.1))
#plt.plot(np.arange(0,15,0.1), np.array([sigmoid(x_data)]), np.array([sigmoid(y_data)]))
#plt.show()