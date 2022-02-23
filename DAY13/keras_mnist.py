from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import Adam
import tensorflow.keras.utils as utils

(x_train, y_train), (x_test, y_test)= mnist.load_data()

x_train=x_train.reshape(60000, 784).astype('float32')
x_test=x_test.reshape(10000, 784).astype('float')
x_train /= 255
x_test /= 255

y_train = utils.to_categorical(y_train, 10)
y_test = utils.to_categorical(y_test, 10)

model=Sequential()
model.add(Dense(512, input_dim=784))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))

model.summary()

# (3) 모델 구축 ------- 중요!!!!
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(),
    metrics=['accuracy']
)

# (4) 데이터 훈련하기(학습하기)
hist=model.fit(x_train, y_train)
print(f'hist => {hist.history}')

# (5) 테스트 데이터로 평과
score=model.evaluate(x_test, y_test, verbose=1)
print('loss=', score[0])
print('accuracy=', score[1])