from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split
# 분류 대상 카테고리 선택
caltech_dir = "./image/101_ObjectCategories"
categories = ["anchor", "flamingo", "garfield", "scorpion", "watch"]
nb_classes = len(categories) # 5
# 이미지 크기 지정(RGB24 bit, 64*64 pixel로 resizing)
image_w = 64 
image_h = 64
pixels = image_w * image_h * 3
# 이미지 데이터 읽기
X = []
Y = []
for idx, cat in enumerate(categories):
    # 레이블 지정
    label = [0 for i in range(nb_classes)]
    label[idx] = 1 # ex) 해당 예시에서 scorpion(3)의 label data는 [0, 0, 0, 1, 0]
    # 이미지
    image_dir = caltech_dir + "/" + cat
    files = glob.glob(image_dir+"/*.jpg") # 특정 확장자만을 검색
    for i, f in enumerate(files):
        img = Image.open(f) 
        img = img.convert("RGB") # 색상 모드 RGB로 전환
        img = img.resize((image_w, image_h))
        data = np.asarray(img) # image 데이터인 img를 배열 데이터로 변환
        X.append(data)
        Y.append(label)
        if i % 10 == 0:
            print(i, "\n", data)
X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = \
    train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/5obj.npy", xy)
print("ok,", len(Y))