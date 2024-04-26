import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

ax = sns.displot(dados["Altura"], kde = False)
ax.figure.set_size_inches(12,6)
ax.set_titles("Distribuição de frequências - Altura", fontsize = 18)
ax.set_xlabels("Metros", fontsize = 14)
plt.show()