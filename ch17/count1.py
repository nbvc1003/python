import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 차트에 한글 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # 부호표시 (-,+) 사용할때
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic['class'])

# x 컬럼, data 테이블..
# 데이터의 갯수를 카운트해서 표로 그린다.  
sns.countplot(x='class', data=titanic)
plt.title('타이타닉 클래스별 승객수')
plt.show()