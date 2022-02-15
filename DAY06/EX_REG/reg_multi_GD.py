# ------------------------------------------------------------------------------
# 지도 학습 - 회귀 (Regression) => 3단계 최적화
# ------------------------------------------------------------------------------

import numpy as np

# (1) 데이터 준비 ----------------------------------------------------------------
# [공부시간, 보충횟수, 점수]
data=[[2,0,81],[4,4,93],[6,2,91],[8,3,97]]
x1 = [i[0] for i in data]
x2 = [i[1] for i in data]
y = [i[2] for i in data]

# 데이터 가공 => ndarray 타입으로 변환한 데이터와 라벨
x1_data=np.array(x1)
x2_data=np.array(x2)
y_data=np.array(y)

# (2) 경사하강법 진행 --------------------------------------------------------------
a1, a2, b  = 0,0,0     # 기울기 a와 절편 b의 초기화
lr = 0.03       # 학습률 초기화
epochs=2001     # 학습 횟수 초기화

for i in range(epochs):
    # 오차계산
    y_pred=a1*x1_data+a2*x2_data+b    # y=ax+b
    error=y_data-y_pred

    # a, b 미분값 계산
    a1_diff=-(2/len(x1_data))*sum(x1_data*(error))
    a2_diff=-(2 / len(x2_data)) * sum(x2_data * (error))
    b_diff=-(2/len(x1_data))*sum(y_data-y_pred)
    
    # a, b 값 업데이트
    a1=a1-lr*a1_diff
    a2 = a2 - lr * a2_diff
    b=b-lr*b_diff

    if i % 100 == 0:
        print(f'epoch={i}, 기울기1={a1}, 기울기2={a2}, 절편={b}, 오차={error}')