import matplotlib.pyplot as plt
import pandas as pd

s1 = pd.Series([84900, 81800, 71756, 92000])
s2 = pd.Series([80500, 82800, 71736, 90000])

plt.figure(figsize=(6,4))

plt.plot(s1, label='04-10', lw=2,c='r',ls='-.',marker='s')
plt.plot(s2, label='04-11',ls=':',color="#F15F5F")

plt.xlim(0.0,4.0)
plt.ylim(70000, 90000)

# 0-> zero, 1-> one
plt.xticks(range(0,5,1), ['zero','one','two','three','four'],
           rotation='vertical')
plt.yticks(range(70000, 105000, 5000))
plt.grid()
plt.xlabel('index')
plt.ylabel('plot graph')
plt.legend()
plt.show()