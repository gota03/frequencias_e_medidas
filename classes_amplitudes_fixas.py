import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv("dados.csv")

n = dados.shape[0] # a função shape mostra quantos registros e quantas classes

k = 1 + (10 / 3) * np.log10(n) # A regra de Sturges é um método para definição do número de classes, baseado no total de amostras do banco de dados

k = int(k.round(0)) # arredondando o número para ficar sem casas decimais

frequencia = pd.value_counts(
    pd.cut(
        x = dados["Renda"],
        bins = 17,
        include_lowest = True
    ),
    sort = False 
)

percentual = pd.value_counts(
    pd.cut(
        x = dados["Renda"],
        bins = 17,
        include_lowest = True
    ),
    sort = False,
    normalize = True
) * 100

dist_freq_quantitativas_amplitudes_fixas = pd.DataFrame({"Frequencia":frequencia, "Porcentagem (%)": percentual})
dist_freq_quantitativas_amplitudes_fixas.rename_axis(None, axis="index", inplace=True)
dist_freq_quantitativas_amplitudes_fixas.rename_axis("Renda", axis="columns", inplace=True)

print(dist_freq_quantitativas_amplitudes_fixas)