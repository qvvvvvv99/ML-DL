import numpy as np

# 전역번수 ------------------------------------------------------------
# 임의의 기울기 및 절편
fake_a_b=[3,76]

# 사용자 정의 함수 -----------------------------------------------------
# 예측값 구하는 함수 y=ax+b
def predict(x):
    return fake_a_b[0]*x + fake_a_b[1]

# MSE 함수
def mse(y, y_hat):
    return ((y-y_hat) ** 2).mean()

# MSE 함수를 각 y값에 대입하여 최종값을 구하는 함수
def mse_val(y, predict_result):
    return mse(np.array(y), np.array(predict_result))

# (1) 데이터 준비 -----------------------------------------------------
# [공부시간, 점수]
data=[[2,81],[4,93],[6,91],[8,97]]

# 데이터/라벨 분리하기
x = [i[0] for i in data]
y = [i[1] for i in data]

# (2) y=ax+b 공식에 x값 대입하여 예측값 구하기 ---------------------------
predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print(f"공부시간 = {x[i]}, 실제점수 = {y[i]}, 예측점수 = {predict(x[i])}")

# (3) 실제값 - 예측값 사이 오차 계산 ------------------------------------
print(f"MSE 최종 오차 : {mse_val(predict_result, y)}")