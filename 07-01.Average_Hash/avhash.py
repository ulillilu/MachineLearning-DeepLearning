from PIL import Image
import numpy as np
# 이미지 데이터를 Average Hash로 변환
def average_hash(fname, size = 16): # 이미지 크기 8*8로 축소
    img = Image.open(fname) # 이미지 데이터 열기
    img = img.convert('L') # 그레이스케일로 변환
    img = img.resize((size, size), Image.ANTIALIAS) # 리사이즈
    pixel_data = img.getdata() # 픽셀 데이터 가져오기
    pixels = np.array(pixel_data) # 픽셀 데이터를 Numpy 배열로 변환
    pixels = pixels.reshape((size, size)) # 2차원 배열로 변환
    avg = pixels.mean() # 각 픽셀의 평균 계산
    diff = 1 * (pixels > avg) # 어두운 정도가 평균보다 크면 1, 작으면 0으로 변환
    return diff
# 이진 해시로 변환
def np2hash(ahash):
    bhash = []
    for nl in ahash.tolist(): # .tolist() 배열에서 리스트인 요소만 추출
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        # 이진수를 16진수 해시값으로 변환
        i = int(s2, 2)
        bhash.append("%04x" % i)
    return "".join(bhash) # "구분자".join(리스트명) : 리스트에 특정 구분자를 추가하여 문자열로 변환
# Average Hash 출력
ahash = average_hash('sky.jpg')
print(ahash)
print(np2hash(ahash))