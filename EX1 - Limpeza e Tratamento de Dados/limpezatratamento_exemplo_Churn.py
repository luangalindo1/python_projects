# -*- coding: utf-8 -*-


import pandas as pd
import seaborn as srn
import statistics as sts

#importar dados
dataset = pd.read_csv("Churn.csv", sep=";")
#visulizar
dataset.head()

#tamanho
dataset.shape

#primeiro problema é dar nomes as colunas
dataset.columns = ["Id","Score","Estado","Genero","Idade","Patrimonio","Saldo",
                   "Produtos","TemCartCredito", "Ativo","Salario","Saiu"]

#visualizar
dataset.head()#explorar dados categoricos

#estado
agrupado = dataset.groupby(['Estado']).size()
print(agrupado)
agrupado.plot.bar(color = 'gray')

#genero
agrupado = dataset.groupby(['Genero']).size()
print(agrupado)
agrupado.plot.bar(color = 'gray')

#explorar colunas numéricas
#score
dataset['Score'].describe()
srn.boxplot(x=dataset['Score']).set_title('Score')
srn.displot(x=dataset['Score'], kde=True)

#idade
dataset['Idade'].describe()
srn.boxplot(x=dataset['Idade']).set_title('Idade')
srn.displot(x=dataset['Idade'], kde=True)

#saldo
dataset['Saldo'].describe()
srn.boxplot(x=dataset['Saldo']).set_title('Saldo')
srn.displot(x=dataset['Saldo'], kde=True)

#salário
dataset['Salario'].describe()
srn.boxplot(x=dataset['Salario']).set_title('Salario')
srn.displot(x=dataset['Salario'], kde=True)

#contamos valores NAN
#genero e salário
dataset.isnull().sum()

#salarios
#remover NANs e substituir pela mediana (melhor nesse caso por causa
#da disperção dos dados)
dataset['Salario'].describe()

mediana = dataset['Salario'].median()
print(mediana)

#substituir NAN por mediana
dataset['Salario'].fillna(mediana, inplace=True)

#Verificamos se NAN não existem mais
dataset['Salario'].isnull().sum()

#genero, falta de padronização e NAs
print(dataset.groupby(['Genero']).size())

#total de NANs
dataset['Genero'].isnull().sum()

dataset['Genero'].describe()
print(sts.mode(dataset['Genero']))

#preenche NANs com a moda
dataset['Genero'].fillna(sts.mode(dataset['Genero']), inplace=True)

#verificamos novamente NANs
dataset['Genero'].isnull().sum()

#padroniza de acordo com o dominio
dataset.loc[dataset['Genero'] ==  'M', 'Genero'] = "Masculino"
dataset.loc[dataset['Genero'].isin( ['Fem','F']), 'Genero'] = "Feminino"
#visualiza o resultado
print(dataset.groupby(['Genero']).size())

#idades fora do dominio
dataset['Idade'].describe()

#visualizar 
dataset.loc[(dataset['Idade'] <=  0 )  | ( dataset['Idade'] >=  100) ]

#calular a mediana
mediana = sts.median(dataset['Idade'])
print(mediana)

#substituir pela mediana
dataset.loc[(dataset['Idade'] <=  0 )  | 
            ( dataset['Idade'] >=  100), 'Idade'] = mediana

#verificamos se ainda existem idades fora do domínio
dataset.loc[(dataset['Idade'] <=  0 )  | ( dataset['Idade'] >=  100) ]

#verifica-se as idades novamente
dataset['Idade'].describe()
srn.boxplot(x=dataset['Idade']).set_title('Idade')
srn.displot(x=dataset['Idade'], kde=True)

#dados duplicados, buscamos pelo ID
dataset[dataset.duplicated(['Id'],keep=False)]

#excluimos pelo ID
dataset.drop_duplicates(subset="Id", keep='first',inplace=True)
#buscamos duplicados 
dataset[dataset.duplicated(['Id'],keep=False)]

#estado foram do domínio
print(dataset.groupby(['Estado']).size())

#atribuímos RP = PR; SP = SC; TD = moda
dataset.loc[dataset['Estado'].isin(['RP']), 'Estado'] = "PR"
dataset.loc[dataset['Estado'].isin(['SP']), 'Estado'] = "SC"
dataset.loc[dataset['Estado'].isin(['TD']), 'Estado'] = sts.mode(dataset['Estado'])
#verificamos o resultado
print(dataset.groupby(['Estado']).size())

#outliers em salário, vamos considerar 2 desvios padrão
#pode ser tbm 1,5xIRQ (distância interquartil)
desv = sts.stdev(dataset['Salario'])
print(desv)

#definir padrão como maior que 2 desvios padrão
#checamos se algum atende critério
dataset.loc[dataset['Salario'] >=  2 * desv ] 

#vamos atualizar salarios para mediana, calculamos
mediana = sts.median(dataset['Salario'])
print(mediana)

#atribumos
dataset.loc[dataset['Salario'] >=  2 * desv, 'Salario'] = mediana
#checamos se algum atende critério
dataset.loc[dataset['Salario'] >=  2 * desv ] 

dataset.head()

dataset.shape



