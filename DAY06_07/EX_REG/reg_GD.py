# ------------------------------------------------------------------------------
# 지도 학습 - 회귀 (Regression) => 3단계 최적화
# ------------------------------------------------------------------------------

import numpy as np

# (1) 데이터 준비 ----------------------------------------------------------------
data=[[2,81],[4,93],[6,91],[8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# 데이터 가공 => ndarray 타입으로 변환한 데이터와 라벨
x_data=np.array(x)
y_data=np.array(y)

# (2) 경사하강법 진행 --------------------------------------------------------------
a, b  = 0,0     # 기울기 a와 절편 b의 초기화
lr = 0.03       # 학습률 초기화
epochs=2001     # 학습 횟수 초기화

for i in range(epochs):
    # 오차계산
    y_hat=a*x_data+b    # y=ax+b
    error=y_data-y_hat

    # a, b 미분값 계산
    a_diff=-(2/len(x_data))*sum(x_data*(error))
    b_diff=-(2/len(x_data))*sum(error)

    # a, b 값 업데이트
    a=a-lr*a_diff
    b=b-lr*b_diff

    if i % 100 == 0:
        print(f'epoch={i}, 기울기={a}, 절편={b}, 오차={error}')