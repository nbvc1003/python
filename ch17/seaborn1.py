import matplotlib.pyplot as plt
import seaborn as sns

print('Seaborn version :', sns.__version__)
sns.set()
sns.set_style('whitegrid')
sns.set_color_codes()
current_palette = sns.color_palette()
sns.palplot(current_palette)
sns.palplot(sns.color_palette('Blues'))
sns.palplot(sns.dark_palette("purple"))

plt.show()
