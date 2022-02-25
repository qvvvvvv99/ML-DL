import os.path

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt
import numpy, os
import tensorflow.keras.utils as utils

(x_train, y_train), (x_test, y_test)= mnist.load_data()
print(f'x_train.shap : ')

x_train=x_train.reshape(x_train.shape[0], 28,28,1).astype('float32')/255
x_test=x_test.reshape(x_test.shape[0], 28,28,1).astype('float32')/255

y_train = utils.to_categorical(y_train)
y_test = utils.to_categorical(y_test)

model=Sequential()
model.add(Conv2D(32,kernel_size=(3,3),
                 input_shape=(28,28,1),
                 activation='relu'))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.summary()

# (3) 모델 구축 ------- 중요!!!!
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

MODEL_DIR='./Model_CNN/'
if not os.path.exists(MODEL_DIR): os.mkdir(MODEL_DIR)

modelpath="./Model_CNN/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath,
                               monitor='val_loss',
                               verbose=1,
                               save_best_only=True)
early_stopping_collback=EarlyStopping(monitor='val_loss',
                                      patience=10)

hist=model.fit(x_train, y_train,
               validation_data=(x_test, y_test),
               epochs=1,
               batch_size=200,
               verbose=0,
               callbacks=[early_stopping_collback, checkpointer])

print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))