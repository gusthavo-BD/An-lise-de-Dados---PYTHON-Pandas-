#%%
import pandas as pd 
df_prouni = pd.read_csv('prouni_2005_2019.csv')

df_prouni

#%%
#Contagem apenas por raça de pessoas que ingressaram nas universidades pelo PROUNI

contagem_raca = df_prouni['RACA_BENEFICIARIO_BOLSA'].value_counts()
contagem_raca = contagem_raca.sort_values(ascending=False)

contagem_raca

#%%
#Contagem dos sexos e raças de pessoas que ingressaram nas universidades pelo PROUNI

contagem_raca_sexo = df_prouni.groupby(['RACA_BENEFICIARIO_BOLSA'])['SEXO_BENEFICIARIO_BOLSA'].value_counts()
contagem_raca_sexo = contagem_raca_sexo.sort_values(ascending=False)
contagem_raca_sexo

#%%
#Ao passar dos anos, tivemos uma crescente ou decrescente de pessoas que utilizaram o PROUNI ?
import matplotlib.pyplot as plt

contagem_por_ano = df_prouni.groupby(['ANO_CONCESSAO_BOLSA']).size()


plt.figure(figsize=(15, 10))
plt.plot(contagem_por_ano.index, contagem_por_ano.values, linestyle='-')
plt.title('Número de bolsas PROUNI concedidas por ano')
plt.show()

print("Como podemos análisar no gráfico, a ingressão nass faculdades pelo progrm PROUNI mais que dobraram")

# %%
#Qual curso teve o mais ingressão pelo PROUNI nesses anos.

contagem = df_prouni.groupby(['NOME_CURSO_BOLSA']).size()
maior_curso = contagem.idxmax()
contagem_maior_curso = contagem.max()
print(f'''O curso que mais teve ingressão com o PROUNI foi {maior_curso},
com {contagem_maior_curso} ingressões de 2005 à 2019.''')


