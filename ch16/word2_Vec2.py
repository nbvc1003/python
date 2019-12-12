from gensim.models import word2vec
model = word2vec.Word2Vec.load("toji.model")

# positive: 긍정적으로 기여하는 ,  negative 부정적으로 기여 하는 단어
print(model.wv.most_similar(positive=['땅'])[0:15])
print(model.wv.most_similar(positive=['집'])[0:5])
print(model.wv.most_similar(positive=['서희','남자'], negative=['남자']))
