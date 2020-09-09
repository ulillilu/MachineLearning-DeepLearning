from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

csv = pd.read_csv("bmi.csv")
# 데이터 정규화
csv["weight"] /= 100
csv["height"] /= 200
X = csv[["weight", "height"]] # pandas로 추출한 데이터를 Keras에서 사용하기 위해 Numpy 데이터로 변환

bclass = {"thin":[1,0,0], "normal":[0,1,0], "fat":[0,0,1]}
y = np.empty((20000,3)) # 20000행 3열의 빈 행렬 생성
# label 데이터를 행렬 y에 삽입
for i, v in enumerate(csv["label"]):
    y[i] = bclass[v]
# 데이터 분할
X_train, y_train = X[1:15001], y[1:15001]
X_test,  y_test  = X[15001:20001], y[15001:20001] 

model = Sequential()

model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer="rmsprop",
    metrics=['accuracy'])

hist = model.fit(
    X_train, y_train,
    batch_size=100, #배치 크기(훈련 데이터를 여러 개의 작은 배치로 나누어 매개변수 수정 시 배치의 크기)
    epochs=20, # 학습 횟수
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)], # 데이터 감시(EalryStopping:정밀도 문제 시 훈련 중지)
    verbose=1)

score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])