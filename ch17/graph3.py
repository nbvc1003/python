from matplotlib import font_manager,rc,rcParams
font_name=font_manager.FontProperties(
    fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)
rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic)
titanic_pivot = titanic.pivot_table(
    index="class",columns="sex", aggfunc="size")
t=titanic_pivot.unstack()
t2=t.reset_index()
print(t2)
t2.columns = ["sex","class","cnt"]
print(t2)
sns.barplot(x="class",y="cnt", hue="sex", data=t2)
plt.show()
