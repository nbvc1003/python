from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

sentence = 'Emma refused to permit us to obtain the refuse permit"'

# 문장을 단어로 분리하고 그것을 품사와 같이 표시
tagged_list = pos_tag(word_tokenize(sentence))
print(tagged_list)
#    t[0]   t[1]      t[0]      t[1]     t[0]  t[1]
#[('Emma', 'NNP'), ('refused', 'VBD'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'), ('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('refuse', 'NN'), ('permit', 'NN'), ("''", "''")]
noun_list = [t[0] for t in tagged_list if t[1] == 'NN']
# 리스트중 =='NN' 인 명사만 가져온다.

print(noun_list)
