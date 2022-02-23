#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint
import pandas as pd
import numpy
import os
import matplotlib.pyplot as plt
import tensorflow as tf

# -------------------------------------------------------------
#  Wine 데이터에 따른 Wine 등급 분류
#  12개 Wine 속성(Attribute, Feature) =>와인 판별
# -------------------------------------------------------------

# seed 값 설정
numpy.random.seed(3)
tf.random.set_seed(3)

# (1) 데이터 준비 -----------------------------------------------------
# (1-1) 데이터 로딩
df_pre = pd.read_csv('../Data/WINE/wine.csv', header=None)
df = df_pre.sample(frac=0.15)

# (1-2) 데이터 + 라벨 분리
X = df.iloc[:,:12]
Y = df.iloc[:,12]

# (2) 모델 구조 설계 --------------------------------------------
model = Sequential()
# 12개 wine 속성 입력, 30개 노드(퍼셉트론)으로 출력
model.add(Dense(30,  input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# (3) 모델 생성 ---------------------------------------------
model.compile(loss='binary_crossentropy',
          optimizer='adam',
          metrics=['accuracy'])

# (4) 학습 및 모델 성능 체크 ---------------------------------------
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR): os.mkdir(MODEL_DIR)

# 모델 저장 조건 설정
modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath,
                               monitor='val_loss',
                               verbose=1,
                               save_best_only=True)

# (4) 학습 및 모델 성능 체크 ---------------------------------------
history = model.fit(X, Y,
                    validation_split=0.33,
                    epochs=3500,
                    batch_size=500)

# (5) 모델 성능 시각화  ---------------------------------------
# 결과 오차 값 저장
y_vloss=history.history['val_loss']

# 정확도 값 저장
y_acc=history.history['accuracy']

# 오차 & 정확도 시각화 ---------------------------------------------
x_len = numpy.arange(len(y_acc))
plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
plt.plot(x_len, y_acc, "o", c="blue", markersize=3)
plt.legend(['loss', 'acc'])

plt.show()
