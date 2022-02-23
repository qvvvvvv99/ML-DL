# -*- coding: utf-8 -*-
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
import pandas as pd
import numpy
import os
import tensorflow as tf

# -------------------------------------------------------------
#  Wine 데이터에 따른 Wine 등급 분류
#  12개 Wine 속성(Attribute, Feature) => 와인판별
# -------------------------------------------------------------

# seed 값 설정
# numpy.random.seed(3)
# tf.random.set_seed(3)

# (1) 데이터 준비 -----------------------------------------------------
# (1-1) 데이터 로딩
df_pre = pd.read_csv('../Data/WINE/wine.csv', header=None)
df = df_pre.sample(frac=0.15) # 전체 데이터 중 15% 데이터만 추출
print(f'df.shape => {df.shape}, {type(df)}')

# (1-2) 데이터 + 라벨 분리
#dataset = df.values
X = df.iloc[:,:12]
Y = df.iloc[:,12]

# (2) 모델 구조 설계 ------------------------------------------------
model = Sequential()
# 12개 wine 속성 입력, 30개 노드(퍼셉트론)으로 출력
model.add(Dense(30,  input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
# 출력 층
model.add(Dense(1, activation='sigmoid'))

# (3) 모델 생성 ---------------------------------------------
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# (4) 학습 및 모델 성능 체크 ---------------------------------------
MODEL_DIR = './model/'
modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
if not os.path.exists(MODEL_DIR): os.mkdir(MODEL_DIR)

# 모델 업데이트 및 저장
checkpointer = ModelCheckpoint(filepath=modelpath,
                               monitor='val_loss',
                               verbose=1,
                               save_best_only=True)

# 학습 자동 중단 설정
early_stopping_callback = EarlyStopping(monitor='val_loss',
                                        patience=100)

# 학습 진행
model.fit(X,
          Y,
          validation_split=0.2,
          epochs=3500,
          batch_size=500,
          verbose=0,
          callbacks=[early_stopping_callback,checkpointer])


