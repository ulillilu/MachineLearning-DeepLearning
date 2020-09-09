# 분류한 이미지를 학습 데이터로 읽어 들일 수 있도록 Numpy로 변환
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from PIL import Image
import os, glob
import numpy as np
# 분류 대상 카테고리 지정
root_dir = "./image/"
categories = ["cake", "drink", "ice", "fruits"]
nb_classes = len(categories)
image_size = 50
# 폴더마다의 이미지 데이터 읽기
X = [] # 이미지 데이터
Y = [] # 레이블 데이터
for idx, cat in enumerate(categories):
    image_dir = root_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    print("---", cat, "처리 중")
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB") # 색상 모드 변경
        img = img.resize((image_size, image_size)) # 이미지 크기 변경
        data = np.asarray(img)
        X.append(data)
        Y.append(idx)
X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = \
    train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./image/dessert.npy", xy)
print("ok,", len(Y))