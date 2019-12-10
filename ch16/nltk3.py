from nltk.stem import PorterStemmer, LancasterStemmer

# 둘다 억간을 찾아주는 모듈 -> 기본형을 찾아 준다.
# PorterStemmer, LancasterStemmer


words = ['lives','crying','files','dying']

st = PorterStemmer()
print([st.stem(w) for w in words] )

ls = LancasterStemmer()
print([ls.stem(w) for w in words])