from urllib.parse import urljoin

url = "http://example.com/html/a.html"
print( urljoin(url, "/hoge.html") )
print( urljoin(url, "http://otherExample.com/wiki") )
print( urljoin(url, "//anotherExample.org/test") )