import urllib.request 
# URL과 저장명 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
# urlopen을 사용하여 읽어들이고 mem에 저장
mem = urllib.request.urlopen(url).read()
# 파일로 저장
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다...!")