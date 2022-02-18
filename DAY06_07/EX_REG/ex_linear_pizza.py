# ---------------------------------------------------------------
# 목표 : 피자 사이즈에 따른 가격 예측
# 단계 1 : 데이터 수집, 데이터 분포 분석
# ---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# 데이터 ---------------------------------------------------------
# 인치 x, 가격 y
x=np.array([6,8,10,15,18])
y=np.array([7,9,13,17.5,19.3])

# 함수선언 -------------------------------------------------------
def draw_linear(data):
    return data*1.0-0.1

def draw_linear2(data):
    return data*1.2-0.1

# 데이터 분포 확인 및 임의의 그래프 그리기 ----------------------------
plt.figure()
plt.plot(x, y, 'ro')
plt.plot(x, draw_linear(x), 'k--')
plt.plot(x, draw_linear2(x), 'g--')
plt.title('Pizza Price(inch)')
plt.xlabel('Inches')
plt.ylabel('Price')
plt.axis([0,25,0,25])
plt.grid()
plt.show()