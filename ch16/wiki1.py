from gensim.models import word2vec

#
model = word2vec.Word2Vec.load('wiki.model')


# print(model.wv.most_similar(positive=['Python','파이썬'])[0:5])
# print(model.wv.most_similar(positive=['아빠','여성'], negative=['남성'])[0:5])
# print(model.wv.most_similar(positive=['왕자','여성'], negative=['남성'])[0:5])
# print(model.wv.most_similar(positive=['서울','일본'], negative=['한국'])[0:5])
# print(model.wv.most_similar(positive=['서울','중국'], negative=['한국'])[0:5])
# print(model.wv.most_similar(positive=['서울','맛집'])[0:5])
# print(model.wv.most_similar(positive=['오른쪽','남자'],negative=['왼쪽'])[0:5])

print(model.wv.most_similar(positive=['안지만'])[0:25])
# print(model.wv.most_similar(positive=['프로야구','홈런'])[0:10])