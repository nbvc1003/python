from nltk.tag import pos_tag, untag
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

# 품사 tag 를 제거 한다.
print(untag(tagged_list))

# 단어와 품사를 묶어서 한 문자열로 변경
def tokenizer(doc):
    return ['/'.join(p) for p in tagged_list]  # 배열을 하나의 문자열로 '/'로 구분해서 합친다. 

print(tokenizer(tagged_list))
# ['Emma/NNP', 'refused/VBD', 'to/TO', 'permit/VB', 'us/PRP', 'to/TO', 'obtain/VB', 'the/DT', 'refuse/NN', 'permit/NN', "''/''"]
