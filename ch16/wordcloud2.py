from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# 한글 그래프 처리시 필수
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

text = """
        사과 수박 수박 수박 수박 수박 복숭아 복숭아 복숭아 복숭아
        키위 바나나 바나나 바나나 바나나 곶감 곶감  
        """

# 제외시길 단어 추가..
stop = set(STOPWORDS)
stop.add("사과")
stop.add("곶감")

wordcloud = WordCloud(font_path= font_path, stopwords=stop).generate(text)


plt.imshow(wordcloud)
plt.axis("off")
plt.show()