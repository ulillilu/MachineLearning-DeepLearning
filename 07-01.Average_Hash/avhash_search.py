from PIL import Image
import numpy as np
import os, re
# 파일 경로 지정
search_dir = "./image/101_ObjectCategories"
cache_dir = "./image/cache_avhash"
if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)
# 이미지 데이터를 Average Hash로 변환 + 다수 파일 계산을 위해 캐시로 저장
def average_hash(fname, size = 16):
    fname2 = fname[len(search_dir):]
    # 이미지 캐시
    cache_file = cache_dir + "/" + fname2.replace('/', '_') + ".csv"
    if not os.path.exists(cache_file): # 해시 생성
        img = Image.open(fname)
        img = img.convert('L').resize((size, size), Image.ANTIALIAS)
        pixels = np.array(img.getdata()).reshape((size, size))
        avg = pixels.mean()
        px = 1 * (pixels > avg)
        np.savetxt(cache_file, px, fmt="%.0f", delimiter=",") # 값을 외부파일에 저장
    else: # 캐시돼 있다면 읽지 않기
        px = np.loadtxt(cache_file, delimiter=",")
    return px
# 해밍 거리(두 정수 사이의 상응하는 위치에서 값이 다른 비트의 개수) 구하기
def hamming_dist(a, b):
    aa = a.reshape(1, -1) # 1차원 배열로 변환하기
    ab = b.reshape(1, -1)
    dist = (aa != ab).sum()
    return dist # 두 이미지의 비유사도 확인
# 모든 폴더에 처리 적용
def enum_all_files(path):
    if __name__ == "__main__":
        root_dir = "./image/"
        for (root, dirs, files) in os.walk(root_dir):
            # print("# root : " + root)
            if len(files) > 0:
                for file_name in files:
                    # print("file: " + file_name)
                    fname=root + "/" + file_name
                    yield fname
# 이미지 찾기
def find_image(fname, rate):
    src = np.loadtxt('./image/cache_avhash/_chair_image_0016.jpg.csv', delimiter=",")
    files = os.listdir("./image/cache_avhash")
    for file in files:
        path = os.path.join("./image/cache_avhash", file)
        dst = np.loadtxt(path, delimiter=",")
        diff_r = hamming_dist(src, dst) / 256
        # print("[check] ",fname)
        if diff_r < rate:
            yield (diff_r, fname) # generator func
# 찾기
srcfile = search_dir + "/chair/image_0016.jpg"
html = ""
sim = list(find_image(srcfile, 0.25))
sim = sorted(sim, key=lambda x:x[0])
for r, f in sim:
    print(r, ">", f)
    s = '<div style="float:left;"><h3>[ 차이 :' + str(r) + '-' + \
        os.path.basename(f) + ']</h3>'+ \
        '<p><a href="' + f + '"><img src="' + f + '" width=400>'+ \
        '</a></p></div>'
    html += s

html = """<html><head><meta charset="utf8"></head>
<body><h3>원래 이미지</h3><p>
<img src='{0}' width=400></p>{1}
</body></html>""".format(srcfile, html)
with open("./avhash-search-output.html", "w", encoding="utf-8") as f:
    f.write(html)
print("ok")