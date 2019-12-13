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

#                     100행 3열 랜덤생성        2019,1,1 부터 100일
df1 = pd.DataFrame(np.random.randn(100, 3), index=pd.date_range('1/1/2019', periods=100),
                   columns=['A','B','C']).cumsum() # 값을 누적 시켜 넣는다.

print(df1)

# pandas 의 DataFrame 에서 내부적으로 import matplotlib 를 해서 연결되어 있기때문에 plot 함수를 사용해서 그려준다.
df1.plot()
plt.show()

