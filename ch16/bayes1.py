import math, sys
from konlpy.tag import Okt

class Bayesianfilter:
    def __init__(self):
        # 전역변수 지정
        # set : 인덱스없고 중복없는 데이터들의 집합
        # Build an unordered collection of unique elements.
        self.words = set() # 출현한 단어 기록 중복허용 않음
        self.words_dict = {}  # 카테고리별 출현 횟수
        self.category_dict = {} # 카테고리 출현 횟수
        
    def split(self,text):
        results = []
        okt = Okt()
        malist = okt.pos(text, norm=True, stem=True)
        for word in malist:
            # 어미, 조사, 구둣점 제외
            if not word[1] in ['Josa','Eomi','Punction']:
                results.append(word[0])
        return results

    # 단어와 카테고리의 출현횟수 세기
    def inc_word(self, word, category):
        # 단어를 카테고리에 추가
        if not category in self.words_dict:
            self.words_dict[category] = {} # dictioanry 안에 또다시 dictionary 형 정의
        if not word in self.words_dict:
            self.words_dict[category][word] = 0
        self.words_dict[category][word] += 1
        self.words.add(word)

    #카테고리 계산
    def inc_category(self, category):
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    # 텍스트 학습
    def fit(self, text, category):
        # 문장이 들어오면 어미 구돗점 , 조사를 제외하고 list로 만듦
        word_list = self.split(text)
        for word in word_list:
            # 카테고리별 단어의 갯수
            self.inc_word(word, category)
        # 카테고리의 출현횟수
        self.inc_category(category)
    
    # 단어 리스트에 점수
    def score(self, words, category):
        # math.log : 값을 작게 만든다.

        # 카테고리에 대한 확률
        score = math.log(self.category_prob(category))
        for word in words:
            # 단어에 대한 확률
            score += math.log(self.word_prob(word,category))

        return score


    #예측, 카테고리일 확률 계산
    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize # 시스템상 가장 낮은수
        words = self.split(text)
        score_list = []
        for category in self.category_dict.keys():
            score = self.score(words, category)
            score_list.append((category,score))
            if score > max_score:
                max_score = score
                best_category = category
        return best_category, score_list

    # 카테고리 내부 단어 출현 횟수
    def get_word_count(self, word, category):
        if word in self.words_dict[category]:
            return self.words_dict[category][word]
        else:
            return 0

    # 카테고리 출현 비율
    def category_prob(self,  category):
        sum_catogories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        return category_v / sum_catogories
    
    # 카테고리 내부 단어 출현 비율
    def word_prob(self, word, category):
        n = self.get_word_count(word, category) +1
        d = sum(self.words_dict[category].values()) + len(self.words)
        return n/d
    




        
        