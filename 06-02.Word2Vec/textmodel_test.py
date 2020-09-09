from gensim.models.word2vec import Word2Vec
model = Word2Vec.load("text.model")

print(model.wv.most_similar(positive='종')) # 유사단어 확인
print(model.wv.most_similar(positive='각'))