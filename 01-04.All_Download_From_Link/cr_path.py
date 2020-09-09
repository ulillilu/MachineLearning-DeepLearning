#상대 경로를 절대 경로로 전환
from urllib.parse import urljoin

url = "http://example.com/html/a.html"
print( urljoin(url, "b.html") )
print( urljoin(url, "sub/c.html") )
print( urljoin(url, "../index.html") )
print( urljoin(url, "../img/hoge.png") )
print( urljoin(url, "../css/hoge.css") )