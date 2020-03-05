from Testes.Circulo import Circulo
from math import pi
cor = ['vermelho', 'verde', 'azul']
raio=[20, 10, 35]
material = ['plastico', 'madeira', 'papel']
c = Circulo(cor, raio, material)


print('Iniciando Teste\n\n')

print('Teste do trocaCor() \n\n')

assert c.cor == c.mostraCor(), f'erro, a cor:{cor} nao esta no objeto'
assert cor == c.mostraCor(), f'Erro, a cor: {cor} nao esta no objeto'

print('Teste do trocaCor(): OK\n\n')


print('Teste do raio \n\n')
assert raio == c.Circulo__raio, ' o raio do circulo não está sendo atribuido'
print('Teste de atribuiçao do raio por parametro: ok \n\n')








