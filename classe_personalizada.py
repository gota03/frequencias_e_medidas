import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

dados.head()

dados["Renda"].min()
dados["Renda"].max()

classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ["E", "D", "C", "B", "A"]

frequencia = pd.value_counts(
    pd.cut(x = dados["Renda"], bins = classes, labels = labels, include_lowest = True) 
)

# a função pd.cut() é utilizada para dividir um conjunto de dados em intervalos específicos, que são chamados de classes. Esses intervalos são definidos pelos parâmetros bins e labels. O parâmetro bins especifica os limites dos intervalos, ou seja, os valores que delimitam cada classe, enquanto o parâmetro labels é utilizado para atribuir rótulos a cada classe.

percentual = pd.value_counts(
    pd.cut(x = dados["Renda"], bins = classes, labels = labels, include_lowest = True),
    normalize = True
) * 100

# a junção do método pd.value_counts com a função pd.cut tem como objetivo contar a frequência de ocorrência de cada classe criada pela função pd.cut.

dist_freq_quantitativas_personalizadas = pd.DataFrame({"Frequencia":frequencia, "Porcentagem (%)": percentual})
dist_freq_quantitativas_personalizadas.rename_axis(None, axis="index",  inplace=True) # retirando o index Sexo da tabela
print(dist_freq_quantitativas_personalizadas.sort_index(ascending = False)) # Quando o parâmetro ascending é definido como False, os índices (labels) são ordenados de forma decrescente

dist_freq_quantitativas_personalizadas["Frequencia"].plot.bar(width = 1, color = "blue", figsize = (12,6), alpha = 0.2)
plt.show()
