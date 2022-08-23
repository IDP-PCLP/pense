# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:42:44 2022

@author: Álvaro Cafe
"""
# Exemplos de variáveis
nome = 'Xerxes'
idade = 16
print(nome, idade)

# Programa de cadastro
## Primeiro, vamos definir as variáveis

nome = 'Calvin'
print(nome)
cpf = '0564684564879'
morador = False

#%% Input do usuário com input()

nome = input("Nome: ")
cpf = input("CPF: ")
morador = input("Morador (S/N): ")

print(f'Bem vindo ao prédio, {nome}. Seu CPF é {cpf}')
print('Bem vindo ao prédio, '+nome+'.')

cpf_numerico = int(cpf)
cpf_texto = str(cpf_numerico)

## Escolhendo o nome de uma lista

nomes = ['Xerxes','Calvin','Ítalo','Álvaro']
nome = input("Qual é seu nome? (0,1,2 ou 3) ")
if int(nome) in [0,1,2,3]:
    print(f'seu nome é {nomes[int(nome)]}')
elif int(nome) == 4:
    print("4 não está na lista")
else:
    print("O número deve ser um dos da lista.")










