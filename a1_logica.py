# -*- coding: utf-8 -*-
"""a1-logica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/mampaiva/33e61890b019930a9bc8abc7895f8da0/a1-logica.ipynb
"""

nome='mateus'
idaide=29

idade=29
idaide=idade

print(f'meu nome é {nome} e tenho {idade}')

def saudacao():
  nome = input('qual é o seu nome ? ')
  print(f'olá {nome}')

saudacao()

def nome_completo():
 primeiro_nome = input('Qual seu primeiro nome? ')
 sobrenome = input('Qual seu sobrenome? ')
 nome_inteiro = primeiro_nome + ' ' + sobrenome
 print(nome_inteiro)

nome_completo()

def saudacao_com_parametro(nome_da_pessoa):
  print(f'olá {nome_da_pessoa}')

saudacao_com_parametro(nome)

idade=29
def vericar_idade(idade):
  if idade >= 18:
    print('tem permissão para dirigir')
  else:
    print('não tem permissão para dirigir')
vericar_idade(idade)

def vericar_idade():
  idade = input('qual é sua idade? ')
  idade = int(idade)
  if idade >= 18:
    print('tem permissão para dirigir')
  else:
    print('não tem permissão para dirigir')
vericar_idade()

idades = [10,23,432,45,67,789]
idades[0:-1]