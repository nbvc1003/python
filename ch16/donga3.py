from konlpy.tag import Okt
from collections import Counter
import pytagcloud


with open('count.txt','r', encoding='utf-8') as f:
    input_data = f.readlines()
    data = []
    for d in input_data:

        # d0,d1 = d.split()
        # if len(d0) > 1: # 2글자 이상
        #     data.append((d0, int(d1)))

        # 위쪽 방법도 된다.
        dd = d.split()
        if len(dd[0]) > 1:
            data.append((dd[0], int(dd[1])))

    tag_list = pytagcloud.make_tags(data, maxsize=100)
    pytagcloud.create_tag_image(tag_list,'dong1.png',
                                size=(900,600), fontname="Korean",rectangular=False)


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("dong1.png")
plt.imshow(img)
plt.axis('off')
plt.show()
