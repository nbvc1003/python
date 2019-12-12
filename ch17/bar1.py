import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 한글 입력 가능하도록
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(
    fname="c:/windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name)
rcParams['axes.unicode_minus'] = False # -표시 보이게
###
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

df = pd.read_csv('korea.csv',encoding='euc=kr')
# width 값을 1.0보다 작게 , color는 rgb 값으로
plt.bar(df.index, df['점수'],width=.8, color='#556677')
plt.xticks(range(0,len(df.index),1),df['이름'])
plt.title('학생 성적표')
plt.show()