# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:32:37 2022

@author: asanorte.labdell
"""

import pandas as pd 
url = 'https://en.wikipedia.org/wiki/FIFA_World_Cup'
tabelas = pd.read_html(url,match='Third place game')
print(len(tabelas))
#%%
dados = tabelas[0]
print(dados['Year'])
print(dados['Year'].mean())
print(dados['Year'].max())
print(dados['Year'].min())
print(dados['Year'].max() - dados['Year'].min())
print(dados['Year'].describe())

#%%
# Revisão variáveis 
# Lista
compras = ['açúcar','tempero','água']
print(compras)
compras[2] = 'tudo que é de bom'
print(compras)
print(compras[2])
# Adicionar novo elemento a lista
compras.append('elemento x')
print(compras)

#%% Dicionários
inquilino = {'nome':'Seu Madruga','ap':9,
             'divida':14} 
inquilino2 = {'nome':'Dona Florinda','ap':6,
             'divida':0} 
inquilino3 = {'nome':'Dona Clotilde','ap':8} 
inquilino3['divida'] = 6
inquilinos = [inquilino, inquilino2, inquilino3]

print(inquilinos[2]['nome'])
print(inquilinos[2]['ap'])
print(inquilinos[2]['divida'])

#%% Controle de Fluxo
# Laço for ou para cada
for compra in compras:
    if compra == 'elemento x':
        print(f"Vou comprar {compra} com a liga de supervilões.")
    else:
        print(f"Vou comprar {compra} no mercado.")

for inquilino in inquilinos:
    if inquilino['divida'] > 1:
        print(f'{inquilino["nome"]}, pague o aluguel!')

numero = 10
while numero >=0:
    print(f'Olá {numero}!')
    numero = numero -1

#%% Funções
def cobrar_aluguel(inquilinos=[]):
    endividados = []
    for inquilino in inquilinos:
        if inquilino['divida'] > 0:
            print(f'{inquilino["nome"]}, pague o aluguel!')
            endividados.append(inquilino["nome"])
    return endividados
endividados = cobrar_aluguel(inquilinos)
print(endividados)














