
###1 - Carregue as bibliotecas NumPy, Pandas, BeautifulSoup, MatPlotLib, Requests, JSON e Seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import json



###2 – Entre no site https://db-engines.com/en/ranking, faça um scraping e gere um DataFrame com a lista de banco de dados do Ranking.

html=requests.get("https://db-engines.com/en/ranking").content
soup=BeautifulSoup(html, 'html5lib')

tabela=soup.find('table', {'class':'dbi'}).find('tbody')

# print(tabela)


linhas=tabela.find_all('tr')
contalinhas=0
banco=[]
pontos=[]
for linha in linhas:
    contalinhas+=1
    if contalinhas>3:
        dado=linha.find_all('td')
        dado2=linha.find('a')
        pontos.append(float(dado[3].text))
        banco.append(dado2.contents[0])

dados=pd.DataFrame(banco,columns=['Banco'])
dados['Pontos']=pontos

# print(dados)



###3 – Com a Biblioteca Seaborn gere um gráfico de colunas, indicando o nome do banco e a quantidade de pontos do banco no mês atual.

sns.barplot(data=dados.head(4), x='Banco', y='Pontos')
# plt.show()



###4 – Gere um novo Dataframe com apenas as 10 primeiras posições da lista, crie um campo de Share (porcentagem de relevância de cada Banco de Dados em relação aos 10 listados, baseado na quantidade de pontos que eles tem). Informe qual é a porcentagem e o nome do banco que aparece em primeiro lugar.

dados_ex4=dados.head(10)

#print(dados_ex4)


total=dados_ex4['Pontos'].sum()
dados_ex4['Share']=dados_ex4['Pontos']/total*100

# print(dados_ex4)



###5 – Usando MatPlotLib gere um gráfico baseado no Share de cada banco em relação aos outros 9 da lista gerada no Exercício 4.

plt.pie(dados_ex4['Share'], labels=dados_ex4['Banco'])

# plt.show()



###6 – Usando o Dataframe completo, crie também uma coluna Share informado a porcentagem de relevância de cada banco em relação aos demais.

total=dados_ex4['Pontos'].sum()
dados['Share']=dados_ex4['Pontos']/total*100

# print(dados)



###7 – Com o Dataframe gerado no Exercício 6, gere um arquivo do tipo CSV chamado “db-ranking.csv”.

# dados.to_csv('db-ranking.csv')



###8 – O Banco Central dispõe de um conjunto de APIs, sendo que uma delas é o valor do Dolar. Nesse endereço tem algumas delas: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos, sendo que a primeira delas é capaz de gerar a cotação do dólar de uma determinada data.
###Utilizando Json, realize uma consulta direta a API e informe a cotação de venda do dólar do dia 16/09/2008.


site="https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='09-16-2008'&$top=100&$format=json"
resposta=requests.get(site)
dados=json.loads(resposta.text)

# print(dados)

print(dados['value'][0]['cotacaoVenda'])


