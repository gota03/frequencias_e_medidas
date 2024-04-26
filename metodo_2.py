import pandas as pd

dados = pd.read_csv("dados.csv")

sexo = {
    0: "Masculino",
    1: "Feminino"
}

cor = {
    0: "Indigena",
    2: "Branca",
    4: "Preta",
    6: "Amarela",
    8: "Parda",
    9: "Sem declaracao"
}

frequencia = pd.crosstab(dados["Sexo"], dados["Cor"], normalize = True) * 100 # a função cria uma tabela com o 1º parâmetro sendo a linha e 2º parâmetro sendoa coluna. A função pd.crosstab() é utilizada para criar tabelas de contingência a partir de variáveis categóricas. Ela conta a frequência com que cada combinação de categorias ocorre.

frequencia_exemplo_media = pd.crosstab(dados["Sexo"], dados["Cor"], aggfunc = "mean", values = dados["Renda"]) #aggfun diz qual função será utilizada, no caso foi média, e values qual valor vai ser feito a média
# print(frequencia_exemplo_media)

frequencia.rename(index = sexo, inplace = True) # como o 1º parâmetro da função crosstab define a linha, basta passar por qual valor a linha vai ser renomeada

frequencia.rename(columns = cor, inplace = True) # como o 2º parâmetro da função crosstab define a coluna, basta passar por qual valor a coluna vai ser renomeada

print(frequencia)