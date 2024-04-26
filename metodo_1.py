import pandas as pd

# Um DataFrame é uma estrutura de dados bidimensional e tabular que é muito utilizada na biblioteca Pandas do Python. Ele é composto por linhas(index) e colunas(columns), semelhante a uma planilha ou tabela de banco de dados. Cada coluna de um DataFrame representa uma variável, enquanto cada linha representa uma entrada ou observação relacionada a essas variáveis.

dados = pd.read_csv("dados.csv") #lê e armazena os dados de um arquivo em uma estrutura dataframe

dados.head() # exibe os 5 primeiros registros

print(sorted(dados["Anos de Estudo"].unique())) # ordena os dados pela coluna e mostra os valores únicos, sem repetir

print(f"Idade minima: {dados["Idade"].min()} \nIdade maxima: {dados["Idade"].max()}") # mostra o menor e maior valor da coluna

print(dados["Sexo"].value_counts()) # mostra a quantidade de cada valor

print(dados["Sexo"].value_counts(normalize=True) * 100) # mostra a quantidade de cada valor em %

frequencia = dados["Sexo"].value_counts()
frequencia.index.name = None # para retirar o nome do objeto original que é herdado no caso "Sexo"

porcentagem = dados["Sexo"].value_counts(normalize=True) * 100
porcentagem.index.name = None # para retirar o nome do objeto original que é herdado no caso "Sexo"

dist_freq_qualitativas = pd.DataFrame({"Frequencia": frequencia, "Porcentagem (%)": porcentagem}) # cria um dataframe utilizando de um dicionário para determinar a chave e valor que a chave seria a coluna e o valor a linha

dist_freq_qualitativas.rename(index={0: "Masculino", 1: "Feminino"}, inplace=True) # o index altera a linha do DataFrame atraves de um dicionário, a linha que eu quero alterar e o seu novo nome, o inplace=True serve para dizer se vai modificar o DataFrame original ou se vai criar uma cópia modificada mas sem alterar o DataFrame original
 
dist_freq_qualitativas.rename_axis("Sexo", axis="columns", inplace=True) # é usado para renomear o eixo de um DataFrame(coluna(columns)/linha(index)) O primeiro argumento do método rename_axis() é o novo nome do eixo. O segundo argumento é o eixo que está sendo renomeado. O terceiro argumento é um booleano que indica se o método deve ser executado na cópia do DataFrame ou no próprio DataFrame. No caso, o booleano está definido como True, então o método será executado no próprio DataFrame.

print(dist_freq_qualitativas)