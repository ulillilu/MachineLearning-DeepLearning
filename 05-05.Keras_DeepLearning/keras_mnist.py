from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam 
from keras.utils import np_utils
# MNIST 데이터 읽기
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# 데이터를 float32 자료형으로 변환
X_train = X_train.reshape(60000, 784).astype('float32')
X_test  = X_test.reshape(10000, 784).astype('float')
# 정규화
X_train /= 255
X_test  /= 255
# 레이블 데이터를 0-9까지의 카테고리를 나타내는 배열로 변환
y_train = np_utils.to_categorical(y_train, 10)
y_test  = np_utils.to_categorical(y_test, 10)
# 모델 구조 정의
model = Sequential() # 딥러닝의 각 층을 add로 추출 가능하게 함

model.add(Dense(512, input_shape=(784,))) # 합성곱층1
model.add(Activation('relu')) # 풀링층1
model.add(Dropout(0.2))

model.add(Dense(512)) # 합성곱층2
model.add(Activation('relu')) # 풀링층2
model.add(Dropout(0.2))

model.add(Dense(10)) # 전결합층
model.add(Activation('softmax')) # 출력층
# 모델 구축
model.compile(
    loss='categorical_crossentropy', # 최적화 함수 지정
    optimizer=Adam(),
    metrics=['accuracy'])
# 데이터 훈련
hist = model.fit(X_train, y_train)
# 정답률 구하기
score = model.evaluate(X_test, y_test, verbose=1)
print('loss=', score[0])
print('accuracy=', score[1])