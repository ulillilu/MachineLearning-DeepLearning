import urllib.request
# URL과 저장명 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
# 다운로드, 실행위치와 같은 장소에 파일저장
urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")