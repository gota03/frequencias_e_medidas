import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("dados.csv")

df = pd.DataFrame(data = {"Fulano": [8, 10, 4, 8, 6, 10, 8],
                          "Beltrano": [10, 2, 0.5, 1, 3, 9.5, 10],
                          "Sicrano": [7.5, 8, 7, 8, 8, 8.5, 7]
                          },
                  index = [
                      "Matematica",
                      "Portugues",
                      "Ingles",
                      "Geografia",
                      "Historia",
                      "Fisica",
                      "Quimica"])

df.rename_axis("Materia", axis = "columns", inplace = True)
print(df["Fulano"].mean()) # mean calcula a média 

print(dados.groupby(dados["Sexo"])["Renda"].mean()) # calculando a renda média por sexo