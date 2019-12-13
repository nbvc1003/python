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

# 홀수만 0.2 나오도록, 국어+영어+수학 : 총계로
df = pd.read_csv('csv_exam1.csv', encoding='euc-kr')
explode = [0, 0.2, 0, 0.2 , 0, 0.2, 0, 0.2, 0, 0.2]
plt.pie(df['국어'] + df['영어'] + df['수학'], labels=df['이름'], explode=explode, autopct='%1.1f%%')
plt.title('점수총계 학생별 비율')
plt.show()
