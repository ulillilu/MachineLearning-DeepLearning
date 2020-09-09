import codecs
from bs4 import BeautifulSoup
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

fp = codecs.open("./4BH00002.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText() + " "
print('코퍼스의 길이: ', len(text))
# 문자를 하나하나 읽기
chars = sorted(list(set(text)))
print('사용되고 있는 문자의 수:', len(chars))
# 문자에 ID 부여
char_indices = dict((c, i) for i, c in enumerate(chars)) # 문자 → ID {문자 : ID}
indices_char = dict((i, c) for i, c in enumerate(chars)) # ID → 문자 {ID : 문자}
# 텍스트를 maxlen개의 문자로 자르고 다음에 오는 문자 등록하기
maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step): 
    sentences.append(text[i: i + maxlen]) # sentences[text[]]에 i번째에서 i + maxlen - 1까지의 문자를 등록
    next_chars.append(text[i + maxlen]) # next_chars[text[]]에i + maxlen번째 문자 등록
print('학습할 구문의 수:', len(sentences)) # 반복문을 수행한 만큼의 수
print('텍스트를 ID 벡터로 변환합니다...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool) # [[[]]]
y = np.zeros((len(sentences), len(chars)), dtype=np.bool) # [[]]

for i, sentence in enumerate(sentences): # maxlen개의 단어로 묶인 text[] 별로 반복
    for t, char in enumerate(sentence): # text[]의 요소인 단어별로 반복
        X[i, t, char_indices[char]] = 1 # 행렬 X에서 현재 단어의 ID와 일치하는 위치의 값을 1 증가 
    y[i, char_indices[next_chars[i]]] = 1 # 행렬 y에서 현재 단어의 ID와 일치하는 위치의 값을 1 증가 
# 모델 구축하기(LSTM)
print('모델을 구축합니다...')
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
# 후보를 배열에서 꺼내기
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds) # 평균
    probas = np.random.multinomial(1, preds, 1) # 다항분포 시뮬레이션 np.random.multinomial(선택 수행 수, 확률의 집합, 사이즈)
    return np.argmax(probas)
# 학습시키고 텍스트 생성하기 반복
for iteration in range(1, 60):
    print()
    print('-' * 50)
    print('반복 =', iteration)
    model.fit(X, y, batch_size=128, epochs=1) # 
    # 임의의 시작 텍스트 선택하기
    start_index = random.randint(0, len(text) - maxlen - 1)
    # 다양한 다양성의 문장 생성
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('--- 다양성 = ', diversity)
        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('--- 시드 = "' + sentence + '"')
        sys.stdout.write(generated)
        # 시드를 기반으로 텍스트 자동 생성
        for i in range(400):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.
            # 다음에 올 문자를 예측하기
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]
            # 출력하기
            generated += next_char
            sentence = sentence[1:] + next_char
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()