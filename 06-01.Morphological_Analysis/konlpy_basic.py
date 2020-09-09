from konlpy.tag import Okt

okt = Okt()
malist = okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True) # norm:일반형으로 stem:원형으로
print(malist)