from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.datasets import imdb
import numpy as np

categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)
image_w = 64 
image_h = 64

X_train, X_test, y_train, y_test = np.load("./image/5obj.npy")
# 데이터 정규화
X_train = X_train.astype("float") / 256
X_test  = X_test.astype("float")  / 256
print('X_train shape:', X_train.shape)

# CNN 모델 구축(5계층)
model = Sequential()
model.add(Convolution2D(32, 3, 3, 
    border_mode='same',
    input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten()) # 2개의 전결합층 배치
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])

# 모델 훈련
model.fit(X_train, y_train, batch_size=32, epochs=50)
    
# 모델 평가
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])


