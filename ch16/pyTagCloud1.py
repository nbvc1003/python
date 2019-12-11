import pytagcloud
from collections import Counter

nouns = list() # 명시적으로 list 형 자료 선언
#nouns.extend(['불고기' for t in rage(8)])
nouns.extend(['불고기' for t in range(8)])
nouns.extend(['비빔밥'])
nouns.extend(['김치찌게' for t in range(5)])
nouns.extend(['된장찌게' for t in range(25)])
nouns.extend(['돈까스' for t in range(12)])
nouns.extend(['짬뽕' for t in range(38)])
nouns.extend(['짜장' for t in range(2)])
nouns.extend(['초밥' for t in range(3)])
nouns.extend(['우동' for t in range(5)])
nouns.extend(['라면' for t in range(28)])
nouns.extend(['만두라면' for t in range(3)])
nouns.extend(['김밥' for t in range(15)])
nouns.extend(['잡채' for t in range(12)])
nouns.extend(['만두' for t in range(20)])
nouns.extend(['냉면' for t in range(20)])

nouns.extend(['피자' for t in range(20)])
nouns.extend(['치킨' for t in range(20)])
nouns.extend(['버거' for t in range(20)])
nouns.extend(['알탕' for t in range(20)])


count = Counter(nouns)
# list 자료형의 각 아이템의 갯수
# print(count)

tag2 = count.most_common(20)

# 글자크기와 색상을 지정해줌
taglist = pytagcloud.make_tags(tag2, maxsize=50)

# print(taglist)

pytagcloud.create_tag_image(taglist, 'wordcloud.png', size=(600, 300)
                            ,fontname='Korean', rectangular=False)

import matplotlib.pyplot as plt
import matplotlib.image as mping

img = mping.imread('wordcloud.png')
imgplot = plt.imshow(img)
plt.show()


